import os
import unittest
import json
from rich import print


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

        print(dataloader[6])

        train_sampler = ACESampler(
            dataloader, task="EE", **config, **config["task_configuration"]["EE"]
        )

        for i, sample in enumerate(train_sampler):
            print(sample["text"])
            if i > 3:
                break

    @unittest.skipIf(
        not os.path.exists("data/rams/dev.jsonlines"), "No RAMS data available"
    )
    def test_RAMS(self):
        from src.tasks.rams.data_loader import RAMSDatasetLoader

        with open("configs/ace_config.json") as f:
            config = json.load(f)

        dataloader = RAMSDatasetLoader("data/rams/dev.jsonlines")

        print(dataloader[2])

        # train_sampler = ACESampler(
        #     dataloader, task="EE", **config, **config["task_configuration"]["EE"]
        # )

        # for i, sample in enumerate(train_sampler):
        #     print(sample["text"])
        #     if i > 3:
        #         break
