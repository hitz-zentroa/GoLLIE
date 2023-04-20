import unittest

import black


def to_str(x):
    return black.format_str(x.__repr__(), mode=black.Mode())


class TestEvaluate(unittest.TestCase):
    def test_annotation_list(self):
        from src.tasks.ace.prompts import GPE, Location, Organization, Person
        from src.tasks.utils_typing import AnnotationList

        text = "Peter went to Hitz-zentroa where Carlos works, after visiting Donosti, Tokyo."

        annotations = [
            Person("Peter"),
            Organization("Hitz-zentroa"),
            Person("carlos"),
            Location("Tokyo"),
            Location("Donosti"),
            GPE("UE"),
        ]

        annotations = AnnotationList.from_output(
            to_str(annotations),
            task_module="src.tasks.ace.prompts",
            text=text,
            filter_hallucinations=True,
        )

        self.assertListEqual(
            annotations,
            AnnotationList(
                [
                    Person("Peter"),
                    Organization("Hitz-zentroa"),
                    Person("carlos"),
                    Location("Tokyo"),
                    Location("Donosti"),
                ]
            ),
        )

    def test_entity_hallucination(self):
        from src.tasks.ace.prompts import (
            GPE,
            Location,
            Organization,
            Person,
        )
        from src.tasks.utils_typing import AnnotationList

        unlabelled_sentence = "Peter was born in Donosti. He married Carlos on May 18th."
        predictions = [
            Person("Peter"),
            Organization("Hitz-zentroa"),
            Person("carlos"),
            Location("Tokyo"),
            Location("Donosti"),
            GPE("UE"),
        ]

        predictions = AnnotationList.from_output(str(predictions), task_module="src.tasks.ace.prompts")
        filtered_predictions = predictions.filter_hallucinations(text=unlabelled_sentence)

        self.assertListEqual(
            filtered_predictions,
            AnnotationList(
                [
                    Person("Peter"),
                    Person("carlos"),
                    Location("Donosti"),
                ]
            ),
        )

    def test_type_hallucination(self):
        from src.tasks.ace.prompts import (
            Location,
            Person,
        )
        from src.tasks.utils_typing import AnnotationList

        unlabelled_sentence = "Peter was born in Donosti. He married Carlos on May 18th."
        predictions = (
            "["
            + "Person('Peter'), "
            + "Organization('Hitz-zentroa'), "
            + "Person('carlos'), "
            + "Location('Tokyo'), "
            + "Location('Donosti'), "
            + "ASDF('UE'), ] "
        )

        predictions = AnnotationList.from_output(predictions, task_module="src.tasks.ace.prompts")
        filtered_predictions = predictions.filter_hallucinations(text=unlabelled_sentence)

        self.assertListEqual(
            filtered_predictions,
            AnnotationList(
                [
                    Person("Peter"),
                    Person("carlos"),
                    Location("Donosti"),
                ]
            ),
        )

    def test_relation_hallucination(self):
        from src.tasks.ace.prompts import (
            Family,
            Geographical,
            Located,
        )
        from src.tasks.utils_typing import AnnotationList

        unlabelled_sentence = "Peter was born in Donosti. He married Carlos on May 18th."
        location = Located("Peter", "Donosti")
        family = Family("Peter", "carlos")
        geographical = Geographical("Donosti", "Spain")
        predictions = [
            location,
            family,
            geographical,
        ]

        predictions = AnnotationList.from_output(str(predictions), task_module="src.tasks.ace.prompts")
        filtered_predictions = predictions.filter_hallucinations(text=unlabelled_sentence)

        self.assertListEqual(
            filtered_predictions,
            AnnotationList(
                [
                    location,
                    family,
                ]
            ),
        )

    def test_event_hallucination(self):
        from src.tasks.ace.prompts import BeBorn, Marry
        from src.tasks.utils_typing import AnnotationList

        text = "Peter was born in Donosti. He married Carlos on May 18th."

        predictions = str(
            [
                BeBorn("born", person=[], time=[], place=[]),
                Marry(
                    "married",
                    person=[
                        "Peter",
                    ],
                    time=["May 18th"],
                    place=["Tokyo"],
                ),
            ]
        )
        predictions = AnnotationList.from_output(
            predictions, task_module="src.tasks.ace.prompts", text=text, filter_hallucinations=True
        )

        self.assertListEqual(
            predictions,
            AnnotationList(
                [
                    BeBorn("born", person=[], time=[], place=[]),
                    Marry(
                        "married",
                        person=[
                            "Peter",
                        ],
                        time=["May 18th"],
                        place=[],
                    ),
                ]
            ),
        )
