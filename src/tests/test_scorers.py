import unittest


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

        scorer_result = scorer(reference=reference, predictions=predictions)["entities"]
        scorer_result.pop("class_scores")

        self.assertDictEqual(
            scorer_result,
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

        scorer_results = scorer(reference=reference, predictions=predictions)["events"]
        if "class_scores" in scorer_results:
            scorer_results.pop("class_scores")

        self.assertDictEqual(
            scorer_results,
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

        scorer_results = scorer(reference=reference, predictions=predictions)["arguments"]
        if "class_scores" in scorer_results:
            scorer_results.pop("class_scores")

        self.assertDictEqual(
            scorer_results,
            {"precision": 0.6666666666666666, "recall": 0.4, "f1-score": 0.5},
        )


class TestRAMSScorers(unittest.TestCase):
    def test_event_scorer(self):
        from src.tasks.rams.prompts import TransferOwnership, Yield
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
        scorer_results = scorer(reference=reference, predictions=reference)["arguments"]
        if "class_scores" in scorer_results:
            scorer_results.pop("class_scores")

        self.assertDictEqual(
            scorer_results,
            {"precision": 1.0, "recall": 1.0, "f1-score": 1.0},
        )

        # No alignment
        scorer_results = scorer(reference=reference, predictions=[])["arguments"]
        if "class_scores" in scorer_results:
            scorer_results.pop("class_scores")

        self.assertDictEqual(
            scorer_results,
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

        scorer_results = scorer(reference=reference, predictions=predictions)["arguments"]
        if "class_scores" in scorer_results:
            scorer_results.pop("class_scores")

        self.assertDictEqual(
            scorer_results,
            {
                "precision": 0.6666666666666666,
                "recall": 0.6666666666666666,
                "f1-score": 0.6666666666666666,
            },
        )


class TestTACREDScorers(unittest.TestCase):
    def test_template_scorer(self):
        from src.tasks.tacred.prompts import PersonTemplate
        from src.tasks.tacred.scorer import TACREDTemplateScorer
        from src.tasks.utils_typing import Name, String, Value

        scorer = TACREDTemplateScorer()

        reference = [
            PersonTemplate(
                query="Peter",
                city_of_birth=Name("Lasarte"),
                age=[Value("26")],
                title=[String("Researcher"), String("Student")],
            )
        ]

        # Assert the typing constrains are satisfied
        for template in reference:
            template.assert_typing_constraints()

        # Perfect alingment
        scorer_results = scorer(reference=reference, predictions=reference)["slots"]
        if "class_scores" in scorer_results:
            scorer_results.pop("class_scores")

        self.assertDictEqual(
            scorer_results,
            {"precision": 1.0, "recall": 1.0, "f1-score": 1.0},
        )

        # No alignment
        scorer_results = scorer(reference=reference, predictions=[])["slots"]
        if "class_scores" in scorer_results:
            scorer_results.pop("class_scores")

        self.assertDictEqual(
            scorer_results,
            {"precision": 0.0, "recall": 0.0, "f1-score": 0.0},
        )

        predictions = [
            PersonTemplate(query="Peter", city_of_birth=Name("Lasarte"), age=Value("26"), origin=Name("Spain"))
        ]

        # Partially aligned
        # TP = 2 (city_of_birth=Name("Lasarte"), age=Value("26"))
        # FP = 1 (origin=Name("Spain"))
        # FN = 2 (title=[String("Researcher"), String("Student"))

        # precision -> 2 / 3 = 0.6666666666666666
        # recall -> 2 / 4 = 0.5
        # F1 -> 2 * (0.6666666666666666 * 0.5) / (0.6666666666666666 + 0.5) = 0.5714285714285715

        # No alignment
        scorer_results = scorer(reference=reference, predictions=predictions)["slots"]
        if "class_scores" in scorer_results:
            scorer_results.pop("class_scores")

        self.assertDictEqual(
            scorer_results,
            {
                "precision": 0.6666666666666666,
                "recall": 0.5,
                "f1-score": 0.5714285714285715,
            },
        )


class TestCASIEScorers(unittest.TestCase):
    def test_event_scorer(self):
        from src.tasks.casie.prompts_ed import VulnerabilityDiscover
        from src.tasks.casie.scorer import CASIEEventScorer

        scorer = CASIEEventScorer(allow_partial_match=True)

        reference = [VulnerabilityDiscover(mention="vulnerability found"), VulnerabilityDiscover(mention="reported")]

        # Perfect alingment
        scorer_results = scorer(reference=reference, predictions=reference)["events"]
        if "class_scores" in scorer_results:
            scorer_results.pop("class_scores")

        self.assertDictEqual(
            scorer_results,
            {"precision": 1.0, "recall": 1.0, "f1-score": 1.0},
        )

        # No alignment

        scorer_results = scorer(reference=reference, predictions=[])["events"]
        if "class_scores" in scorer_results:
            scorer_results.pop("class_scores")
        self.assertDictEqual(
            scorer_results,
            {"precision": 0.0, "recall": 0.0, "f1-score": 0.0},
        )

        predictions = [VulnerabilityDiscover(mention="vulnerability"), VulnerabilityDiscover(mention="discovered")]

        scorer_results = scorer(reference=reference, predictions=predictions)["events"]
        if "class_scores" in scorer_results:
            scorer_results.pop("class_scores")

        self.assertDictEqual(
            scorer_results,
            {
                "precision": 1.0,
                "recall": 1.0,
                "f1-score": 1.0,
            },
        )

    def test_event_argument_scorer(self):
        from src.tasks.casie.prompts_eae import VulnerabilityDiscover
        from src.tasks.casie.scorer import CASIEEventArgumentScorer

        scorer = CASIEEventArgumentScorer(allow_partial_match=True)

        reference = [
            VulnerabilityDiscover(
                mention="says",
                cve=["CVE-2018-12799", "CVE-2018-12808"],
                used_for=["lead to arbitrary code execution"],
                discoverer=["The tech giant"],
                supported_platform=[],
                vulnerability=[
                    "an out of bounds write issue",
                    "the security flaws",
                    "an untrusted pointer dereference problem",
                ],
                vulnerable_system=[],
                system_owner=[],
                system_version=[],
                time=[],
            ),
        ]

        # Perfect alingment
        scorer_results = scorer(reference=reference, predictions=reference)["arguments"]
        if "class_scores" in scorer_results:
            scorer_results.pop("class_scores")

        self.assertDictEqual(
            scorer_results,
            {"precision": 1.0, "recall": 1.0, "f1-score": 1.0},
        )

        # No alignment
        scorer_results = scorer(reference=reference, predictions=[])["arguments"]
        if "class_scores" in scorer_results:
            scorer_results.pop("class_scores")

        self.assertDictEqual(
            scorer_results,
            {"precision": 0.0, "recall": 0.0, "f1-score": 0.0},
        )

        predictions = [
            VulnerabilityDiscover(
                mention="says",
                cve="CVE-2018-12799",
                used_for=["arbitrary code execution"],
                discoverer=["tech giant"],
                supported_platform=[],
                vulnerability=[
                    "an out of bounds write issue",
                    "the security flaws",
                    "an untrusted pointer",
                ],
                vulnerable_system=[],
                system_owner=[],
                system_version=[],
                time=[],
            ),
        ]
        for pred in predictions:
            pred.assert_typing_constraints()

        import rich

        rich.print(predictions)
        rich.print(reference)

        # Partially aligned
        # TP = 6
        #   - cve(""CVE-2018-12799"")
        #   - used_for("lead to arbitrary code execution")
        #   - discoverer("The tech giant")
        #   - vulnerability("an out of bounds write issue")
        #   - vulnerability("the security flaws")
        #   - vulnerability("an untrusted pointer dereference problem")
        # FP = 0
        # FN = 0

        # precision -> 6 / 6 = 1.0
        # recall -> 6 / 7 = 0.8571428571428571
        # F1 -> 2 * (0.8571428571428571 * 1.0) / (0.8571428571428571 + 1.0) = 0.9285714285714286
        scorer_results = scorer(reference=reference, predictions=predictions)["arguments"]
        if "class_scores" in scorer_results:
            scorer_results.pop("class_scores")
        self.assertDictEqual(
            scorer_results,
            {
                "precision": 1.0,
                "recall": 0.8571428571428571,
                "f1-score": 0.923076923076923,
            },
        )
