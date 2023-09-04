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
from src.dataset.dataset import CollieDataset, DataCollatorForCoLLIE
from src.evaluate import evaluate
from src.model.load_model import load_model, merge_lora_model
from src.trainer import CollieTrainer, ConcatDataset, get_correct_torch_dtype
from transformers import (
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

    model, tokenizer = load_model(
        inference=False,
        model_weights_name_or_path=model_args.model_name_or_path,
        quantization=model_args.quantization,
        use_lora=model_args.use_lora,
        lora_r=model_args.lora_r,
        lora_target_modules=model_args.lora_target_modules,
        torch_dtype=get_correct_torch_dtype(
            quantization=model_args.quantization, model_args=model_args, training_args=training_args
        ),
        force_auto_device_map=model_args.force_auto_device_map,
        use_gradient_checkpointing=training_args.gradient_checkpointing,
        use_better_transformer=model_args.use_better_transformer,
        trust_remote_code=model_args.trust_remote_code,
        use_flash_attention=model_args.use_flash_attention,
        fsdp_training=len(training_args.fsdp) > 1 or training_args.fsdp_config is not None,
        max_memory_MB=model_args.max_memory_MB,
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
        f" {data_args.ignore_pad_token_for_loss} and 'prompt_loss_weight':"
        f" {data_args.prompt_loss_weight}"
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
            prompt_loss_weight=data_args.prompt_loss_weight,
            max_examples=data_args.max_examples_per_task_train,
        )
        training_datasets.append(train_dataset)

    train_dataset = ConcatDataset(training_datasets)

    dev_datasets = DatasetDict()
    for dev_task in data_args.validation_tasks:
        dev_path = os.path.join(data_args.dataset_dir, f"{dev_task}.dev.jsonl")
        dev_dataset = CollieDataset(
            tokenizer=tokenizer,
            dataset_path=dev_path,
            max_length=data_args.max_seq_length,
            is_encoder_decoder=model.config.is_encoder_decoder,
            inference=False,
            prompt_loss_weight=0.0,
            max_examples=data_args.max_examples_per_task_val,
        )
        dev_datasets[os.path.splitext(os.path.basename(dev_path))[0]] = dev_dataset

    trainer = CollieTrainer(
        model=model,
        tokenizer=tokenizer,
        train_dataset=train_dataset,
        eval_dataset=dev_datasets,
        args=training_args,
        data_collator=DataCollatorForCoLLIE(
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

    delete_merged_model: bool = False
    if model_args.merge_lora_before_eval:
        logging.info("You have specified to merge the LORA weights before evaluation. We will attempt to do so.")
        if model_args.quantization is None:
            logging.warning(
                "You have specified to create a merged model (merge_lora_before_eval=True), but you have not specified"
                " a quantization precision. Model loades without quantization are automatically merged when loaded for"
                " inference, so there is no need to save a merged model and reaload it. This flag is only useful when"
                " you want to merge a model and then load it using 4 bits ot 8 bits quantization or if you plan to"
                " release the merged model."
            )
        if os.path.exists(os.path.join(training_args.output_dir, "merged_model")):
            logging.info(
                f"A merged model already exists at {os.path.join(training_args.output_dir,'merged_model')}. We will"
                " use this model."
            )
            delete_merged_model = False

        else:
            merge_lora_model(
                weights_path=model_path,
                lora_weights_name_or_path=lora_weights_name_or_path,
                torch_dtype=model_args.torch_dtype,
                output_path=os.path.join(training_args.output_dir, "merged_model"),
            )
            delete_merged_model = not model_args.keep_merged_model_after_eval

        model_path = os.path.join(training_args.output_dir, "merged_model")
        lora_weights_name_or_path = None
        clean_cache()  # Ensure that nothing remains in the cache, as we will load the mergen model next.

    model, tokenizer = load_model(
        inference=True,
        model_weights_name_or_path=model_path,
        quantization=model_args.quantization_inference,
        use_lora=model_args.lora_weights_name_or_path is not None,
        lora_weights_name_or_path=lora_weights_name_or_path,
        force_auto_device_map=model_args.force_auto_device_map,
        torch_dtype=get_correct_torch_dtype(
            quantization=model_args.quantization_inference, model_args=model_args, training_args=training_args
        ),
        use_better_transformer=model_args.use_better_transformer,
        trust_remote_code=model_args.trust_remote_code,
        use_flash_attention=model_args.use_flash_attention,
        max_memory_MB=model_args.max_memory_MB,
    )

    trainer = CollieTrainer(
        model=model,
        args=training_args,
        data_collator=DataCollatorForCoLLIE(
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
            prompt_loss_weight=0.0,
            max_examples=data_args.max_examples_per_task_test,
        )

        logging.info(f"Running inference on {test_task}...")
        predictions = trainer.predict(test_dataset)

        if not trainer.is_world_process_zero():
            # In distributed training, we only want one process to write predictions to the file.
            continue

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

    if training_args.predict_with_generate and trainer.is_world_process_zero():
        task_scores = evaluate(model_args, data_args, training_args, checkpoint_path=checkpoint_path)
        # Add test_ prefix to report test scores
        task_scores = {f"test_{task}": score for task, score in task_scores.items()}
        # Report
        trainer.log(task_scores)

    if delete_merged_model:
        logging.info(f"Deleting merged model at {model_path}")
        import shutil

        try:
            shutil.rmtree(model_path)
        except OSError as e:
            logging.error(
                f"Unable to delete the merged model {model_path} : {e.strerror}\n"
                "You may need to delete the merged model manually."
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
        if model_args.use_lora and model_args.merge_lora_after_training:
            merge_lora_model(
                weights_path=model_args.model_name_or_path,
                lora_weights_name_or_path=training_args.output_dir,
                torch_dtype=model_args.torch_dtype,
                output_path=os.path.join(training_args.output_dir, "merged_model"),
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
            no_eval_checkpoints = [c for c in checkpoints if int(c.split("-")[-1]) < 1000]
            if len(no_eval_checkpoints) > 0:
                logging.warning(
                    f"Found {len(no_eval_checkpoints)} checkpoints in {training_args.output_dir} that will not be"
                    f" evaluated: {no_eval_checkpoints} . We will evaluate only checkpoints trained for 1000 or more"
                    " steps, underfit models are very slow to evaluate."
                )

            checkpoints = [c for c in checkpoints if int(c.split("-")[-1]) >= 1000]

            # Add also the last checkpoint (stored in the output_dir)
            # checkpoints.append(training_args.output_dir)

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
