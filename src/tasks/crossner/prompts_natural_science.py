from ..utils_typing import Entity, dataclass


"""Entity definitions

The entity definitions are derived from the official CrossNER corpus guidelines:
https://arxiv.org/pdf/2012.04373.pdf

"""


@dataclass
class Scientist(Entity):
    """{crossner_naturalscience_scientist}"""

    span: str


@dataclass
class Person(Entity):
    """{crossner_naturalscience_person}"""

    span: str


@dataclass
class University(Entity):
    """{crossner_naturalscience_university}"""

    span: str


@dataclass
class Organization(Entity):
    """{crossner_naturalscience_organization}"""

    span: str


@dataclass
class Country(Entity):
    """{crossner_naturalscience_country}"""

    span: str


@dataclass
class Location(Entity):
    """{crossner_naturalscience_location}"""

    span: str


@dataclass
class Discipline(Entity):
    """{crossner_naturalscience_discipline}"""

    span: str


@dataclass
class Enzyme(Entity):
    """{crossner_naturalscience_enzyme}"""

    span: str


@dataclass
class Protein(Entity):
    """{crossner_naturalscience_protein}"""

    span: str


@dataclass
class ChemicalElement(Entity):
    """{crossner_naturalscience_chemicalelement}"""

    span: str


@dataclass
class ChemicalCompound(Entity):
    """{crossner_naturalscience_chemicalcompound}"""

    span: str


@dataclass
class AstronomicalObject(Entity):
    """{crossner_naturalscience_astronomicalobject}"""

    span: str


@dataclass
class AcademicJournal(Entity):
    """{crossner_naturalscience_academicjournal}"""

    span: str


@dataclass
class Event(Entity):
    """{crossner_naturalscience_event}"""

    span: str


@dataclass
class Theory(Entity):
    """{crossner_naturalscience_theory}"""

    span: str


@dataclass
class Award(Entity):
    """{crossner_naturalscience_award}"""

    span: str


@dataclass
class Miscellaneous(Entity):
    """{crossner_naturalscience_miscellaneous}"""

    span: str


ENTITY_DEFINITIONS_NATURAL_SCIENCE = [
    Scientist,
    Person,
    University,
    Organization,
    Country,
    Location,
    Discipline,
    Enzyme,
    Protein,
    ChemicalElement,
    ChemicalCompound,
    AstronomicalObject,
    AcademicJournal,
    Event,
    Theory,
    Award,
    Miscellaneous,
]

# __all__ = list(map(str, [*ENTITY_DEFINITIONS]))
