import json

import numpy as np
import pandas as pd
from tabulate import tabulate


SUP_DATASETS = [
    ("ace05.ner", "entities"),
    ("ace05.re", "relations"),
    ("ace05.ee", "events"),
    ("ace05.eae", "arguments"),
    ("bc5cdr.ner", "entities"),
    ("conll03.ner", "entities"),
    ("diann.ner", "entities"),
    ("ncbidisease.ner", "entities"),
    ("ontonotes5.ner", "entities"),
    ("rams.eae", "arguments"),
    ("tacred.sf", "slots"),
    ("wnut17.ner", "entities"),
]

ZERO_DATASETS = [
    ("broadtwitter.ner", "entities"),
    ("casie.ee", "events"),
    ("casie.eae", "arguments"),
    ("crossner.crossner_ai", "entities"),
    ("crossner.crossner_literature", "entities"),
    ("crossner.crossner_music", "entities"),
    ("crossner.crossner_politics", "entities"),
    ("crossner.crossner_natural_science", "entities"),
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

PATHS = {
    "Baseline": "/ikerlariak/osainz006/models/collie/Baseline-7b_CodeLLaMA{seed}/task_scores_summary.json",
    "GoLLIE": "/ikerlariak/osainz006/models/collie/CoLLIE+-7b_CodeLLaMA{seed}/task_scores_summary.json",
    "w/o Candidates": "/ikerlariak/osainz006/models/collie/CoLLIE-7b_CodeLLaMA{seed}/task_scores_summary.json",
    "w/o Masking": (
        "/ikerlariak/osainz006/models/collie/CoLLIE+-7b_CodeLLaMA{seed}_abl_masking/task_scores_summary.json"
    ),
    "w/o Dropout": (
        "/ikerlariak/osainz006/models/collie/CoLLIE+-7b_CodeLLaMA{seed}_abl_dropout/task_scores_summary.json"
    ),
    "13B": "/ikerlariak/osainz006/models/collie/CoLLIE+-13b_CodeLLaMA{seed}/task_scores_summary.json",
    "34B": "/ikerlariak/osainz006/models/collie/CoLLIE+-34b_CodeLLaMA{seed}/task_scores_summary.json",
}

SEEDS = ["", "_2", "_3"]


data = []
for name, path in PATHS.items():
    print()
    print(name)
    sup_results, zero_results = [], []
    i = 0
    for seed in SEEDS:
        print(seed)
        if name == "Baseline" and seed:
            seed += "/1"
        try:
            with open(path.format(seed=seed)) as f:
                results = json.load(f)
        except FileNotFoundError:
            continue
        i += 1
        _sup_results = []
        for dataset, task in SUP_DATASETS:
            _sup_results.append(results[dataset][task]["f1-score"] * 100)
        sup_results.append(_sup_results + [np.mean(_sup_results)])
        _zero_results, _zero_sota_results = [], []
        for dataset, task in ZERO_DATASETS:
            _zero_results.append(results[dataset][task]["f1-score"] * 100)
            if dataset.startswith("crossner") or dataset.startswith("mit") or dataset.startswith("wikievents"):
                _zero_sota_results.append(results[dataset][task]["f1-score"] * 100)
        zero_results.append(_zero_results + [np.mean(_zero_sota_results), np.mean(_zero_results)])

    sup_results.append(np.array(sup_results).mean(0))
    sup_results.append(np.array(sup_results).std(0))

    zero_results.append(np.array(zero_results).mean(0))
    zero_results.append(np.array(zero_results).std(0))

    columns = list(map(str, range(i))) + ["Average", "Std"]

    sup_results = pd.DataFrame(sup_results, columns=[dataset[0] for dataset in SUP_DATASETS] + ["Average"]).T
    sup_results.columns = columns
    print(tabulate(sup_results, headers=columns, floatfmt=".1f"))

    zero_results = pd.DataFrame(
        zero_results, columns=[dataset[0] for dataset in ZERO_DATASETS] + ["Zero Average", "Average"]
    ).T
    zero_results.columns = columns
    print(tabulate(zero_results, headers=columns, floatfmt=".1f"))

    # print(tabulate(sup_results, floatfmt=".1f", headers=[dataset[0] for dataset in SUP_DATASETS]))
    # print(tabulate(zero_results, floatfmt=".1f", headers=[dataset[0] for dataset in ZERO_DATASETS]))
