from typing import List

from ..utils_typing import Entity, dataclass


"""Entity definitions

The entity definitions are derived from the official CrossNER corpus guidelines:
https://arxiv.org/pdf/2012.04373.pdf

"""


@dataclass
class Person(Entity):
    """{crossner_politics_person}"""

    span: str  # {crossner_politics_person_examples}


@dataclass
class Organization(Entity):
    """{crossner_politics_organization}"""

    span: str  # {crossner_politics_organization_examples}


@dataclass
class Location(Entity):
    """{crossner_politics_location}"""

    span: str  # {crossner_politics_location_examples}


@dataclass
class Politician(Entity):
    """{crossner_politics_politician}"""

    span: str  # {crossner_politics_politician_examples}


@dataclass
class PoliticalParty(Entity):
    """{crossner_politics_politicalparty}"""

    span: str  # {crossner_politics_politicalparty_examples}


@dataclass
class Election(Entity):
    """{crossner_politics_election}"""

    span: str  # {crossner_politics_election_examples}


@dataclass
class Event(Entity):
    """{crossner_politics_event}"""

    span: str  # {crossner_politics_event_examples}


@dataclass
class Country(Entity):
    """{crossner_politics_country}"""

    span: str  # {crossner_politics_country_examples}


@dataclass
class Other(Entity):
    """{crossner_politics_miscellaneous}"""

    span: str  # {crossner_politics_miscellaneous_examples}


ENTITY_DEFINITIONS_POLITICS: List[Entity] = [
    Person,
    Organization,
    Location,
    Politician,
    PoliticalParty,
    Election,
    Event,
    Country,
    Other,
]

ENTITY_DEFINITIONS_POLITICS_woMISC: List[Entity] = [
    Person,
    Organization,
    Location,
    Politician,
    PoliticalParty,
    Election,
    Event,
    Country,
]

# __all__ = list(map(str, [*ENTITY_DEFINITIONS]))
