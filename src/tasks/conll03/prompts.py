from typing import List

from ..utils_typing import Entity, dataclass


"""Entity definitions

The entity definitions are derived from the official ConLL2003 guidelines:
https://www.clips.uantwerpen.be/conll2003/ner/
Based on: Nancy Chinchor, Erica Brown, Lisa Ferro, Patty Robinson,
           "1999 Named Entity Task Definition". MITRE and SAIC, 1999.
"""


@dataclass
class Person(Entity):
    """{ner_person}"""

    span: str  # {ner_person_examples}


@dataclass
class Organization(Entity):
    """{ner_organization}"""

    span: str  # {ner_organization_examples}


@dataclass
class Location(Entity):
    """{ner_location}"""

    span: str  # {ner_location_examples}


@dataclass
class Miscellaneous(Entity):
    """{ner_miscellaneous}"""

    span: str  # {ner_miscellaneous_examples}


ENTITY_DEFINITIONS: List[Entity] = [
    Person,
    Organization,
    Location,
    Miscellaneous,
]

ENTITY_DEFINITIONS_woMISC: List[Entity] = [
    Person,
    Organization,
    Location,
]


# __all__ = list(map(str, [*ENTITY_DEFINITIONS]))
