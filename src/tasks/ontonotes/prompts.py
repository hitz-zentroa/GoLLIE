from typing import List

from ..utils_typing import Entity, dataclass


"""Entity definitions

The entity definitions are derived from the official OntoNotes 5.0 guidelines:
https://catalog.ldc.upenn.edu/docs/LDC2013T19/OntoNotes-Release-5.0.pdf
"""


@dataclass
class Person(Entity):
    """{ontonotes_person}"""

    span: str  # {ontonotes_person_examples}


@dataclass
class NORP(Entity):
    """{ontonotes_norp}"""

    span: str  # {ontonotes_norp_examples}


@dataclass
class Facility(Entity):
    """{ontonotes_facility}"""

    span: str  # {ontonotes_facility_examples}


@dataclass
class Organization(Entity):
    """{ontonotes_organization}"""

    span: str  # {ontonotes_organization_examples}


@dataclass
class GPE(Entity):
    """{ontonotes_gpe}"""

    span: str  # {ontonotes_gpe_examples}


@dataclass
class Location(Entity):
    """{ontonotes_location}"""

    span: str  # {ontonotes_location_examples}


@dataclass
class Product(Entity):
    """{ontonotes_product}"""

    span: str  # {ontonotes_product_examples}


@dataclass
class Event(Entity):
    """{ontonotes_event}"""

    span: str  # {ontonotes_event_examples}


@dataclass
class WorkOfArt(Entity):
    """{ontonotes_work_of_art}"""

    span: str  # {ontonotes_work_of_art_examples}


@dataclass
class Law(Entity):
    """{ontonotes_law}"""

    span: str  # {ontonotes_law_examples}


@dataclass
class Language(Entity):
    """{ontonotes_language}"""

    span: str  # {ontonotes_language_examples}


@dataclass
class Date(Entity):
    """{ontonotes_date}"""

    span: str  # {ontonotes_date_examples}


@dataclass
class Time(Entity):
    """{ontonotes_time}"""

    span: str  # {ontonotes_time_examples}


@dataclass
class Percentage(Entity):
    """{ontonotes_percent}"""

    span: str  # {ontonotes_percent_examples}


@dataclass
class Money(Entity):
    """{ontonotes_money}"""

    span: str  # {ontonotes_money_examples}


@dataclass
class Quantity(Entity):
    """{ontonotes_quantity}"""

    span: str  # {ontonotes_quantity_examples}


@dataclass
class Ordinal(Entity):
    """{ontonotes_ordinal}"""

    span: str  # {ontonotes_ordinal_examples}


@dataclass
class Cardinal(Entity):
    """{ontonotes_cardinal}"""

    span: str  # {ontonotes_cardinal_examples}


ENTITY_DEFINITIONS: List[Entity] = [
    Person,
    Organization,
    Location,
    NORP,
    Facility,
    GPE,
    Product,
    Event,
    WorkOfArt,
    Law,
    Language,
    Date,
    Time,
    Percentage,
    Money,
    Quantity,
    Ordinal,
    Cardinal,
]

# __all__ = list(map(str, [*ENTITY_DEFINITIONS]))
