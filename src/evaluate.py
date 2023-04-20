import glob
import importlib
import json
import logging
import os
import sys
from typing import Any, Dict, List, Type

from src.config import DataTrainingArguments, ModelArguments
from src.tasks import TASK_ID_TO_TASKS
from src.tasks.utils_typing import AnnotationList
from transformers import HfArgumentParser, Seq2SeqTrainingArguments


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
    globals().update(dict(names.items()))


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


def remove_hallucinations(unlabelled_sentence: str, predictions: List[Any]) -> List[Any]:
    """Removes predictions that are not in the unlabelled sentence.
    Args:
        unlabelled_sentence (str): The unlabelled sentence.
        predictions (List[Any]): The list of predictions.
    Returns:
        List[Any]: The list of predictions that are in the unlabelled sentence.
    """
    accepted_list: List[Any] = []
    for prediction in predictions:
        if prediction.exists_in(unlabelled_sentence):
            accepted_list.append(prediction)
    return accepted_list


def evaluate(
    model_args: ModelArguments,
    data_args: DataTrainingArguments,
    training_args: Seq2SeqTrainingArguments,
    checkpoint_path: str = None,
) -> Dict[str, Dict[str, float]]:
    """This function evaluates the output of a model.

    Args:
        model_args (ModelArguments): Model arguments. See `ModelArguments` docs.
        data_args (DataTrainingArguments): Data arguments. See `DataTrainingArguments` docs.

    Returns:
        Dict[str, Dict[str, float]]: A dictionary containing the scores for each task
        present in the dataset.
    """
    if checkpoint_path is None:
        output_dir = training_args.output_dir
    else:
        output_dir = checkpoint_path

    predictions_dir = os.path.join(output_dir, "predictions")

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
        impossible_to_parse: int = 0
        valid_predictions: int = 0
        hallucinated_predictions: int = 0
        total_predictions: int = 0

        with open(gold_path, "rt") as gold_f, open(pred_path, "rt") as pred_f:
            for gold_line, pred_line in zip(gold_f, pred_f):
                gold_line = json.loads(gold_line)
                pred_line = json.loads(pred_line)

                if not task_module:
                    task_module = TASK_ID_TO_TASKS[gold_line["task_id"]] + ".prompts"
                    import_prompts(task_module)

                if not scorer:
                    scorer = get_class(gold_line["scorer_cls"])()

                gold_labels = AnnotationList.from_output(str(gold_line["labels"]), task_module=task_module)

                pred_labels = pred_line["model_prediction"].strip().split("result = ")[-1]
                pred_labels = AnnotationList.from_output(str(pred_labels), task_module=task_module)
                filtered_pred_labels = pred_labels.filter_hallucinations(gold_line["unlabelled_sentence"])

                valid_predictions += len(filtered_pred_labels)
                hallucinated_predictions += len(pred_labels) - len(filtered_pred_labels)
                total_predictions += len(pred_labels)

                labels.append(gold_labels)
                predictions.append(filtered_pred_labels)

        # rich.print(list(zip(labels, predictions)))

        scores = scorer(reference=labels, predictions=predictions)
        all_scores[task] = scores
        all_scores[task]["prediction_stats"] = {}
        all_scores[task]["prediction_stats"]["impossible_to_parse"] = {}
        all_scores[task]["prediction_stats"]["hallucinated_predictions"] = {}
        all_scores[task]["prediction_stats"]["total"] = {}

        all_scores[task]["prediction_stats"]["impossible_to_parse"]["total"] = impossible_to_parse
        all_scores[task]["prediction_stats"]["impossible_to_parse"]["percentage"] = impossible_to_parse / len(
            predictions
        )
        all_scores[task]["prediction_stats"]["hallucinated_predictions"]["total"] = hallucinated_predictions
        all_scores[task]["prediction_stats"]["hallucinated_predictions"]["percentage"] = (
            hallucinated_predictions / total_predictions
        )
        all_scores[task]["prediction_stats"]["total"]["predictions"] = sum([len(x) for x in predictions])
        all_scores[task]["prediction_stats"]["total"]["gold"] = sum([len(x) for x in labels])

    scores_file_name = os.path.join(output_dir, "task_scores.json")
    with open(scores_file_name, "wt") as f:
        json.dump(all_scores, f, indent=4, ensure_ascii=False)
    logging.info(f"Scores saved in: {scores_file_name}")

    return all_scores


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    parser = HfArgumentParser((ModelArguments, DataTrainingArguments, Seq2SeqTrainingArguments))

    if len(sys.argv) == 2 and sys.argv[1].endswith(".json"):
        # If we pass only one argument to the script and it's the path to a json file,
        # let's parse it to get our arguments.
        model_args, data_args, training_args = parser.parse_json_file(json_file=os.path.abspath(sys.argv[1]))

    elif len(sys.argv) == 2 and sys.argv[1].endswith(".yaml"):
        # If we pass only one argument to the script and it's the path to a yaml file,
        # let's parse it to get our arguments.
        model_args, data_args, training_args = parser.parse_yaml_file(yaml_file=os.path.abspath(sys.argv[1]))
    else:
        model_args, data_args, training_args = parser.parse_args_into_dataclasses()

    if data_args.test_tasks is not None:
        if not data_args.evaluate_all_checkpoints:
            evaluate(
                model_args,
                data_args,
                training_args,
            )
        else:
            checkpoints = [
                c
                for c in glob.glob(
                    os.path.join(training_args.output_dir, "checkpoint-*"),
                )
                if os.path.isdir(c)
            ]

            logging.info(
                f"Found {len(checkpoints)} checkpoints in {training_args.output_dir}:"
                f" {checkpoints} . We will evaluate each of them."
            )

            for checkpoint in checkpoints:
                logging.info(f"Evaluating {checkpoint}")
                evaluate(
                    model_args,
                    data_args,
                    training_args,
                    checkpoint_path=checkpoint,
                )
