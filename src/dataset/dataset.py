import os
from torch.utils.data import Dataset
from transformers import PreTrainedTokenizerBase, BatchEncoding
import json
from typing import List, Sized, Iterator
from rich.progress import Progress, TimeElapsedColumn, SpinnerColumn
import math
from multiprocessing import Pool
from functools import partial
import logging
from itertools import chain


def batch(iterable: Sized, n=1) -> Iterator:
    """
    Yield successive n-sized chunks from iterable.
    :param iterable: The iterable to split.
    :param n: The size of the chunks.
    :return: An iterator with the chunks.
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
    pad_to_max_length: bool = False,
    inference: bool = False,
) -> BatchEncoding:
    """
    Prepare data for training or inference.
    :param example:  The example to prepare.
    :param tokenizer: The tokenizer to use.
    :param is_encoder_decoder: Whether the model is an encoder-decoder model.
    :param max_length: The maximum length of the input.
    :param pad_to_max_length: Whether to pad the input to the maximum length.
    :param inference: Whether to prepare the data for inference.
                    During inference labels are not included in model inputs.
    :return: BatchEncoding with the prepared data.
    """

    if is_encoder_decoder:
        prompt, result = example.split("result = [")
        prompt = prompt + "result = ["

        model_inputs = tokenizer(
            text=prompt,
            max_length=max_length,
            truncation=True,
            padding="max_length" if pad_to_max_length else False,
            return_tensors=None,
            add_special_tokens=True,
        )
        if not inference:
            model_inputs["labels"] = tokenizer(
                text_target=result,
                max_length=max_length,
                truncation=True,
                padding="max_length" if pad_to_max_length else False,
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
                padding="max_length" if pad_to_max_length else False,
                return_tensors=None,
                add_special_tokens=True,
            )

        else:
            model_inputs = tokenizer(
                text=example,
                max_length=max_length,
                truncation=True,
                padding="max_length" if pad_to_max_length else False,
                return_tensors=None,
                add_special_tokens=True,
            )

            model_inputs["labels"] = model_inputs["input_ids"].copy()

    return model_inputs


def batch_tokenization(
    tokenizer: PreTrainedTokenizerBase,
    dataset_name: str,
    is_encoder_decoder: bool,
    max_length: int,
    pad_to_max_length: bool,
    inference: bool,
    examples: List[str],
    process_no: int,
) -> List[BatchEncoding]:
    """
    Batch tokenization function.
    :param tokenizer: The tokenizer to use.
    :param is_encoder_decoder: Whether the model is an encoder-decoder model.
    :param max_length: The maximum length of the input.
    :param pad_to_max_length: Whether to pad the input to the maximum length.
    :param inference: Whether to prepare the data for inference. If model is_encoder_decoder=False, inputs ids
                        will be truncated to don't include the results section of the example. Labels will still
                        include the full correct example. If model is_encoder_decoder=True, this parameter is ignored.
    :return: List of BatchEncoding with the prepared data.
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
                        example,
                        tokenizer,
                        is_encoder_decoder,
                        max_length,
                        pad_to_max_length,
                        inference,
                    )
                )
                progress.update(task, advance=1)
    else:
        tokenized_examples = [
            prepare_data(
                example,
                tokenizer,
                is_encoder_decoder,
                max_length,
                pad_to_max_length,
                inference,
            )
            for example in examples
        ]

    return tokenized_examples


class CollieDataset(Dataset):
    """
    Dataset for Collie.
    """

    def __init__(
        self,
        tokenizer: PreTrainedTokenizerBase,
        dataset_path: str,
        is_encoder_decoder: bool = False,
        max_length: int = 2048,
        pad_to_max_length: bool = False,
        inference: bool = False,
        num_workers: int = 0,
    ):
        """
        :param tokenizer: The tokenizer to use.
        :param dataset_path: The path to the jsonl file containing the dataset.
        :param is_encoder_decoder: Whether the model is an encoder-decoder model.
        :param max_length: The maximum length of the input.
        :param pad_to_max_length: Whether to pad the input to the maximum length.
        :param inference: Whether to prepare the data for inference. If model is_encoder_decoder=False, inputs ids
                            will be truncated to don't include the results section of the example. Labels will still
                            include the full correct example. If model is_encoder_decoder=True, this parameter is ignored.
        :param num_workers: The number of workers to use for tokenization.
        """

        self.dataset_name = os.path.splitext(os.path.basename(dataset_path))[0]

        examples: List[str] = []
        with open(dataset_path, "r", encoding="utf8") as f:
            examples = f.readlines()

        examples = [json.loads(example.strip())["text"] for example in examples]

        if num_workers == 0:
            self.tokenized_examples = batch_tokenization(
                tokenizer,
                self.dataset_name,
                is_encoder_decoder,
                max_length,
                pad_to_max_length,
                inference,
                examples,
                0,
            )
        else:
            tokenizer_fn = partial(
                batch_tokenization,
                tokenizer,
                self.dataset_name,
                is_encoder_decoder,
                max_length,
                pad_to_max_length,
                inference,
            )
            with Pool(num_workers) as p:
                self.tokenized_examples = p.starmap(
                    tokenizer_fn,
                    zip(batch(examples, num_workers), range(num_workers)),
                )
                self.tokenized_examples = list(
                    chain.from_iterable(self.tokenized_examples)
                )

        logging.info(
            f"Loaded {len(self.tokenized_examples)} examples from {self.dataset_name}"
        )

    def __len__(self):
        return len(self.tokenized_examples)

    def __getitem__(self, idx):
        return self.tokenized_examples[idx]
