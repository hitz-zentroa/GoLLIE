from __future__ import annotations

import importlib
import inspect
import logging
import re
from collections import defaultdict
from copy import deepcopy
from dataclasses import dataclass as org_dataclass
from typing import Any, Dict, Tuple, Type, TypeVar, Union


def dataclass(
    cls=None,
    /,
    *,
    init=True,
    repr=True,
    eq=False,
    order=False,
    unsafe_hash=False,
    frozen=False,
):
    return org_dataclass(
        cls,
        init=init,
        repr=repr,
        eq=eq,
        order=order,
        unsafe_hash=unsafe_hash,
        frozen=frozen,
    )


def cast_to(obj: Any, dtype: Type) -> Any:
    if not isinstance(obj, dtype):
        raise TypeError(f"Type {dtype} must be a parent class of object {obj}.")

    _inst = {param: getattr(obj, param) for param in inspect.signature(dtype).parameters.keys() if hasattr(obj, param)}
    return dtype(**_inst)


class HallucinatedType:
    def __init__(self, *args, **kwargs) -> None:
        pass

    def exists_in(self, text: str) -> bool:
        """
        Checks whether the annotation exists on a given text. This function is used to
        identify model alucinations.

        Args:
            text (`str`):
                The text used to check whether the annotation is an alucionation or not.

        Returns:
            `bool`:
                Whether the annotation exists on the input text or not.
        """
        return True


@dataclass
class Entity:
    """A general class to represent entities."""

    span: str

    def __eq__(self: Entity, other: Entity) -> bool:
        self_span = self.span.lower().strip()
        other_span = other.span.lower().strip()
        return type(self) == type(other) and self_span == other_span

    def key(self) -> Union[str, None]:
        """
        Return the key span.

        Returns:
            Union[str, None]:
                The span that represents the annotation.
        """
        return self.span.lower()

    def exists_in(self, text: str) -> bool:
        """
        Checks whether the annotation exists on a given text. This function is used to
        identify model alucinations.

        Args:
            text (`str`):
                The text used to check whether the annotation is an alucionation or not.

        Returns:
            `bool`:
                Whether the annotation exists on the input text or not.
        """
        return self.span.lower().strip() in text.lower()

    def index(self, text: str) -> int:
        """
        Returns the first position of the span given the text.

        Args:
            text (`str`):
                The text to search the span on.

        Raises:
            IndexError:
                Raised when the span does not exist in the text

        Returns:
            `Tuple[int, int]`:
                The position of the span in the text.
        """
        if not self.exists_in(text):
            raise IndexError("The span is not in text.")

        pos = text.lower().index(self.span.lower().strip())
        return (pos, pos + len(self.span))


@dataclass
class Value:
    """A general class to represent values."""

    span: str

    def __eq__(self: Value, other: Value) -> bool:
        return type(self) == type(other) and self.span == other.span

    def key(self) -> Union[str, None]:
        """
        Return the key span.

        Returns:
            Union[str, None]:
                The span that represents the annotation.
        """
        return self.span.lower()

    def exists_in(self, text: str) -> bool:
        """
        Checks whether the annotation exists on a given text. This function is used to
        identify model alucinations.

        Args:
            text (`str`):
                The text used to check whether the annotation is an alucionation or not.

        Returns:
            `bool`:
                Whether the annotation exists on the input text or not.
        """
        return self.span.lower() in text.lower()

    def index(self, text: str) -> int:
        """
        Returns the first position of the span given the text.

        Args:
            text (`str`):
                The text to search the span on.

        Raises:
            IndexError:
                Raised when the span does not exist in the text

        Returns:
            `Tuple[int, int]`:
                The position of the span in the text.
        """
        if not self.exists_in(text):
            raise IndexError("The span is not in text.")

        pos = text.lower().index(self.span.lower().strip())
        return (pos, pos + len(self.span))


@dataclass
class Relation:
    """A general class to represent relations."""

    arg1: str
    arg2: str

    def __eq__(self: Value, other: Value) -> bool:
        return type(self) == type(other) and self.arg1 == other.arg1 and self.arg2 == other.arg2

    def key(self) -> Union[str, None]:
        """
        Return the key span.

        Returns:
            Union[str, None]:
                The span that represents the annotation.
        """
        return None

    def exists_in(self, text: str) -> bool:
        """
        Checks whether the annotation exists on a given text. This function is used to
        identify model alucinations.

        Args:
            text (`str`):
                The text used to check whether the annotation is an alucionation or not.

        Returns:
            `bool`:
                Whether the annotation exists on the input text or not.
        """
        return self.arg1.lower() in text.lower() and self.arg2.lower() in text.lower()

    def index(self, text: str) -> Tuple[int, int]:
        """
        Returns the first position of the span given the text.

        Args:
            text (`str`):
                The text to search the span on.

        Raises:
            IndexError:
                Raised when the span does not exist in the text

        Returns:
            `Tuple[int, int]`:
                The position of the span in the text.
        """
        if not self.exists_in(text):
            raise IndexError("The span is not in text.")

        pos = text.lower().index(self.arg1.lower().strip())
        return (pos, pos + len(self.arg1))


@dataclass
class Event:
    """A general class to represent events."""

    mention: str

    def __eq__(self: Event, other: Event) -> bool:
        return type(self) == type(other) and self.mention == other.mention

    def __and__(self: Event, other: Event) -> Event:
        attrs = {
            attr: []
            for attr, values in inspect.getmembers(self)
            if not (attr.startswith("__") or attr in ["mention", "subtype"] or inspect.ismethod(values))
        }
        if self == other:
            for attr in attrs.keys():
                self_values = getattr(self, attr)
                other_values = deepcopy(getattr(other, attr))
                for value in self_values:
                    if value in other_values:
                        attrs[attr].append(value)
                        other_values.pop(other_values.index(value))

        pos_args = []
        if hasattr(self, "mention"):
            pos_args.append(self.mention)
        if hasattr(self, "subtype"):
            pos_args.append(self.subtype)

        return type(self)(*pos_args, **attrs)

    def __len__(self: Event) -> int:
        attrs = {
            attr: values
            for attr, values in inspect.getmembers(self)
            if not (attr.startswith("__") or attr in ["mention", "subtype"] or inspect.ismethod(values))
        }
        _len = 0
        for values in attrs.values():
            _len += len(values)

        return _len

    def key(self) -> Union[str, None]:
        """
        Return the key span.

        Returns:
            Union[str, None]:
                The span that represents the annotation.
        """
        if self.mention:
            return self.mention.lower()

        return None

    def exists_in(self, text: str) -> Event:
        """
        Checks whether the annotation exists on a given text. This function is used to
        identify model alucinations.

        Args:
            text (`str`):
                The text used to check whether the annotation is an alucionation or not.

        Returns:
            `bool`:
                Whether the annotation exists on the input text or not.
        """
        text = text.lower()
        # Only return None if the mention is defined and is not in the text
        if self.mention and self.mention.lower() not in text:
            return None

        attrs = {
            attr: []
            for attr, values in inspect.getmembers(self)
            if not (attr.startswith("__") or attr in ["mention", "subtype"] or inspect.ismethod(values))
        }
        for attr in attrs.keys():
            self_values = getattr(self, attr)
            for value in self_values:
                if value.lower() in text:
                    attrs[attr].append(value)

        pos_args = []
        if hasattr(self, "mention"):
            pos_args.append(self.mention)
        if hasattr(self, "subtype"):
            pos_args.append(self.subtype)

        return type(self)(*pos_args, **attrs)

    def index(self, text: str) -> int:
        """
        Returns the first position of the span given the text.

        Args:
            text (`str`):
                The text to search the span on.

        Raises:
            IndexError:
                Raised when the span does not exist in the text

        Returns:
            `int`:
                The position of the span in the text.
        """
        # Return len(text) if there is no mention defined
        if not self.mention:
            return (len(text), len(text))

        if not self.exists_in(text):
            raise IndexError("The span is not in text.")

        pos = text.lower().index(self.mention.lower().strip())
        return (pos, pos + len(self.mention))


class AnnotationList(list):
    """
    A class that handles the list of system outputs.

    Args:
        list (List[Any]):
            List of annotations generated by the system.
    """

    SIMPLE_TYPES = [Entity, Value, Relation]
    COMPLEX_TYPES = [Event]

    @staticmethod
    def _load_guidelines(task_module: str) -> Dict[str, TypeVar]:
        mdl = importlib.import_module(task_module)
        names = {x: y for x, y in mdl.__dict__.items() if not x.startswith("_")}

        return names

    def filter_hallucinations(self, text: str) -> AnnotationList:
        _elems = []
        _counts = defaultdict(int)
        for elem in self:
            if any(isinstance(elem, _type) for _type in self.SIMPLE_TYPES):
                elem = elem if elem.exists_in(text) else None
            elif any(isinstance(elem, _type) for _type in self.COMPLEX_TYPES):
                elem = elem.exists_in(text)
            elif isinstance(elem, HallucinatedType) or isinstance(elem, type):
                continue
            else:
                print(elem)
                if hasattr(elem, "exist_in"):
                    elem = elem if elem.exists_in(text) else None
                else:
                    continue

            if elem is not None:
                key = elem.key()
                # Check if key is not None
                if key:
                    _counts[key] += 1
                    text_counts = text.lower().count(key)
                    # Skip element if the maximum allowed elements already exists
                    if text_counts < _counts[key]:
                        continue

                _elems.append(elem)

        return type(self)(_elems)

    @classmethod
    def from_output(
        cls, ann: str, task_module: str, text: str = None, filter_hallucinations: bool = False
    ) -> AnnotationList:
        # Import guidelines
        guidelines = cls._load_guidelines(task_module)
        locals().update(guidelines)

        reading = True
        while reading:
            try:
                _elems = eval(ann)
                reading = False
            # Handle hallucinations
            except NameError as e:
                name = re.search(r"'\w+'", e.args[0]).group(0).strip("'")
                logging.warning(f"An hallucinated predicted guideline found: {name}")
                locals().update({name: HallucinatedType})
            except Exception:
                _elems = []
                reading = False

        self = cls(_elems)

        if filter_hallucinations:
            if text is None:
                raise ValueError("To filter the allucinations the text argument must not be None.")
            self = self.filter_hallucinations(text)

        return self

    @classmethod
    def from_gold(
        cls, ann: str, task_module: str, text: str = None, filter_hallucinations: bool = False
    ) -> AnnotationList:
        # Import guidelines
        guidelines = cls._load_guidelines(task_module)
        locals().update(guidelines)

        # Remove malformed elements
        _elems = []
        for elem in eval(ann):
            try:
                elem = eval(elem)
                _elems.append(elem)
            except SyntaxError:
                logging.warning(f"Found an incorrectly formated gold: {elem}")

        self = cls(_elems)

        if filter_hallucinations:
            if text is None:
                raise ValueError("To filter the allucinations the text argument must not be None.")
            self = self.filter_hallucinations(text)

        return self
