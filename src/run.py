import gc
import glob
import json
import logging
import os
import sys

import torch
import torch.utils.data
from datasets import DatasetDict

from src.config import DataTrainingArguments, ModelArguments
from src.dataset.dataset import CollieDataset
from src.evaluate import evaluate
from src.model.load_model import load_model_for_inference, load_model_for_training
from src.trainer import CollieTrainer
from transformers import (
    DataCollatorForSeq2Seq,
    HfArgumentParser,
    Seq2SeqTrainingArguments,
)


def clean_cache():
    """Clean cache to avoid memory leak.
    This fixes this issue: https://github.com/huggingface/transformers/issues/22801"""

    logging.info(f"Cleaning GPU memory. Current memory usage: {torch.cuda.memory_allocated()}")
    torch.cuda.empty_cache()
    gc.collect()
    torch.cuda.empty_cache()
    logging.info(f"GPU memory usage after cleaning: {torch.cuda.memory_allocated()}")


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
        lora_target_modules=model_args.lora_target_modules,
        torch_dtype=model_args.torch_dtype,
    )

    logging.info("Loading datasets...")
    training_datasets_path = [
        f"{os.path.join(data_args.dataset_dir, task)}.train.jsonl" for task in data_args.train_tasks
    ]
    development_datasets_path = [
        f"{os.path.join(data_args.dataset_dir, task)}.dev.jsonl" for task in data_args.validation_tasks
    ]

    logging.info(
        f"We will train CoLLIE on {len(training_datasets_path)} datasets: {', '.join(training_datasets_path)}"
    )

    logging.info(
        f"We will validate CoLLIE on {len(development_datasets_path)} datasets: {', '.join(development_datasets_path)}"
    )

    logging.info(
        "Training dataset will be loaded with. 'ignore_pad_token_for_loss':"
        f" {data_args.ignore_pad_token_for_loss} and 'ignore_prompt_loss':"
        f" {data_args.ignore_prompt_loss}"
    )

    training_datasets = []
    for train_task in data_args.train_tasks:
        train_path = os.path.join(data_args.dataset_dir, f"{train_task}.train.jsonl")
        train_dataset = CollieDataset(
            tokenizer=tokenizer,
            dataset_path=train_path,
            max_length=data_args.max_seq_length,
            is_encoder_decoder=model.config.is_encoder_decoder,
            inference=False,
            ignore_prompt_loss=data_args.ignore_prompt_loss,
        )
        training_datasets.append(train_dataset)

    train_dataset = torch.utils.data.ConcatDataset(training_datasets)

    dev_datasets = DatasetDict()
    for dev_task in data_args.validation_tasks:
        dev_path = os.path.join(data_args.dataset_dir, f"{dev_task}.dev.jsonl")
        dev_dataset = CollieDataset(
            tokenizer=tokenizer,
            dataset_path=dev_path,
            max_length=data_args.max_seq_length,
            is_encoder_decoder=model.config.is_encoder_decoder,
            inference=False,
            ignore_prompt_loss=data_args.ignore_prompt_loss,
        )
        dev_datasets[os.path.splitext(os.path.basename(dev_path))[0]] = dev_dataset

    trainer = CollieTrainer(
        model=model,
        train_dataset=train_dataset,
        eval_dataset=dev_datasets,
        args=training_args,
        data_collator=DataCollatorForSeq2Seq(
            tokenizer,
            pad_to_multiple_of=8,
            return_tensors="pt",
            padding=True,
            label_pad_token_id=(-100 if data_args.ignore_pad_token_for_loss else tokenizer.pad_token_id),
        ),
    )

    trainer.train(resume_from_checkpoint=training_args.resume_from_checkpoint)

    # Save the model
    trainer.save_model()

    # model.save_pretrained(training_args.output_dir)
    # model.config.save_pretrained(training_args.output_dir)
    # tokenizer.save_pretrained(training_args.output_dir)


def inference_collie(
    model_args: ModelArguments,
    data_args: DataTrainingArguments,
    training_args: Seq2SeqTrainingArguments,
    checkpoint_path: str = None,
):
    if not training_args.predict_with_generate:
        logging.warning(
            "You have set predict_with_generate to False. We will only compute the loss"
            " on the test set. If you want to generate predictions, set"
            " predict_with_generate to True."
        )

        if not training_args.prediction_loss_only:
            logging.warning(
                "You have set predict_with_generate to False, so you only "
                "want to compute the loss on the test set. But you have set "
                "prediction_loss_only to False. This is contradictory, please "
                "review you configuration. We will attempt to continue but "
                "you might get unexpected results."
            )

    if training_args.do_train:
        if not checkpoint_path:
            logging.warning(
                "You are doing inference after training a model! We will load the "
                f"pretrained model saved in {training_args.output_dir}."
            )
            if model_args.use_lora:
                model_path = model_args.model_name_or_path
                lora_weights_name_or_path = training_args.output_dir
            else:
                model_path = training_args.output_dir
                lora_weights_name_or_path = None
        else:
            logging.warning(
                "You are doing inference after training a model! We will load the "
                f"pretrained model saved in {checkpoint_path}."
            )
            if model_args.use_lora:
                model_path = model_args.model_name_or_path
                lora_weights_name_or_path = checkpoint_path
            else:
                model_path = checkpoint_path
                lora_weights_name_or_path = None
    else:
        if not checkpoint_path:
            model_path = model_args.model_name_or_path
            lora_weights_name_or_path = model_args.lora_weights_name_or_path
        else:
            if model_args.use_lora:
                model_path = model_args.model_name_or_path
                lora_weights_name_or_path = checkpoint_path
            else:
                model_path = checkpoint_path
                lora_weights_name_or_path = None

    if model_args.use_lora and lora_weights_name_or_path is None:
        logging.warning(
            "You are have specified to use LORA, but have not specified a path to the "
            "LORA weights. We will attempt to load the LORA weights from the same "
            f"path as the model weights: {model_path}."
        )

    model, tokenizer = load_model_for_inference(
        weights_path=model_path,
        int8_quantization=model_args.int8_quantization,
        lora_weights_name_or_path=lora_weights_name_or_path,
    )

    trainer = CollieTrainer(
        model=model,
        args=training_args,
        data_collator=DataCollatorForSeq2Seq(
            tokenizer,
            pad_to_multiple_of=8,
            return_tensors="pt",
            padding=True,
            label_pad_token_id=tokenizer.pad_token_id,
        ),
    )

    for test_task in data_args.test_tasks:
        test_dataset = os.path.join(
            data_args.dataset_dir,
            f"{test_task}.{'test' if not data_args.use_dev_inference else 'dev'}.jsonl",
        )
        test_dataset = CollieDataset(
            tokenizer=tokenizer,
            dataset_path=test_dataset,
            max_length=data_args.max_seq_length,
            is_encoder_decoder=model.config.is_encoder_decoder,
            inference=True if training_args.predict_with_generate else False,
        )

        logging.info(f"Running inference on {test_task}...")
        predictions = trainer.predict(test_dataset)

        output_dir = training_args.output_dir if checkpoint_path is None else checkpoint_path
        if training_args.predict_with_generate:
            output_name = f"{os.path.join(output_dir,'predictions',test_task)}.predictions.jsonl"

            os.makedirs(os.path.join(output_dir, "predictions"), exist_ok=True)

            with open(output_name, "w", encoding="utf8") as f:
                logging.info(f"Writing predictions to {output_name}")
                predictions = predictions.predictions
                # Switch all -100 to tokenizer.pad_token_id, so we can decode the predictions
                predictions[predictions == -100] = tokenizer.pad_token_id

                try:
                    predictions = tokenizer.batch_decode(predictions, skip_special_tokens=True)
                except OverflowError:
                    raise OverflowError(f"Unable to decode predictions: {predictions}")

                for prediction in predictions:
                    print(
                        json.dumps({"model_prediction": prediction}, ensure_ascii=False),
                        file=f,
                    )

        else:
            metrics_name = f"{os.path.join(output_dir,test_task)}.metrics.json"
            with open(metrics_name, "w", encoding="utf8") as f:
                logging.info(f"Writing metrics to {metrics_name}")
                json.dump(predictions.metrics, fp=f, ensure_ascii=False, indent=4)

    if training_args.predict_with_generate:
        evaluate(model_args, data_args, training_args, checkpoint_path=checkpoint_path)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    parser = HfArgumentParser((ModelArguments, DataTrainingArguments, Seq2SeqTrainingArguments))
    logging.info(f"Sys args {sys.argv}")

    if len(sys.argv) > 0 and sys.argv[-1].endswith(".json"):
        # If we pass only one argument to the script, and it's the path to a json file,
        # let's parse it to get our arguments.
        logging.info(f"Loading json config {sys.argv[-1]}")
        model_args, data_args, training_args = parser.parse_json_file(json_file=os.path.abspath(sys.argv[-1]))

    elif len(sys.argv) > 0 and sys.argv[-1].endswith(".yaml"):
        # If we pass only one argument to the script, and it's the path to a yaml file,
        # let's parse it to get our arguments.
        logging.info(f"Loading yaml config {sys.argv[-1]}")
        model_args, data_args, training_args = parser.parse_yaml_file(yaml_file=os.path.abspath(sys.argv[-1]))
    else:
        logging.info("No config file passed, using command line arguments.")
        model_args, data_args, training_args = parser.parse_args_into_dataclasses()

    if data_args.train_tasks is not None:
        train_collie(
            model_args,
            data_args,
            training_args,
        )
        clean_cache()

    if data_args.test_tasks is not None:
        if not data_args.evaluate_all_checkpoints:
            inference_collie(
                model_args,
                data_args,
                training_args,
            )
            clean_cache()
        else:
            # Find all checkpoints in the output directory
            checkpoints = [
                c
                for c in glob.glob(
                    os.path.join(training_args.output_dir, "checkpoint-*"),
                )
                if os.path.isdir(c)
            ]

            # Sort checkpoints by step number
            checkpoints = sorted(checkpoints, key=lambda x: int(x.split("-")[-1]))
            # Evaluate only checkpoints with more than 1000 steps, underfited models are very slow to evaluate
            checkpoints = [c for c in checkpoints if int(c.split("-")[-1]) > 1000]

            logging.info(
                f"Found {len(checkpoints)} checkpoints in {training_args.output_dir}:"
                f" {checkpoints} . We will evaluate each of them."
            )

            # Evaluate each checkpoint
            for checkpoint in checkpoints:
                inference_collie(
                    model_args,
                    data_args,
                    training_args,
                    checkpoint_path=checkpoint,
                )
                clean_cache()
