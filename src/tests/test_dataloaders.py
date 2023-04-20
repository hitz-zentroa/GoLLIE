import json
import os
import unittest


class TestDataLoaders(unittest.TestCase):
    @unittest.skipIf(not os.path.exists("data/ace05/english.sentence.json"), "No ACE data available")
    def test_ACE(self):
        from src.tasks.ace.data_loader import ACEDatasetLoader, ACESampler

        with open("configs/data_configs/ace_config.json") as f:
            config = json.load(f)

        dataloader = ACEDatasetLoader("data/ace05/english.sentence.json", group_by="sentence")

        sampler=list(ACESampler(dataloader, task="EE", **config, **config["task_configuration"]["EE"]))

        # TODO: Implement a better TEST

    @unittest.skipIf(not os.path.exists("data/rams/dev.jsonlines"), "No RAMS data available")
    def test_RAMS(self):
        from src.tasks.rams.data_loader import RAMSDatasetLoader, RAMSSampler

        with open("configs/data_configs/rams_config.json") as f:
            config = json.load(f)

        dataloader = RAMSDatasetLoader("data/rams/dev.jsonlines")

        sampler = list(RAMSSampler(dataloader, task="EAE", **config, **config["task_configuration"]["EAE"]))

        # TODO: Implement a better TEST

    def test_CoNLL03(self):
        from src.tasks.conll03.data_loader import CoNLLDatasetLoader, CONLL03Sampler
        from src.tasks.conll03.prompts import Person,Organization,Location,Miscellaneous

        with open("configs/data_configs/conll03_config.json") as f:
            config = json.load(f)

        dataloader = CoNLLDatasetLoader("validation")

        sampler = list(CONLL03Sampler(dataloader, task="NER", **config, **config["task_configuration"]["NER"]))

        