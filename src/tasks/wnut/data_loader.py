from typing import Dict, List, Tuple, Type, Union

from src.tasks.label_encoding import rewrite_labels
from src.tasks.wnut.guidelines import GUIDELINES
from src.tasks.wnut.guidelines_gold import EXAMPLES
from src.tasks.wnut.prompts import ENTITY_DEFINITIONS, Corporation, CreativeWork, Group, Location, Person, Product

from ..utils_data import DatasetLoader, Sampler
from ..utils_typing import Entity


def get_bwnut_hf(
    split: str,
    ENTITY_TO_CLASS_MAPPING: Dict[str, Type[Entity]],
) -> Tuple[List[List[str]], List[List[Entity]]]:
    """
    Get the Wnut dataset from the huggingface datasets library
    Args:
        split (str): The path_or_split to load. Can be one of `train`, `validation` or `test`.
    Returns:
        (List[str],List[Entity]): The text and the entities
    """
    from datasets import load_dataset

    dataset = load_dataset("wnut_17")
    # Dirty fix to prevent errors reading the labels
    label_names = dataset["train"].features["ner_tags"].feature.names
    i = label_names.index("B-creative-work")
    label_names[i] = "B-creative_work"
    i = label_names.index("I-creative-work")
    label_names[i] = "I-creative_work"

    id2label = dict(enumerate(label_names))
    dataset_sentences: List[List[str]] = []
    dataset_entities: List[List[Entity]] = []

    for example in dataset[split]:
        words = example["tokens"]
        # Ensure IOB2 encoding
        labels = rewrite_labels(labels=[id2label[label] for label in example["ner_tags"]], encoding="iob2")

        # Get labeled word spans
        spans = []
        for i, label in enumerate(labels):
            if label == "O":
                continue
            elif label.startswith("B-"):
                spans.append([label[2:], i, i + 1])
            elif label.startswith("I-"):
                spans[-1][2] += 1
            else:
                raise ValueError(f"Found an unexpected label: {label}")

        # Get entities
        entities = []
        for label, start, end in spans:
            entities.append(ENTITY_TO_CLASS_MAPPING[label](span=" ".join(words[start:end])))

        dataset_sentences.append(words)
        dataset_entities.append(entities)

    return dataset_sentences, dataset_entities


class WnutDatasetLoader(DatasetLoader):
    """
    A `DatasetLoader` for the Wnut dataset.

    Args:
        split (`str`):
            The split to load. Can be one of `train`, `validation` or `test`.

    Raises:
        `ValueError`:
            raised when a not defined value found.
    """

    ENTITY_TO_CLASS_MAPPING = None

    def __init__(self, path_or_split: str, **kwargs) -> None:
        self.ENTITY_TO_CLASS_MAPPING = {
            "corporation": Corporation,
            "creative_work": CreativeWork,
            "group": Group,
            "location": Location,
            "person": Person,
            "product": Product,
        }

        self.elements = {}

        dataset_words, dataset_entities = get_bwnut_hf(
            split=path_or_split,
            ENTITY_TO_CLASS_MAPPING=self.ENTITY_TO_CLASS_MAPPING,
        )

        for id, (words, entities) in enumerate(zip(dataset_words, dataset_entities)):
            self.elements[id] = {
                "id": id,
                "doc_id": id,
                "text": " ".join(words),
                "entities": entities,
                "gold": entities,
            }


class WnutSampler(Sampler):
    """
    A data `Sampler` for the Wnut dataset.

    Args:
        dataset_loader (`WnutDatasetLoader`):
            The dataset loader that contains the data information.
        task (`str`, optional):
            The task to sample. It must be one of the following: NER, VER, RE, EE.
            Defaults to `None`.
        split (`str`, optional):
            The path_or_split to sample. It must be one of the following: "train", "dev" or
            "test". Depending on the path_or_split the sampling strategy differs. Defaults to
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
            Defaults to `False`.
        dataset_name (str, optional):
            The name of the dataset. Defaults to `None`.
        scorer (`str`, optional):
           The scorer class import string. Defaults to `None`.
        sample_only_gold_guidelines (`bool`, optional):
            Whether to sample only guidelines of present annotations. Defaults to `False`.
    """

    def __init__(
        self,
        dataset_loader: WnutDatasetLoader,
        task: str = None,
        split: str = "train",
        parallel_instances: Union[int, Tuple[int, int]] = 1,
        max_guidelines: int = -1,
        guideline_dropout: float = 0.0,
        seed: float = 0,
        prompt_template: str = "templates/prompt.txt",
        ensure_positives_on_train: bool = False,
        dataset_name: str = None,
        scorer: str = None,
        sample_only_gold_guidelines: bool = False,
        **kwargs,
    ) -> None:
        assert task in [
            "NER",
        ], f"Wnut only supports NER task. {task} is not supported."

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
            definitions=GUIDELINES,
            examples=EXAMPLES,
            **kwargs,
        )
