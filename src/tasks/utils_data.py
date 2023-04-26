import inspect
import math
import random
import re
from typing import Any, Dict, List, Tuple, Type, Union

import black
import numpy as np
from jinja2 import Template


class DatasetLoader:
    """An abstract class for dataset loaders."""

    def __iter__(self):
        for elem in self.elements.values():
            yield elem

    def __len__(self):
        return len(self.elements)

    def __getitem__(self, idx: Union[int, str]) -> Dict[str, Any]:
        if isinstance(idx, int):
            return list(self.elements.values())[idx]  # Not very efficient
        else:
            return self.elements[idx]


class Sampler:
    """
    A generic data `Sampler` class.

    Args:
        dataset_loader (`DatasetLoader`):
            The dataset loader that contains the data information.
        task (`str`, optional):
            The task to sample. Defaults to `None`.
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
        sample_total_guidelines (`int`, optional):
            The total number of guidelines to sample. If `-1` is given then all the
            guidelines are sampled. Defaults to `-1`.
        guideline_dropout (`float`, optional):
            The probability to dropout a guideline definition for the given example. This
            is only applied on training. Defaults to `0.0`.
        seed (`float`, optional):
            The seed to sample the examples. Defaults to `0`.
        prompt_template (`str`, optional):
            The path to the prompt template. Defaults to `"templates/prompt_eae.txt"`.
        ensure_positives_on_train (bool, optional):
            Whether to ensure that the guidelines of annotated examples are not removed.
            Defaults to `True`.
        dataset_name (str, optional):
            The name of the dataset. Defaults to `None`.
        scorer (`str`, optional):
           The scorer class import string. Defaults to `None`.
        sample_only_gold_guidelines (`bool`, optional):
            Whether to sample only guidelines of present annotations. Defaults to `False`.
        task_definitions (`List[Type]`, optional):
            The task definitions or guidelines. Defaults to `None`.
        task_target (`str`, optional):
            The key of the target task annotations in the dict outputed by the
            `DatasetLoader`. This is useful when the `DataLoader` returns annotations for
            different tasks. Defaults to "labels".

    Raises:
        ValueError:
            raised when no task definitions are given.
    """

    def __init__(
        self,
        dataset_loader: DatasetLoader,
        task: str = None,
        split: str = "train",
        parallel_instances: Union[int, Tuple[int, int]] = 1,
        max_guidelines: int = -1,
        sample_total_guidelines: int = -1,
        guideline_dropout: float = 0.0,
        seed: float = 0,
        prompt_template: str = "templates/prompt.txt",
        ensure_positives_on_train: bool = False,
        sample_only_gold_guidelines: bool = False,
        dataset_name: str = None,
        scorer: str = None,
        task_definitions: List[Type] = None,
        task_target: str = "labels",
        remove_guidelines: bool = False,
        **kwargs,
    ) -> None:
        self.loader = dataset_loader
        self.task = task
        assert split in [
            "train",
            "dev",
            "test",
        ], f"{split} must be either 'train', 'dev' or 'test'."
        self.split = split
        if isinstance(parallel_instances, int):
            parallel_instances = (1, parallel_instances)
        self.parallel_instances = tuple(parallel_instances)
        self.guideline_dropout = guideline_dropout
        self.seed = seed
        if not task_definitions or not len(task_definitions):
            raise ValueError("task_definitions argument must not be None or empty")
        self.task_definitions = task_definitions
        self.task_target = task_target

        if max_guidelines < 0 or max_guidelines > len(self.task_definitions):
            self.max_guidelines = len(self.task_definitions)
        else:
            self.max_guidelines = max_guidelines
        if sample_total_guidelines < 0 or sample_total_guidelines > len(self.task_definitions):
            self.sample_total_guidelines = len(self.task_definitions)
        else:
            self.sample_total_guidelines = sample_total_guidelines
        self.ensure_positives_on_train = ensure_positives_on_train
        self.sample_only_gold_guidelines = sample_only_gold_guidelines

        with open(prompt_template, "rt") as f:
            self.template = Template(f.read())

        self.dataset_name = dataset_name
        self.scorer_cls = scorer

        self._black_mode = black.Mode()
        self.remove_guidelines = remove_guidelines
        self._remove_guidelines_re = re.compile(r'"""(.+\n?)*"""')
        self._remove_comments_re = re.compile(r"#.+?\n")

    def _sample(self, instances):
        _gold = [gold for inst in instances for gold in inst["gold"]]
        if self.sample_only_gold_guidelines:
            guidelines = [
                definition
                for definition in self.task_definitions
                if any(isinstance(ann, definition) for inst in instances for ann in inst[self.task_target])
            ]
            random.shuffle(guidelines)
            splits = math.ceil(len(guidelines) / self.max_guidelines)
            for i in range(splits):
                _guidelines = guidelines[i * self.max_guidelines : (i + 1) * self.max_guidelines]
                _ann = [ann for inst in instances for ann in inst[self.task_target] if type(ann) in _guidelines]
                _text = " ".join([inst["text"] for inst in instances]).strip()

                _guidelines = [inspect.getsource(definition) for definition in _guidelines]
                if self.remove_guidelines:
                    _guidelines = [self._remove_guidelines_re.sub("", definition) for definition in _guidelines]
                    _guidelines = [self._remove_comments_re.sub("\n", definition) for definition in _guidelines]

                yield {
                    "ids": [inst["id"] for inst in instances],
                    "task_id": f"{self.dataset_name}_{self.task}",
                    "scorer_cls": self.scorer_cls,
                    "labels": black.format_str(_ann.__repr__(), mode=self._black_mode),
                    "text": black.format_str(
                        self.template.render(guidelines=_guidelines, text=_text, annotations=_ann, gold=_gold),
                        mode=self._black_mode,
                    ),
                    "unlabelled_sentence": _text,
                }
        elif self.split == "train":
            positive_guidelines = {type(ann) for inst in instances for ann in inst[self.task_target]}
            # Assign a probability distribution that helps positive classes
            # if ensure_positives_on_train is True
            p = np.asarray(
                [
                    (5.0 if _def in positive_guidelines and self.ensure_positives_on_train else 0.0)
                    for _def in self.task_definitions
                ]
            )
            p += 1.0 / p.shape[0]
            p /= p.sum()
            guidelines = np.random.choice(
                np.asarray(self.task_definitions),
                size=(self.sample_total_guidelines,),
                replace=False,
                p=p,
            ).tolist()
            splits = math.ceil(len(guidelines) / self.max_guidelines)
            for i in range(splits):
                _guidelines = guidelines[i * self.max_guidelines : (i + 1) * self.max_guidelines]
                # Apply guideline dropout
                _guidelines = [
                    _def
                    for _def in _guidelines
                    if random.random() > self.guideline_dropout
                    or (_def in positive_guidelines and self.ensure_positives_on_train)
                ]
                _ann = [ann for inst in instances for ann in inst[self.task_target] if type(ann) in _guidelines]
                _text = " ".join([inst["text"] for inst in instances]).strip()

                _guidelines = [inspect.getsource(definition) for definition in _guidelines]
                if self.remove_guidelines:
                    _guidelines = [self._remove_guidelines_re.sub("", definition) for definition in _guidelines]
                    _guidelines = [self._remove_comments_re.sub("\n", definition) for definition in _guidelines]

                yield {
                    "ids": [inst["id"] for inst in instances],
                    "task_id": f"{self.dataset_name}_{self.task}",
                    "scorer_cls": self.scorer_cls,
                    "labels": black.format_str(_ann.__repr__(), mode=self._black_mode),
                    "text": black.format_str(
                        self.template.render(guidelines=_guidelines, text=_text, annotations=_ann, gold=_gold),
                        mode=self._black_mode,
                    ),
                    "unlabelled_sentence": _text,
                }
        else:
            guidelines = list(self.task_definitions)
            random.shuffle(guidelines)
            splits = math.ceil(len(guidelines) / self.max_guidelines)
            for i in range(splits):
                _guidelines = guidelines[i * self.max_guidelines : (i + 1) * self.max_guidelines]
                _ann = [ann for inst in instances for ann in inst[self.task_target] if type(ann) in _guidelines]
                _text = " ".join([inst["text"] for inst in instances]).strip()

                _guidelines = [inspect.getsource(definition) for definition in _guidelines]
                if self.remove_guidelines:
                    _guidelines = [self._remove_guidelines_re.sub("", definition) for definition in _guidelines]
                    _guidelines = [self._remove_comments_re.sub("\n", definition) for definition in _guidelines]

                yield {
                    "ids": [inst["id"] for inst in instances],
                    "task_id": f"{self.dataset_name}_{self.task}",
                    "scorer_cls": self.scorer_cls,
                    "labels": black.format_str(_ann.__repr__(), mode=self._black_mode),
                    "text": black.format_str(
                        self.template.render(guidelines=_guidelines, text=_text, annotations=_ann, gold=_gold),
                        mode=self._black_mode,
                    ),
                    "unlabelled_sentence": _text,
                }

    def __iter__(self):
        random.seed(self.seed)
        np.random.seed(self.seed)
        instances = []
        total_inst = random.randint(*self.parallel_instances)
        prev_id = None
        for elem in self.loader:
            # Prevent mixing sentences from different documents. TODO: generalize
            if (len(instances) == total_inst) or (prev_id is not None and elem["doc_id"] != prev_id):
                for samp in self._sample(instances):
                    yield samp
                instances = []
                total_inst = random.randint(*self.parallel_instances)

            instances.append(elem)
            prev_id = elem["doc_id"]

        if len(instances):
            for samp in self._sample(instances):
                yield samp
