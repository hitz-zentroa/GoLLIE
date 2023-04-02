from typing import Dict, List, Type

from src.tasks.utils_typing import Entity, Value

from .prompts import ENTITY_DEFINITIONS, VALUE_DEFINITIONS, EVENT_DEFINITIONS
from ..utils_scorer import RelationScorer, SpanScorer, EventScorer


class ACEEntityScorer(SpanScorer):
    """ACE Entity identification and classification scorer."""

    valid_types: List[Type] = ENTITY_DEFINITIONS

    def __call__(
        self, reference: List[Entity], predictions: List[Entity]
    ) -> Dict[str, Dict[str, float]]:
        output = super().__call__(reference, predictions)
        return {"entities": output["spans"]}


class ACEValueScorer(SpanScorer):
    """ACE Values identification and classification scorer."""

    valid_types: List[Type] = VALUE_DEFINITIONS

    def __call__(
        self, reference: List[Value], predictions: List[Value]
    ) -> Dict[str, Dict[str, float]]:
        output = super().__call__(reference, predictions)
        return {"values": output["spans"]}


class ACERelationScorer(RelationScorer):
    """ACE Relation identification and classification scorer."""

    valid_types: List[Type] = EVENT_DEFINITIONS


class ACEEventScorer(EventScorer):
    """ACE Event and argument classification scorer."""

    valid_types: List[Type] = EVENT_DEFINITIONS
