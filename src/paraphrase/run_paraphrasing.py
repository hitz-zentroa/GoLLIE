import json
import logging
import os
import sys

from fastchat.conversation import get_conv_template

from src.config import ModelArguments
from src.model.load_model import load_model
from src.paraphrase.config import DataInferenceArguments
from src.paraphrase.dataset import ParaphraseDataset
from src.paraphrase.utils import clean_guidelines, format_guidelines_as_py, update_guidelines
from src.tasks import task_id_to_guidelines
from src.trainer import get_correct_torch_dtype
from transformers import DataCollatorForSeq2Seq, HfArgumentParser, Seq2SeqTrainer, Seq2SeqTrainingArguments


def run_paraphrasing(
    model_args: ModelArguments,
    data_args: DataInferenceArguments,
    training_args: Seq2SeqTrainingArguments,
):
    if not training_args.predict_with_generate:
        raise ValueError("Set `predict_with_generate` to `True` in the config file to run this script.")

    logging.info(
        f"Loading model from {model_args.model_name_or_path}.\n"
        f"   - quantization: {model_args.quantization}\n"
        f"   - lora_weights_name_or_path: {model_args.lora_weights_name_or_path}\n"
    )

    model, tokenizer = load_model(
        inference=True,
        model_weights_name_or_path=model_args.model_name_or_path,
        quantization=model_args.quantization,
        use_lora=model_args.lora_weights_name_or_path is not None,
        lora_weights_name_or_path=model_args.lora_weights_name_or_path,
        force_auto_device_map=model_args.force_auto_device_map,
        torch_dtype=get_correct_torch_dtype(
            quantization=model_args.quantization_inference, model_args=model_args, training_args=training_args
        ),
        use_better_transformer=model_args.use_better_transformer,
        trust_remote_code=model_args.trust_remote_code,
        use_flash_attention=model_args.use_flash_attention,
        max_memory_MB=model_args.max_memory_MB,
    )

    trainer = Seq2SeqTrainer(
        tokenizer=tokenizer,
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

    with open(data_args.generation_args_json, "r", encoding="utf8") as f:
        gen_kwargs = json.load(f)
        logging.info(f"Generation kwargs: {json.dumps(gen_kwargs, indent=2,ensure_ascii=False)}")

    if gen_kwargs["num_beams"] > 1 and gen_kwargs["do_sample"]:
        logging.warning(
            "You are using `num_beams` > 1 and `do_sample`. Beam-search multinomial sampling from huggingface"
            " transformers is not stable, you may get this error: 'RuntimeError: probability tensor contains either"
            " inf, nan or element < 0'. To avoid this error, set `do_sample` to `False` or use `num_beams` = 1."
        )

    num_return_sequences = gen_kwargs.pop("num_return_sequences", 1)

    for dataset_name in data_args.datasets:
        logging.info(f"Running inference on {dataset_name}...")

        guidelines = task_id_to_guidelines(dataset_name)
        guidelines = clean_guidelines(guidelines)

        test_dataset = ParaphraseDataset(
            tokenizer=tokenizer,
            dataset_name=dataset_name,
            language=data_args.language,
            is_encoder_decoder=model.config.is_encoder_decoder,
            max_length=1024,
            conv_template=data_args.config_template,
        )

        output_path = os.path.join(training_args.output_dir, dataset_name, "guidelines.py")
        output_path_orig_outputs = os.path.join(training_args.output_dir, dataset_name, "original_outputs.txt")

        os.makedirs(os.path.dirname(output_path), exist_ok=True)

        # Trainer.predict does not support multiple return sequences, so we have to do it manually

        with open(output_path_orig_outputs, "w", encoding="utf8") as f:
            for i in range(num_return_sequences):
                predictions = trainer.predict(test_dataset, **gen_kwargs).predictions
                predictions[predictions == -100] = tokenizer.pad_token_id

                try:
                    predictions = tokenizer.batch_decode(predictions, skip_special_tokens=True)
                except OverflowError:
                    raise OverflowError(f"Unable to decode predictions: {predictions}")

                for prediction in predictions:
                    print(prediction, file=f)
                    print("\n====================\n", file=f)

                if data_args.config_template is not None:
                    conv = get_conv_template(data_args.config_template)
                    predictions = [prediction.split(conv.roles[1])[-1].strip() for prediction in predictions]
                # rich.print(predictions)

                predictions = [prediction.strip().strip("\n") for prediction in predictions]
                predictions = [prediction.split("\n")[-1].strip() for prediction in predictions]
                predictions = [":".join(prediction.split(":")[1:]) for prediction in predictions]

                guidelines = update_guidelines(
                    paraphrases=predictions,
                    guidelines=guidelines,
                    language=data_args.language,
                )

                f.flush()

        with open(output_path, "w", encoding="utf8") as f:
            print(format_guidelines_as_py(guidelines), file=f)
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
