from typing import List

from ..utils_typing import Entity, dataclass


"""Entity definitions

The entity definitions are derived from the official CrossNER corpus guidelines:
https://arxiv.org/pdf/2012.04373.pdf

"""


@dataclass
class Book(Entity):
    """{crossner_literature_book}"""

    span: str  # {crossner_literature_book_examples}


@dataclass
class Writer(Entity):
    """{crossner_literature_writer}"""

    span: str  # {crossner_literature_writer_examples}


@dataclass
class Award(Entity):
    """{crossner_literature_award}"""

    span: str  # {crossner_literature_award_examples}


@dataclass
class Poem(Entity):
    """{crossner_literature_poem}"""

    span: str  # {crossner_literature_poem_examples}


@dataclass
class Event(Entity):
    """{crossner_literature_event}"""

    span: str  # {crossner_literature_event_examples}


@dataclass
class Magazine(Entity):
    """{crossner_literature_magazine}"""

    span: str  # {crossner_literature_magazine_examples}


@dataclass
class LiteraryGenre(Entity):
    """{crossner_literature_literarygenre}"""

    span: str  # {crossner_literature_literarygenre_examples}


@dataclass
class Person(Entity):
    """{crossner_literature_person}"""

    span: str  # {crossner_literature_person_examples}


@dataclass
class Location(Entity):
    """{crossner_literature_location}"""

    span: str  # {crossner_literature_location_examples}


@dataclass
class Organization(Entity):
    """{crossner_literature_organization}"""

    span: str  # {crossner_literature_organization_examples}


@dataclass
class Country(Entity):
    """{crossner_literature_country}"""

    span: str  # {crossner_literature_country_examples}


@dataclass
class Other(Entity):
    """{crossner_literature_miscellaneous}"""

    span: str  # {crossner_literature_miscellaneous_examples}


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
    Other,
]

ENTITY_DEFINITIONS_LITERATURE_woMISC: List[Entity] = [
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
]

# __all__ = list(map(str, [*ENTITY_DEFINITIONS]))
