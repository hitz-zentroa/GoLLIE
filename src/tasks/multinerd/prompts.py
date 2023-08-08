from typing import List

from ..utils_typing import Entity, dataclass


"""Entity definitions

The entity definitions are derived from the official Multi-NERD guidelines:
https://aclanthology.org/2022.findings-naacl.60.pdf

"""


@dataclass
class Person(Entity):
    """{multinerd_person}"""

    span: str  # {multinerd_person_examples}


@dataclass
class Organization(Entity):
    """{multinerd_organization}"""

    span: str  # {multinerd_organization_examples}


@dataclass
class Location(Entity):
    """{multinerd_location}"""

    span: str  # {multinerd_location_examples}


@dataclass
class Animal(Entity):
    """{multinerd_animal}"""

    span: str  # {multinerd_animal_examples}


@dataclass
class Biological(Entity):
    """{multinerd_biological}"""

    span: str  # {multinerd_biological_examples}


@dataclass
class Celestial(Entity):
    """{multinerd_celestial}"""

    span: str  # {multinerd_celestial_examples}


@dataclass
class Disease(Entity):
    """{multinerd_disease}"""

    span: str  # {multinerd_disease_examples}


@dataclass
class Event(Entity):
    """{multinerd_event}"""

    span: str  # {multinerd_event_examples}


@dataclass
class Food(Entity):
    """{multinerd_food}"""

    span: str  # {multinerd_food_examples}


@dataclass
class Instrument(Entity):
    """{multinerd_instrument}"""

    span: str  # {multinerd_instrument_examples}


@dataclass
class Media(Entity):
    """{multinerd_media}"""

    span: str  # {multinerd_media_examples}


@dataclass
class Plant(Entity):
    """{multinerd_plant}"""

    span: str  # {multinerd_plant_examples}


@dataclass
class Mythological(Entity):
    """{multinerd_mythological}"""

    span: str  # {multinerd_mythological_examples}


@dataclass
class Time(Entity):
    """{multinerd_time}"""

    span: str  # {multinerd_time_examples}


@dataclass
class Vehicle(Entity):
    """{multinerd_vehicle}"""

    span: str  # {multinerd_vehicle_examples}


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
