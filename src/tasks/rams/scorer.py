from typing import List, Type

from src.tasks.rams.prompts import EVENT_DEFINITIONS
from src.tasks.utils_scorer import EventScorer


class RAMSEventScorer(EventScorer):
    """RAMS Argument classification scorer."""

    valid_types: List[Type] = EVENT_DEFINITIONS
