from transformers import (
    Seq2SeqTrainingArguments,
    HfArgumentParser,
    DataCollatorForSeq2Seq,
    Seq2SeqTrainer,
)
from datasets import DatasetDict

from dataset.dataset import CollieDataset
from model.load_model import load_model_for_training, load_model_for_inference
from config import ModelArguments, DataTrainingArguments
import sys
import os
import torch.utils.data
import logging


def train_collie(
    model_args: ModelArguments,
    data_args: DataTrainingArguments,
    training_args: Seq2SeqTrainingArguments,
):
    logging.info(f"Loading {model_args.model_name_or_path} model...")
    model, tokenizer = load_model_for_training(
        model_weights_name_or_path=model_args.model_name_or_path,
        int8_quantization=model_args.int8_quantization,
        use_lora=model_args.use_lora,
        torch_dtype=model_args.torch_dtype,
    )

    logging.info("Loading datasets...")
    training_datasets_path = [
        f"{os.path.join(data_args.dataset_dir, task)}.train.jsonl"
        for task in data_args.train_tasks
    ]
    development_datasets_path = [
        f"{os.path.join(data_args.dataset_dir, task)}.dev.jsonl"
        for task in data_args.validation_tasks
    ]

    logging.info(
        f"We will train CoLLIE on {len(training_datasets_path)} datasets:"
        f" {', '.join(training_datasets_path)}"
    )

    logging.info(
        f"We will validate CoLLIE on {len(development_datasets_path)} datasets:"
        f" {', '.join(development_datasets_path)}"
    )

    training_datasets = []
    for train_path in data_args.train_tasks:
        train_dataset = CollieDataset(
            tokenizer=tokenizer,
            dataset_path=train_path,
            max_length=data_args.max_seq_length,
            pad_to_max_length=False,
            is_encoder_decoder=model.config.is_encoder_decoder,
            inference=False,
        )
        training_datasets.append(train_dataset)

    train_dataset = torch.utils.data.ConcatDataset(training_datasets)

    dev_datasets = DatasetDict()
    for dev_path in data_args.validation_tasks:
        dev_dataset = CollieDataset(
            tokenizer=tokenizer,
            dataset_path=dev_path,
            max_length=data_args.max_seq_length,
            pad_to_max_length=False,
            is_encoder_decoder=model.config.is_encoder_decoder,
            inference=False,
        )
        dev_datasets[os.path.splitext(os.path.basename(dev_path))[0]] = dev_dataset

    trainer = Seq2SeqTrainer(
        model=model,
        train_dataset=train_dataset,
        eval_dataset=dev_datasets,
        args=training_args,
        data_collator=DataCollatorForSeq2Seq(
            tokenizer,
            pad_to_multiple_of=8,
            return_tensors="pt",
            padding=True,
            label_pad_token_id=(
                -100 if data_args.ignore_pad_token_for_loss else tokenizer.pad_token_id
            ),
        ),
    )

    trainer.train(resume_from_checkpoint=training_args.resume_from_checkpoint)

    trainer.save_model()

    model.save_pretrained(training_args.output_dir)


def inference_collie(
    model_args: ModelArguments,
    data_args: DataTrainingArguments,
    training_args: Seq2SeqTrainingArguments,
):
    model, tokenizer = load_model_for_inference(
        weights_path=model_args.model_name_or_path,
        int8_quantization=model_args.int8_quantization,
        lora_weights_name_or_path=model_args.lora_weights_name_or_path,
    )

    trainer = Seq2SeqTrainer(
        model=model,
        args=training_args,
        data_collator=DataCollatorForSeq2Seq(
            tokenizer,
            pad_to_multiple_of=8,
            return_tensors="pt",
            padding=True,
        ),
    )

    for dataset in data_args.test_tasks:
        test_dataset = CollieDataset(
            tokenizer=tokenizer,
            dataset_path=f"{os.path.join(data_args.dataset_dir, dataset)}.test.jsonl",
            max_length=data_args.max_seq_length,
            pad_to_max_length=False,
            is_encoder_decoder=model.config.is_encoder_decoder,
            inference=True,
        )

        predictions = trainer.predict(test_dataset)

        output_name = (
            f"{os.path.join(training_args.output_dir,os.path.splitext(os.path.basename(dataset))[0])}"
            ".predictions.txt"
        )

        with open(output_name, "w", encoding="utf8") as f:
            logging.info(f"Writing predictions to {output_name}")
            for prediction in predictions.predictions:
                print(tokenizer.decode(prediction, skip_special_tokens=True), file=f)


if __name__ == "__main__":
    parser = HfArgumentParser(
        (ModelArguments, DataTrainingArguments, Seq2SeqTrainingArguments)
    )
    print(sys.argv)
    print(len(sys.argv))
    print(sys.argv[1].endswith(".yaml"))
    if len(sys.argv) == 2 and sys.argv[1].endswith(".json"):
        # If we pass only one argument to the script and it's the path to a json file,
        # let's parse it to get our arguments.
        model_args, data_args, training_args = parser.parse_json_file(
            json_file=os.path.abspath(sys.argv[1])
        )

    elif len(sys.argv) == 2 and sys.argv[1].endswith(".yaml"):
        # If we pass only one argument to the script and it's the path to a yaml file,
        # let's parse it to get our arguments.
        model_args, data_args, training_args = parser.parse_yaml_file(
            yaml_file=os.path.abspath(sys.argv[1])
        )
    else:
        model_args, data_args, training_args = parser.parse_args_into_dataclasses()

    if data_args.train_files is not None:
        train_collie(
            model_args,
            data_args,
            training_args,
        )

    if data_args.test_files is not None:
        inference_collie(
            model_args,
            data_args,
            training_args,
        )
