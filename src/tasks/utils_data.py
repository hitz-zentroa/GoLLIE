import inspect
import logging
import math
import random
import re
from string import Formatter
from typing import Any, Dict, List, Set, Tuple, Type, Union

import black
import numpy as np
from jinja2 import Template

from src.tasks.utils_typing import cast_to


class DatasetLoader:
    """An abstract class for dataset loaders."""

    def __iter__(self):
        for elem in self.elements.values():
            yield elem

    def __len__(self):
        return len(self.elements)

    def __getitem__(self, idx: Union[int, str]) -> Dict[str, Any]:
        if isinstance(idx, int) or isinstance(idx, slice):
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
        remove_guidelines (`bool`, optional):
            Whether or not to remove guideline information. This is usefull for building the
            baseline. Defaults to `False`.
        is_coarse_to_fine (`bool`, optional):
            Whether or not the task is coarse_to_fine classification. Defaults to `False`.
        coarse_to_fine (`Dict[Type, List[Type]]`, optional):
            If `is_coarse_to_fine` this argument contains the information to map from coarse
            labels to fine labels. Defaults to `None`.
        fine_to_coarse (`Dict[Type, Type]`, optional):
            If `is_coarse_to_fine` this argument contains the information to map from fine
            labels to coarse labels. Defaults to `None`.
        lang (`str`, optional):
            Language of the guidelines to sample. Defaults to `"en"`.
        definitions (`Dict[str, Any]`, optional):
            Dictionary from where to sample the guideline definitions. Defaults to None.
        include_examples_prob (float, optional):
            Whether or not include examples in the guidelines. Defaults to `0.0`.
        examples (`Dict[str, Any]`, optional):
            Dictionary from where to sample the examples. Defaults to None.
        label_noise_prob (`float`, optional):
            The probability to hide the label names. Defaults to `0.0`.

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
        is_coarse_to_fine: bool = False,
        coarse_to_fine: Dict[Type, List[Type]] = None,
        fine_to_coarse: Dict[Type, Type] = None,
        lang: str = "en",
        definitions: Dict[str, Any] = None,
        include_examples_prob: float = 0.0,
        examples: Dict[str, Any] = None,
        label_noise_prob: float = 0.0,
        coarse_dropout: float = 0.0,
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
        self.coarse_dropout = coarse_dropout
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

        # Maping information for coarse --> fine tasks such as EAE or RC
        self.is_coarse_to_fine = is_coarse_to_fine
        self._coarse_to_fine = coarse_to_fine
        self._fine_to_coarse = fine_to_coarse

        self._black_mode = black.Mode()
        self.remove_guidelines = remove_guidelines
        # self._remove_guidelines_re = re.compile(r'"""(.+\n?)*"""')
        self._remove_guidelines_re = re.compile(r'"""[^"]+"""')
        self._remove_guidelines_fn = lambda x: self._remove_guidelines_re.sub("", x).replace("\n    \n", "\n")

        self._remove_comments_re = re.compile(r"#.+?\n")
        self._remove_comments_fn = lambda x: self._remove_comments_re.sub("\n", x)

        self._remove_empty_comments_re = re.compile(r"#()*\n")
        self._remove_empty_comments_fn = lambda x: self._remove_empty_comments_re.sub("\n", x)
        self._formatter = Formatter()

        self.lang = lang
        self.definitions = definitions
        if not self.definitions:
            raise ValueError("You must provide definitions for your guidelines!")
        self.include_examples_prob = include_examples_prob
        # Make 1.0 prob on example sampling in evaluation for reproducibility
        if self.include_examples_prob > 0 and self.split != "train":
            self.include_examples_prob = 1.0
        self.examples = examples
        if include_examples_prob > 0 and not self.examples:
            logging.warn(
                "`include_examples_prob` is > 0 but `examples` is None. If you want to include examples, you must"
                " provide examples. `include_examples_prob` has been changed to 0.0"
            )
            self.include_examples_prob = 0

        self.label_noise_prob = label_noise_prob
        self._class_label_re = re.compile(r"class (\w+)")

    def _sample(self, instances):
        # _gold refers to specifc gold information that is used in the template (depends on the task)
        _gold: List[Any] = [gold for inst in instances for gold in inst["gold"]]
        # positive_guidelines referst just to the guidelines definitions of the labels in the example
        positive_guidelines: Set[Type] = {type(ann) for inst in instances for ann in inst[self.task_target]}
        if self.is_coarse_to_fine:
            coarse_guidelines: Set[Type] = {self._fine_to_coarse[_def] for _def in positive_guidelines}

        guidelines: List[Type] = [*self.task_definitions]

        # The variable all_guidelines makes compatible the coarse-to-fine with normal tasks
        all_guidelines = [guidelines] if not self.is_coarse_to_fine else coarse_guidelines
        for guidelines in all_guidelines:
            if self.is_coarse_to_fine:
                if self.coarse_dropout and random.random() < self.coarse_dropout:
                    continue
                # In case of `is_coarse_to_fine` the guidelines variable is a single type
                coarse_type = guidelines
                guidelines = self._coarse_to_fine[coarse_type]

            if self.sample_only_gold_guidelines:
                # This may defer with `positive_guidelines` because we can apply this after coarse-to-fine conversion
                guidelines = [
                    definition
                    for definition in guidelines
                    if any(isinstance(ann, definition) for inst in instances for ann in inst[self.task_target])
                ]

            # Reduce the ammount of labels by sampling. We can make sure positive guidelines are sampled using `ensure_positives_on_train`
            if self.sample_total_guidelines < len(guidelines) and not self.sample_only_gold_guidelines:
                p = np.asarray(
                    [
                        (100.0 if _def in positive_guidelines and self.ensure_positives_on_train else 0.0)
                        for _def in guidelines
                    ]
                )
                p += 1.0 / p.shape[0]
                p /= p.sum()
                guidelines = np.random.choice(
                    np.asarray(guidelines),
                    size=(self.sample_total_guidelines,),
                    replace=False,
                    p=p,
                ).tolist()

            # Shuffle the guidelines
            random.shuffle(guidelines)
            # Split the guidelines according to `max_guidelines`
            splits = math.ceil(len(guidelines) / self.max_guidelines)
            for i in range(splits):
                _guidelines = guidelines[i * self.max_guidelines : (i + 1) * self.max_guidelines]
                # Apply guideline dropout
                if self.split == "train":
                    _guidelines_dropout = [
                        _def
                        for _def in _guidelines
                        if random.random() > self.guideline_dropout
                        or (_def in positive_guidelines and self.ensure_positives_on_train)
                    ]

                    if len(_guidelines_dropout) == 0 and len(_guidelines) > 0:
                        # Ensure at least one guideline is used
                        _guidelines_dropout.append(random.choice(_guidelines))
                    _guidelines = _guidelines_dropout

                _ann = [ann for inst in instances for ann in inst[self.task_target] if type(ann) in _guidelines]
                _text = " ".join([inst["text"] for inst in instances]).strip()
                # This makes the gold information useful for coarse to fine tasks
                if self.is_coarse_to_fine:
                    _gold = [cast_to(ann, coarse_type) for ann in _ann]

                # Remove the chances for hallucination because the task is classification
                if self.is_coarse_to_fine and not len(_ann):
                    continue

                _guidelines = [inspect.getsource(definition) for definition in _guidelines]
                # Apply definition paraphrases if train
                _definitions = {
                    key: random.choice(value[self.lang]) if self.split == "train" else value[self.lang][0]
                    for key, value in self.definitions.items()
                }
                # Sample few-shot examples if train (add epsilon for not sampling a 0.0)
                if min(random.random() + 1e-6, 1.0) <= self.include_examples_prob:
                    _examples = {
                        key: (
                            f"""Such as: "{'", "'.join(random.sample(value[self.lang], k=min(5,len(value[self.lang]))))}" """
                            if self.split == "train"
                            else f"""Such as: "{'", "'.join(value[self.lang][:5])}" """
                        )
                        for key, value in self.examples.items()
                    }
                else:
                    # _examples = {key: "" for key in self.examples.keys()}
                    _examples = {
                        key[1]: ""
                        for definition in _guidelines
                        for key in self._formatter.parse(definition)
                        if key[1] is not None and "example" in key[1]
                    }
                _repl = {**_examples, **_definitions}
                _guidelines = [definition.format(**_repl) for definition in _guidelines]
                # If no examples are provide, empty comments are created, the following line removes them
                _guidelines = {self._remove_empty_comments_fn(definition) for definition in _guidelines}

                # Remove definitions for baseline
                if self.remove_guidelines:
                    _guidelines = [self._remove_guidelines_fn(definition) for definition in _guidelines]
                    _guidelines = [self._remove_comments_fn(definition) for definition in _guidelines]

                text = self.template.render(guidelines=_guidelines, text=_text, annotations=_ann, gold=_gold)
                # Apply label noise (but keem them if we are removing the guidelines)
                if self.split == "train" and self.label_noise_prob > 0.0 and not self.remove_guidelines:
                    pretext_idx = text.index("\ntext =")
                    results_idx = text.index("\nresult =")
                    _pretext = text[:pretext_idx]
                    _intext = text[pretext_idx:results_idx]
                    _postext = text[results_idx:]
                    class_names = self._class_label_re.findall(_pretext)
                    random.shuffle(class_names)
                    i = 1
                    for name in class_names:
                        if random.random() <= self.label_noise_prob:
                            _pretext = _pretext.replace(f"{name}", f"LABEL_{i}")
                            _postext = _postext.replace(f"{name}(", f"LABEL_{i}(")
                            i += 1
                    text = _pretext + _intext + _postext

                yield {
                    "ids": [inst["id"] for inst in instances],
                    "task_id": f"{self.dataset_name}_{self.task}",
                    "scorer_cls": self.scorer_cls,
                    "labels": black.format_str(_ann.__repr__(), mode=self._black_mode),
                    "text": black.format_str(text, mode=self._black_mode),
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
