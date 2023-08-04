from typing import List

from ..utils_typing import Entity, dataclass


"""Entity definitions

The entity definitions are derived from the official CrossNER corpus guidelines:
https://arxiv.org/pdf/2012.04373.pdf

"""


@dataclass
class Field(Entity):
    """{crossner_ai_field}"""

    span: str


@dataclass
class Task(Entity):
    """{crossner_ai_task}"""

    span: str


@dataclass
class Product(Entity):
    """{crossner_ai_product}"""

    span: str


@dataclass
class Algorithm(Entity):
    """{crossner_ai_algorithm}"""

    span: str


@dataclass
class Researcher(Entity):
    """{crossner_ai_researcher}"""

    span: str


@dataclass
class Metric(Entity):
    """{crossner_ai_metric}"""

    span: str


@dataclass
class University(Entity):
    """{crossner_ai_university}"""

    span: str


@dataclass
class Country(Entity):
    """{crossner_ai_country}"""

    span: str


@dataclass
class Person(Entity):
    """{crossner_ai_person}"""

    span: str


@dataclass
class Organization(Entity):
    """{crossner_ai_organization}"""

    span: str


@dataclass
class Location(Entity):
    """{crossner_ai_location}"""

    span: str


@dataclass
class ProgrammingLanguage(Entity):
    """{crossner_ai_programminglanguage}"""

    span: str


@dataclass
class Conference(Entity):
    """{crossner_ai_conference}"""

    span: str


@dataclass
class Miscellaneous(Entity):
    """{crossner_ai_miscellaneous}"""

    span: str


ENTITY_DEFINITIONS_AI: List[Entity] = [
    Field,
    Task,
    Product,
    Algorithm,
    Researcher,
    Metric,
    University,
    Country,
    Person,
    Organization,
    Location,
    ProgrammingLanguage,
    Conference,
    Miscellaneous,
]

# __all__ = list(map(str, [*ENTITY_DEFINITIONS]))
