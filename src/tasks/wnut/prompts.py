from typing import List

from ..utils_typing import Entity, dataclass


"""Entity definitions

The entity definitions are derived from the official WNUT17 guidelines:
https://aclanthology.org/W17-4418.pdf


"""


@dataclass
class Person(Entity):
    """{wnut_person}"""

    span: str  # {wnut_person_examples}


@dataclass
class Location(Entity):
    """{wnut_location}"""

    span: str  # {wnut_location_examples}


@dataclass
class Corporation(Entity):
    """{wnut_corporation}"""

    span: str  # {wnut_corporation_examples}


@dataclass
class Product(Entity):
    """{wnut_product}"""

    span: str  # {wnut_product_examples}


@dataclass
class CreativeWork(Entity):
    """{wnut_creativework}"""

    span: str  # {wnut_creativework_examples}


@dataclass
class Group(Entity):
    """{wnut_group}"""

    span: str  # {wnut_group_examples}


ENTITY_DEFINITIONS: List[Entity] = [Person, Location, Corporation, Product, CreativeWork, Group]

# __all__ = list(map(str, [*ENTITY_DEFINITIONS]))
