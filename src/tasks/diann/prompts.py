from typing import List

from ..utils_typing import Entity, dataclass


"""Entity definitions

The entity definitions are derived from the official Diann guidelines:
http://nlp.uned.es/diann/#data
"""


@dataclass
class Disability(Entity):
    """{diann_disability}"""

    span: str


class Negation(Entity):
    """{diann_negation}"""

    span: str


ENTITY_DEFINITIONS: List[Entity] = [Disability, Negation]

# __all__ = list(map(str, [*ENTITY_DEFINITIONS]))