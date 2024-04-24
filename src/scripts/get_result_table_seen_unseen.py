import copy
import json

import numpy as np
from tabulate import tabulate


ZERO_DATASETS = [
    (
        "broadtwitter.ner",
        "entities",
        {"seen": {"Location", "Organization", "Person"}, "unseen": {}},
        {
            "TP": 0,
            "total_pos": 0,
            "total_pre": 0,
            "F1": 0,
        },  # Seen
        {
            "TP": 0,
            "total_pos": 0,
            "total_pre": 0,
            "F1": 0,
        },  # Unseen
        [0.0],  # Total F1
    ),
    (
        "casie.ee",
        "events",
        {
            "seen": {},
            "unseen": {
                "DatabreachAttack",
                "PhisingAttack",
                "RansomAttack",
                "VulnerabilityDiscover",
                "VulnerabilityPatch",
            },
        },
        {
            "TP": 0,
            "total_pos": 0,
            "total_pre": 0,
            "F1": 0,
        },  # Seen
        {
            "TP": 0,
            "total_pos": 0,
            "total_pre": 0,
            "F1": 0,
        },  # Unseen
        [0.0],  # Total F1
    ),
    (
        "crossner.crossner_ai",
        "entities",
        {
            "seen": {"Product", "Country", "Person", "Organization", "Location", "Miscellaneous", "Other"},
            "unseen": {
                "Field",
                "Task",
                "Algorithm",
                "Researcher",
                "Metric",
                "University",
                "ProgrammingLanguage",
                "Conference",
            },
        },
        {
            "TP": 0,
            "total_pos": 0,
            "total_pre": 0,
            "F1": 0,
        },  # Seen
        {
            "TP": 0,
            "total_pos": 0,
            "total_pre": 0,
            "F1": 0,
        },  # Unseen
        [0.0],  # Total F1
    ),
    (
        "crossner.crossner_literature",
        "entities",
        {
            "seen": {"Event", "Person", "Location", "Organization", "Country", "Miscellaneous", "Other"},
            "unseen": {"Book", "Writer", "Award", "Poem", "Magazine", "LiteraryGenre"},
        },
        {
            "TP": 0,
            "total_pos": 0,
            "total_pre": 0,
            "F1": 0,
        },  # Seen
        {
            "TP": 0,
            "total_pos": 0,
            "total_pre": 0,
            "F1": 0,
        },  # Unseen
        [0.0],  # Total F1
    ),
    (
        "crossner.crossner_music",
        "entities",
        {
            "seen": {"Event", "Country", "Location", "Organization", "Person", "Miscellaneous", "Other"},
            "unseen": {"MusicGenre", "Song", "Band", "Album", "MusicalArtist", "MusicalInstrument", "Award"},
        },
        {
            "TP": 0,
            "total_pos": 0,
            "total_pre": 0,
            "F1": 0,
        },  # Seen
        {
            "TP": 0,
            "total_pos": 0,
            "total_pre": 0,
            "F1": 0,
        },  # Unseen
        [0.0],  # Total F1
    ),
    (
        "crossner.crossner_politics",
        "entities",
        {
            "seen": {"Person", "Organization", "Location", "Election", "Event", "Country", "Miscellaneous", "Other"},
            "unseen": {"Politician", "PoliticalParty"},
        },
        {
            "TP": 0,
            "total_pos": 0,
            "total_pre": 0,
            "F1": 0,
        },  # Seen
        {
            "TP": 0,
            "total_pos": 0,
            "total_pre": 0,
            "F1": 0,
        },  # Unseen
        [0.0],  # Total F1
    ),
    (
        "crossner.crossner_natural_science",
        "entities",
        {
            "seen": {
                "Person",
                "Organization",
                "Country",
                "Location",
                "ChemicalElement",
                "ChemicalCompound",
                "Event",
                "Miscellaneous",
                "Other",
            },
            "unseen": {
                "Scientist",
                "University",
                "Discipline",
                "Enzyme",
                "Protein",
                "AstronomicalObject",
                "AcademicJournal",
                "Theory",
                "Award",
            },
        },
        {
            "TP": 0,
            "total_pos": 0,
            "total_pre": 0,
            "F1": 0,
        },  # Seen
        {
            "TP": 0,
            "total_pos": 0,
            "total_pre": 0,
            "F1": 0,
        },  # Unseen
        [0.0],  # Total F1
    ),
    (
        "e3c.ner",
        "entities",
        {"seen": {"ClinicalEntity"}, "unseen": {}},
        {
            "TP": 0,
            "total_pos": 0,
            "total_pre": 0,
            "F1": 0,
        },  # Seen
        {
            "TP": 0,
            "total_pos": 0,
            "total_pre": 0,
            "F1": 0,
        },  # Unseen
        [0.0],  # Total F1
    ),
    (
        "fabner.ner",
        "entities",
        {
            "seen": {"Biomedical"},
            "unseen": {
                "Material",
                "ManufacturingProcess",
                "MachineEquipment",
                "Application",
                "EngineeringFeatures",
                "MechanicalProperties",
                "ProcessCharacterization",
                "ProcessParameters",
                "EnablingTechnology",
                "ConceptPrinciples",
                "ManufacturingStandards",
            },
        },
        {
            "TP": 0,
            "total_pos": 0,
            "total_pre": 0,
            "F1": 0,
        },  # Seen
        {
            "TP": 0,
            "total_pos": 0,
            "total_pre": 0,
            "F1": 0,
        },  # Unseen
        [0.0],  # Total F1
    ),
    (
        "harveyner.ner",
        "entities",
        {"seen": {}, "unseen": {"Point", "Area", "Road", "River"}},
        {
            "TP": 0,
            "total_pos": 0,
            "total_pre": 0,
            "F1": 0,
        },  # Seen
        {
            "TP": 0,
            "total_pos": 0,
            "total_pre": 0,
            "F1": 0,
        },  # Unseen
        [0.0],  # Total F1
    ),
    (
        "mitmovie.ner",
        "entities",
        {
            "seen": {"Year"},
            "unseen": {
                "Actor",
                "Character",
                "Director",
                "Genre",
                "Plot",
                "Rating",
                "RatingsAverage",
                "Review",
                "Song",
                "Tittle",
                "Trailer",
            },
        },
        {
            "TP": 0,
            "total_pos": 0,
            "total_pre": 0,
            "F1": 0,
        },  # Seen
        {
            "TP": 0,
            "total_pos": 0,
            "total_pre": 0,
            "F1": 0,
        },  # Unseen
        [0.0],  # Total F1
    ),
    (
        "mitrestaurant.ner",
        "entities",
        {"seen": {"Location", "Price", "Hours"}, "unseen": {"Rating", "Amenity", "RestaurantName", "Dish", "Cuisine"}},
        {
            "TP": 0,
            "total_pos": 0,
            "total_pre": 0,
            "F1": 0,
        },  # Seen
        {
            "TP": 0,
            "total_pos": 0,
            "total_pre": 0,
            "F1": 0,
        },  # Unseen
        [0.0],  # Total F1
    ),
    (
        "multinerd.ner",
        "entities",
        {
            "seen": {"Person", "Location", "Organization", "Biological", "Disease", "Event", "Time", "Vehicle"},
            "unseen": {"Animal", "Celestial", "Food", "Instrument", "Media", "Plant", "Mythological"},
        },
        {
            "TP": 0,
            "total_pos": 0,
            "total_pre": 0,
            "F1": 0,
        },  # Seen
        {
            "TP": 0,
            "total_pos": 0,
            "total_pre": 0,
            "F1": 0,
        },  # Unseen
        [0.0],  # Total F1
    ),
    (
        "wikievents.ner",
        "entities",
        {
            "seen": {
                "CommercialProduct",
                "Facility",
                "GPE",
                "Location",
                "MedicalHealthIssue",
                "Money",
                "Organization",
                "Person",
                "JobTitle",
                "Numeric",
                "Vehicle",
                "Weapon",
            },
            "unseen": {"Abstract", "BodyPart", "Information", "SideOfConflict"},
        },
        {
            "TP": 0,
            "total_pos": 0,
            "total_pre": 0,
            "F1": 0,
        },  # Seen
        {
            "TP": 0,
            "total_pos": 0,
            "total_pre": 0,
            "F1": 0,
        },  # Unseen
        [0.0],  # Total F1
    ),
    (
        "wikievents.ee",
        "events",
        {
            "seen": {
                "ConflictEvent",
                "ContactEvent",
                "GenericCrimeEvent",
                "JusticeEvent",
                "MedicalEvent",
                "MovementTransportEvent",
                "PersonnelEvent",
                "TransactionEvent",
            },
            "unseen": {"ArtifactExistanceEvent", "CognitiveEvent", "ControlEvent", "DisasterEvent", "LifeEvent"},
        },
        {
            "TP": 0,
            "total_pos": 0,
            "total_pre": 0,
            "F1": 0,
        },  # Seen
        {
            "TP": 0,
            "total_pos": 0,
            "total_pre": 0,
            "F1": 0,
        },  # Unseen
        [0.0],  # Total F1
    ),
]

PATHS = {
    "Baseline": "/tartalo02/users/osainz006/models/collie/Baseline-7b_CodeLLaMA{seed}/task_scores.json",
    "GoLLIE": "/tartalo02/users/osainz006/models/collie/CoLLIE+-7b_CodeLLaMA{seed}/task_scores.json",
    # "w/o Candidates": "/tartalo02/users/osainz006/models/collie/CoLLIE-7b_CodeLLaMA{seed}/task_scores.json",
    # "w/o Masking": "/tartalo02/users/osainz006/models/collie/CoLLIE+-7b_CodeLLaMA{seed}_abl_masking/task_scores.json",
    # "w/o Dropout": "/tartalo02/users/osainz006/models/collie/CoLLIE+-7b_CodeLLaMA{seed}_abl_dropout/task_scores.json",
    "13B": "/tartalo02/users/osainz006/models/collie/CoLLIE+-13b_CodeLLaMA{seed}/task_scores.json",
    "34B": "/tartalo02/users/osainz006/models/collie/CoLLIE+-34b_CodeLLaMA{seed}/task_scores.json",
}

SEEDS = ["", "_2", "_3"]

unseen_entity_f1 = {}
seen_entity_f1 = {}

for dataset, task, entity_dict, seen_scores, unseen_scores, general_f1 in ZERO_DATASETS:
    for entity in entity_dict["seen"]:
        seen_entity_f1[f"{dataset}_{entity}"] = []
        for i in range(len(SEEDS)):
            seen_entity_f1[f"{dataset}_{entity}"].append({
                "TP": 0,
                "total_pos": 0,
                "total_pre": 0,
                "F1": 0,
            })
    for entity in entity_dict["unseen"]:
        unseen_entity_f1[f"{dataset}_{entity}"] = []
        for i in range(len(SEEDS)):
            unseen_entity_f1[f"{dataset}_{entity}"].append({
                "TP": 0,
                "total_pos": 0,
                "total_pre": 0,
                "F1": 0,
            })

for name, path in PATHS.items():
    print()
    print(name)

    iter_results = []

    for seed_no, seed in enumerate(SEEDS):
        print(seed)
        ZERO_DATASETS_iter = copy.deepcopy(ZERO_DATASETS)

        if name == "Baseline" and seed:
            seed += "/1"

        with open(path.format(seed=seed)) as f:
            results = json.load(f)

        for elems in ZERO_DATASETS_iter:
            try:
                dataset, task, entity_dict, seen_scores, unseen_scores, general_f1 = elems
            except ValueError as e:
                raise ValueError(f"{elems}\n{e}")
            for class_name, class_score in results[dataset][task]["class_scores"].items():
                if class_name in entity_dict["seen"]:
                    seen_scores["TP"] += class_score["tp"]
                    seen_scores["total_pos"] += class_score["total_pos"]
                    seen_scores["total_pre"] += class_score["total_pre"]
                    seen_entity_f1[f"{dataset}_{class_name}"][seed_no]["TP"] += class_score["tp"]
                    seen_entity_f1[f"{dataset}_{class_name}"][seed_no]["total_pos"] += class_score["total_pos"]
                    seen_entity_f1[f"{dataset}_{class_name}"][seed_no]["total_pre"] += class_score["total_pre"]
                elif class_name in entity_dict["unseen"]:
                    unseen_scores["TP"] += class_score["tp"]
                    unseen_scores["total_pos"] += class_score["total_pos"]
                    unseen_scores["total_pre"] += class_score["total_pre"]
                    unseen_entity_f1[f"{dataset}_{class_name}"][seed_no]["TP"] += class_score["tp"]
                    unseen_entity_f1[f"{dataset}_{class_name}"][seed_no]["total_pos"] += class_score["total_pos"]
                    unseen_entity_f1[f"{dataset}_{class_name}"][seed_no]["total_pre"] += class_score["total_pre"]
                else:
                    raise ValueError(f"Class {class_name} not found in {dataset}.")

            general_f1[0] = results[dataset][task]["f1-score"] * 100  # Total F1

        for _, _, _, seen_scores, unseen_scores, _ in ZERO_DATASETS_iter:
            precision = seen_scores["TP"] / seen_scores["total_pre"] if seen_scores["total_pre"] > 0 else 0.0
            recall = seen_scores["TP"] / seen_scores["total_pos"] if seen_scores["total_pos"] > 0 else 0.0
            seen_scores["F1"] = (
                2 * precision * recall / (precision + recall) if (precision + recall) > 0.0 else 0.0
            ) * 100

            precision = unseen_scores["TP"] / unseen_scores["total_pre"] if unseen_scores["total_pre"] > 0 else 0.0
            recall = unseen_scores["TP"] / unseen_scores["total_pos"] if unseen_scores["total_pos"] > 0 else 0.0
            unseen_scores["F1"] = (
                2 * precision * recall / (precision + recall) if (precision + recall) > 0.0 else 0.0
            ) * 100

        iter_results.append(ZERO_DATASETS_iter)
        # print(ZERO_DATASETS_iter)

    result_table = []

    dataset_names = []
    for dataset, task, entity_dict, seen_scores, unseen_scores, _ in iter_results[0]:
        dataset_names.append(dataset)

    # print(dataset_names)

    avg_seen = [[] for x in range(len(iter_results))]
    avg_unseen = [[] for x in range(len(iter_results))]
    avg_general = [[] for x in range(len(iter_results))]

    for dataser_no, dataset_name in enumerate(dataset_names):
        seen_f1s = []
        unseen_f1s = []
        general_f1s = []
        for it in range(len(iter_results)):
            dataset, task, entity_dict, seen_scores, unseen_scores, f1 = iter_results[it][dataser_no]
            seen_f1s.append(seen_scores["F1"])
            unseen_f1s.append(unseen_scores["F1"])
            general_f1s.append(f1[0])
            avg_general[it].append(f1[0])
            avg_seen[it].append(seen_scores["F1"])
            avg_unseen[it].append(unseen_scores["F1"])
            avg_general[it].append(f1[0])

        # print(general_f1s)
        result_table.append([
            dataset_name,
            np.array(seen_f1s).mean(0),
            np.array(seen_f1s).std(0),
            np.array(unseen_f1s).mean(0),
            np.array(unseen_f1s).std(0),
            np.array(general_f1s).mean(0),
            np.array(general_f1s).std(0),
        ])

    # Append averages
    avg_seen = np.array(avg_seen).mean(1)
    avg_unseen = np.array(avg_unseen).mean(1)
    avg_general = np.array(avg_general).mean(1)
    # print(avg_general)
    result_table.append([
        "Average",
        np.array(avg_seen).mean(0),
        np.array(avg_seen).std(0),
        np.array(avg_unseen).mean(0),
        np.array(avg_unseen).std(0),
        np.array(avg_general).mean(0),
        np.array(avg_general).std(0),
    ])

    columns = ["Dataset", "Seen F1", "Seen F1 Std", "Unseen F1", "Unseen F1 Std", "Total F1", "Total F1 Std"]

    print(tabulate(result_table, headers=columns, floatfmt=".1f"))

    # Build bar plot
    for entity_name, scores in unseen_entity_f1.items():
        for i in range(len(scores)):
            precision = scores[i]["TP"] / scores[i]["total_pre"] if scores[i]["total_pre"] > 0 else 0.0
            recall = scores[i]["TP"] / scores[i]["total_pos"] if scores[i]["total_pos"] > 0 else 0.0
            scores[i]["F1"] = (
                2 * precision * recall / (precision + recall) if (precision + recall) > 0.0 else 0.0
            ) * 100

    for entity_name, scores in seen_entity_f1.items():
        for i in range(len(scores)):
            precision = scores[i]["TP"] / scores[i]["total_pre"] if scores[i]["total_pre"] > 0 else 0.0
            recall = scores[i]["TP"] / scores[i]["total_pos"] if scores[i]["total_pos"] > 0 else 0.0
            scores[i]["F1"] = (
                2 * precision * recall / (precision + recall) if (precision + recall) > 0.0 else 0.0
            ) * 100

    seen_entity_f1_avg = {}
    unseen_entity_f1_avg = {}

    for entity_name, scores in unseen_entity_f1.items():
        unseen_entity_f1_avg[entity_name] = np.array([score["F1"] for score in scores]).mean(0)

    for entity_name, scores in seen_entity_f1.items():
        seen_entity_f1_avg[entity_name] = np.array([score["F1"] for score in scores]).mean(0)

    # Print seen_entity_f1_avg as table

    print("Seen")
    for entity_name, score in seen_entity_f1_avg.items():
        print(entity_name, score)

    # Print unseen_entity_f1_avg as table
    print("Unseen")
    for entity_name, score in unseen_entity_f1_avg.items():
        print(entity_name, score)

    print("Seen: ")
    for entity_name, score in seen_entity_f1_avg.items():
        print(score, end=", ")
    print()
    print("Unseen: ")
    for entity_name, score in unseen_entity_f1_avg.items():
        print(score, end=", ")
