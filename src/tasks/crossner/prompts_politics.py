from typing import List

from ..utils_typing import Entity, dataclass


"""Entity definitions

The entity definitions are derived from the official CrossNER corpus guidelines:
https://arxiv.org/pdf/2012.04373.pdf

"""


@dataclass
class Person(Entity):
    """{crossner_politics_person}"""

    span: str


@dataclass
class Organization(Entity):
    """{crossner_politics_organization}"""

    span: str


@dataclass
class Location(Entity):
    """{crossner_politics_location}"""

    span: str


@dataclass
class Politican(Entity):
    """{crossner_politics_politician}"""

    span: str


@dataclass
class PoliticalParty(Entity):
    """{crossner_politics_politicalparty}"""

    span: str


@dataclass
class Election(Entity):
    """{crossner_politics_election}"""

    span: str


@dataclass
class Event(Entity):
    """{crossner_politics_event}"""

    span: str


@dataclass
class Country(Entity):
    """{crossner_politics_country}"""

    span: str


@dataclass
class Miscellaneous(Entity):
    """{crossner_politics_miscellaneous}"""

    span: str


ENTITY_DEFINITIONS_POLITICS: List[Entity] = [
    Person,
    Organization,
    Location,
    Politican,
    PoliticalParty,
    Election,
    Event,
    Country,
    Miscellaneous,
]

# __all__ = list(map(str, [*ENTITY_DEFINITIONS]))
