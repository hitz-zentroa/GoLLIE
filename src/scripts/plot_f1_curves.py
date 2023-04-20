import glob
import json
import logging
import os
import time
from argparse import ArgumentParser

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


sns.set_theme(style="whitegrid")


def plot_curves(args):
    results_dict = {}
    for dir_path in glob.glob(os.path.join(args.models_path, args.regexp)):
        logging.info("Processing model output:" + dir_path)

        key = os.path.basename(dir_path)

        for chkpt in glob.glob(os.path.join(dir_path, "checkpoint-*")):
            logging.info("Checkpoint: " + os.path.basename(chkpt))
            scores_file = os.path.join(chkpt, "task_scores.json")
            if not os.path.exists(scores_file):
                continue

            step = int(os.path.basename(chkpt).split("-")[-1])

            trainer_state_file = os.path.join(chkpt, "trainer_state.json")
            if os.path.exists(trainer_state_file):
                with open(trainer_state_file) as f:
                    step_info = json.load(f)["log_history"][-1]
            else:
                step_info = {"step": step}

            with open(scores_file) as f:
                scores = json.load(f)

            for dataset, values in scores.items():
                for task, values in values.items():
                    if task == "prediction_stats":
                        continue
                    if dataset not in results_dict:
                        results_dict[dataset] = {}

                    if task not in results_dict[dataset]:
                        results_dict[dataset][task] = {}

                    if args.hue:
                        _key = key.replace(args.hue, "").replace("__", "_").rstrip("_")

                    if args.hue and _key not in results_dict[dataset][task]:
                        results_dict[dataset][task][_key] = {}
                    elif not args.hue and key not in results_dict[dataset][task]:
                        results_dict[dataset][task][key] = {}

                    if args.hue:
                        if step not in results_dict[dataset][task][_key]:
                            results_dict[dataset][task][_key][step] = {}

                        results_dict[dataset][task][_key][step][args.hue in key] = {**values, **step_info}
                    else:
                        if step not in results_dict[dataset][task][key]:
                            results_dict[dataset][task][key][step] = {}

                        results_dict[dataset][task][key][step] = {**values, **step_info}

    result_list = []
    for dataset, values in results_dict.items():
        for task, values in values.items():
            for model, values in values.items():
                for chkpt, values in values.items():
                    if args.hue:
                        for hue, values in values.items():
                            result_list.append(
                                {
                                    "dataset": dataset,
                                    "task": task,
                                    "model": model,
                                    "steps": chkpt,
                                    f"{args.hue}": hue,
                                    **values,
                                }
                            )
                    else:
                        result_list.append(
                            {
                                "dataset": dataset,
                                "task": task,
                                "model": model,
                                "steps": chkpt,
                                f"{args.hue}": False,
                                **values,
                            }
                        )
    localtime = time.localtime()
    timestamp = (
        f"{localtime.tm_year}-{localtime.tm_mon}-{localtime.tm_mday}-{localtime.tm_hour}-"
        + f"{localtime.tm_min}-{localtime.tm_sec}"
    )

    df = pd.DataFrame(result_list)
    logging.info(f"Available columns: {df.columns}")
    f = plt.figure(figsize=(10, 5))
    sns.lineplot(
        data=df,
        x=args.x,
        y=args.y,
        hue="model",
        size=args.hue,
        size_order=[True, False] if args.hue else None,
        palette="tab10",
        linewidth=2.5,
    )
    plt.tight_layout()
    f.savefig(f"assets/plots/{timestamp}.png", dpi=400)


if __name__ == "__main__":
    """
    Example: python -m src.scripts.plot_f1_curves --regexp "*optim*" --hue "ignore_prompt_loss"
    """
    logging.basicConfig(level=logging.INFO)

    parser = ArgumentParser()

    parser.add_argument("--models_path", type=str, default="/ikerlariak/igarcia945/CoLLIE/pretrained_models")
    parser.add_argument("--regexp", type=str, default="*")
    parser.add_argument("--hue", type=str, default=None)
    parser.add_argument("--x", type=str, default="steps")
    parser.add_argument("--y", type=str, default="f1-score")

    args = parser.parse_args()
    plot_curves(args)
