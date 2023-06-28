from typing import List

from ..utils_typing import Entity, dataclass


"""Entity definitions

The entity definitions are derived from the official Multi-NERD guidelines:
https://aclanthology.org/2022.findings-naacl.60.pdf

"""


@dataclass
class Person(Entity):
    """{multinerd_person}"""

    span: str


@dataclass
class Organization(Entity):
    """{multinerd_organization}"""

    span: str


@dataclass
class Location(Entity):
    """{multinerd_location}"""

    span: str


@dataclass
class Animal(Entity):
    """{multinerd_animal}"""

    span: str


@dataclass
class Biological(Entity):
    """{multinerd_biological}"""

    span: str


@dataclass
class Celestial(Entity):
    """{multinerd_celestial}"""

    span: str


@dataclass
class Disease(Entity):
    """{multinerd_disease}"""

    span: str


@dataclass
class Event(Entity):
    """{multinerd_event}"""

    span: str


@dataclass
class Food(Entity):
    """{multinerd_food}"""

    span: str


@dataclass
class Instrument(Entity):
    """{multinerd_instrument}"""

    span: str


@dataclass
class Media(Entity):
    """{multinerd_media}"""

    span: str


@dataclass
class Plant(Entity):
    """{multinerd_plant}"""

    span: str


@dataclass
class Mythological(Entity):
    """{multinerd_mythological}"""

    span: str


@dataclass
class Time(Entity):
    """{multinerd_time}"""

    span: str


@dataclass
class Vehicle(Entity):
    """{multinerd_vehicle}"""

    span: str


ENTITY_DEFINITIONS: List[Entity] = [
    Person,
    Location,
    Organization,
    Animal,
    Biological,
    Celestial,
    Disease,
    Event,
    Food,
    Instrument,
    Media,
    Plant,
    Mythological,
    Time,
    Vehicle,
]

# __all__ = list(map(str, [*ENTITY_DEFINITIONS]))
