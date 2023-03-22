from typing import List, Type

from .prompts import ENTITY_DEFINITIONS, VALUE_DEFINITIONS
from ..utils_scorer import SpanScorer


class ACEEntityScorer(SpanScorer):
    """ACE Entity identification and classification scorer."""

    valid_types: List[Type] = ENTITY_DEFINITIONS


class ACEValueScorer(SpanScorer):
    """ACE Values identification and classification scorer."""

    valid_types: List[Type] = VALUE_DEFINITIONS
