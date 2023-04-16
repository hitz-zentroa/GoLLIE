import unittest

from src.tasks.rams.prompts import TransferOwnership, Yield


class TestACEScorers(unittest.TestCase):
    def test_entity_scorer(self):
        from src.tasks.ace.prompts import (
            GPE,
            Location,
            Organization,
            Person,
        )
        from src.tasks.ace.scorer import ACEEntityScorer

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
            scorer(reference=reference, predictions=predictions)["entities"],
            {"precision": 0.5, "recall": 0.4, "f1-score": 0.4444444444444445},
        )

    def test_event_scorer(self):
        from src.tasks.ace.prompts import (
            BeBorn,
            Marry,
        )
        from src.tasks.ace.scorer import ACEEventScorer

        reference = [
            BeBorn("born", person=["Peter"], time=[], place=["Donosti"]),
            Marry("married", person=["Peter", "Carlos"], time=["May 18th"], place=[]),
        ]
        predictions = [
            BeBorn("birth", person=[], time=[], place=[]),
            Marry(
                "married",
                person=[
                    "Peter",
                ],
                time=["May 18th"],
                place=["Tokyo"],
            ),
        ]

        scorer = ACEEventScorer()

        # Events
        # TP = 1 (Marry("married"))
        # FP = 1 (BeBorn("birth"))
        # FN = 1 (BeBorn("born"))
        # precision -> 1 / 2 = 0.5
        # recall -> 1 / 2 = 0.5
        # F1 -> 2* 0.5 * 0.5 / (0.5 + 0.5) = 0.5
        self.assertDictEqual(
            scorer(reference=reference, predictions=predictions)["events"],
            {"precision": 0.5, "recall": 0.5, "f1-score": 0.5},
        )
        # Arguments
        # TP = 2 (Marry("married", person=["Peter"], time=["May 18th"]))
        # FP = 1 (Marry("married", time=["Tokyo"]))
        # FN = 3 (BeBorn("born", person=["Peter"], place=["Donosti"]),
        #         Marry("married", person=["Carlos"]))
        # precision -> 2 / 3 = 0.6666666666666666
        # recall -> 2 / 5 = 0.4
        # F1 -> 2 * (0.6666666666666666 * 0.4) / (0.6666666666666666 + 0.4) = 0.5
        self.assertDictEqual(
            scorer(reference=reference, predictions=predictions)["arguments"],
            {"precision": 0.6666666666666666, "recall": 0.4, "f1-score": 0.5},
        )


class TestRAMSScorers(unittest.TestCase):
    def test_event_scorer(self):
        from src.tasks.rams.scorer import RAMSEventScorer

        scorer = RAMSEventScorer()

        reference = [
            TransferOwnership(
                mention="bought",
                subtype=None,
                giver=["commodities trader"],
                recipient=[],
                beneficiary=[],
                artifact=["appointment"],
                preventer=[],
                place=[],
            ),
            Yield(
                mention="surrendered",
                subtype=None,
                agent=["Japan"],
                recipient=[],
                place=[],
                origin=[],
                destination=[],
            ),
        ]

        # Perfect alingment
        self.assertDictEqual(
            scorer(reference=reference, predictions=reference)["arguments"],
            {"precision": 1.0, "recall": 1.0, "f1-score": 1.0},
        )

        # No alignment
        self.assertDictEqual(
            scorer(reference=reference, predictions=[])["arguments"],
            {"precision": 0.0, "recall": 0.0, "f1-score": 0.0},
        )

        predictions = [
            TransferOwnership(
                mention="bought",
                subtype=None,
                giver=[],
                recipient=["commodities trader"],
                beneficiary=[],
                artifact=["appointment"],
                preventer=[],
                place=[],
            ),
            Yield(
                mention="surrendered",
                subtype=None,
                agent=["Japan"],
                recipient=[],
                place=[],
                origin=[],
                destination=[],
            ),
        ]

        # Partially aligned
        # TP = 2 (artifact("apointment"), agent("Japan"))
        # FP = 1 (recipient("commodities trader"))
        # FN = 1 (giver("commodities trader"))

        # precision -> 2 / 3 = 0.6666666666666666
        # recall -> 2 / 3 = 0.6666666666666666
        # F1 -> 2 * (0.6666666666666666 * 0.6666666666666666) / (0.6666666666666666 + 0.6666666666666666) = 0.6666666666666666

        # No alignment
        self.assertDictEqual(
            scorer(reference=reference, predictions=predictions)["arguments"],
            {
                "precision": 0.6666666666666666,
                "recall": 0.6666666666666666,
                "f1-score": 0.6666666666666666,
            },
        )
