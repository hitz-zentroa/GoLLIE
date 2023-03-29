from model.load_model import load_model_for_training
from accelerate import Accelerator
from torch.utils.data import DataLoader, Dataset
from transformers import (
    BatchEncoding,
    PreTrainedTokenizerBase,
    DataCollatorForSeq2Seq,
    PreTrainedModel,
)
import random
from torch.optim import AdamW
from fairseq.optim.adafactor import Adafactor
import bitsandbytes as bnb
from tabulate import tabulate
import argparse
import torch
import string


def generate_random_sentence(sentence_length: int = 5120):
    sentence = ""
    for i in range(sentence_length):
        # generate a random word of length between 1 and 10 characters
        word = "".join(
            random.choice(string.ascii_lowercase) for i in range(random.randint(1, 10))
        )
        sentence += word + " "
    return sentence


class TestDataset(Dataset):
    def __init__(self, tokenizer: PreTrainedTokenizerBase, seq_len: int, data_len: int):
        self.data = []
        for i in range(data_len):
            model_inputs = tokenizer(
                generate_random_sentence(),
                return_tensors=None,
                padding="max_length",
                truncation=True,
                max_length=seq_len,
                add_special_tokens=True,
            )

            model_inputs["labels"] = model_inputs["input_ids"].copy()

            self.data.append(model_inputs)

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        return self.data[idx]


def get_dataloader(
    tokenizer: PreTrainedTokenizerBase,
    batch_size: int,
    data_len: int,
):
    dataset = TestDataset(tokenizer, batch_size, data_len)
    data_collator = DataCollatorForSeq2Seq(
        tokenizer, padding=True, pad_to_multiple_of=8, return_tensors="pt"
    )
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
    seq_len: int,
    batch_size: int,
    use_lora: bool,
    int8_quantization: bool,
    optimizer_name: str,
    learning_rate: float,
):
    assert optimizer_name in [
        "adamW",
        "AdaFactor",
    ], f"Optimizer {optimizer_name} not supported. Choose between adamW and AdaFactor."

    accelerator = Accelerator()

    dataloader = get_dataloader(
        tokenizer=tokenizer, batch_size=batch_size, data_len=seq_len
    )

    if int8_quantization:
        if optimizer_name != "adamW":
            raise ValueError(
                "Int8 quantization is only supported with adamW optimizer."
            )
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

    model, optimizer, dataloader = accelerator.prepare(model, optimizer, dataloader)
    model.train()
    for i, batch in enumerate(dataloader):
        optimizer.zero_grad()
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
        default=[512, 1024, 1536, 2048, 5120],
        help="Sequence lengths to test",
    )
    parser.add_argument(
        "--batch_size",
        type=int,
        nargs="+",
        default=[1, 4, 8, 16, 32, 64],
        help="Batch sizes to test",
    )
    parser.add_argument(
        "--use_lora",
        action="store_true",
        help="Use LORA",
    )
    parser.add_argument(
        "--int8_quantization",
        action="store_true",
        help="Use int8 quantization",
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
        default=1e-4,
        help="Learning rate",
    )
    return parser.parse_args()


def main():
    args = get_params()
    seq_lens = args.seq_len
    batch_sizes = args.batch_size

    result_matrix = [[0 for i in range(len(batch_sizes))] for j in range(len(seq_lens))]

    print(f"***** Experiment parameters *****")
    print(f"Model name or path: {args.model_name_or_path}")
    print(f"Sequence lengths: {seq_lens}")
    print(f"Batch sizes: {batch_sizes}")
    print(f"Use LORA: {args.use_lora}")
    print(f"Use int8 quantization: {args.int8_quantization}")
    print(f"Optimizer: {args.optimizer_name}")
    print(f"Learning rate: {args.learning_rate}")
    print(f"*********************************")
    print()
    print(f"Loading model {args.model_name_or_path}...")
    model, tokenizer = load_model_for_training(
        model_weights_name_or_path=args.model_name_or_path,
        use_lora=args.use_lora,
        int8_quantization=args.int8_quantization,
    )
    print("Model loaded.")
    print()

    for i, seq_len in enumerate(seq_lens):
        for j, batch_size in enumerate(batch_sizes):
            print(f"Running test with seq_len={seq_len} and batch_size={batch_size}...")
            try:
                result_matrix[i][j] = run_training_test(
                    model=model,
                    tokenizer=tokenizer,
                    seq_len=seq_len,
                    batch_size=batch_size,
                    use_lora=args.use_lora,
                    int8_quantization=args.int8_quantization,
                    optimizer_name=args.optimizer_name,
                    learning_rate=args.learning_rate,
                )
                print("Test passed.")
            except RuntimeError as e:
                if "out of memory" in str(e):
                    print("| WARNING: ran out of memory, retrying batch")
                    for p in model.parameters():
                        if p.grad is not None:
                            del p.grad  # free some memory
                    torch.cuda.empty_cache()
                    print("Test failed.")
                    continue
                else:
                    raise e
            print()

    table = tabulate(
        tabular_data=result_matrix, headers=batch_sizes, showindex=seq_lens
    )
    print(table)


if __name__ == "__main__":
    main()
