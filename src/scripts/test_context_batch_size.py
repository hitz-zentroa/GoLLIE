import argparse
import logging
import random
import string

import bitsandbytes as bnb
import torch
from accelerate import Accelerator
from fairseq.optim.adafactor import Adafactor
from tabulate import tabulate
from torch.optim import AdamW
from torch.utils.data import DataLoader, Dataset

from src.model.load_model import load_model
from transformers import (
    BatchEncoding,
    DataCollatorForSeq2Seq,
    PreTrainedModel,
    PreTrainedTokenizerBase,
)


def generate_random_sentence(sentence_length: int = 5120) -> str:
    """
    Generates a random string of specific length with ascii characters.

    Args:
        sentence_length (`int`, optional):
            Length of the sentence. Defaults to `5120`.

    Returns:
        str:
            A random sentence of length `sentence_length`.
    """
    sentence = ""
    for i in range(sentence_length):
        # generate a random word of length between 1 and 10 characters
        word = "".join(random.choice(string.ascii_lowercase) for _ in range(random.randint(1, 10)))
        sentence += word + " "
    return sentence


class TestDataset(Dataset):
    """
    A dummy dataset used for testing.

    Args:
        tokenizer (`PreTrainedTokenizerBase`):
            The pre-trained tokenizer.
        seq_len (`int`):
            The length of the sentences.
        data_len (`int`):
            The length of the data.
    """

    def __init__(self, tokenizer: PreTrainedTokenizerBase, seq_len: int, data_len: int):
        self.data = []
        for i in range(data_len):
            # model_inputs = tokenizer(
            #    generate_random_sentence(),
            #    return_tensors=None,
            #    padding="max_length",
            #    truncation=True,
            #    max_length=seq_len,
            #    add_special_tokens=True,
            # )

            # model_inputs["labels"] = model_inputs["input_ids"].copy()

            # self.data.append(model_inputs)

            inputs_ids = random.sample(range(100, len(tokenizer) - 100), seq_len)

            self.data.append(
                BatchEncoding(
                    {
                        "input_ids": inputs_ids,
                        "attention_mask": [1] * seq_len,
                        "labels": inputs_ids.copy(),
                    }
                )
            )

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        return self.data[idx]


def get_dataloader(
    tokenizer: PreTrainedTokenizerBase,
    batch_size: int,
    seq_len: int,
) -> DataLoader:
    """
    A function that returns a `DataLoader` instance

    Args:
        tokenizer (`PreTrainedTokenizerBase`):
            The pre-trained tokenizer.
        batch_size (`int`):
            The size of the batch.
        seq_len (`int`):
            The size of the sequence.

    Returns:
        `DataLoader`:
            The dataloader that fits the configuration given.
    """
    dataset = TestDataset(tokenizer=tokenizer, seq_len=seq_len, data_len=batch_size)
    data_collator = DataCollatorForSeq2Seq(tokenizer, padding=True, pad_to_multiple_of=8, return_tensors="pt")
    return DataLoader(
        dataset,
        batch_size=batch_size,
        collate_fn=data_collator,
        shuffle=True,
        pin_memory=True,
    )


def run_training_test(
    model: PreTrainedModel,
    tokenizer: PreTrainedTokenizerBase,
    accelerator: Accelerator,
    seq_len: int,
    batch_size: int,
    use_lora: bool,
    quantization: bool,
    optimizer_name: str,
    learning_rate: float,
):
    """
    Runs the stress test to check if the current hardware allows it.

    Args:
        model (`PreTrainedModel`):
            The model to be tested.
        tokenizer (`PreTrainedTokenizerBase`):
            The tokenizer of the model to be tested.
        accelerator (`Accelerator`):
            The accelerator instance.
        seq_len (`int`):
            The length of the sequence.
        batch_size (`int`):
            The length of the batch.
        use_lora (`bool`):
            Whether to use LoRA or not.
        quantization (`int`):
            Whether to use 4 bits / 8 bits quantization or not.
        optimizer_name (`str`):
            The optimizer to use on the test.
        learning_rate (`float`):
            The learning rate to use on the test.

    Raises:
        `ValueError`:
            raised when `optimizer_name!="adamW"` and `quantization!=None`.
    """
    assert optimizer_name in [
        "adamW",
        "AdaFactor",
    ], f"Optimizer {optimizer_name} not supported. Choose between adamW and AdaFactor."

    model.config.max_length = seq_len

    dataloader = get_dataloader(tokenizer=tokenizer, batch_size=batch_size, seq_len=seq_len)

    if quantization:
        if optimizer_name != "adamW":
            raise ValueError("Quantization is only supported with adamW optimizer.")
        optimizer = bnb.optim.AdamW8bit(
            model.parameters(),
            lr=learning_rate,
            betas=(0.9, 0.995),
        )
    else:
        if optimizer_name == "adamW":
            optimizer = AdamW(model.parameters(), lr=learning_rate, eps=1e-7)
        else:
            optimizer = Adafactor(
                params=model.parameters(),
                scale_parameter=False,
                relative_step=False,
                warmup_init=False,
                lr=learning_rate,
                clip_threshold=1.0,
            )

    optimizer, dataloader = accelerator.prepare(optimizer, dataloader)

    model.train()

    for i, batch in enumerate(dataloader):
        optimizer.zero_grad()
        # print("Data devices:")
        # print(batch.input_ids.device)
        # print(batch.attention_mask.device)
        # print(batch.labels.device)
        # print("Model devices:")
        # print(model.device)
        outputs = model(
            input_ids=batch.input_ids,
            labels=batch.labels,
            attention_mask=batch.attention_mask,
        )
        loss = outputs.loss
        accelerator.backward(loss)
        optimizer.step()
        optimizer.zero_grad()

    accelerator.wait_for_everyone()

    return 1


def get_params():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--model_name_or_path",
        type=str,
        default="/gaueko1/hizkuntza-ereduak/LLaMA/lm/huggingface/65B/",
        help="Model name or path",
    )
    parser.add_argument(
        "--seq_len",
        type=int,
        nargs="+",
        default=[128, 256, 512, 1024, 1536, 2048, 4096],
        help="Sequence lengths to test",
    )
    parser.add_argument(
        "--batch_size",
        type=int,
        nargs="+",
        default=[1, 4, 8, 16, 32, 64, 128],
        help="Batch sizes to test",
    )
    parser.add_argument(
        "--use_lora",
        action="store_true",
        help="Use LORA",
    )
    parser.add_argument(
        "--quantization",
        type=int,
        default=None,
        help="Use 4 bits / 8 bits quantization or not",
    )
    parser.add_argument(
        "--optimizer_name",
        type=str,
        default="adamW",
        choices=["adamW", "AdaFactor"],
        help="Optimizer to use",
    )
    parser.add_argument(
        "--learning_rate",
        type=float,
        default=5e-5,
        help="Learning rate",
    )
    return parser.parse_args()


def main():
    args = get_params()
    seq_lens = args.seq_len
    batch_sizes = args.batch_size

    result_matrix = [[0 for i in range(len(batch_sizes))] for j in range(len(seq_lens))]

    logging.info("***** Experiment parameters *****")
    logging.info(f"Model name or path: {args.model_name_or_path}")
    logging.info(f"Sequence lengths: {seq_lens}")
    logging.info(f"Batch sizes: {batch_sizes}")
    logging.info(f"Use LORA: {args.use_lora}")
    logging.info(f"Use quantization: {args.quantization}")
    logging.info(f"Optimizer: {args.optimizer_name}")
    logging.info(f"Learning rate: {args.learning_rate}")
    logging.info("*********************************")
    logging.info(f"Loading model {args.model_name_or_path}...")
    model, tokenizer = load_model(
        inference=False,
        model_weights_name_or_path=args.model_name_or_path,
        use_lora=args.use_lora,
        quantization=args.quantization,
        use_gradient_checkpointing=True,
        use_flash_attention=True,
    )
    logging.info("Model loaded.")

    accelerator = Accelerator()
    model = accelerator.prepare(model)

    for i, seq_len in enumerate(seq_lens):
        for j, batch_size in enumerate(batch_sizes):
            logging.info(f"Running test with seq_len={seq_len} and batch_size={batch_size}...")
            try:
                result_matrix[i][j] = run_training_test(
                    model=model,
                    tokenizer=tokenizer,
                    accelerator=accelerator,
                    seq_len=seq_len,
                    batch_size=batch_size,
                    use_lora=args.use_lora,
                    quantization=args.quantization,
                    optimizer_name=args.optimizer_name,
                    learning_rate=args.learning_rate,
                )
                logging.info("Test passed.")
            except RuntimeError as e:
                if "out of memory" in str(e):
                    logging.info("| WARNING: ran out of memory, retrying batch")
                    for p in model.parameters():
                        if p.grad is not None:
                            del p.grad  # free some memory
                    torch.cuda.empty_cache()
                    logging.info("Test failed.")
                    continue
                else:
                    raise e

    table = tabulate(tabular_data=result_matrix, headers=batch_sizes, showindex=seq_lens)
    print(table)


if __name__ == "__main__":
    main()
