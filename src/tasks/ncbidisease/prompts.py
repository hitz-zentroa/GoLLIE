from typing import List

from ..utils_typing import Entity, dataclass


"""Entity definitions

The entity definitions are derived from the official NCBI-Disease guidelines:
https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3951655/
Disease definition from: https://en.wikipedia.org/wiki/Disease which is based on the definitions from:
 [1] "Disease" at Dorland's Medical Dictionary
 [2] White, Tim (19 December 2014). "What is the Difference Between an "Injury" and "Disease" for Comcare Commonwealth
 Compensation Claims?". Tindall Gask Bentley. Archived from the original on 27 October 2017. Retrieved 6 November 2017.


"""


@dataclass
class Disease(Entity):
    """{ncbi_disease}"""

    span: str  # {ncbi_disease_examples}


ENTITY_DEFINITIONS: List[Entity] = [Disease]

# __all__ = list(map(str, [*ENTITY_DEFINITIONS]))
