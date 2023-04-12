import json
import os
import sys
from typing import Dict, Type
from transformers import HfArgumentParser, Seq2SeqTrainingArguments

import logging
import importlib
import rich

from src.config import DataTrainingArguments, ModelArguments
from src.tasks import TASK_ID_TO_TASKS


def import_prompts(task_module: str) -> None:
    """Imports everything from a module.

    Args:
        task_module (str): the module to import everything from.
    """
    # get a handle on the module
    mdl = importlib.import_module(task_module)

    # # is there an __all__?  if so respect it
    # if "__all__" in mdl.__dict__:
    #     names = mdl.__dict__["__all__"]
    # else:
    #     # otherwise we import all names that don't begin with _
    #     names = [x for x in mdl.__dict__ if not x.startswith("_")]
    names = {x: y for x, y in mdl.__dict__.items() if not x.startswith("_")}

    # now drag them in
    globals().update({k: v for k, v in names.items()})


def get_class(class_path: str) -> Type:
    components = class_path.split(".")
    mod = __import__(components[0])
    for comp in components[1:]:
        mod = getattr(mod, comp)

    return mod


def fix_prompt_outputs(text: str) -> str:
    """Fixes some known structural bugs.

    Args:
        text (str): Bugged output.

    Returns:
        str: Corrected output.
    """

    text = text.replace(")\n ", "),\n ")
    return text


def evaluate(
    model_args: ModelArguments,
    data_args: DataTrainingArguments,
    training_args: Seq2SeqTrainingArguments,
) -> Dict[str, Dict[str, float]]:
    """This function evaluates the output of a model.

    Args:
        model_args (ModelArguments): Model arguments. See `ModelArguments` docs.
        data_args (DataTrainingArguments): Data arguments. See `DataTrainingArguments` docs.

    Returns:
        Dict[str, Dict[str, float]]: A dictionary containing the scores for each task
        present in the dataset.
    """

    predictions_dir = os.path.join(model_args.lora_weights_name_or_path, "predictions")
    gold_data_dir = data_args.dataset_dir
    all_scores = {}

    for task in data_args.test_tasks:
        gold_path = os.path.join(
            gold_data_dir,
            f"{task}.{'test' if not data_args.use_dev_inference else 'dev'}.jsonl",
        )
        pred_path = os.path.join(predictions_dir, task) + ".predictions.jsonl"

        if not os.path.exists(gold_path):
            raise FileNotFoundError(f"File not found: '{gold_path}'")

        if not os.path.exists(pred_path):
            raise FileNotFoundError(f"File not found: '{pred_path}'")

        task_module = None
        scorer = None

        labels = []
        predictions = []
        with open(gold_path, "rt") as gold_f, open(pred_path, "rt") as pred_f:
            for gold_line, pred_line in zip(gold_f, pred_f):
                gold_line = json.loads(gold_line)
                pred_line = json.loads(pred_line)

                # TODO: Filtrar por spans que aparezcan en la frase


                if not task_module:
                    task_module = TASK_ID_TO_TASKS[gold_line['task_id']] + ".prompts"
                    import_prompts(task_module)

                if not scorer:
                    scorer = get_class(gold_line["scorer_cls"])()

                try:
                    gold_labels = fix_prompt_outputs(str(gold_line["labels"]))
                    gold_labels = [eval(item) for item in eval(gold_labels)]
                except Exception:
                    # TODO: Guardar los bugs
                    logging.warn("Found an incorrect formated gold file!")
                    gold_labels = []

                try:
                    pred_labels = fix_prompt_outputs(
                        pred_line["model_prediction"].strip().split("result = ")[-1]
                    )
                    pred_labels = eval(pred_labels)
                except Exception:
                    logging.warn("Found an incorrect formated pred file!")
                    pred_labels = []

                labels.append(gold_labels)
                predictions.append(pred_labels)

        # rich.print(list(zip(labels, predictions)))

        scores = scorer(reference=labels, predictions=predictions)
        all_scores[task] = scores

    scores_file_name = os.path.join(training_args.output_dir, 'task_scores.json')
    with open(scores_file_name, 'wt') as f:
        json.dump(all_scores, f, indent=4, ensure_ascii=False)
    logging.info(f"Scores saved in: {scores_file_name}")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    parser = HfArgumentParser(
        (ModelArguments, DataTrainingArguments, Seq2SeqTrainingArguments)
    )

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

    if data_args.test_tasks is not None:
        evaluate(
            model_args,
            data_args,
            training_args,
        )
