from typing import Dict, List
from copy import deepcopy

from .prompts import ENTITY_DEFINITIONS
from ..utils import Scorer, Entity


class ACEEntityScorer(Scorer):
    valid_types: List[Entity] = ENTITY_DEFINITIONS

    def __call__(
        self, reference: List[Entity], predictions: List[Entity]
    ) -> Dict[str, float]:
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
            total_pos += len(ref)
            total_pre += len(pre)

            ref = deepcopy(ref)
            for entity in pre:
                if type(entity) not in self.valid_types:
                    continue
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
