from typing import List

from ..utils_typing import Entity, dataclass


"""Entity definitions

The entity definitions are derived from the official CrossNER corpus guidelines:
https://arxiv.org/pdf/2012.04373.pdf

"""


@dataclass
class Book(Entity):
    """{crossner_literature_book}"""

    span: str


@dataclass
class Writer(Entity):
    """{crossner_literature_writer}"""

    span: str


@dataclass
class Award(Entity):
    """{crossner_literature_award}"""

    span: str


@dataclass
class Poem(Entity):
    """{crossner_literature_poem}"""

    span: str


@dataclass
class Event(Entity):
    """{crossner_literature_event}"""

    span: str


@dataclass
class Magazine(Entity):
    """{crossner_literature_magazine}"""

    span: str


@dataclass
class LiteraryGenre(Entity):
    """{crossner_literature_literarygenre}"""

    span: str


@dataclass
class Person(Entity):
    """{crossner_literature_person}"""

    span: str


@dataclass
class Location(Entity):
    """{crossner_literature_location}"""

    span: str


@dataclass
class Organization(Entity):
    """{crossner_literature_organization}"""

    span: str


@dataclass
class Country(Entity):
    """{crossner_literature_country}"""

    span: str


@dataclass
class Miscellaneous(Entity):
    """{crossner_literature_miscellaneous}"""

    span: str


ENTITY_DEFINITIONS_LITERATURE: List[Entity] = [
    Book,
    Writer,
    Award,
    Poem,
    Event,
    Magazine,
    LiteraryGenre,
    Person,
    Location,
    Organization,
    Country,
    Miscellaneous,
]

# __all__ = list(map(str, [*ENTITY_DEFINITIONS]))
