from copy import deepcopy
from typing import Any, Dict, List, Type, Union
from .utils_typing import Scorer, Entity, Value


class SpanScorer(Scorer):
    """A general scorer implementation for span identification and classification
    tasks.
    """
    valid_types: List[Type] = [Entity, Value]

    def __call__(self, reference: List[Union[Entity, Value]], predictions: List[Union[Entity, Value]]) -> Dict[str, float]:
        if len(reference) and not isinstance(reference[0], list):
            reference = [reference]
        if len(predictions) and not isinstance(predictions[0], list):
            predictions = [predictions]

        assert len(reference) == len(predictions), (
            f"Reference ({len(reference)}) and prediction ({len(predictions)}) amount"
            " must be equal."
        )

        tp = total_pos = total_pre = 0
        for ref, pre in zip(reference, predictions):
            ref = self._filter_valid_types(ref)
            pre = self._filter_valid_types(pre)

            total_pos += len(ref)
            total_pre += len(pre)
            for entity in pre:
                if entity in ref:
                    tp += 1
                    ref.pop(ref.index(entity))

        precision = tp / total_pre if total_pre > 0.0 else 0.0
        recall = tp / total_pos if total_pos > 0.0 else 0.0
        f1_score = (
            2 * precision * recall / (precision + recall)
            if (precision + recall) > 0.0
            else 0.0
        )

        return {"precision": precision, "recall": recall, "f1-score": f1_score}
    
    def _filter_valid_types(self, elems: List[Any]) -> List[Union[Entity, Value]]:
        return [elem for elem in elems if any(isinstance(elem, _type) for _type in self.valid_types)]