from __future__ import annotations

import glob
import json
import os
from argparse import ArgumentParser
from collections import defaultdict, namedtuple
from typing import Dict, Iterable, List, Tuple


class CasieProcessor:
    trigger = namedtuple("Trigger", ["start", "end", "text"])
    argument = namedtuple("Argument", ["start", "end", "text", "role"])

    EVENT_MAPPING: Dict[str, str] = {
        "Vulnerability-related_DiscoverVulnerability": "Vulnerability:Discover",
        "Attack_Phishing": "Attack:Phising",
        "Vulnerability-related_PatchVulnerability": "Vulnerability:Patch",
        "Attack_Databreach": "Attack:Databreach",
        "Attack_Ransom": "Attack:Ransom",
    }

    def __init__(self) -> CasieProcessor:
        self._nlp = None

    def _sent_tokenize(self: CasieProcessor, text: str, start_pos: int) -> Iterable[Tuple[int, str]]:
        if not self._nlp:
            import spacy

            self._nlp = spacy.load("en_core_web_sm")

        for sent in self._nlp(text).sents:
            yield [sent[0].idx + start_pos, sent.text]

    @staticmethod
    def get_sent_id(span: Tuple[int, int], sentences: List[Tuple[int, str]]) -> int:
        for idx, sent in enumerate(sentences):
            if sent[0] <= span[0] and sent[0] + len(sent[1]) >= span[1]:
                return idx
        raise ValueError("No sentence found")

    def __call__(self, input_path: str) -> Iterable[dict]:
        annotations = defaultdict(list)
        with open(input_path, "r", encoding="utf-8") as f:
            try:
                data = json.load(f)
            except json.decoder.JSONDecodeError:
                return []
            doc_name = os.path.basename(input_path).replace(".json", "")
            text = data["content"]
            sentences = list(self._sent_tokenize(text, 0))

            events = [event for idx in data["cyberevent"]["hopper"] for event in idx["events"]]
            for event in events:
                _type = self.EVENT_MAPPING[event["type"] + "_" + event["subtype"]]
                try:
                    sentence_id = self.get_sent_id(
                        (event["nugget"]["startOffset"], event["nugget"]["endOffset"]), sentences
                    )
                except ValueError:
                    continue
                start_idx, sentence = sentences[sentence_id]

                # Normalize the trigger
                if (
                    event["nugget"]["text"]
                    != sentence[event["nugget"]["startOffset"] - start_idx : event["nugget"]["endOffset"] - start_idx]
                ):
                    event["nugget"]["startOffset"] = sentence.find(event["nugget"]["text"]) + start_idx
                    event["nugget"]["endOffset"] = event["nugget"]["startOffset"] + len(event["nugget"]["text"])
                trigger = self.trigger(
                    event["nugget"]["startOffset"] - start_idx,
                    event["nugget"]["endOffset"] - start_idx,
                    event["nugget"]["text"],
                )
                assert trigger.text == sentence[trigger.start : trigger.end]

                arguments = []
                if "argument" not in event:
                    event["argument"] = []
                for argument in event["argument"]:
                    try:
                        arg_sent_id = self.get_sent_id((argument["startOffset"], argument["endOffset"]), sentences)
                    except ValueError:
                        continue
                    if sentence_id != arg_sent_id:
                        print("skip")
                        continue

                    if (
                        argument["text"]
                        != sentence[argument["startOffset"] - start_idx : argument["endOffset"] - start_idx]
                    ):
                        argument["startOffset"] = sentence.find(argument["text"]) + start_idx
                        argument["endOffset"] = argument["startOffset"] + len(argument["text"])

                    argument = self.argument(
                        argument["startOffset"] - start_idx,
                        argument["endOffset"] - start_idx,
                        argument["text"],
                        argument["role"]["type"],
                    )

                    assert argument.text == sentence[argument.start : argument.end]
                    arguments.append(argument)

                annotations[sentence_id].append(
                    {"type": _type, "trigger": trigger._asdict(), "arguments": [arg._asdict() for arg in arguments]}
                )

        for sent_id, anns in annotations.items():
            yield {"sent_id": f"{doc_name}:{sent_id}", "text": sentences[sent_id][-1], "events": anns}


def main(args):
    processor = CasieProcessor()
    with open(os.path.join(args.path, "data.jsonl"), "wt", encoding="utf-8") as f:
        for _file in glob.glob(os.path.join(args.path, "annotation", "*.json")):
            for anns in processor(_file):
                f.write(json.dumps(anns, ensure_ascii=False) + "\n")


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("--path", type=str, default="data/casie")
    args = parser.parse_args()
    main(args)
