import glob
import json
import logging
import math
import os
import random
from dataclasses import dataclass
from functools import partial
from itertools import chain
from multiprocessing import Pool
from typing import Any, Dict, Iterator, List, Optional, Sized, Union

import numpy as np
from rich.progress import Progress, SpinnerColumn, TimeElapsedColumn
from torch.utils.data import Dataset

from transformers import BatchEncoding, PreTrainedTokenizerBase
from transformers.utils import PaddingStrategy


def batch(iterable: Sized, n=1) -> Iterator:
    """
    Yield successive n-sized chunks from iterable.

    Args:
        iterable (`Sized`):
            The iterable to split.
        n (`int`, optional):
            The size of the chunks. Defaults to `1`.

    Yields:
        `Iterator`:
            An iterator with the chunks.
    """
    l: int = len(iterable)
    p: int = math.ceil(l / n)
    for ndx in range(0, l, p):
        yield iterable[ndx : min(ndx + p, l)]


def prepare_data(
    example: str,
    tokenizer: PreTrainedTokenizerBase,
    is_encoder_decoder: bool = False,
    max_length: int = 2048,
    inference: bool = False,
    prompt_loss_weight: float = 0.05,
) -> BatchEncoding:
    """
    Prepare data for training or inference.

    Args:
        example (`str`):
            The example to prepare.
        tokenizer (`PreTrainedTokenizerBase`):
            The tokenizer to use.
        is_encoder_decoder (`bool`, optional):
            Whether the model is an encoder-decoder model. Defaults to `False`.
        max_length (`int`, optional):
            The maximum length of the input. Defaults to `2048`.
        inference (`bool`, optional):
            Whether to prepare the data for inference. During inference labels
            are not included in model inputs. Defaults to `False`.
        prompt_loss_weight (`float`, optional):
            The weight of the prompt tokens in the loss. If set to '0.05' the prompt tokens will have a total weight
            of 5% in the loss while the result tokens will have a total weight of 95%. Defaults to `0.05`.

    Returns:
        `BatchEncoding`: `BatchEncoding` with the prepared data.
    """

    if is_encoder_decoder:
        prompt, result = example.split("result =")
        prompt = prompt + "result ="
        prompt = prompt.strip()
        result = result.strip()

        model_inputs = tokenizer(
            text=prompt,
            max_length=max_length,
            truncation=True,
            padding=False,
            return_tensors=None,
            add_special_tokens=True,
        )
        if not inference:
            model_inputs["labels"] = tokenizer(
                text_target=result,
                max_length=max_length,
                truncation=True,
                padding=False,
                return_tensors=None,
                add_special_tokens=True,
            )["input_ids"]

            model_inputs["loss_weight_mask"] = np.ones(len(model_inputs["labels"]), dtype=np.float32)

    else:
        if inference:
            prompt = example.split("result =")[0] + "result ="
            model_inputs = tokenizer(
                text=prompt,
                max_length=max_length,
                truncation=True,
                padding=False,
                return_tensors=None,
                add_special_tokens=True,
            )

            # Remove the last token if it is an eos token
            if model_inputs["input_ids"][-1] == tokenizer.eos_token_id:
                model_inputs["input_ids"] = model_inputs["input_ids"][:-1]
                model_inputs["attention_mask"] = model_inputs["attention_mask"][:-1]

        else:
            model_inputs = tokenizer(
                text=example,
                max_length=max_length,
                truncation=True,
                padding=False,
                return_tensors=None,
                add_special_tokens=True,
            )

            # Make sure the `eos_token_id` is added at the end
            # This bug is reported at https://github.com/huggingface/transformers/issues/22794
            if model_inputs["input_ids"][-1] != tokenizer.eos_token_id:
                model_inputs["input_ids"].append(tokenizer.eos_token_id)
                model_inputs["attention_mask"].append(1)

            model_inputs["labels"] = model_inputs["input_ids"].copy()

            # Find the prompt length
            prompt = example.split("result =")[0] + "result ="
            prompt = tokenizer(
                text=prompt,
                max_length=max_length,
                truncation=True,
                padding=False,
                return_tensors=None,
                add_special_tokens=True,
            )["input_ids"]

            # Remove the last token if it is an eos token
            if prompt[-1] == tokenizer.eos_token_id:
                prompt = prompt[:-1]

            if len(prompt) > len(model_inputs["labels"]):
                raise ValueError(
                    f"Prompt is longer than the input, something went wrong. Prompt: {prompt}, input:"
                    f" {model_inputs['input_ids']}"
                )

            # Create the weight mask
            loss_weight_mask = np.ones(len(model_inputs["labels"]), dtype=np.float32)

            # The sum of the loss of the prompt tokens should be equal to 'prompt_loss_weight' percent of the total loss
            len_prompt = len(prompt)
            len_result = len(model_inputs["labels"]) - len_prompt
            prompt_token_weight = len_result * prompt_loss_weight  # 'prompt_loss_weight' percent of the total loss
            try:
                prompt_token_weight = prompt_token_weight * (
                    len_result / (len_result * (1 - prompt_loss_weight))
                )  # Scale so result tokens can have 1.0 weight
                prompt_token_weight = prompt_token_weight / len_prompt  # Divide by the number of prompt tokens
            except ZeroDivisionError:
                logging.warning(
                    "Found division by zero in prompt token weight calculation. You might have an empty prompt, empty"
                    f" result, or both. Example with error: {example}. Setting prompt token weight to 0.0."
                )
                prompt_token_weight = 0.0

            for i in range(len(prompt)):
                loss_weight_mask[i] = prompt_token_weight

            model_inputs["loss_weight_mask"] = loss_weight_mask

    if "token_type_ids" in model_inputs:
        # LLaMa tokenizer adds token type ids, but we don't need them
        model_inputs.pop("token_type_ids")

    return model_inputs


def batch_tokenization(
    tokenizer: PreTrainedTokenizerBase,
    dataset_name: str,
    is_encoder_decoder: bool,
    max_length: int,
    inference: bool,
    prompt_loss_weight: float,
    examples: List[str],
    process_no: int,
) -> List[BatchEncoding]:
    """
    Batch tokenization function.

    Args:
        tokenizer (`PreTrainedTokenizerBase`):
            The tokenizer to use.
        dataset_name (`str`):
            The name of the dataset.
        is_encoder_decoder (`bool`):
            Whether the model is an encoder-decoder model.
        max_length (`int`):
            The maximum length of the input.
        inference (`bool`):
            Whether to prepare the data for inference. If model
            `is_encoder_decoder=False`, inputs ids will be truncated to don't include the
            results section of the example. Labels will still include the full correct
            example. If model `is_encoder_decoder=True`, this parameter is ignored.
        prompt_loss_weight (`float`):
            The weight of the prompt tokens in the loss. If set to '0.05' the prompt tokens will have a total weight
            of 5% in the loss while the result tokens will have a total weight of 95%. Defaults to `0.05`.
        examples (`List[str]`):
            The examples to tokenize.
        process_no (`int`):
            The process number.

    Returns:
        `List[BatchEncoding]`:
            List of BatchEncoding with the prepared data.
    """
    tokenized_examples: List[BatchEncoding] = []
    if process_no == 0:
        with Progress(
            SpinnerColumn(),
            *Progress.get_default_columns(),
            TimeElapsedColumn(),
        ) as progress:
            task = progress.add_task(f"Tokenizing {dataset_name}", total=len(examples))

            for example in examples:
                tokenized_examples.append(
                    prepare_data(
                        example=example,
                        tokenizer=tokenizer,
                        is_encoder_decoder=is_encoder_decoder,
                        max_length=max_length,
                        inference=inference,
                        prompt_loss_weight=prompt_loss_weight,
                    )
                )
                progress.update(task, advance=1)
    else:
        tokenized_examples = [
            prepare_data(
                example=example,
                tokenizer=tokenizer,
                is_encoder_decoder=is_encoder_decoder,
                max_length=max_length,
                inference=inference,
                prompt_loss_weight=prompt_loss_weight,
            )
            for example in examples
        ]

    return tokenized_examples


class CollieDataset(Dataset):
    """
    Dataset for Collie.

    Args:
        tokenizer (`PreTrainedTokenizerBase`):
            The tokenizer to use.
        dataset_path (`str`):
            The path to the jsonl file containing the dataset.
        is_encoder_decoder (`bool`, optional):
            Whether the model is an encoder-decoder model. Defaults to `False`.
        max_length (`int`, optional):
            The maximum length of the input. Defaults to `2048`.
        inference (`bool`, optional):
            Whether to prepare the data for inference. If model
            `is_encoder_decoder=False`, inputs ids will be truncated to don't include
            the results section of the example. Labels will still include the full
            correct example. If model `is_encoder_decoder=True`, this parameter is
            ignored. Defaults to `False`.
        prompt_loss_weight (`float`, optional):
            The weight of the prompt tokens in the loss. If set to '0.05' the prompt tokens will have a total weight
            of 5% in the loss while the result tokens will have a total weight of 95%. Defaults to `0.05`.
        num_workers (`int`, optional):
            The number of workers to use for tokenization. Defaults to
            `min(os.cpu_count(), 16)`.
        max_examples (`Optional[int]`, optional):
            The maximum number of examples to load. Defaults to `None`. If `None` all
            examples will be loaded. If `max_examples` is smaller is set we will randomly
            sample `max_examples` examples from the dataset.
    """

    def __init__(
        self,
        tokenizer: PreTrainedTokenizerBase,
        dataset_path: str,
        is_encoder_decoder: bool = False,
        max_length: int = 2048,
        inference: bool = False,
        prompt_loss_weight: float = 0.0,
        num_workers: int = min(os.cpu_count(), 16),
        max_examples: Optional[int] = None,
    ):
        self.is_encoder_decoder = is_encoder_decoder
        self.max_length = max_length
        self.inference = inference
        self.max_examples = max_examples

        assert (
            prompt_loss_weight >= 0.0 and prompt_loss_weight < 1.0
        ), f"Prompt loss weight must be in [0, 1). Found {prompt_loss_weight}."

        self.prompt_loss_weight = prompt_loss_weight

        try:
            self.dataset_name, self.task_name, self.split, extension = os.path.basename(dataset_path).split(".")
        except ValueError:
            raise ValueError(
                f"Something is wrong with the dataset path {dataset_path}. Please check it and ensure "
                "it follows the format `dataset_name.task_name.split.jsonl`"
            )

        # Find pre-computed epoch datasets for training
        self.dataset_dict: Dict[int, List[BatchEncoding]] = {}
        self.dataset_keys: List[int] = []
        self.current_dataset_key: int = 0

        if self.split == "train":
            epoch_datasets = glob.glob(
                os.path.join(
                    os.path.dirname(dataset_path), f"{self.dataset_name}.{self.task_name}.{self.split}.*.jsonl"
                )
            )
            if epoch_datasets:
                epoch_datasets.sort(key=lambda x: int(x.split(".")[-2]))
                logging.info(f"Found {len(epoch_datasets)} pre-computed epoch datasets.")
                for dataset in epoch_datasets:
                    try:
                        _, _, _, epoch, _ = os.path.basename(dataset).split(".")
                    except ValueError:
                        logging.warning(f"Error loading pre-computed epoch {dataset} . Skipping...")
                        continue

                    self.dataset_dict[int(epoch)] = self.compute_tokenized_examples(
                        dataset_path=dataset,
                        num_workers=num_workers,
                        tokenizer=tokenizer,
                    )

                    self.dataset_keys.append(int(epoch))

                # Truncate datasers to ensure all datasets have the same length
                # min_length = min([len(x) for x in self.dataset_dict.values()])
                # for key in self.dataset_dict.keys():
                #    if len(self.dataset_dict[key]) > min_length:
                #        logging.warning(f"Truncating dataset {key} from {len(self.dataset_dict[key])} to {min_length}")
                #    self.dataset_dict[key] = self.dataset_dict[key][:min_length]

                # Oversample datasets to ensure all datasets have the same length
                max_length = max([len(x) for x in self.dataset_dict.values()])
                for key in self.dataset_dict.keys():
                    if len(self.dataset_dict[key]) < max_length:
                        logging.warning(
                            f"Oversampling dataset {key} from {len(self.dataset_dict[key])} to {max_length}"
                        )
                        num_samples = max_length - len(self.dataset_dict[key])
                        random_samples = random.choices(self.dataset_dict[key], k=num_samples)
                        self.dataset_dict[key].extend(random_samples)

                self.current_dataset_key = self.dataset_keys[0]

        if len(self.dataset_dict) == 0:
            self.dataset_dict[0] = self.compute_tokenized_examples(
                dataset_path=dataset_path,
                num_workers=num_workers,
                tokenizer=tokenizer,
            )
            self.dataset_keys.append(0)
            self.current_dataset_key = self.dataset_keys[0]

        logging.info(f"Loaded {[len(x) for x in self.dataset_dict.values()]} examples from {dataset_path}")

    def compute_tokenized_examples(
        self,
        dataset_path,
        num_workers,
        tokenizer,
    ) -> List[BatchEncoding]:
        """
        Compute the tokenized examples.

        Args:
            dataset_path (`str`):
                The path to the jsonl file containing the dataset.
            num_workers (`int`):
                The number of workers to use for tokenization.
            tokenizer (`PreTrainedTokenizerBase`):
                The tokenizer to use.

        Returns:
            `List[BatchEncoding]`:
                List of BatchEncoding with the prepared data.

        """

        with open(dataset_path, "r", encoding="utf8") as f:
            examples = f.readlines()

        examples = [json.loads(example.strip())["text"] for example in examples]

        if self.max_examples is not None and self.max_examples < len(examples):
            examples = random.sample(examples, self.max_examples)

        if num_workers <= 1:
            return batch_tokenization(
                tokenizer=tokenizer,
                dataset_name=".".join([self.dataset_name, self.task_name, self.split]),
                is_encoder_decoder=self.is_encoder_decoder,
                max_length=self.max_length,
                inference=self.inference,
                prompt_loss_weight=self.prompt_loss_weight,
                examples=examples,
                process_no=0,
            )
        else:
            tokenizer_fn = partial(
                batch_tokenization,
                tokenizer,
                ".".join([self.dataset_name, self.task_name, self.split]),
                self.is_encoder_decoder,
                self.max_length,
                self.inference,
                self.prompt_loss_weight,
            )
            with Pool(num_workers) as p:
                tokenized_examples = p.starmap(
                    tokenizer_fn,
                    zip(batch(examples, num_workers), range(num_workers)),
                )

            return list(chain.from_iterable(tokenized_examples))

    def __len__(self) -> int:
        return len(self.dataset_dict[self.current_dataset_key])

    def __getitem__(self, idx) -> List[BatchEncoding]:
        return self.dataset_dict[self.current_dataset_key][idx].copy()

    def rotate_split(self):
        """
        Rotate the current dataset to the next one.
        """
        self.current_dataset_key = self.dataset_keys[
            (self.dataset_keys.index(self.current_dataset_key) + 1) % len(self.dataset_keys)
        ]

        if len(self.dataset_dict) > 1:
            logging.info(
                f' Dataset {".".join([self.dataset_name, self.task_name, self.split])} rotated to split'
                f" {self.current_dataset_key}"
            )


@dataclass
class DataCollatorForCoLLIE:
    """
    Adapted from transformers.DataCollatorForSeq2Seq to handle CoLLIE data.

    Data collator that will dynamically pad the inputs received, as well as the labels.

    Args:
        tokenizer ([`PreTrainedTokenizer`] or [`PreTrainedTokenizerFast`]):
            The tokenizer used for encoding the data.
        model ([`PreTrainedModel`]):
            The model that is being trained. If set and has the *prepare_decoder_input_ids_from_labels*, use it to
            prepare the *decoder_input_ids*

            This is useful when using *label_smoothing* to avoid calculating loss twice.
        padding (`bool`, `str` or [`~utils.PaddingStrategy`], *optional*, defaults to `True`):
            Select a strategy to pad the returned sequences (according to the model's padding side and padding index)
            among:

            - `True` or `'longest'` (default): Pad to the longest sequence in the batch (or no padding if only a single
              sequence is provided).
            - `'max_length'`: Pad to a maximum length specified with the argument `max_length` or to the maximum
              acceptable input length for the model if that argument is not provided.
            - `False` or `'do_not_pad'`: No padding (i.e., can output a batch with sequences of different lengths).
        max_length (`int`, *optional*):
            Maximum length of the returned list and optionally padding length (see above).
        pad_to_multiple_of (`int`, *optional*):
            If set will pad the sequence to a multiple of the provided value.

            This is especially useful to enable the use of Tensor Cores on NVIDIA hardware with compute capability >=
            7.5 (Volta).
        label_pad_token_id (`int`, *optional*, defaults to -100):
            The id to use when padding the labels (-100 will be automatically ignored by PyTorch loss functions).
        return_tensors (`str`):
            The type of Tensor to return. Allowable values are "np", "pt" and "tf".
    """

    tokenizer: PreTrainedTokenizerBase
    model: Optional[Any] = None
    padding: Union[bool, str, PaddingStrategy] = True
    max_length: Optional[int] = None
    pad_to_multiple_of: Optional[int] = None
    label_pad_token_id: int = -100
    return_tensors: str = "pt"

    def __call__(self, features, return_tensors=None):
        if return_tensors is None:
            return_tensors = self.return_tensors
        labels = [feature["labels"] for feature in features] if "labels" in features[0].keys() else None
        loss_weight_mask = (
            [feature["loss_weight_mask"] for feature in features] if "loss_weight_mask" in features[0].keys() else None
        )
        # We have to pad the labels before calling `tokenizer.pad` as this method won't pad them and needs them of the
        # same length to return tensors.
        if labels is not None:
            max_label_length = max(len(l) for l in labels)
            if self.pad_to_multiple_of is not None:
                max_label_length = (
                    (max_label_length + self.pad_to_multiple_of - 1)
                    // self.pad_to_multiple_of
                    * self.pad_to_multiple_of
                )

            padding_side = self.tokenizer.padding_side
            for feature in features:
                remainder = [self.label_pad_token_id] * (max_label_length - len(feature["labels"]))
                if isinstance(feature["labels"], list):
                    feature["labels"] = (
                        feature["labels"] + remainder if padding_side == "right" else remainder + feature["labels"]
                    )
                elif padding_side == "right":
                    feature["labels"] = np.concatenate([feature["labels"], remainder]).astype(np.int64)
                else:
                    feature["labels"] = np.concatenate([remainder, feature["labels"]]).astype(np.int64)

        if loss_weight_mask is not None:
            max_loss_weight_mask_length = max(len(l) for l in loss_weight_mask)
            if self.pad_to_multiple_of is not None:
                max_loss_weight_mask_length = (
                    (max_loss_weight_mask_length + self.pad_to_multiple_of - 1)
                    // self.pad_to_multiple_of
                    * self.pad_to_multiple_of
                )

            padding_side = self.tokenizer.padding_side
            for feature in features:
                remainder = [0.0 if self.label_pad_token_id == -100 else 1.0] * (
                    max_loss_weight_mask_length - len(feature["loss_weight_mask"])
                )
                if isinstance(feature["loss_weight_mask"], list):
                    feature["loss_weight_mask"] = (
                        feature["loss_weight_mask"] + remainder
                        if padding_side == "right"
                        else remainder + feature["loss_weight_mask"]
                    )
                elif padding_side == "right":
                    feature["loss_weight_mask"] = np.concatenate([feature["loss_weight_mask"], remainder]).astype(
                        np.float32
                    )
                else:
                    feature["loss_weight_mask"] = np.concatenate([remainder, feature["loss_weight_mask"]]).astype(
                        np.float32
                    )

        features = self.tokenizer.pad(
            features,
            padding=self.padding,
            max_length=self.max_length,
            pad_to_multiple_of=self.pad_to_multiple_of,
            return_tensors=return_tensors,
        )

        # prepare decoder_input_ids
        if (
            labels is not None
            and self.model is not None
            and hasattr(self.model, "prepare_decoder_input_ids_from_labels")
        ):
            decoder_input_ids = self.model.prepare_decoder_input_ids_from_labels(labels=features["labels"])
            features["decoder_input_ids"] = decoder_input_ids

        return features
