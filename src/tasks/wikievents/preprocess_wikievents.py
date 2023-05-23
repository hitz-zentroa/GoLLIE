from __future__ import annotations

import json
import os
from argparse import ArgumentParser
from collections import defaultdict
from copy import deepcopy
from typing import Iterable, Tuple

from tqdm.auto import tqdm


class WikiEventsPreprocessor:
    def __init__(self) -> WikiEventsPreprocessor:
        self._nlp = None

    def _sent_tokenize(self: WikiEventsPreprocessor, text: str, start_pos: int) -> Iterable[Tuple[int, str]]:
        if not self._nlp:
            import spacy

            self._nlp = spacy.load("en_core_web_sm")

        for sent in self._nlp(text).sents:
            yield [sent[0].idx + start_pos, sent.text]

    @staticmethod
    def _find_subsentence(offset, sentences):
        sentences_ = sentences.copy() + [(sentences[-1][0] + len(sentences[-1][1]) + 1, "")]
        return next((i - 1 for i, (idx, _) in enumerate(sentences_) if offset < idx), -1)

    def __call__(self, input_path: str) -> Iterable[dict]:
        """A function that loads and converts the WikiEvents dataset into sentence level."""
        with open(input_path, "rt") as data_f:
            for data_line in tqdm(data_f):
                instance = json.loads(data_line)

                entities = {entity["id"]: entity for entity in instance["entity_mentions"]}
                tokens = [token for sentence in instance["sentences"] for token in sentence[0]]

                sub_sentence_information = defaultdict(dict)
                all_sub_sentences = [
                    list(self._sent_tokenize(text, tokens[0][1])) for tokens, text in instance["sentences"]
                ]

                for i, sentences in enumerate(all_sub_sentences):
                    for j, sent in enumerate(sentences):
                        sub_sentence_information[f"{i}-{j}"]["text"] = sent[-1]

                for value in entities.values():
                    sent_idx = value["sent_idx"]
                    sub_sent_idx = self._find_subsentence(tokens[value["start"]][1], all_sub_sentences[sent_idx])

                    sentence = sub_sentence_information[f"{sent_idx}-{sub_sent_idx}"]["text"]

                    new_value = deepcopy(value)
                    new_value["start"] = tokens[value["start"]][1] - all_sub_sentences[sent_idx][sub_sent_idx][0]
                    # Fix start if needed
                    _shift = sentence[new_value["start"] :].find(new_value["text"])
                    if _shift == -1:
                        continue
                    elif _shift > 0:
                        new_value["start"] += _shift

                    # new_value["end"] = tokens[value["end"] - 1][-1] - all_sub_sentences[sent_idx][sub_sent_idx][0]
                    new_value["end"] = new_value["start"] + len(new_value["text"])

                    assert (
                        sentence[new_value["start"] : new_value["end"]] == new_value["text"]
                    ), f"{sentence[new_value['start']:new_value['end']]}|{new_value['text']}"

                    if "entity_mentions" not in sub_sentence_information[f"{sent_idx}-{sub_sent_idx}"]:
                        sub_sentence_information[f"{sent_idx}-{sub_sent_idx}"]["entity_mentions"] = []

                    sub_sentence_information[f"{sent_idx}-{sub_sent_idx}"]["entity_mentions"].append(new_value)

                for event in instance["event_mentions"]:
                    sent_idx = event["trigger"]["sent_idx"]
                    sub_sent_idx = self._find_subsentence(
                        tokens[event["trigger"]["start"]][1], all_sub_sentences[sent_idx]
                    )

                    sentence = sub_sentence_information[f"{sent_idx}-{sub_sent_idx}"]["text"]

                    new_value = deepcopy(event)
                    new_value["trigger"]["start"] = (
                        tokens[event["trigger"]["start"]][1] - all_sub_sentences[sent_idx][sub_sent_idx][0]
                    )
                    # Fix start if needed
                    _shift = sentence[new_value["trigger"]["start"] :].find(new_value["trigger"]["text"])
                    if _shift == -1:
                        continue
                    elif _shift > 0:
                        new_value["trigger"]["start"] += _shift
                    # new_value["trigger"]["end"] = (
                    #     tokens[event["trigger"]["end"] - 1][-1] - all_sub_sentences[sent_idx][sub_sent_idx][0]
                    # )
                    new_value["trigger"]["end"] = new_value["trigger"]["start"] + len(new_value["trigger"]["text"])

                    sent_entities = (
                        {
                            ent["id"]
                            for ent in sub_sentence_information[f"{sent_idx}-{sub_sent_idx}"]["entity_mentions"]
                        }
                        if "entity_mentions" in sub_sentence_information[f"{sent_idx}-{sub_sent_idx}"]
                        else {}
                    )

                    for argument in new_value["arguments"]:
                        if argument["entity_id"] not in sent_entities:
                            argument["role"] = f"[OOR]_{argument['role']}"

                    assert (
                        sentence[new_value["trigger"]["start"] : new_value["trigger"]["end"]]
                        == new_value["trigger"]["text"]
                    ), f"{sentence[new_value['trigger']['start']:new_value['trigger']['end']]}|{new_value['trigger']['text']}"

                    if "event_mentions" not in sub_sentence_information[f"{sent_idx}-{sub_sent_idx}"]:
                        sub_sentence_information[f"{sent_idx}-{sub_sent_idx}"]["event_mentions"] = []

                    sub_sentence_information[f"{sent_idx}-{sub_sent_idx}"]["event_mentions"].append(new_value)

                for i, sentences in enumerate(all_sub_sentences):
                    for j, _ in enumerate(sentences):
                        info = sub_sentence_information[f"{i}-{j}"]
                        info["doc_id"] = f"{instance['doc_id']}_{i}_{j}"

                        if "entity_mentions" not in info and "event_mentions" not in info and len(info["text"]) <= 25:
                            continue

                        if "entity_mentions" not in info:
                            info["entity_mentions"] = []
                        if "event_mentions" not in info:
                            info["event_mentions"] = []

                        yield info


def main(args):
    processor = WikiEventsPreprocessor()

    for filename in os.listdir(args.dir_path):
        full_name = os.path.join(args.dir_path, filename)
        if os.path.isfile(full_name) and "sentence" not in filename:
            output_file = os.path.join(args.dir_path, filename.replace(".jsonl", ".sentence.jsonl"))
            with open(output_file, "w", encoding="utf-8") as f:
                for inst in processor(full_name):
                    print(json.dumps(inst, ensure_ascii=False), file=f)


if __name__ == "__main__":
    parser = ArgumentParser("WikiEvents preprocessing")

    parser.add_argument("-d", "--dir_path", type=str, default="data/wikievents/")

    args = parser.parse_args()
    main(args)
