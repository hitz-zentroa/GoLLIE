import argparse
import json
import os
from typing import Dict, List


def compare_class_scores(model_paths: str, output_path: str):
    """
    Compare the class scores of multiple models and save the results to a CSV file.

    Args:
        model_paths (`List[str]`):
            List of paths to the models to compare.
        output_path (`str`):
            Path to the output CSV file.
    """
    class_scores: Dict[str, Dict[str, List[str]]] = {}
    for model_path in model_paths:
        task_scores_json = os.path.join(model_path, "task_scores.json")
        if not os.path.exists(task_scores_json):
            raise FileNotFoundError(f"task_scores.json not found in {model_path}")
        with open(task_scores_json, "r", encoding="utf8") as f:
            task_scores = json.load(f)
        for dataset, values in task_scores.items():
            for task, values in values.items():
                if "class_scores" in values:
                    name = f"{dataset}.{task}"
                    if name not in class_scores:
                        class_scores[name] = {}

                    for label, score in values["class_scores"].items():
                        if label not in class_scores[name]:
                            class_scores[name][label] = []
                        class_scores[name][label].append(str(score["f1-score"]))

    # Convert dict into CSV
    with open(output_path, "w", encoding="utf8") as f:
        print(f"Label,{','.join(model_paths)}", file=f)
        for name, scores in class_scores.items():
            print(name, file=f)
            for label, score in scores.items():
                print(f"{label},{','.join(score)}", file=f)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--model_paths", type=str, nargs="+", required=True, help="Paths to the models to compare.")
    parser.add_argument("--output_path", type=str, required=True, help="Path to the output CSV file.")
    args = parser.parse_args()
    compare_class_scores(args.model_paths, args.output_path)
