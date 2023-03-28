from typing import List, Type

from .prompts import ENTITY_DEFINITIONS, VALUE_DEFINITIONS, EVENT_DEFINITIONS
from ..utils_scorer import RelationScorer, SpanScorer, EventScorer


class ACEEntityScorer(SpanScorer):
    """ACE Entity identification and classification scorer."""

    valid_types: List[Type] = ENTITY_DEFINITIONS


class ACEValueScorer(SpanScorer):
    """ACE Values identification and classification scorer."""

    valid_types: List[Type] = VALUE_DEFINITIONS


class ACERelationScorer(RelationScorer):
    """ACE Relation identification and classification scorer."""

    valid_types: List[Type] = EVENT_DEFINITIONS


class ACEEventScorer(EventScorer):
    """ACE Event and argument classification scorer."""

    valid_types: List[Type] = EVENT_DEFINITIONS
