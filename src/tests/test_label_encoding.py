import unittest

from src.tasks.label_encoding import rewrite_labels


class TestToIOB(unittest.TestCase):
    def test_from_iob(self):
        text_in = (
            "word1 O\n"
            "word2 I-LOC\n"
            "word3 I-LOC\n"
            "word4 I-LOC\n"
            "wordnl  O\n"
            "word5 I-LOC\n"
            "word6 O\n"
            "word7 I-PER\n"
            "word8 B-PER\n"
            "word9 I-LOC\n"
            "word10 O\n"
            "word11 I-LOC\n"
            "word12 I-ORG\n"
            "word13 I-LOC\n"
            "word14 O\n"
            "word15 O\n"
            "word16 O\n"
            "word17 O\n"
            "word18 I-PER\n"
            "word19 O\n"
        )

        in_labels = [label for _, label in [line.split() for line in text_in.splitlines()]]
        gold_labels = [label for _, label in [line.split() for line in text_in.splitlines()]]

        rewritten_labels = rewrite_labels(labels=in_labels, encoding="iob")

        self.assertEqual(gold_labels, rewritten_labels)

    def test_from_corrupted_iob(self):
        text_in = (
            "word1 O\n"
            "word2 I-LOC\n"
            "word3 I-LOC\n"
            "word4 I-LOC\n"
            "wordnl  O\n"
            "word5 I-LOC\n"
            "word6 O\n"
            "word7 B-PER\n"
            "word8 B-PER\n"
            "word9 I-LOC\n"
            "word10 O\n"
            "word11 I-LOC\n"
            "word12 B-ORG\n"
            "word13 I-LOC\n"
            "word14 O\n"
            "word15 O\n"
            "word16 O\n"
            "word17 O\n"
            "word18 B-PER\n"
            "word19 O\n"
        )

        text_out = (
            "word1 O\n"
            "word2 I-LOC\n"
            "word3 I-LOC\n"
            "word4 I-LOC\n"
            "wordnl  O\n"
            "word5 I-LOC\n"
            "word6 O\n"
            "word7 I-PER\n"
            "word8 B-PER\n"
            "word9 I-LOC\n"
            "word10 O\n"
            "word11 I-LOC\n"
            "word12 I-ORG\n"
            "word13 I-LOC\n"
            "word14 O\n"
            "word15 O\n"
            "word16 O\n"
            "word17 O\n"
            "word18 I-PER\n"
            "word19 O\n"
        )

        in_labels = [label for _, label in [line.split() for line in text_in.splitlines()]]
        gold_labels = [label for _, label in [line.split() for line in text_out.splitlines()]]

        rewritten_labels = rewrite_labels(labels=in_labels, encoding="iob")

        self.assertEqual(gold_labels, rewritten_labels)

    def test_from_iob2(self):
        text_in = (
            "word1 O\n"
            "word2 B-LOC\n"
            "word3 I-LOC\n"
            "word4 I-LOC\n"
            "wordnl  O\n"
            "word5 B-LOC\n"
            "word6 O\n"
            "word7 B-PER\n"
            "word8 B-PER\n"
            "word9 B-LOC\n"
            "word10 O\n"
            "word11 B-LOC\n"
            "word12 B-ORG\n"
            "word13 B-LOC\n"
            "word14 O\n"
            "word15 O\n"
            "word16 O\n"
            "word17 O\n"
            "word18 B-PER\n"
            "word19 I-PER\n"
        )

        text_out = (
            "word1 O\n"
            "word2 I-LOC\n"
            "word3 I-LOC\n"
            "word4 I-LOC\n"
            "wordnl  O\n"
            "word5 I-LOC\n"
            "word6 O\n"
            "word7 I-PER\n"
            "word8 B-PER\n"
            "word9 I-LOC\n"
            "word10 O\n"
            "word11 I-LOC\n"
            "word12 I-ORG\n"
            "word13 I-LOC\n"
            "word14 O\n"
            "word15 O\n"
            "word16 O\n"
            "word17 O\n"
            "word18 I-PER\n"
            "word19 I-PER\n"
        )

        in_labels = [label for _, label in [line.split() for line in text_in.splitlines()]]
        gold_labels = [label for _, label in [line.split() for line in text_out.splitlines()]]

        rewritten_labels = rewrite_labels(labels=in_labels, encoding="iob")

        self.assertEqual(gold_labels, rewritten_labels)

    def test_from_bilou(self):
        text_in = (
            "word1 O\n"
            "word2 B-LOC\n"
            "word3 I-LOC\n"
            "word4 L-LOC\n"
            "word5 U-LOC\n"
            "word6 O\n"
            "word7 U-PER\n"
            "word8 U-PER\n"
            "word9 U-LOC\n"
            "word10 O\n"
            "word11 U-LOC\n"
            "word12 U-ORG\n"
            "word13 U-LOC\n"
            "word14 O\n"
            "word15 O\n"
            "word16 O\n"
            "word17 O\n"
            "word18 B-PER\n"
            "word19 L-PER\n"
        )

        text_out = (
            "word1 O\n"
            "word2 I-LOC\n"
            "word3 I-LOC\n"
            "word4 I-LOC\n"
            "word5 B-LOC\n"
            "word6 O\n"
            "word7 I-PER\n"
            "word8 B-PER\n"
            "word9 I-LOC\n"
            "word10 O\n"
            "word11 I-LOC\n"
            "word12 I-ORG\n"
            "word13 I-LOC\n"
            "word14 O\n"
            "word15 O\n"
            "word16 O\n"
            "word17 O\n"
            "word18 I-PER\n"
            "word19 I-PER\n"
        )

        in_labels = [label for _, label in [line.split() for line in text_in.splitlines()]]
        [label for _, label in [line.split() for line in text_out.splitlines()]]

        rewrite_labels(labels=in_labels, encoding="iob")


class TestToIOB2(unittest.TestCase):
    def test_from_iob(self):
        text_in = (
            "word1 O\n"
            "word2 I-LOC\n"
            "word3 I-LOC\n"
            "word4 I-LOC\n"
            "wordnl  O\n"
            "word5 I-LOC\n"
            "word6 O\n"
            "word7 I-PER\n"
            "word8 B-PER\n"
            "word9 I-LOC\n"
            "word10 O\n"
            "word11 I-LOC\n"
            "word12 I-ORG\n"
            "word13 I-LOC\n"
            "word14 O\n"
            "word15 O\n"
            "word16 O\n"
            "word17 O\n"
            "word18 I-PER\n"
            "word19 I-PER\n"
        )

        text_out = (
            "word1 O\n"
            "word2 B-LOC\n"
            "word3 I-LOC\n"
            "word4 I-LOC\n"
            "wordnl  O\n"
            "word5 B-LOC\n"
            "word6 O\n"
            "word7 B-PER\n"
            "word8 B-PER\n"
            "word9 B-LOC\n"
            "word10 O\n"
            "word11 B-LOC\n"
            "word12 B-ORG\n"
            "word13 B-LOC\n"
            "word14 O\n"
            "word15 O\n"
            "word16 O\n"
            "word17 O\n"
            "word18 B-PER\n"
            "word19 I-PER\n"
        )

        in_labels = [label for _, label in [line.split() for line in text_in.splitlines()]]
        gold_labels = [label for _, label in [line.split() for line in text_out.splitlines()]]

        rewritten_labels = rewrite_labels(labels=in_labels, encoding="iob2")

        self.assertEqual(gold_labels, rewritten_labels)

    def test_from_iob2(self):
        text_in = (
            "word1 O\n"
            "word2 B-LOC\n"
            "word3 I-LOC\n"
            "word4 I-LOC\n"
            "word5 B-LOC\n"
            "word6 O\n"
            "word7 B-PER\n"
            "word8 B-PER\n"
            "word9 B-LOC\n"
            "word10 O\n"
            "word11 B-LOC\n"
            "word12 B-ORG\n"
            "word13 B-LOC\n"
            "word14 O\n"
            "word15 O\n"
            "word16 O\n"
            "word17 O\n"
            "word18 B-PER\n"
            "word19 I-PER\n"
        )

        in_labels = [label for _, label in [line.split() for line in text_in.splitlines()]]
        gold_labels = [label for _, label in [line.split() for line in text_in.splitlines()]]

        rewritten_labels = rewrite_labels(labels=in_labels, encoding="iob2")

        self.assertEqual(gold_labels, rewritten_labels)

    def test_from_bilou(self):
        text_in = (
            "word1 O\n"
            "word2 B-LOC\n"
            "word3 I-LOC\n"
            "word4 L-LOC\n"
            "word5 U-LOC\n"
            "word6 O\n"
            "word7 U-PER\n"
            "word8 U-PER\n"
            "word9 U-LOC\n"
            "word10 O\n"
            "word11 U-LOC\n"
            "word12 U-ORG\n"
            "word13 U-LOC\n"
            "word14 O\n"
            "word15 O\n"
            "word16 O\n"
            "word17 O\n"
            "word18 B-PER\n"
            "word19 L-PER\n"
        )

        text_out = (
            "word1 O\n"
            "word2 B-LOC\n"
            "word3 I-LOC\n"
            "word4 I-LOC\n"
            "word5 B-LOC\n"
            "word6 O\n"
            "word7 B-PER\n"
            "word8 B-PER\n"
            "word9 B-LOC\n"
            "word10 O\n"
            "word11 B-LOC\n"
            "word12 B-ORG\n"
            "word13 B-LOC\n"
            "word14 O\n"
            "word15 O\n"
            "word16 O\n"
            "word17 O\n"
            "word18 B-PER\n"
            "word19 I-PER\n"
        )

        in_labels = [label for _, label in [line.split() for line in text_in.splitlines()]]
        gold_labels = [label for _, label in [line.split() for line in text_out.splitlines()]]

        rewritten_labels = rewrite_labels(labels=in_labels, encoding="iob2")

        self.assertEqual(gold_labels, rewritten_labels)

    def test_from_corrupted_iob2(self):
        text_in = (
            "word1 O\n"
            "word2 B-LOC\n"
            "word3 I-LOC\n"
            "word4 L-LOC\n"
            "word5 B-LOC\n"
            "word6 O\n"
            "word7 B-PER\n"
            "word8 U-PER\n"
            "word9 B-LOC\n"
            "word10 O\n"
            "word11 B-LOC\n"
            "word12 I-ORG\n"
            "word13 I-LOC\n"
            "word14 O\n"
            "word15 O\n"
            "word16 O\n"
            "word17 O\n"
            "word18 B-PER\n"
            "word19 L-PER\n"
        )

        text_out = (
            "word1 O\n"
            "word2 B-LOC\n"
            "word3 I-LOC\n"
            "word4 I-LOC\n"
            "word5 B-LOC\n"
            "word6 O\n"
            "word7 B-PER\n"
            "word8 B-PER\n"
            "word9 B-LOC\n"
            "word10 O\n"
            "word11 B-LOC\n"
            "word12 B-ORG\n"
            "word13 B-LOC\n"
            "word14 O\n"
            "word15 O\n"
            "word16 O\n"
            "word17 O\n"
            "word18 B-PER\n"
            "word19 I-PER\n"
        )

        in_labels = [label for _, label in [line.split() for line in text_in.splitlines()]]
        gold_labels = [label for _, label in [line.split() for line in text_out.splitlines()]]

        rewritten_labels = rewrite_labels(labels=in_labels, encoding="iob2")

        self.assertEqual(gold_labels, rewritten_labels)


class TestToBILOU(unittest.TestCase):
    def test_from_iob(self):
        text_in = (
            "word1 O\n"
            "word2 I-LOC\n"
            "word3 I-LOC\n"
            "word4 I-LOC\n"
            "wordnl  O\n"
            "word5 I-LOC\n"
            "word6 O\n"
            "word7 I-PER\n"
            "word8 B-PER\n"
            "word9 I-LOC\n"
            "word10 O\n"
            "word11 I-LOC\n"
            "word12 I-ORG\n"
            "word13 I-LOC\n"
            "word14 O\n"
            "word15 O\n"
            "word16 O\n"
            "word17 O\n"
            "word18 I-PER\n"
            "word19 I-PER\n"
        )

        text_out = (
            "word1 O\n"
            "word2 B-LOC\n"
            "word3 I-LOC\n"
            "word4 L-LOC\n"
            "wordnl  O\n"
            "word5 U-LOC\n"
            "word6 O\n"
            "word7 U-PER\n"
            "word8 U-PER\n"
            "word9 U-LOC\n"
            "word10 O\n"
            "word11 U-LOC\n"
            "word12 U-ORG\n"
            "word13 U-LOC\n"
            "word14 O\n"
            "word15 O\n"
            "word16 O\n"
            "word17 O\n"
            "word18 B-PER\n"
            "word19 L-PER\n"
        )

        in_labels = [label for _, label in [line.split() for line in text_in.splitlines()]]
        gold_labels = [label for _, label in [line.split() for line in text_out.splitlines()]]

        rewritten_labels = rewrite_labels(labels=in_labels, encoding="bilou")

        self.assertEqual(gold_labels, rewritten_labels)

    def test_from_iob2(self):
        text_in = (
            "word1 O\n"
            "word2 B-LOC\n"
            "word3 I-LOC\n"
            "word4 I-LOC\n"
            "word5 B-LOC\n"
            "word6 O\n"
            "word7 B-PER\n"
            "word8 B-PER\n"
            "word9 B-LOC\n"
            "word10 O\n"
            "word11 B-LOC\n"
            "word12 B-ORG\n"
            "word13 B-LOC\n"
            "word14 O\n"
            "word15 O\n"
            "word16 O\n"
            "word17 O\n"
            "word18 B-PER\n"
            "word19 I-PER\n"
            "word20 B-PER\n"
            "word21 O\n"
        )

        text_out = (
            "word1 O\n"
            "word2 B-LOC\n"
            "word3 I-LOC\n"
            "word4 L-LOC\n"
            "word5 U-LOC\n"
            "word6 O\n"
            "word7 U-PER\n"
            "word8 U-PER\n"
            "word9 U-LOC\n"
            "word10 O\n"
            "word11 U-LOC\n"
            "word12 U-ORG\n"
            "word13 U-LOC\n"
            "word14 O\n"
            "word15 O\n"
            "word16 O\n"
            "word17 O\n"
            "word18 B-PER\n"
            "word19 L-PER\n"
            "word20 U-PER\n"
            "word21 O\n"
        )

        in_labels = [label for _, label in [line.split() for line in text_in.splitlines()]]
        gold_labels = [label for _, label in [line.split() for line in text_out.splitlines()]]

        rewritten_labels = rewrite_labels(labels=in_labels, encoding="bilou")

        self.assertEqual(gold_labels, rewritten_labels)

    def test_from_bilou(self):
        text_in = (
            "word1 O\n"
            "word2 B-LOC\n"
            "word3 I-LOC\n"
            "word4 L-LOC\n"
            "word5 U-LOC\n"
            "word6 O\n"
            "word7 U-PER\n"
            "word8 U-PER\n"
            "word9 U-LOC\n"
            "word10 O\n"
            "word11 U-LOC\n"
            "word12 U-ORG\n"
            "word13 U-LOC\n"
            "word14 O\n"
            "word15 O\n"
            "word16 O\n"
            "word17 O\n"
            "word18 B-PER\n"
            "word19 L-PER\n"
        )

        in_labels = [label for _, label in [line.split() for line in text_in.splitlines()]]
        gold_labels = [label for _, label in [line.split() for line in text_in.splitlines()]]

        rewritten_labels = rewrite_labels(labels=in_labels, encoding="bilou")

        self.assertEqual(gold_labels, rewritten_labels)

    def test_from_corrupted_bilou(self):
        text_in = (
            "word1 O\n"
            "word2 B-LOC\n"
            "word3 L-LOC\n"
            "word4 L-LOC\n"
            "word5 U-LOC\n"
            "word6 O\n"
            "word7 U-PER\n"
            "word8 U-PER\n"
            "word9 U-LOC\n"
            "word10 O\n"
            "word11 U-LOC\n"
            "word12 B-ORG\n"
            "word13 U-LOC\n"
            "word14 O\n"
            "word15 O\n"
            "word16 O\n"
            "word17 B-PER\n"
            "word18 L-PER\n"
            "word19 L-PER\n"
            "word20 B-PER\n"
            "word21 L-LOC\n"
            "word22 L-PER\n"
            "word23 B-PER\n"
            "word24 I-PER\n"
            "word25 I-PER\n"
        )

        text_out = (
            "word1 O\n"
            "word2 B-LOC\n"
            "word3 I-LOC\n"
            "word4 L-LOC\n"
            "word5 U-LOC\n"
            "word6 O\n"
            "word7 U-PER\n"
            "word8 U-PER\n"
            "word9 U-LOC\n"
            "word10 O\n"
            "word11 U-LOC\n"
            "word12 U-ORG\n"
            "word13 U-LOC\n"
            "word14 O\n"
            "word15 O\n"
            "word16 O\n"
            "word17 B-PER\n"
            "word18 I-PER\n"
            "word19 L-PER\n"
            "word20 U-PER\n"
            "word21 U-LOC\n"
            "word22 U-PER\n"
            "word23 B-PER\n"
            "word24 I-PER\n"
            "word25 L-PER\n"
        )

        in_labels = [label for _, label in [line.split() for line in text_in.splitlines()]]
        gold_labels = [label for _, label in [line.split() for line in text_out.splitlines()]]

        rewritten_labels = rewrite_labels(labels=in_labels, encoding="bilou")

        self.assertEqual(gold_labels, rewritten_labels)
