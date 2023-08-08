from typing import List

from ..utils_typing import Entity, dataclass


"""Entity definitions

The entity definitions are derived from the official BC5DR guidelines:
https://biocreative.bioinformatics.udel.edu/media/store/files/2015/bc5_CDR_data_guidelines.pdf


"""


@dataclass
class Disease(Entity):
    """{bc5cdr_disease}"""

    span: str  # {bc5cdr_disease_examples}


@dataclass
class Chemical(Entity):
    """{bc5cdr_chemical}"""

    span: str  # {bc5cdr_chemical_examples}


ENTITY_DEFINITIONS: List[Entity] = [Disease, Chemical]

# __all__ = list(map(str, [*ENTITY_DEFINITIONS]))
