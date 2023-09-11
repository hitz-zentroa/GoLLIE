from typing import Dict, List, Tuple, Type, Union

from src.tasks.conll03.data_loader import read_tsv
from src.tasks.diann.guidelines import GUIDELINES
from src.tasks.diann.guidelines_gold import EXAMPLES
from src.tasks.diann.prompts import ENTITY_DEFINITIONS, Disability  # , Negation
from src.tasks.label_encoding import rewrite_labels

from ..utils_data import DatasetLoader, Sampler
from ..utils_typing import Entity


def load_diann_tsv(
    path: str,
    include_misc: bool,
    ENTITY_TO_CLASS_MAPPING: Dict[str, Type[Entity]],
) -> Tuple[List[List[str]], List[List[Entity]]]:
    """
    Load the conll dataset from a tsv file
    REMOVE THE NEGATION LABELS
    Args:
        path (str): The path to the tsv file
        include_misc (bool): Whether to include the MISC entity type. Defaults to `True`.
    Returns:
        (List[str],List[Union[Location,Organization,Person,Miscellaneous]]): The text and the entities
    """
    dataset_sentences: List[List[str]] = []
    dataset_entities: List[List[Entity]] = []

    dataset_words, dataset_labels = read_tsv(path)

    for words, labels in zip(dataset_words, dataset_labels):
        # Some of the CoNLL02-03 datasets are in IOB1 format instead of IOB2,
        # we convert them to IOB2, so we don't have to deal with this later.
        labels = rewrite_labels(labels=labels, encoding="iob2")
        # Remove Negation labels
        for i in range(len(labels)):
            if labels[i].endswith("Neg"):
                labels[i] = "O"

        # Rewrite just in case
        labels = rewrite_labels(labels=labels, encoding="iob2")

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
            if include_misc or label.lower() != "misc":
                entities.append(ENTITY_TO_CLASS_MAPPING[label](span=" ".join(words[start:end])))

        dataset_sentences.append(words)
        dataset_entities.append(entities)

    return dataset_sentences, dataset_entities


class DiannDatasetLoader(DatasetLoader):
    """
    A `DatasetLoader` for the diann dataset.

    Args:
        path (`str`):
            The path to the dataset to load.

    Raises:
        `ValueError`:
            raised when a not defined value found.
    """

    ENTITY_TO_CLASS_MAPPING = None

    def __init__(self, path_or_split: str, **kwargs) -> None:
        self.ENTITY_TO_CLASS_MAPPING = {
            "Dis": Disability,
            # "Neg": Negation,
        }

        self.elements = {}

        dataset_words, dataset_entities = load_diann_tsv(
            path=path_or_split,
            include_misc=True,
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


class DiannSampler(Sampler):
    """
    A data `Sampler` for the Diann dataset.

    Args:
        dataset_loader (`DiannDiseaseDatasetLoader`):
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
        dataset_loader: DiannDatasetLoader,
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
        ], f"Diann Disease only supports NER task. {task} is not supported."

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
