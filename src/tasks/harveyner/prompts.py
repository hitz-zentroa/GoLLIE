from typing import List

from ..utils_typing import Entity, dataclass


"""Entity definitions

The entity definitions are derived from the official harveyner guidelines:
https://aclanthology.org/2022.naacl-main.243.pdf

"""


@dataclass
class Point(Entity):
    """{harveyner_point}"""

    span: str  # {harveyner_point_examples}


class Area(Entity):
    """{harveyner_area}"""

    span: str  # {harveyner_area_examples}


class Road(Entity):
    """{harveyner_road}"""

    span: str  # {harveyner_road_examples}


class River(Entity):
    """{harveyner_river}"""

    span: str  # {harveyner_river_examples}


ENTITY_DEFINITIONS: List[Entity] = [
    Point,
    Area,
    Road,
    River,
]

# __all__ = list(map(str, [*ENTITY_DEFINITIONS]))
