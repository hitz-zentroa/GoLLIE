from typing import List

from ..utils_typing import Entity, dataclass


"""Entity definitions

The entity definitions are derived from the official Diann guidelines:
http://nlp.uned.es/diann/#data
"""


@dataclass
class Disability(Entity):
    """{diann_disability}"""

    span: str  # {diann_disability_examples}


"""
@dataclass
class Negation(Entity):
    \"""{diann_negation}\"""

    span: str  # {diann_negation_examples}
"""

ENTITY_DEFINITIONS: List[Entity] = [Disability]

# __all__ = list(map(str, [*ENTITY_DEFINITIONS]))
