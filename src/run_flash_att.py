from src.model.path_flash_att_llama import replace_llama_attn_with_flash_attn


replace_llama_attn_with_flash_attn()

import glob
import logging
import os
import sys

from src.run import clean_cache, inference_collie, train_collie

from src.config import DataTrainingArguments, ModelArguments
from transformers import (
    HfArgumentParser,
    Seq2SeqTrainingArguments,
)


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

    if training_args.do_train and data_args.train_tasks is not None:
        train_collie(
            model_args,
            data_args,
            training_args,
        )
        clean_cache()

    if training_args.do_predict and data_args.test_tasks is not None:
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
            # Evaluate only checkpoints trained for 1000 or more steps, underfit models are very slow to evaluate
            checkpoints = [c for c in checkpoints if int(c.split("-")[-1]) >= 1000]

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
