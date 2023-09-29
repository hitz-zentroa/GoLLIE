from __future__ import annotations

import dataclasses
import importlib
import inspect
import logging
import re
from collections import defaultdict
from copy import deepcopy
from dataclasses import dataclass as org_dataclass
from typing import Any, Dict, List, Tuple, Type, TypeVar, Union


def dataclass(
    cls=None,
    /,
    *,
    init=True,
    repr=False,
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


class Name(str):
    def __repr__(self):
        return f"Name({super().__repr__()})"


class Value(str):
    def __repr__(self) -> str:
        return f"Value({super().__repr__()})"


class String(str):
    def __repr__(self) -> str:
        return f"String({super().__repr__()})"


@dataclass
class Entity:
    """A general class to represent entities."""

    span: str

    def __post_init__(self: Entity) -> None:
        self._allow_partial_match: bool = False

    def __eq__(self: Entity, other: Entity) -> bool:
        self_span = self.span.lower().strip()
        other_span = other.span.lower().strip()
        if self._allow_partial_match:
            return type(self) == type(other) and (self.span in other_span or other_span in self.span)

        return type(self) == type(other) and self_span == other_span

    def __repr__(self) -> str:
        """Returns a string containing only the non-default field values."""
        s = ", ".join(
            f"{field.name}={getattr(self, field.name)!r}"
            for field in dataclasses.fields(self)
            if getattr(self, field.name) != field.default
        )
        return f"{type(self).__name__}({s})"

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

        # Check if the span is not None
        if not isinstance(self.span, str):
            return False

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
class Relation:
    """A general class to represent relations."""

    arg1: str
    arg2: str

    def __post_init__(self: Relation) -> None:
        self._allow_partial_match: bool = False

    def __eq__(self: Value, other: Value) -> bool:
        if self._allow_partial_match:
            return (
                type(self) == type(other)
                and (self.arg1 in other.arg1 or other.arg1 in self.arg1)
                and (self.arg2 in other.arg2 or other.arg2 in self.arg2)
            )
        return type(self) == type(other) and self.arg1 == other.arg1 and self.arg2 == other.arg2

    def __repr__(self) -> str:
        """Returns a string containing only the non-default field values."""
        s = ", ".join(
            f"{field.name}={getattr(self, field.name)!r}"
            for field in dataclasses.fields(self)
            if getattr(self, field.name) != field.default
        )
        return f"{type(self).__name__}({s})"

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
        if not isinstance(self.arg1, str) or not isinstance(self.arg2, str):
            return False

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

    def __post_init__(self: Event) -> None:
        self._allow_partial_match: bool = False

    def __eq__(self: Event, other: Event) -> bool:
        if self._allow_partial_match:
            # On events we consider partial match if just the type is predicted
            # Some datasets has different guidelines when annotating event triggers
            return type(self) == type(other)
        return type(self) == type(other) and self.key() == other.key()

    def __and__(self: Event, other: Event) -> Event:
        attrs = {
            attr: []
            for attr, values in inspect.getmembers(self)
            if not (attr.startswith("_") or attr in ["mention", "subtype"] or inspect.ismethod(values))
        }
        if self == other:
            for attr in attrs.keys():
                self_values = getattr(self, attr)
                other_values = deepcopy(getattr(other, attr))
                for value in self_values:
                    if self._allow_partial_match:
                        for i, _value in enumerate(other_values):
                            if value in _value or _value in value:
                                attrs[attr].append(value)
                                other_values.pop(i)
                                break
                    else:
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
            if not (attr.startswith("_") or attr in ["mention", "subtype"] or inspect.ismethod(values))
        }
        _len = 0
        for values in attrs.values():
            _len += len(values)

        return _len

    def __repr__(self) -> str:
        """Returns a string containing only the non-default field values."""
        s = ", ".join(
            f"{field.name}={getattr(self, field.name)!r}"
            for field in dataclasses.fields(self)
            if getattr(self, field.name) != field.default
        )
        return f"{type(self).__name__}({s})"

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
            if not (attr.startswith("_") or attr in ["mention", "subtype"] or inspect.ismethod(values))
        }
        for attr in attrs.keys():
            self_values = getattr(self, attr)
            if not isinstance(self_values, list):
                import rich

                rich.print(self)
                raise TypeError(f"{attr}:{self_values} is not iterable")
            for value in self_values:
                # Avoid calling lower to a list when the model hallucinates
                if hasattr(value, "lower") and value.lower() in text:
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

    def assert_typing_constraints(self) -> bool:
        import typing

        def check_types(var: Any, _type: TypeVar) -> Tuple[bool, Any]:
            if _type is type(None):
                return (var is None, var)
            elif isinstance(_type, type):
                is_correct = isinstance(var, _type)
                if not is_correct:
                    if isinstance(var, list):
                        var = var[0] if len(var) else _type()
                    var = _type(var)
                return (is_correct, var)
            # elif _type is type(None):
            #     return (var is None, var)
            elif isinstance(_type, typing._GenericAlias):
                origin = _type.__origin__
                if origin is typing.Union:
                    is_correct = False
                    _var = None
                    for _t in _type.__args__:
                        _is_correct, tmp_var = check_types(var, _t)
                        if _is_correct:
                            return (_is_correct, tmp_var)
                        if _t is not type(None):
                            _var = tmp_var
                        is_correct |= _is_correct
                    # return any(check_types(var, _t) for _t in _type.__args__)
                    return (is_correct, _var)
                elif origin is list:
                    if not isinstance(var, list):
                        var = [var]
                    for _t in _type.__args__:
                        _var = []
                        is_correct = True
                        for v in var:
                            _is_correct, v = check_types(v, _t)
                            is_correct &= _is_correct
                            _var.append(v)
                        if is_correct:
                            return (is_correct, _var)  # Small difference here to allow empty lists

                    return (is_correct, _var)
                    # return any(all(check_types(v, _t) for v in var) if isinstance(var, list) else False for _t in _type.__args__)
                elif any(issubclass(origin, _t) for _t in [str, int, float, bool]):
                    return check_types(var, origin)
                else:
                    raise ValueError(f"Unsupported type: {origin}")
            else:
                raise ValueError("Only native types or typing module types are supported.")

        correct = True
        for field in dataclasses.fields(self):
            _correct, value = check_types(getattr(self, field.name), field.type)
            correct &= _correct
            setattr(self, field.name, value)

        return correct


@dataclass
class Template:
    """A general class to represent templates."""

    query: str

    def __eq__(self: Template, other: Template) -> bool:
        return type(self) == type(other) and self.key() == other.key()

    def __repr__(self) -> str:
        """Returns a string containing only the non-default field values."""
        s = ", ".join(
            f"{field.name}={getattr(self, field.name)!r}"
            for field in dataclasses.fields(self)
            if getattr(self, field.name) != field.default
        )
        return f"{type(self).__name__}({s})"

    def _get_attributes(self, ignore: bool = False) -> Dict[str, Any]:
        """Returns the non-positional attributes of a Template instance."""
        attrs = {}
        for attr, values in inspect.getmembers(self):
            if attr.startswith("_") or attr in ["query"] or inspect.ismethod(values):
                continue
            if ignore and values:
                attrs[attr] = type(values)()
            else:
                attrs[attr] = values
        return attrs

    def _get_pos_attributes(self: Template) -> List[Any]:
        """Return the positional attributes of a Template instance."""
        return [getattr(self, attr) for attr in ["query"]]

    def __and__(self: Template, other: Template) -> Template:
        attrs = self._get_attributes(ignore=True)
        if self == other:
            for attr in attrs.keys():
                self_values = getattr(self, attr)
                other_values = deepcopy(getattr(other, attr))
                if self_values is None:
                    continue
                if isinstance(self_values, list):
                    if not isinstance(other_values, list):
                        other_values = [other_values]
                    for value in self_values:
                        if value in other_values:
                            attrs[attr].append(value)
                            other_values.pop(other_values.index(value))
                else:
                    if isinstance(other_values, list):
                        attrs[attr] = self_values if self_values in other_values else None
                    else:
                        attrs[attr] = self_values if self_values == other_values else None

        pos_args = self._get_pos_attributes()

        return type(self)(*pos_args, **attrs)

    def __len__(self: Template) -> int:
        attrs = self._get_attributes()
        _len = 0
        for values in attrs.values():
            if not values:
                continue
            _len += len(values) if isinstance(values, list) else 1

        return _len

    def key(self: Template) -> Union[str, None]:
        """
        Return the key span.

        Returns:
            Union[str, None]:
                The span that represents the annotation.
        """
        if self.query:
            return self.query.lower()

        return None

    def exists_in(self: Template, text: str) -> Template:
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
        # Only return None if the key is defined and is not in the text
        if self.key() and self.key() not in text:
            return None

        attrs = self._get_attributes(ignore=True)
        for attr in attrs.keys():
            self_values = getattr(self, attr)
            if self_values:
                if isinstance(self_values, list):
                    for value in self_values:
                        if value.lower() in text:
                            attrs[attr].append(value)
                else:
                    if self_values.lower() in text:
                        attrs[attr] = self_values

        pos_args = self._get_pos_attributes()

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
        if not self.key():
            return (len(text), len(text))

        if not self.exists_in(text):
            raise IndexError("The span is not in text.")

        pos = text.lower().index(self.key().strip())
        return (pos, pos + len(self.key()))

    def assert_typing_constraints(self) -> bool:
        import typing

        def check_types(var: Any, _type: TypeVar) -> Tuple[bool, Any]:
            if _type is type(None):
                return (var is None, var)
            elif isinstance(_type, type):
                is_correct = isinstance(var, _type)
                if not is_correct:
                    if isinstance(var, list):
                        var = var[0] if len(var) else _type()
                    var = _type(var)
                return (is_correct, var)
            # elif _type is type(None):
            #     return (var is None, var)
            elif isinstance(_type, typing._GenericAlias):
                origin = _type.__origin__
                if origin is typing.Union:
                    is_correct = False
                    _var = None
                    for _t in _type.__args__:
                        _is_correct, tmp_var = check_types(var, _t)
                        if _is_correct:
                            return (_is_correct, tmp_var)
                        if _t is not type(None):
                            _var = tmp_var
                        is_correct |= _is_correct
                    # return any(check_types(var, _t) for _t in _type.__args__)
                    return (is_correct, _var)
                elif origin is list:
                    if not isinstance(var, list):
                        var = [var]
                    for _t in _type.__args__:
                        _var = []
                        is_correct = True
                        for v in var:
                            _is_correct, v = check_types(v, _t)
                            is_correct &= _is_correct
                            _var.append(v)
                        if is_correct:
                            return (is_correct, _var if len(_var) else None)

                    return (is_correct, _var)
                    # return any(all(check_types(v, _t) for v in var) if isinstance(var, list) else False for _t in _type.__args__)
                elif any(issubclass(origin, _t) for _t in [str, int, float, bool]):
                    return check_types(var, origin)
                else:
                    raise ValueError(f"Unsupported type: {origin}")
            else:
                raise ValueError("Only native types or typing module types are supported.")

        correct = True
        for field in dataclasses.fields(self):
            _correct, value = check_types(getattr(self, field.name), field.type)
            correct &= _correct
            setattr(self, field.name, value)

        return correct


@dataclass
class Generic:
    """A general class to represent Generics."""

    def __eq__(self, other) -> bool:
        return type(self) == type(other)

    def __repr__(self) -> str:
        """Returns a string containing only the non-default field values."""
        s = ", ".join(
            f"{field.name}={getattr(self, field.name)!r}"
            for field in dataclasses.fields(self)
            if getattr(self, field.name) != field.default
        )
        return f"{type(self).__name__}({s})"

    def _get_attributes(self, ignore: bool = False) -> Dict[str, Any]:
        """Returns the non-positional attributes of a Generic instance."""
        attrs = {}
        for attr, values in inspect.getmembers(self):
            if attr.startswith("_") or attr in ["query"] or inspect.ismethod(values):
                continue
            if ignore and values:
                attrs[attr] = type(values)()
            else:
                attrs[attr] = values
        return attrs

    def _get_pos_attributes(self) -> List[Any]:
        """Return the positional attributes of a Generic instance."""
        return []

    def __and__(self, other):
        attrs = self._get_attributes(ignore=True)
        if self == other:
            for attr in attrs.keys():
                self_values = getattr(self, attr)
                other_values = deepcopy(getattr(other, attr))
                if self_values is None:
                    continue
                if isinstance(self_values, list):
                    if not isinstance(other_values, list):
                        other_values = [other_values]
                    for value in self_values:
                        if value in other_values:
                            attrs[attr].append(value)
                            other_values.pop(other_values.index(value))
                else:
                    if isinstance(other_values, list):
                        attrs[attr] = self_values if self_values in other_values else None
                    else:
                        attrs[attr] = self_values if self_values == other_values else None

        pos_args = self._get_pos_attributes()

        return type(self)(*pos_args, **attrs)

    def __len__(self) -> int:
        attrs = self._get_attributes()
        _len = 0
        for values in attrs.values():
            if not values:
                continue
            _len += len(values) if isinstance(values, list) else 1

        return _len

    def exists_in(self, text: str):
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

        attrs = self._get_attributes(ignore=True)
        for attr in attrs.keys():
            self_values = getattr(self, attr)
            if self_values:
                if isinstance(self_values, list):
                    for value in self_values:
                        if value.lower() in text:
                            attrs[attr].append(value)
                else:
                    if self_values.lower() in text:
                        attrs[attr] = self_values

        pos_args = self._get_pos_attributes()

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

        raise IndexError("Generic template does not support this function yet")

    def assert_typing_constraints(self) -> bool:
        import typing

        def check_types(var: Any, _type: TypeVar) -> Tuple[bool, Any]:
            if _type is type(None):
                return (var is None, var)
            elif isinstance(_type, type):
                is_correct = isinstance(var, _type)
                if not is_correct:
                    if isinstance(var, list):
                        var = var[0] if len(var) else _type()
                    var = _type(var)
                return (is_correct, var)
            # elif _type is type(None):
            #     return (var is None, var)
            elif isinstance(_type, typing._GenericAlias):
                origin = _type.__origin__
                if origin is typing.Union:
                    is_correct = False
                    _var = None
                    for _t in _type.__args__:
                        _is_correct, tmp_var = check_types(var, _t)
                        if _is_correct:
                            return (_is_correct, tmp_var)
                        if _t is not type(None):
                            _var = tmp_var
                        is_correct |= _is_correct
                    # return any(check_types(var, _t) for _t in _type.__args__)
                    return (is_correct, _var)
                elif origin is list:
                    if not isinstance(var, list):
                        var = [var]
                    for _t in _type.__args__:
                        _var = []
                        is_correct = True
                        for v in var:
                            _is_correct, v = check_types(v, _t)
                            is_correct &= _is_correct
                            _var.append(v)
                        if is_correct:
                            return (is_correct, _var if len(_var) else None)

                    return (is_correct, _var)
                    # return any(all(check_types(v, _t) for v in var) if isinstance(var, list) else False for _t in _type.__args__)
                elif any(issubclass(origin, _t) for _t in [str, int, float, bool]):
                    return check_types(var, origin)
                else:
                    raise ValueError(f"Unsupported type: {origin}")
            else:
                raise ValueError("Only native types or typing module types are supported.")

        correct = True
        for field in dataclasses.fields(self):
            _correct, value = check_types(getattr(self, field.name), field.type)
            correct &= _correct
            setattr(self, field.name, value)

        return correct


class AnnotationList(list):
    """
    A class that handles the list of system outputs.

    Args:
        list (List[Any]):
            List of annotations generated by the system.
    """

    SIMPLE_TYPES = [Entity, Value, Relation]
    COMPLEX_TYPES = [Event, Template]

    def __init__(self, elems: List[Any], hallucinated_no: int = 0, parse_error: bool = False):
        self._hallucinated_no = hallucinated_no
        self._parse_error = parse_error
        super().__init__(elems)

    @property
    def hallucinated_no(self) -> int:
        return self._hallucinated_no

    @property
    def parse_error(self) -> bool:
        return self._parse_error

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

        return type(self)(_elems, hallucinated_no=len(self) - len(_elems), parse_error=self.parse_error)

    def assert_typing_constraints(self) -> None:
        for elem in self:
            if hasattr(elem, "assert_typing_constraints"):
                elem.assert_typing_constraints()

    @classmethod
    def from_output(
        cls,
        ann: str,
        task_module: str,
        text: str = None,
        filter_hallucinations: bool = False,
        assert_typing_constraints: bool = True,
    ) -> AnnotationList:
        # Import guidelines
        guidelines = cls._load_guidelines(task_module)
        locals().update(guidelines)

        reading = True
        parse_error = False
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
                parse_error = True

        self = cls(_elems, parse_error=parse_error)

        if filter_hallucinations:
            if text is None:
                raise ValueError("To filter the hallucinations the text argument must not be None.")
            self = self.filter_hallucinations(text)

        if assert_typing_constraints:
            self.assert_typing_constraints()

        return self

    @classmethod
    def from_gold(
        cls,
        ann: str,
        task_module: str,
        text: str = None,
        filter_hallucinations: bool = False,
        assert_typing_constraints: bool = True,
    ) -> AnnotationList:
        # Import guidelines
        guidelines = cls._load_guidelines(task_module)
        locals().update(guidelines)

        # Remove malformed elements
        _elems = []
        pase_error = False
        for elem in eval(ann):
            try:
                elem = eval(elem)
                _elems.append(elem)
            except SyntaxError:
                logging.warning(f"Found an incorrectly formatted gold: {elem}")
                pase_error = True

        self = cls(_elems, parse_error=pase_error)

        if filter_hallucinations:
            if text is None:
                raise ValueError("To filter the hallucinations the text argument must not be None.")
            self = self.filter_hallucinations(text)

        if assert_typing_constraints:
            self.assert_typing_constraints()

        return self

    def to_string(self) -> str:
        return str(self)
