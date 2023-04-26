from typing import List, Type

from src.tasks.tacred.prompts import RELATION_DEFINITIONS
from src.tasks.utils_scorer import RelationScorer


class ACERelationScorer(RelationScorer):
    """ACE Relation identification and classification scorer."""

    valid_types: List[Type] = RELATION_DEFINITIONS
