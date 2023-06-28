from typing import Dict, List, Type

from src.tasks.utils_scorer import EventScorer, SpanScorer
from src.tasks.utils_typing import Entity
from src.tasks.wikievents.prompts import (
    COARSE_EVENT_DEFINITIONS,
    ENTITY_DEFINITIONS,
    EVENT_DEFINITIONS,
)


class WikiEventsEntityScorer(SpanScorer):
    """WikiEvents Entity identification and classification scorer."""

    valid_types: List[Type] = ENTITY_DEFINITIONS

    def __call__(self, reference: List[Entity], predictions: List[Entity]) -> Dict[str, Dict[str, float]]:
        output = super().__call__(reference, predictions)
        return {"entities": output["spans"]}


class WikiEventsEventScorer(EventScorer):
    """WikiEvents Event and argument classification scorer."""

    valid_types: List[Type] = COARSE_EVENT_DEFINITIONS


class WikiEventsEventArgumentScorer(EventScorer):
    """WikiEvents Event and argument classification scorer."""

    valid_types: List[Type] = EVENT_DEFINITIONS
