import json

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


sns.set_theme(style="whitegrid")

MODELS_DIR = "/ikerlariak/osainz006/models/collie"
BASELINE_PATH = (
    f"{MODELS_DIR}/CoLLIE-7b_CodeLLaMA_baseline_lora4_flash_together/checkpoint-15486/task_scores_summary.json"
)
CoLLIE_PATH = f"{MODELS_DIR}/CoLLIE-7b_CodeLLaMA_lora4_flash_together/checkpoint-15486/task_scores_summary.json"
CoLLIEp_PATH = f"{MODELS_DIR}/CoLLIE-7b_CodeLLaMA_examples_lora4_flash_together_lora_r_8_all_3e-4/checkpoint-15486/task_scores_summary.json"

ZERO_SHOT_DATASETS = [
    ("broadtwitter.ner", "entities"),
    ("casie.ee", "events"),
    ("casie.eae", "arguments"),
    ("e3c.ner", "entities"),
    ("fabner.ner", "entities"),
    ("harveyner.ner", "entities"),
    ("mitmovie.ner", "entities"),
    ("mitrestaurant.ner", "entities"),
    ("multinerd.ner", "entities"),
    ("wikievents.ner", "entities"),
    ("wikievents.ee", "events"),
    ("wikievents.eae", "arguments"),
]


def main():
    with open(BASELINE_PATH) as f:
        baseline_results = json.load(f)

    baseline_ner_results = [
        baseline_results.get(dataset[0])[dataset[1]]["f1-score"]
        for dataset in ZERO_SHOT_DATASETS
        if dataset[1] == "entities"
    ]
    baseline_ee_results = [
        baseline_results.get(dataset[0])[dataset[1]]["f1-score"]
        for dataset in ZERO_SHOT_DATASETS
        if dataset[1] == "events"
    ]
    baseline_eae_results = [
        baseline_results.get(dataset[0])[dataset[1]]["f1-score"]
        for dataset in ZERO_SHOT_DATASETS
        if dataset[1] == "arguments"
    ]

    with open(CoLLIE_PATH) as f:
        collie_results = json.load(f)

    collie_ner_results = [
        collie_results.get(dataset[0])[dataset[1]]["f1-score"]
        for dataset in ZERO_SHOT_DATASETS
        if dataset[1] == "entities"
    ]
    collie_ee_results = [
        collie_results.get(dataset[0])[dataset[1]]["f1-score"]
        for dataset in ZERO_SHOT_DATASETS
        if dataset[1] == "events"
    ]
    collie_eae_results = [
        collie_results.get(dataset[0])[dataset[1]]["f1-score"]
        for dataset in ZERO_SHOT_DATASETS
        if dataset[1] == "arguments"
    ]

    with open(CoLLIEp_PATH) as f:
        colliep_results = json.load(f)

    colliep_ner_results = [
        colliep_results.get(dataset[0])[dataset[1]]["f1-score"]
        for dataset in ZERO_SHOT_DATASETS
        if dataset[1] == "entities"
    ]
    colliep_ee_results = [
        colliep_results.get(dataset[0])[dataset[1]]["f1-score"]
        for dataset in ZERO_SHOT_DATASETS
        if dataset[1] == "events"
    ]
    colliep_eae_results = [
        colliep_results.get(dataset[0])[dataset[1]]["f1-score"]
        for dataset in ZERO_SHOT_DATASETS
        if dataset[1] == "arguments"
    ]

    fig, ax = plt.subplots(1, 3, figsize=(15, 5))

    ax[0].set_title("NER")
    ax[0].bar(
        x=[0.5, 1.0, 1.5],
        height=[
            np.mean(baseline_ner_results) - 0.3,
            np.mean(collie_ner_results) - 0.3,
            np.mean(colliep_ner_results) - 0.3,
        ],
        align="edge",
        width=0.5,
        bottom=0.3,
    )
    ax[0].set_xticks(np.arange(0, 3.0, 0.5), [])
    ax[0].set_yticks(np.arange(0.3, 0.7, 0.1))

    ax[1].set_title("EE")
    ax[1].bar(
        x=[0.5, 1.0, 1.5],
        height=[
            np.mean(baseline_ee_results) - 0.3,
            np.mean(collie_ee_results) - 0.3,
            np.mean(colliep_ee_results) - 0.3,
        ],
        align="edge",
        width=0.5,
        bottom=0.3,
    )
    ax[1].set_xticks(np.arange(0, 3.0, 0.5), [])
    ax[1].set_yticks(np.arange(0.3, 0.7, 0.1))

    ax[2].set_title("EAE")
    ax[2].bar(
        x=[0.5, 1.0, 1.5],
        height=[
            np.mean(baseline_eae_results) - 0.3,
            np.mean(collie_eae_results) - 0.3,
            np.mean(colliep_eae_results) - 0.3,
        ],
        align="edge",
        width=0.5,
        bottom=0.3,
    )
    ax[2].set_xticks(np.arange(0, 3.0, 0.5), [])
    ax[2].set_yticks(np.arange(0.3, 0.7, 0.1))

    plt.savefig("assets/plots/zero_shot_results.png", dpi=300)


if __name__ == "__main__":
    main()
