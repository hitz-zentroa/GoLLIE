from typing import Dict, List, Type

from src.tasks.crossner.prompts_ai import ENTITY_DEFINITIONS_AI
from src.tasks.crossner.prompts_literature import ENTITY_DEFINITIONS_LITERATURE
from src.tasks.crossner.prompts_music import ENTITY_DEFINITIONS_MUSIC
from src.tasks.crossner.prompts_natural_science import ENTITY_DEFINITIONS_NATURAL_SCIENCE
from src.tasks.crossner.prompts_politics import ENTITY_DEFINITIONS_POLITICS
from src.tasks.utils_scorer import SpanScorer
from src.tasks.utils_typing import Entity


class CrossNERPoliticsEntityScorer(SpanScorer):
    """CoNLL03 Entity identification and classification scorer."""

    valid_types: List[Type] = ENTITY_DEFINITIONS_POLITICS

    def __call__(self, reference: List[Entity], predictions: List[Entity]) -> Dict[str, Dict[str, float]]:
        output = super().__call__(reference, predictions)
        return {"entities": output["spans"]}


class CrossNERMusicEntityScorer(SpanScorer):
    """CoNLL03 Entity identification and classification scorer."""

    valid_types: List[Type] = ENTITY_DEFINITIONS_MUSIC

    def __call__(self, reference: List[Entity], predictions: List[Entity]) -> Dict[str, Dict[str, float]]:
        output = super().__call__(reference, predictions)
        return {"entities": output["spans"]}


class CrossNERLiteratureEntityScorer(SpanScorer):
    """CoNLL03 Entity identification and classification scorer."""

    valid_types: List[Type] = ENTITY_DEFINITIONS_LITERATURE

    def __call__(self, reference: List[Entity], predictions: List[Entity]) -> Dict[str, Dict[str, float]]:
        output = super().__call__(reference, predictions)
        return {"entities": output["spans"]}


class CrossNERAIEntityScorer(SpanScorer):
    """CoNLL03 Entity identification and classification scorer."""

    valid_types: List[Type] = ENTITY_DEFINITIONS_AI

    def __call__(self, reference: List[Entity], predictions: List[Entity]) -> Dict[str, Dict[str, float]]:
        output = super().__call__(reference, predictions)
        return {"entities": output["spans"]}


class CrossNERNaturalScienceEntityScorer(SpanScorer):
    """CoNLL03 Entity identification and classification scorer."""

    valid_types: List[Type] = ENTITY_DEFINITIONS_NATURAL_SCIENCE

    def __call__(self, reference: List[Entity], predictions: List[Entity]) -> Dict[str, Dict[str, float]]:
        output = super().__call__(reference, predictions)
        return {"entities": output["spans"]}
