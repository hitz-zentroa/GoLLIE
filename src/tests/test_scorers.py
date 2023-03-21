import unittest


class TestEntityScorers(unittest.TestCase):
    def test_ACE(self):
        from src.tasks.ace.scorer import ACEEntityScorer
        from src.tasks.ace.prompts import Person, Organization, GPE, Location

        reference = [
            Person("Peter"),
            Organization("OpenAI"),
            Person("Carlos"),
            Person("Peter"),
            Location("Tokyo"),
        ]
        predictions = [
            Person("Peter"),
            Organization("Google"),
            Person("Carlos"),
            GPE("Tokyo"),
        ]

        scorer = ACEEntityScorer()

        # TP = 2 (Person("Peter"), Person("Carlos"))
        # FP = 2 (Organization("Google"), GPE("Tokyo"))
        # FN = 3 (Organization("OpenAI"), Person("Peter"), Location("Tokyo"))
        # precision -> 2 / 4 = 0.5
        # recall -> 2 / 5 = 0.4
        # F1 -> 2 * 0.5 * 0.4 / (0.5 + 0.4) = 0.5
        self.assertDictEqual(
            scorer(reference=reference, predictions=predictions),
            {"precision": 0.5, "recall": 0.4, "f1-score": 0.4444444444444445},
        )
