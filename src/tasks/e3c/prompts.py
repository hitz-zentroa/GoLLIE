from typing import List

from ..utils_typing import Entity, dataclass


"""Entity definitions

The entity definitions are derived from the official E3C corpus guidelines:
https://github.com/hltfbk/E3C-Corpus/blob/main/documentation/CLINICALENTITY_ANNOTATION_GUIDELINES_v1.1.pdf

"""


@dataclass
class ClinicalEntity(Entity):
    """{e3c_disease}"""

    span: str  # {e3c_disease_examples}


ENTITY_DEFINITIONS: List[Entity] = [ClinicalEntity]

# __all__ = list(map(str, [*ENTITY_DEFINITIONS]))
