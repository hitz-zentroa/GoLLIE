from typing import Any, Dict, List, Type, Union
from .utils_typing import Event, Relation, Entity, Value


class Scorer:
    """An abstract class for scorers."""

    def __call__(self, reference: Any, predictions: Any) -> Dict[str, float]:
        raise NotImplementedError("This method must be implemented.")

    def _filter_valid_types(self, elems: List[Any]) -> List[Union[Entity, Value]]:
        return [
            elem
            for elem in elems
            if any(isinstance(elem, _type) for _type in self.valid_types)
        ]


class SpanScorer(Scorer):
    """A general scorer implementation for span identification and classification
    tasks.
    """

    valid_types: List[Type] = [Entity, Value]

    def __call__(
        self,
        reference: List[Union[Entity, Value]],
        predictions: List[Union[Entity, Value]],
    ) -> Dict[str, Dict[str, float]]:
        if not len(reference) or (len(reference) and not isinstance(reference[0], list)):
            reference = [reference]
        if not len(predictions) or (
            len(predictions) and not isinstance(predictions[0], list)
        ):
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

        return {"spans": {"precision": precision, "recall": recall, "f1-score": f1_score}}


class RelationScorer(SpanScorer):
    """A general scorer implementation for relation identification and
    classification tasks
    """

    valid_types: List[Type] = [Relation]

    def __call__(
        self, reference: List[Relation], predictions: List[Relation]
    ) -> Dict[str, Dict[str, float]]:
        output = super().__call__(reference, predictions)
        return {"relations": output["spans"]}


class EventScorer(Scorer):
    """A general scorer implementation for event and argument extraction."""

    valid_types: List[Type] = [Event]

    def __call__(self, reference: Any, predictions: Any) -> Dict[str, Dict[str, float]]:
        if not len(reference) or (len(reference) and not isinstance(reference[0], list)):
            reference = [reference]
        if not len(predictions) or (
            len(predictions) and not isinstance(predictions[0], list)
        ):
            predictions = [predictions]

        assert len(reference) == len(predictions), (
            f"Reference ({len(reference)}) and prediction ({len(predictions)}) amount"
            " must be equal."
        )
        e_tp = e_total_pos = e_total_pre = 0
        a_tp = a_total_pos = a_total_pre = 0
        for ref, pre in zip(reference, predictions):
            ref = self._filter_valid_types(ref)
            pre = self._filter_valid_types(pre)

            e_total_pos += len(ref)
            for event in ref:
                a_total_pos += len(event)

            e_total_pre += len(pre)
            for pre_event in pre:
                a_total_pre += len(pre_event)
                if pre_event in ref:
                    ref_event = ref.pop(ref.index(pre_event))
                    e_tp += 1
                    a_tp += len(ref_event & pre_event)

        e_precision = e_tp / e_total_pre if e_total_pre > 0.0 else 0.0
        a_precision = a_tp / a_total_pre if a_total_pre > 0.0 else 0.0
        e_recall = e_tp / e_total_pos if e_total_pos > 0.0 else 0.0
        a_recall = a_tp / a_total_pos if a_total_pos > 0.0 else 0.0
        e_f1_score = (
            2 * e_precision * e_recall / (e_precision + e_recall)
            if (e_precision + e_recall) > 0.0
            else 0.0
        )
        a_f1_score = (
            2 * a_precision * a_recall / (a_precision + a_recall)
            if (a_precision + a_recall) > 0.0
            else 0.0
        )

        return {
            "events": {
                "precision": e_precision,
                "recall": e_recall,
                "f1-score": e_f1_score,
            },
            "arguments": {
                "precision": a_precision,
                "recall": a_recall,
                "f1-score": a_f1_score,
            },
        }
