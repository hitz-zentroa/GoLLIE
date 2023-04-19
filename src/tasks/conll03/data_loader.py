from typing import Tuple, Union

from datasets import load_dataset

from src.tasks.conll03.prompts import (
    ENTITY_DEFINITIONS,
    Location,
    Miscellaneous,
    Organization,
    Person,
)
from src.tasks.label_encoding import rewrite_labels

from ..utils_data import DatasetLoader, Sampler


class CoNLLDatasetLoader(DatasetLoader):
    """
    A `DatasetLoader` for the ConLL03 dataset.

    Args:
        split (`str`):
            The split to load. Can be one of `train`, `validation` or `test`.
        include_misc (`str`, optional):
            Whether to include the MISC entity type. Defaults to `True`.

    Raises:
        `ValueError`:
            raised when a not defined value found.
    """

    ENTITY_TO_CLASS_MAPPING = {
        "LOC": Location,
        "ORG": Organization,
        "PER": Person,
        "MISC": Miscellaneous,
    }

    def __init__(self, split: str, include_misc: bool = True, **kwargs) -> None:
        self.elements = {}

        assert split in [
            "train",
            "validation",
            "test",
        ], f"Split {split} not found, should be one of train, validation or test."

        dataset = load_dataset("conll2003")
        id2label = {v: k for k, v in dataset["train"].features["ner_tags"].feature.names.items()}
        for example in dataset[split]:
            words = example["tokens"]
            # Some of the CoNLL02-03 datasets are in IOB1 format instead of IOB2,
            # we convert them to IOB2, so we don't have to deal with this later.
            labels = rewrite_labels(labels=[id2label[label] for label in example["ner_tags"]], encoding="iob2")

            # Get labeled word spans
            spans = []
            for i, label in enumerate(labels):
                if label == "O":
                    continue
                elif label.startswith("B-"):
                    spans.append((label[2:], i, i + 1))
                elif label.startswith("I-"):
                    spans[-1][2] += 1
                else:
                    raise ValueError(f"Found an unexpected label: {label}")

            # Get entities
            entities = []
            for label, start, end in spans:
                if include_misc or label != "MISC":
                    entities.append(self.ENTITY_TO_CLASS_MAPPING[label](span=" ".join(words[start:end])))

            self.elements[example["id"]] = {
                "id": example["id"],
                "doc_id": example["id"],
                "text": " ".join(words),
                "labels": entities,
            }


class CONLL03Sampler(Sampler):
    """
    A data `Sampler` for the CONLL03 dataset.

    Args:
        dataset_loader (`CoNLLDatasetLoader`):
            The dataset loader that contains the data information.
        task (`str`, optional):
            The task to sample. It must be one of the following: NER, VER, RE, EE.
            Defaults to `None`.
        split (`str`, optional):
            The split to sample. It must be one of the following: "train", "dev" or
            "test". Depending on the split the sampling strategy differs. Defaults to
            `"train"`.
        parallel_instances (`Union[int, Tuple[int, int]]`, optional):
            The number of sentences sampled in parallel. Options:

                * **`int`**: The amount of elements that will be sampled in parallel.
                * **`tuple`**: The range of elements that will be sampled in parallel.

            Defaults to 1.
        max_guidelines (`int`, optional):
            The number of guidelines to append to the example at the same time. If `-1`
            is given then all the guidelines are appended. Defaults to `-1`.
        guideline_dropout (`float`, optional):
            The probability to dropout a guideline definition for the given example. This
            is only applied on training. Defaults to `0.0`.
        seed (`float`, optional):
            The seed to sample the examples. Defaults to `0`.
        prompt_template (`str`, optional):
            The path to the prompt template. Defaults to `"templates/prompt.txt"`.
        ensure_positives_on_train (bool, optional):
            Whether to ensure that the guidelines of annotated examples are not removed.
            Defaults to `True`.
        dataset_name (str, optional):
            The name of the dataset. Defaults to `None`.
        scorer (`str`, optional):
           The scorer class import string. Defaults to `None`.
        sample_only_gold_guidelines (`bool`, optional):
            Whether to sample only guidelines of present annotations. Defaults to `False`.
    """

    def __init__(
        self,
        dataset_loader: CoNLLDatasetLoader,
        task: str = None,
        split: str = "train",
        parallel_instances: Union[int, Tuple[int, int]] = 1,
        max_guidelines: int = -1,
        guideline_dropout: float = 0.0,
        seed: float = 0,
        prompt_template: str = "templates/prompt.txt",
        ensure_positives_on_train: bool = True,
        dataset_name: str = None,
        scorer: str = None,
        sample_only_gold_guidelines: bool = False,
        **kwargs,
    ) -> None:
        assert task in [
            "NER",
        ], f"CoNLL03 only supports NER task. {task} is not supported."

        task_definitions, task_target = {
            "NER": (ENTITY_DEFINITIONS, "entities"),
        }[task]

        super().__init__(
            dataset_loader=dataset_loader,
            task=task,
            split=split,
            parallel_instances=parallel_instances,
            max_guidelines=max_guidelines,
            guideline_dropout=guideline_dropout,
            seed=seed,
            prompt_template=prompt_template,
            ensure_positives_on_train=ensure_positives_on_train,
            sample_only_gold_guidelines=sample_only_gold_guidelines,
            dataset_name=dataset_name,
            scorer=scorer,
            task_definitions=task_definitions,
            task_target=task_target,
            **kwargs,
        )
