from typing import List

from ..utils_typing import Entity, dataclass


"""Entity definitions

The entity definitions are derived from the official OntoNotes 5.0 guidelines:
https://catalog.ldc.upenn.edu/docs/LDC2013T19/OntoNotes-Release-5.0.pdf
"""


@dataclass
class Person(Entity):
    """{ontonotes_person}"""

    span: str


@dataclass
class NORP(Entity):
    """{ontonotes_norp}"""

    span: str


@dataclass
class Facility(Entity):
    """{ontonotes_facility}"""

    span: str


@dataclass
class Organization(Entity):
    """{ontonotes_organization}"""

    span: str


@dataclass
class GPE(Entity):
    """{ontonotes_gpe}"""

    span: str


@dataclass
class Location(Entity):
    """{ontonotes_location}"""

    span: str


@dataclass
class Product(Entity):
    """{ontonotes_product}"""

    span: str


@dataclass
class Event(Entity):
    """{ontonotes_event}"""

    span: str


@dataclass
class WorkOfArt(Entity):
    """{ontonotes_work_of_art}"""

    span: str


@dataclass
class Law(Entity):
    """{ontonotes_law}"""

    span: str


@dataclass
class Language(Entity):
    """{ontonotes_language}"""

    span: str


@dataclass
class Date(Entity):
    """{ontonotes_date}"""

    span: str


@dataclass
class Time(Entity):
    """{ontonotes_time}"""

    span: str


@dataclass
class Percentage(Entity):
    """{ontonotes_percent}"""

    span: str


@dataclass
class Money(Entity):
    """{ontonotes_money}"""

    span: str


@dataclass
class Quantity(Entity):
    """{ontonotes_quantity}"""

    span: str


@dataclass
class Ordinal(Entity):
    """{ontonotes_ordinal}"""

    span: str


@dataclass
class Cardinal(Entity):
    """{ontonotes_cardinal}"""

    span: str


ENTITY_DEFINITIONS: List[Entity] = [
    Person,
    Organization,
    Location,
    NORP,
    Facility,
    GPE,
    Product,
    Event,
    WorkOfArt,
    Law,
    Language,
    Date,
    Time,
    Percentage,
    Money,
    Quantity,
    Ordinal,
    Cardinal,
]

# __all__ = list(map(str, [*ENTITY_DEFINITIONS]))
