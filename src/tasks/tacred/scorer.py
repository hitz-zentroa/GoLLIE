from typing import List, Type

from src.tasks.tacred.prompts import TEMPLATE_DEFINITIONS
from src.tasks.utils_scorer import TemplateScorer


class TACREDTemplateScorer(TemplateScorer):
    """TACRED Template scorer."""

    valid_types: List[Type] = TEMPLATE_DEFINITIONS
