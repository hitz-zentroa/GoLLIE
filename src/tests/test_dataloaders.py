import os
import unittest
import json


class TestDataLoaders(unittest.TestCase):
    @unittest.skipIf(
        not os.path.exists("data/ace05/english.sentence.json"), "No ACE data available"
    )
    def test_ACE(self):
        from src.tasks.ace.data_loader import ACEDatasetLoader, ACESampler

        with open("configs/ace_config.json") as f:
            config = json.load(f)

        dataloader = ACEDatasetLoader(
            "data/ace05/english.sentence.json", group_by="sentence"
        )

        ACESampler(dataloader, task="EE", **config, **config["task_configuration"]["EE"])

        # TODO: Implement a better TEST

    @unittest.skipIf(
        not os.path.exists("data/rams/dev.jsonlines"), "No RAMS data available"
    )
    def test_RAMS(self):
        from src.tasks.rams.data_loader import RAMSDatasetLoader, RAMSSampler

        with open("configs/rams_config.json") as f:
            config = json.load(f)

        dataloader = RAMSDatasetLoader("data/rams/dev.jsonlines")

        RAMSSampler(
            dataloader, task="EAE", **config, **config["task_configuration"]["EAE"]
        )

        # TODO: Implement a better TEST
