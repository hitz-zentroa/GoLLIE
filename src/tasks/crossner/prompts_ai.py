from typing import List

from ..utils_typing import Entity, dataclass


"""Entity definitions

The entity definitions are derived from the official CrossNER corpus guidelines:
https://arxiv.org/pdf/2012.04373.pdf

"""


@dataclass
class Field(Entity):
    """{crossner_ai_field}"""

    span: str  # {crossner_ai_field_examples}


@dataclass
class Task(Entity):
    """{crossner_ai_task}"""

    span: str  # {crossner_ai_task_examples}


@dataclass
class Product(Entity):
    """{crossner_ai_product}"""

    span: str  # {crossner_ai_product_examples}


@dataclass
class Algorithm(Entity):
    """{crossner_ai_algorithm}"""

    span: str  # {crossner_ai_algorithm_examples}


@dataclass
class Researcher(Entity):
    """{crossner_ai_researcher}"""

    span: str  # {crossner_ai_researcher_examples}


@dataclass
class Metric(Entity):
    """{crossner_ai_metric}"""

    span: str  # {crossner_ai_metric_examples}


@dataclass
class University(Entity):
    """{crossner_ai_university}"""

    span: str  # {crossner_ai_university_examples}


@dataclass
class Country(Entity):
    """{crossner_ai_country}"""

    span: str  # {crossner_ai_country_examples}


@dataclass
class Person(Entity):
    """{crossner_ai_person}"""

    span: str  # {crossner_ai_person_examples}


@dataclass
class Organization(Entity):
    """{crossner_ai_organization}"""

    span: str  # {crossner_ai_organization_examples}


@dataclass
class Location(Entity):
    """{crossner_ai_location}"""

    span: str  # {crossner_ai_location_examples}


@dataclass
class ProgrammingLanguage(Entity):
    """{crossner_ai_programminglanguage}"""

    span: str  # {crossner_ai_programminglanguage_examples}


@dataclass
class Conference(Entity):
    """{crossner_ai_conference}"""

    span: str  # {crossner_ai_conference_examples}


@dataclass
class Other(Entity):
    """{crossner_ai_miscellaneous}"""

    span: str  # {crossner_ai_miscellaneous_examples}


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
    Other,
]

ENTITY_DEFINITIONS_AI_woMISC: List[Entity] = [
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
]


# __all__ = list(map(str, [*ENTITY_DEFINITIONS]))
