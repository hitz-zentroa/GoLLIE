from typing import Any, Dict, List, Type

from typing_extensions import override

from src.tasks.casie.prompts_eae import EAE_EVENT_DEFINITIONS
from src.tasks.casie.prompts_ed import ED_EVENT_DEFINITIONS
from src.tasks.utils_scorer import EventScorer


class CASIEEventScorer(EventScorer):
    """CASIE Event and argument classification scorer."""

    valid_types: List[Type] = ED_EVENT_DEFINITIONS

    def __init__(self, allow_partial_match: bool = True) -> None:
        super().__init__()

        self.allow_partial_match: bool = allow_partial_match

    @override
    def __call__(self, reference: Any, predictions: Any) -> Dict[str, Dict[str, float]]:
        if not len(reference) or (len(reference) and not isinstance(reference[0], list)):
            reference = [reference]
        if not len(predictions) or (len(predictions) and not isinstance(predictions[0], list)):
            predictions = [predictions]

        for ref in reference:
            for ref in ref:
                ref._allow_partial_match = self.allow_partial_match
        for pred in predictions:
            for pred in pred:
                pred._allow_partial_match = self.allow_partial_match

        return super().__call__(reference, predictions)


class CASIEEventArgumentScorer(EventScorer):
    """CASIE Event and argument classification scorer."""

    valid_types: List[Type] = EAE_EVENT_DEFINITIONS

    def __init__(self, allow_partial_match: bool = True) -> None:
        super().__init__()

        self.allow_partial_match: bool = allow_partial_match

    @override
    def __call__(self, reference: Any, predictions: Any) -> Dict[str, Dict[str, float]]:
        if not len(reference) or (len(reference) and not isinstance(reference[0], list)):
            reference = [reference]
        if not len(predictions) or (len(predictions) and not isinstance(predictions[0], list)):
            predictions = [predictions]

        for ref in reference:
            for ref in ref:
                ref._allow_partial_match = self.allow_partial_match
        for pred in predictions:
            for pred in pred:
                pred._allow_partial_match = self.allow_partial_match

        return super().__call__(reference, predictions)
