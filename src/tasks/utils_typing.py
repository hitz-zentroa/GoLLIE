from __future__ import annotations
from dataclasses import dataclass as org_dataclass
import inspect
from copy import deepcopy


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


@dataclass
class Entity:
    """A general class to represent entities."""

    span: str

    def __eq__(self: Entity, other: Entity) -> bool:
        self_span = self.span.lower().strip()
        other_span = other.span.lower().strip()
        return type(self) == type(other) and self_span == other_span

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


@dataclass
class Value:
    """A general class to represent values."""

    span: str

    def __eq__(self: Value, other: Value) -> bool:
        return type(self) == type(other) and self.span == other.span

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


@dataclass
class Relation:
    """A general class to represent relations."""

    arg1: str
    arg2: str

    def __eq__(self: Value, other: Value) -> bool:
        return (
            type(self) == type(other)
            and self.arg1 == other.arg1
            and self.arg2 == other.arg2
        )

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
            if not (
                attr.startswith("__")
                or attr in ["mention", "subtype"]
                or inspect.ismethod(values)
            )
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
            if not (
                attr.startswith("__")
                or attr in ["mention", "subtype"]
                or inspect.ismethod(values)
            )
        }
        _len = 0
        for values in attrs.values():
            _len += len(values)

        return _len

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
        return True  # TODO: implement exists_in for Event
