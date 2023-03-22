from __future__ import annotations
from dataclasses import dataclass


@dataclass
class Entity:
    """A general class to represent entities."""

    span: str

    def __eq__(self: Entity, other: Entity) -> bool:
        return type(self) == type(other) and self.span == self.other


@dataclass
class Value:
    """A general class to represent values."""

    span: str

    def __eq__(self: Entity, other: Entity) -> bool:
        return type(self) == type(other) and self.span == self.other


class Relation:
    """A general class to represent relations."""

    pass


class Scorer:
    """An abstract class for scorers"""

    pass
