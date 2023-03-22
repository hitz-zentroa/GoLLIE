import os
import unittest
from rich import print


class TestDataLoaders(unittest.TestCase):
    @unittest.skipIf(
        not os.path.exists("data/ace05/dev.event.json"), "No ACE data available"
    )
    def test_ACE(self):
        from src.tasks.ace.data_loader import ACEDatasetLoader

        dataloader = ACEDatasetLoader("data/ace05/dev.event.json", group_by="sentence")

        print(dataloader[12])
