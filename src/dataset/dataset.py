import glob
import json
import logging
import math
import os
import random
from functools import partial
from itertools import chain
from multiprocessing import Pool
from typing import Dict, Iterator, List, Sized

from rich.progress import Progress, SpinnerColumn, TimeElapsedColumn
from torch.utils.data import Dataset

from transformers import BatchEncoding, PreTrainedTokenizerBase


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
    ignore_prompt_loss: bool = False,
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
        ignore_prompt_loss (`bool`, optional):
            Whether to ignore the prompt tokens when calculating the loss (set to -100).
            Defaults to `False`

    Returns:
        `BatchEncoding`: `BatchEncoding` with the prepared data.
    """

    if is_encoder_decoder:
        prompt, result = example.split("result = [")
        prompt = prompt + "result = ["
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

    else:
        if inference:
            prompt = example.split("result = [")[0] + "result = ["
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
            if ignore_prompt_loss:
                prompt = example.split("result = [")[0] + "result = ["
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

                model_inputs["labels"] = model_inputs["input_ids"].copy()

                if len(prompt) > len(model_inputs["labels"]):
                    raise ValueError(
                        f"Prompt is longer than the input, something went wrong. Prompt: {prompt}, input:"
                        f" {model_inputs['input_ids']}"
                    )

                # Set labels to -100 for prompt tokens
                for i in range(len(prompt)):
                    model_inputs["labels"][i] = -100

            else:
                model_inputs["labels"] = model_inputs["input_ids"].copy()

            # Make sure the `eos_token_id` is added at the end
            # This bug is reported at https://github.com/huggingface/transformers/issues/22794
            if model_inputs["input_ids"][-1] != tokenizer.eos_token_id:
                model_inputs["input_ids"].append(tokenizer.eos_token_id)
                model_inputs["labels"].append(tokenizer.eos_token_id)
                model_inputs["attention_mask"].append(1)

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
    ignore_prompt_loss: bool,
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
        ignore_prompt_loss (`bool`, optional):
            Whether to ignore the prompt tokens when calculating the loss (set to -100).
            Defaults to `False`
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
                        ignore_prompt_loss=ignore_prompt_loss,
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
                ignore_prompt_loss=ignore_prompt_loss,
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
        ignore_prompt_loss (`bool`, optional):
            Whether to ignore the prompt tokens when calculating the loss (set to -100).
            Defaults to `False`
        num_workers (`int`, optional):
            The number of workers to use for tokenization. Defaults to
            `min(os.cpu_count(), 16)`.
    """

    def __init__(
        self,
        tokenizer: PreTrainedTokenizerBase,
        dataset_path: str,
        is_encoder_decoder: bool = False,
        max_length: int = 2048,
        inference: bool = False,
        ignore_prompt_loss: bool = False,
        num_workers: int = min(os.cpu_count(), 16),
    ):
        self.is_encoder_decoder = is_encoder_decoder
        self.max_length = max_length
        self.inference = inference
        self.ignore_prompt_loss = ignore_prompt_loss

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

        if num_workers <= 1:
            return batch_tokenization(
                tokenizer=tokenizer,
                dataset_name=".".join([self.dataset_name, self.task_name, self.split]),
                is_encoder_decoder=self.is_encoder_decoder,
                max_length=self.max_length,
                inference=self.inference,
                ignore_prompt_loss=self.ignore_prompt_loss,
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
                self.ignore_prompt_loss,
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
