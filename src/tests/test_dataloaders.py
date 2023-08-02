import json
import os
import unittest


class TestDataLoaders(unittest.TestCase):
    @unittest.skipIf(not os.path.exists("data/ace05/english.sentence.json"), "No ACE data available")
    def test_ACE(self):
        from src.tasks.ace.data_loader import ACEDatasetLoader, ACESampler

        with open("configs/data_configs/ace_config.json") as f:
            config = json.load(f)
        if isinstance(config["seed"], list):
            config["seed"] = 0
            config["label_noise_prob"] = 0.0

        dataloader = ACEDatasetLoader("data/ace05/english.sentence.json", group_by="sentence")

        _ = list(ACESampler(dataloader, task="RE", **config, **config["task_configuration"]["RE"]))

        # TODO: Implement a better TEST

    @unittest.skipIf(not os.path.exists("data/casie/data.jsonl"), "No CASIE data available")
    def test_CASIE(self):
        from src.tasks.casie.data_loader import CASIEDatasetLoader, CASIESampler

        with open("configs/data_configs/casie_config.json") as f:
            config = json.load(f)

        dataloader = CASIEDatasetLoader("data/casie/data.dev.jsonl")

        _ = list(
            CASIESampler(
                dataloader, task="EAE", remove_guidelines=True, **config, **config["task_configuration"]["EE"]
            )
        )

    @unittest.skipIf(not os.path.exists("data/wikievents/train.sentence.jsonl"), "No WikiEvents data available")
    def test_WikiEvents(self):
        from src.tasks.wikievents.data_loader import WikiEventsDatasetLoader, WikiEventsSampler

        with open("configs/data_configs/wikievents_config.json") as f:
            config = json.load(f)
        if isinstance(config["seed"], list):
            config["seed"] = 0
            config["label_noise_prob"] = 0.0

        dataloader = WikiEventsDatasetLoader("data/wikievents/train.sentence.jsonl", group_by="sentence")

        _ = list(WikiEventsSampler(dataloader, task="EAE", **config, **config["task_configuration"]["EAE"]))

        # TODO: Implement a better TEST

    @unittest.skipIf(not os.path.exists("data/rams/dev.jsonlines"), "No RAMS data available")
    def test_RAMS(self):
        from src.tasks.rams.data_loader import RAMSDatasetLoader, RAMSSampler

        with open("configs/data_configs/rams_config.json") as f:
            config = json.load(f)
        if isinstance(config["seed"], list):
            config["seed"] = 0
            config["label_noise_prob"] = 0.0

        dataloader = RAMSDatasetLoader("data/rams/dev.jsonlines")

        _ = list(RAMSSampler(dataloader, task="EAE", **config, **config["task_configuration"]["EAE"]))

        # TODO: Implement a better TEST

    @unittest.skipIf(not os.path.exists("data/tacred/dev.json"), "No TACRED data available")
    def test_TACRED(self):
        from src.tasks.tacred.data_loader import TACREDDatasetLoader, TACREDSampler

        with open("configs/data_configs/tacred_config.json") as f:
            config = json.load(f)
        if isinstance(config["seed"], list):
            config["seed"] = 0
            config["label_noise_prob"] = 0.0

        dataloader = TACREDDatasetLoader("data/tacred/train.json")[:10]

        _ = list(TACREDSampler(dataloader, task="SF", **config, **config["task_configuration"]["SF"]))

    @unittest.skipIf(not os.path.exists("data/conll/en.conll.train.tsv"), "No CoNLL data available")
    def test_CoNLL03(self):
        from src.tasks.conll03.data_loader import CoNLL03Sampler, CoNLLDatasetLoader
        from src.tasks.conll03.prompts import Miscellaneous, Organization, Person

        with open("configs/data_configs/conll03_config.json") as f:
            config = json.load(f)
        if isinstance(config["seed"], list):
            config["seed"] = 0
            config["label_noise_prob"] = 0.0

        config["task_configuration"] = {
            "NER": {
                "parallel_instances": 1,
                "max_guidelines": -1,
                "guideline_dropout": 0,
                "scorer": "src.tasks.conll03.scorer.CoNLL03EntityScorer",
            }
        }

        config["include_misc"] = True
        dataloader = CoNLLDatasetLoader("validation", **config)

        _ = list(CoNLL03Sampler(dataloader, task="NER", **config, **config["task_configuration"]["NER"]))

        self.assertDictEqual(
            {
                "id": 0,
                "doc_id": 0,
                "text": "CRICKET - LEICESTERSHIRE TAKE OVER AT TOP AFTER INNINGS VICTORY .",
                "entities": [Organization(span="LEICESTERSHIRE")],
                "gold": [Organization(span="LEICESTERSHIRE")],
            },
            dataloader[0],
        )

        self.assertDictEqual(
            {
                "id": 2,
                "doc_id": 2,
                "text": (
                    "West Indian all-rounder Phil Simmons took four for 38 on Friday as Leicestershire beat Somerset"
                    " by an innings and 39 runs in two days to take over at the head of the county championship ."
                ),
                "entities": [
                    Miscellaneous(span="West Indian"),
                    Person(span="Phil Simmons"),
                    Organization(span="Leicestershire"),
                    Organization(span="Somerset"),
                ],
                "gold": [
                    Miscellaneous(span="West Indian"),
                    Person(span="Phil Simmons"),
                    Organization(span="Leicestershire"),
                    Organization(span="Somerset"),
                ],
            },
            dataloader[2],
        )

        config["include_misc"] = False
        dataloader = CoNLLDatasetLoader("validation", **config)

        _ = list(CoNLL03Sampler(dataloader, task="NER", **config, **config["task_configuration"]["NER"]))

        self.assertDictEqual(
            {
                "id": 0,
                "doc_id": 0,
                "text": "CRICKET - LEICESTERSHIRE TAKE OVER AT TOP AFTER INNINGS VICTORY .",
                "entities": [Organization(span="LEICESTERSHIRE")],
                "gold": [Organization(span="LEICESTERSHIRE")],
            },
            dataloader[0],
        )

        self.assertDictEqual(
            {
                "id": 2,
                "doc_id": 2,
                "text": (
                    "West Indian all-rounder Phil Simmons took four for 38 on Friday as Leicestershire beat Somerset"
                    " by an innings and 39 runs in two days to take over at the head of the county championship ."
                ),
                "entities": [
                    Person(span="Phil Simmons"),
                    Organization(span="Leicestershire"),
                    Organization(span="Somerset"),
                ],
                "gold": [
                    Person(span="Phil Simmons"),
                    Organization(span="Leicestershire"),
                    Organization(span="Somerset"),
                ],
            },
            dataloader[2],
        )
