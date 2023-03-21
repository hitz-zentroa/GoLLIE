from dataclasses import dataclass


@dataclass
class Person:
    """This class is used to instantiate persons, human beings."""

    span: str


ENTITY_DEFINITIONS = [Person]
