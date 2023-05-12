from src.model.load_model import load_model_for_inference
from transformers import Trainer, Seq2SeqTrainingArguments, HfArgumentParser, DataCollatorForSeq2Seq
from src.paraphrase.config import DataInferenceArguments
from src.config import ModelArguments
from src.paraphrase.dataset import ParaphraseDataset
import torch
import argparse
import logging
import os
from src.paraphrase.utils import update_guidelines, get_num_return_sentences, format_guidelines_as_py
import sys


def run_paraphrasing(
    model_args: ModelArguments,
    data_args: DataInferenceArguments,
    training_args: Seq2SeqTrainingArguments,
):
    if not training_args.predict_with_generate:
        raise ValueError("Set `predict_with_generate` to `True` in the config file to run this script.")

    model, tokenizer = load_model_for_inference(
        weights_path=model_args.model_name_or_path,
        int8_quantization=model_args.int8_quantization,
        lora_weights_name_or_path=model_args.lora_weights_name_or_path,
    )

    trainer = Trainer(
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

    for dataset_name in data_args.datasets:
        logging.info(f"Running inference on {dataset_name}...")

        test_dataset = ParaphraseDataset(
            tokenizer=tokenizer,
            dataset_name=dataset_name,
            language=data_args.language,
            is_encoder_decoder=model.config.is_encoder_decoder,
            max_length=training_args.max_length,
            conv_template=data_args.config_template,
        )

        output_path = os.path.join(training_args.output_dir, dataset_name, "guidelines_paraphrase.py")

        os.makedirs(os.path.dirname(output_path), exist_ok=True)

        predictions = trainer.predict(test_dataset).predictions
        predictions[predictions == -100] = tokenizer.pad_token_id

        try:
            predictions = tokenizer.batch_decode(predictions, skip_special_tokens=True)
        except OverflowError:
            raise OverflowError(f"Unable to decode predictions: {predictions}")

        augmented_guidelines = update_guidelines(
            paraphrases=predictions,
            task_name=dataset_name,
            language=data_args.language,
            num_paraphrases_per_guideline=get_num_return_sentences(training_args.generation_config),
        )

        with open(output_path, "w", encoding="utf8") as f:
            print(format_guidelines_as_py(augmented_guidelines), file=f)
            logging.info(f"Saved guidelines to {output_path}")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    parser = HfArgumentParser((ModelArguments, DataInferenceArguments, Seq2SeqTrainingArguments))
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

    run_paraphrasing(
        model_args=model_args,
        data_args=data_args,
        training_args=training_args,
    )
