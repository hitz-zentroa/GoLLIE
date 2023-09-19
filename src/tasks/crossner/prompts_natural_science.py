from typing import List

from ..utils_typing import Entity, dataclass


"""Entity definitions

The entity definitions are derived from the official CrossNER corpus guidelines:
https://arxiv.org/pdf/2012.04373.pdf

"""


@dataclass
class Scientist(Entity):
    """{crossner_naturalscience_scientist}"""

    span: str  # {crossner_naturalscience_scientist_examples}


@dataclass
class Person(Entity):
    """{crossner_naturalscience_person}"""

    span: str  # {crossner_naturalscience_person_examples}


@dataclass
class University(Entity):
    """{crossner_naturalscience_university}"""

    span: str  # {crossner_naturalscience_university_examples}


@dataclass
class Organization(Entity):
    """{crossner_naturalscience_organization}"""

    span: str  # {crossner_naturalscience_organization_examples}


@dataclass
class Country(Entity):
    """{crossner_naturalscience_country}"""

    span: str  # {crossner_naturalscience_country_examples}


@dataclass
class Location(Entity):
    """{crossner_naturalscience_location}"""

    span: str  # {crossner_naturalscience_location_examples}


@dataclass
class Discipline(Entity):
    """{crossner_naturalscience_discipline}"""

    span: str  # {crossner_naturalscience_discipline_examples}


@dataclass
class Enzyme(Entity):
    """{crossner_naturalscience_enzyme}"""

    span: str  # {crossner_naturalscience_enzyme_examples}


@dataclass
class Protein(Entity):
    """{crossner_naturalscience_protein}"""

    span: str  # {crossner_naturalscience_protein_examples}


@dataclass
class ChemicalElement(Entity):
    """{crossner_naturalscience_chemicalelement}"""

    span: str  # {crossner_naturalscience_chemicalelement_examples}


@dataclass
class ChemicalCompound(Entity):
    """{crossner_naturalscience_chemicalcompound}"""

    span: str  # {crossner_naturalscience_chemicalcompound_examples}


@dataclass
class AstronomicalObject(Entity):
    """{crossner_naturalscience_astronomicalobject}"""

    span: str  # {crossner_naturalscience_astronomicalobject_examples}


@dataclass
class AcademicJournal(Entity):
    """{crossner_naturalscience_academicjournal}"""

    span: str  # {crossner_naturalscience_academicjournal_examples}


@dataclass
class Event(Entity):
    """{crossner_naturalscience_event}"""

    span: str  # {crossner_naturalscience_event_examples}


@dataclass
class Theory(Entity):
    """{crossner_naturalscience_theory}"""

    span: str  # {crossner_naturalscience_theory_examples}


@dataclass
class Award(Entity):
    """{crossner_naturalscience_award}"""

    span: str  # {crossner_naturalscience_award_examples}


@dataclass
class Other(Entity):
    """{crossner_naturalscience_miscellaneous}"""

    span: str  # {crossner_naturalscience_miscellaneous_examples}


ENTITY_DEFINITIONS_NATURAL_SCIENCE: List[Entity] = [
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
    Other,
]

ENTITY_DEFINITIONS_NATURAL_SCIENCE_woMISC: List[Entity] = [
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
]

# __all__ = list(map(str, [*ENTITY_DEFINITIONS]))
