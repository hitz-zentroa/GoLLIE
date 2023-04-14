import unittest


class TestEvaluate(unittest.TestCase):
    def test_entity_hallucination(self):
        from src.evaluate import remove_hallucinations
        from src.tasks.ace.prompts import (
            Person,
            Organization,
            GPE,
            Location,
        )

        unlabelled_sentence = "Peter was born in Donosti. He married Carlos on May 18th."
        predictions = [
            Person("Peter"),
            Organization("Hitz-zentroa"),
            Person("carlos"),
            Location("Tokyo"),
            Location("Donosti"),
            GPE("UE"),
        ]

        filtered_predictions = remove_hallucinations(
            unlabelled_sentence=unlabelled_sentence, predictions=predictions
        )

        self.assertListEqual(
            filtered_predictions,
            [
                Person("Peter"),
                Person("carlos"),
                Location("Donosti"),
            ],
        )

    def test_relation_hallucination(self):
        from src.evaluate import remove_hallucinations
        from src.tasks.ace.prompts import (
            Located,
            Geographical,
            Family,
        )

        unlabelled_sentence = "Peter was born in Donosti. He married Carlos on May 18th."
        location = Located("Peter", "Donosti")
        family = Family("Peter", "carlos")
        geographical = Geographical("Donosti", "Spain")
        predictions = [
            location,
            family,
            geographical,
        ]

        filtered_predictions = remove_hallucinations(
            unlabelled_sentence=unlabelled_sentence, predictions=predictions
        )

        self.assertListEqual(
            filtered_predictions,
            [
                location,
                family,
            ],
        )

    def test_event_hallucination(self):
        self.assertTrue(True)
        # TODO: Implement this test
