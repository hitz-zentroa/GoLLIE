"""
Adapted from OneIE: http://blender.cs.illinois.edu/software/oneie/
This script extracts IE annotations from ACE2005 (LDC2006T06).
"""

import glob
import json
import os
import re
from argparse import ArgumentParser
from dataclasses import dataclass
from typing import Any, Dict, List, Tuple

import tqdm
from bs4 import BeautifulSoup
from nltk import (
    sent_tokenize as sent_tokenize_,
)
from nltk import (
    wordpunct_tokenize as wordpunct_tokenize_,
)


TAG_PATTERN = re.compile("<[^<>]+>", re.MULTILINE)

DOCS_TO_REVISE_SENT = {
    "CNN_ENG_20030529_130011.6": [
        (209, 254),
        (461, 504),
        (668, 859),
        (984, 1074),
        (1577, 1632),
    ],
    "CNN_ENG_20030626_203133.11": [(1497, 1527)],
    "CNN_ENG_20030526_180540.6": [(67, 99)],
    "CNNHL_ENG_20030523_221118.14": [(136, 174)],
    "BACONSREBELLION_20050127.1017": [(2659, 2663), (4381, 4405), (410, 458)],
    "misc.legal.moderated_20050129.2225": [(4118, 4127), (4710, 4794)],
    "alt.vacation.las-vegas_20050109.0133": [(1201, 1248)],
    "alt.obituaries_20041121.1339": [(1947, 2044), (1731, 1737)],
    "APW_ENG_20030326.0190": [(638, 739)],
    "APW_ENG_20030403.0862": [(729, 781)],
    "CNN_IP_20030405.1600.02": [(699, 705)],
    "CNN_IP_20030403.1600.00-1": [(2392, 2399)],
    "CNN_IP_20030409.1600.04": [(1039, 1050)],
    "CNN_IP_20030412.1600.03": [(741, 772)],
    "CNN_IP_20030402.1600.02-1": [(885, 892)],
    "CNN_IP_20030329.1600.02": [(3229, 3235)],
    "CNN_IP_20030409.1600.02": [(477, 498)],
    "CNN_CF_20030304.1900.04": [(522, 575), (5193, 5210), (5461, 5542)],
    "CNN_IP_20030403.1600.00-3": [(1487, 1493)],
    "soc.history.war.world-war-ii_20050127.2403": [(414, 441)],
}

# Inconsistency between data and annotation guideline argument names
arg_name_mapping = {
    "ATTACK": {"Victim": "Target", "Agent": "Attacker"},
    "APPEAL": {"Plaintiff": "Prosecutor"},
    "PHONE-WRITE": {"Place": None},
}


def mask_escape(text: str) -> str:
    """Replaces escaped characters with rare sequences.

    Args:
        text (str): text to mask.

    Returns:
        str: masked string.
    """
    return text.replace("&amp;", "ҪҪҪҪҪ").replace("&lt;", "ҚҚҚҚ").replace("&gt;", "ҺҺҺҺ")


def unmask_escape(text: str) -> str:
    """Replaces masking sequences with the original escaped characters.

    Args:
        text (str): masked string.

    Returns:
        str: unmasked string.
    """
    return text.replace("ҪҪҪҪҪ", "&amp;").replace("ҚҚҚҚ", "&lt;").replace("ҺҺҺҺ", "&gt;")


def recover_escape(text: str) -> str:
    """Converts named character references in the given string to the corresponding
    Unicode characters. I didn't notice any numeric character references in this
    dataset.

    Args:
        text (str): text to unescape.

    Returns:
        str: unescaped string.
    """
    return text.replace("&amp;", "&").replace("&lt;", "<").replace("&gt;", ">")


def sent_tokenize(text: Tuple[str, int, int], language: str = "english") -> List[Tuple[str, int, int]]:
    """Performs sentence tokenization. For English, it uses NLTK's sent_tokenize
    function. For Chinese, it uses split_chinese_sentence, a simple sentence
    tokenizer implemented by myself.

    Args:
        text (Tuple[str, int, int]): a tuple of three elements, text to split
            into sentences, start offset, and end offset.
        language (str): available options: english, chinese.

    Returns:
        List[Tuple[str, int, int]]: a list of sentences.
    """
    text, start, end = text
    if language == "chinese":
        sentences = split_chinese_sentence(text)
    else:
        sentences = sent_tokenize_(text, language=language)

    last = 0
    sentences_ = []
    for sent in sentences:
        index = text[last:].find(sent)
        if index == -1:
            print(text, sent)
        else:
            sentences_.append((sent, last + index + start, last + index + len(sent) + start))
        last += index + len(sent)
    return sentences_


def wordpunct_tokenize(text: str, language: str = "english") -> List[str]:
    """Performs word tokenization. For English, it uses NLTK's
    wordpunct_tokenize function. For Chinese, it simply splits the sentence into
    characters.

    Args:
        text (str): text to split into words.
        language (str): available options: english, chinese.

    Returns:
        List[str]: a list of words.
    """
    if language == "chinese":
        return [c for c in text if c.strip()]
    return wordpunct_tokenize_(text)


def split_chinese_sentence(text: str) -> List[str]:
    """Performs sentence tokenization for Chinese.

    Args:
        text (str): text to split into sentences.

    Returns:
        List[str]: a list of sentences.
    """
    sentences = []
    quote_mark_count = 0
    sentence = ""
    for i, c in enumerate(text):
        sentence += c
        if c in {"”", "」"}:
            sentences.append(sentence)
            sentence = ""
        elif c in {"。", "!", "?", "！", "？"}:
            if i < len(text) - 1 and text[i + 1] not in {"”", '"', "」"}:
                sentences.append(sentence)
                sentence = ""
        elif c == '"':
            quote_mark_count += 1
            if quote_mark_count % 2 == 0 and len(sentence) > 2 and sentence[-2] in {"？", "！", "。", "?", "!"}:
                sentences.append(sentence)
                sentence = ""
    if sentence:
        sentences.append(sentence)
    return sentences


@dataclass
class Span:
    start: int
    end: int
    text: str

    def __post_init__(self):
        self.start = int(self.start)
        self.end = int(self.end)
        self.text = self.text.replace("\n", " ")

    def char_offsets_to_token_offsets(self, tokens: List[Tuple[int, int, str]]):
        """Converts self.start and self.end from character offsets to token
        offsets.

        Args:
            tokens (List[int, int, str]): a list of token tuples. Each item in
                the list is a triple (start_offset, end_offset, text).
        """
        start_ = end_ = -1
        for i, (s, e, _) in enumerate(tokens):
            if s == self.start:
                start_ = i
            if e == self.end:
                end_ = i + 1
        if start_ == -1 or end_ == -1 or start_ > end_:
            raise ValueError(
                "Failed to update offsets for {}-{}:{} in {}".format(self.start, self.end, self.text, tokens)
            )
        self.start, self.end = start_, end_

    def to_dict(self) -> Dict[str, Any]:
        """Converts instance variables to a dict.

        Returns:
            dict: a dict of instance variables.
        """
        return {"text": recover_escape(self.text), "start": self.start, "end": self.end}

    def remove_space(self):
        """Removes heading and trailing spaces in the span text."""
        # heading spaces
        text = self.text.lstrip(" ")
        self.start += len(self.text) - len(text)
        # trailing spaces
        text = text.rstrip(" ")
        self.text = text
        self.end = self.start + len(text)

    def copy(self):
        """Makes a copy of itself.

        Returns:
            Span: a copy of itself."""
        return Span(self.start, self.end, self.text)


@dataclass
class Entity(Span):
    entity_id: str
    mention_id: str
    entity_type: str
    entity_subtype: str
    mention_type: str
    value: str = None

    def to_dict(self) -> Dict[str, Any]:
        """Converts instance variables to a dict.

        Returns:
            Dict: a dict of instance variables.
        """
        entity_dict = {
            "text": recover_escape(self.text),
            "entity_id": self.entity_id,
            "mention_id": self.mention_id,
            "start": self.start,
            "end": self.end,
            "entity_type": self.entity_type,
            "entity_subtype": self.entity_subtype,
            "mention_type": self.mention_type,
        }
        if self.value:
            entity_dict["value"] = self.value
        return entity_dict


@dataclass
class RelationArgument:
    mention_id: str
    role: str
    text: str

    def to_dict(self) -> Dict[str, Any]:
        """Converts instance variables to a dict.

        Returns:
            Dict[str, Any]: a dict of instance variables.
        """
        return {
            "mention_id": self.mention_id,
            "role": self.role,
            "text": recover_escape(self.text),
        }


@dataclass
class Relation:
    relation_id: str
    relation_type: str
    relation_subtype: str
    arg1: RelationArgument
    arg2: RelationArgument

    def to_dict(self) -> Dict[str, Any]:
        """Converts instance variables to a dict.

        Returns:
            Dict[str, Any]: a dict of instance variables.
        """
        return {
            "relation_id": self.relation_id,
            "relation_type": self.relation_type,
            "relation_subtype": self.relation_subtype,
            "arg1": self.arg1.to_dict(),
            "arg2": self.arg2.to_dict(),
        }


@dataclass
class EventArgument:
    mention_id: str
    role: str
    text: str

    def to_dict(self) -> Dict[str, Any]:
        """Converts instance variables to a dict.

        Returns:
            Dict[str, Any]: a dict of instance variables.
        """
        return {
            "mention_id": self.mention_id,
            "role": self.role,
            "text": recover_escape(self.text),
        }


@dataclass
class Event:
    event_id: str
    mention_id: str
    event_type: str
    event_subtype: str
    trigger: Span
    arguments: List[EventArgument]

    def to_dict(self) -> Dict[str, Any]:
        """Converts instance variables to a dict.

        Returns:
            Dict[str, Any]: a dict of instance variables.
        """
        return {
            "event_id": self.event_id,
            "mention_id": self.mention_id,
            "event_type": self.event_type,
            "event_subtype": self.event_subtype,
            "trigger": self.trigger.to_dict(),
            "arguments": [arg.to_dict() for arg in self.arguments],
        }


@dataclass
class Sentence(Span):
    sent_id: str
    tokens: List[str]
    entities: List[Entity]
    relations: List[Relation]
    events: List[Event]

    def to_dict(self) -> Dict[str, Any]:
        """Converts instance variables to a dict.

        Returns:
            Dict[str, Any]: a dict of instance variables.
        """
        return {
            "sent_id": self.sent_id,
            "tokens": [recover_escape(t) for t in self.tokens],
            "entities": [entity.to_dict() for entity in self.entities],
            "relations": [relation.to_dict() for relation in self.relations],
            "events": [event.to_dict() for event in self.events],
            "start": self.start,
            "end": self.end,
            "text": recover_escape(self.text).replace("\t", " "),
        }


@dataclass
class Document:
    doc_id: str
    sentences: List[Sentence]

    def to_dict(self) -> Dict[str, Any]:
        """Converts instance variables to a dict.

        Returns:
            Dict[str, Any]: a dict of instance variables.
        """
        return {
            "doc_id": self.doc_id,
            "sentences": [sent.to_dict() for sent in self.sentences],
        }


def revise_sentences(sentences: List[Tuple[str, int, int]], doc_id: str) -> List[Tuple[int, int, str]]:
    """Automatic sentence tokenization may have errors for a few documents.

    Args:
        sentences (List[Tuple[str, int, int]]): a list of sentence tuples.
        doc_id (str): document ID.

    Returns:
        List[Tuple[str, int, int]]: a list of revised sentence tuples.
    """
    sentences_ = []

    offset_list = DOCS_TO_REVISE_SENT[doc_id]
    first_part_offsets = {offset for offset, _ in offset_list}
    second_part_offsets = {offset for _, offset in offset_list}

    for sentence_idx, (text, start, end) in enumerate(sentences):
        if start in first_part_offsets:
            next_text, next_start, next_end = sentences[sentence_idx + 1]
            space = " " * (next_start - end)
            sentences_.append((text + space + next_text, start, next_end))
        elif start in second_part_offsets:
            continue
        else:
            sentences_.append((text, start, end))

    return sentences_


def read_sgm_file(path: str, language: str = "english") -> List[Tuple[str, int, int]]:
    """Reads a SGM text file.

    Args:
        path (str): path to the input file.
        language (str): document language. Valid values: "english" or "chinese".

    Returns:
        List[Tuple[str, int, int]]: a list of sentences. Each item in the list
            is a tuple of three elements, sentence text, start offset, and end
            offset.
    """
    data = open(path, "r", encoding="utf-8").read()

    # Chunk the document
    chunks = TAG_PATTERN.sub("⁑", data).split("⁑")

    # Get the offset of <TEXT>
    data = data.replace("<TEXT>", "⁂")
    data = TAG_PATTERN.sub("", data)
    min_offset = max(0, data.find("⁂"))
    data = data.replace("⁂", "")

    # Extract sentences from chunks
    chunk_offset = 0
    sentences = []
    for chunk in chunks:
        lines = chunk.split("\n")
        current_sentence = []
        start = offset = 0
        for line in lines:
            offset += len(line) + 1
            if line.strip():
                current_sentence.append(line)
            else:
                # empty line
                if current_sentence:
                    sentence = " ".join(current_sentence)
                    if start + chunk_offset >= min_offset:
                        sentences.append(
                            (
                                sentence,
                                start + chunk_offset,
                                start + chunk_offset + len(sentence),
                            )
                        )
                    current_sentence = []
                start = offset
        if current_sentence:
            sentence = " ".join(current_sentence)
            if start + chunk_offset >= min_offset:
                sentences.append(
                    (
                        sentence,
                        start + chunk_offset,
                        start + chunk_offset + len(sentence),
                    )
                )
        chunk_offset += len(chunk)

    # Re-tokenize sentences
    sentences = [s for sent in sentences for s in sent_tokenize(sent, language=language)]

    return sentences


def read_apf_file(path: str, time_and_val: bool = False) -> Tuple[str, str, List[Entity], List[Relation], List[Event]]:
    """Reads an APF file.

    Args:
        path (str): path to the input file.
        time_and_val (bool): extract times and values or not.

    Returns:
        doc_id (str): document ID.
        source (str): document source.
        entity_list (List[Entity]): a list of Entity instances.
        relation_list (List[Relation]): a list of Relation instances.
        event_list (List[Event]): a list of Events instances.
    """
    data = open(path, "r", encoding="utf-8").read()
    soup = BeautifulSoup(data, "lxml-xml")

    # metadata
    root = soup.find("source_file")
    source = root["SOURCE"]
    doc = root.find("document")
    doc_id = doc["DOCID"]

    entity_list, relation_list, event_list = [], [], []

    # entities: nam, nom, pro
    for entity in doc.find_all("entity"):
        entity_id = entity["ID"]
        entity_type = entity["TYPE"]
        entity_subtype = entity["SUBTYPE"]
        for entity_mention in entity.find_all("entity_mention"):
            mention_id = entity_mention["ID"]
            mention_type = entity_mention["TYPE"]
            head = entity_mention.find("head").find("charseq")
            start, end, text = int(head["START"]), int(head["END"]), head.text
            entity_list.append(
                Entity(
                    start,
                    end,
                    text,
                    entity_id,
                    mention_id,
                    entity_type,
                    entity_subtype,
                    mention_type,
                )
            )

    if time_and_val:
        # entities: value
        for entity in doc.find_all("value"):
            entity_id = entity["ID"]
            entity_type = entity["TYPE"]
            entity_subtype = entity.get("SUBTYPE", None)
            for entity_mention in entity.find_all("value_mention"):
                mention_id = entity_mention["ID"]
                mention_type = "VALUE"
                extent = entity_mention.find("extent").find("charseq")
                start, end, text = int(extent["START"]), int(extent["END"]), extent.text
                entity_list.append(
                    Entity(
                        start,
                        end,
                        text,
                        entity_id,
                        mention_id,
                        entity_type,
                        entity_subtype,
                        mention_type,
                    )
                )

        # entities: timex
        for entity in doc.find_all("timex2"):
            entity_id = entity["ID"]
            entity_subtype = "TIME"
            value = entity.get("VAL", None)
            for entity_mention in entity.find_all("timex2_mention"):
                mention_id = entity_mention["ID"]
                mention_type = "TIME"
                extent = entity_mention.find("extent").find("charseq")
                start, end, text = int(extent["START"]), int(extent["END"]), extent.text
                entity_list.append(
                    Entity(
                        start,
                        end,
                        text,
                        entity_id,
                        mention_id,
                        entity_type,
                        entity_subtype,
                        mention_type,
                        value=value,
                    )
                )

    # relations
    for relation in doc.find_all("relation"):
        relation["ID"]
        relation_type = relation["TYPE"]
        if relation_type == "METONYMY":
            continue
        relation_subtype = relation["SUBTYPE"]
        for relation_mention in relation.find_all("relation_mention"):
            mention_id = relation_mention["ID"]
            arg1 = arg2 = None
            for arg in relation_mention.find_all("relation_mention_argument"):
                arg_mention_id = arg["REFID"]
                arg_role = arg["ROLE"]
                arg_text = arg.find("extent").find("charseq").text
                if arg_role == "Arg-1":
                    arg1 = RelationArgument(arg_mention_id, arg_role, arg_text)
                elif arg_role == "Arg-2":
                    arg2 = RelationArgument(arg_mention_id, arg_role, arg_text)
            if arg1 and arg2:
                relation_list.append(Relation(mention_id, relation_type, relation_subtype, arg1, arg2))

    # events
    for event in doc.find_all("event"):
        event_id = event["ID"]
        event_type = event["TYPE"]
        event_subtype = event["SUBTYPE"]
        for event_mention in event.find_all("event_mention"):
            mention_id = event_mention["ID"]
            trigger = event_mention.find("anchor").find("charseq")
            trigger_start, trigger_end = int(trigger["START"]), int(trigger["END"])
            trigger_text = trigger.text
            event_args = []
            for arg in event_mention.find_all("event_mention_argument"):
                arg_mention_id = arg["REFID"]
                arg_role = arg["ROLE"]
                arg_text = arg.find("extent").find("charseq").text
                event_args.append(EventArgument(arg_mention_id, arg_role, arg_text))
            event_list.append(
                Event(
                    event_id,
                    mention_id,
                    event_type,
                    event_subtype,
                    Span(trigger_start, trigger_end + 1, trigger_text),
                    event_args,
                )
            )

    # remove heading/tailing spaces
    for entity in entity_list:
        entity.remove_space()
    for event in event_list:
        event.trigger.remove_space()

    return doc_id, source, entity_list, relation_list, event_list


def process_entities(entities: List[Entity], sentences: List[Tuple[str, int, int]]) -> List[List[Entity]]:
    """Cleans entities and splits them into lists

    Args:
        entities (List[Entity]): a list of Entity instances.
        sentences (List[Tuple[str, int, int]]): a list of sentences.

    Returns:
        List[List[Entity]]: a list of sentence entity lists.
    """
    sentence_entities = [[] for _ in range(len(sentences))]

    # assign each entity to the sentence where it appears
    for entity in entities:
        start, end = entity.start, entity.end
        for i, (_, s, e) in enumerate(sentences):
            if start >= s and end <= e:
                sentence_entities[i].append(entity)
                break

    # remove overlapping entities
    sentence_entities_cleaned = [[] for _ in range(len(sentences))]
    for i, entities in enumerate(sentence_entities):
        if not entities:
            continue
        # prefer longer entities
        entities.sort(key=lambda x: (x.end - x.start), reverse=True)
        chars = [0] * max([x.end for x in entities])
        for entity in entities:
            overlap = False
            for j in range(entity.start, entity.end):
                if chars[j] == 1:
                    overlap = True
                    break
            if not overlap:
                chars[entity.start : entity.end] = [1] * (entity.end - entity.start)
                sentence_entities_cleaned[i].append(entity)
        sentence_entities_cleaned[i].sort(key=lambda x: x.start)

    return sentence_entities_cleaned


def process_events(
    events: List[Event],
    sentence_entities: List[List[Entity]],
    sentences: List[Tuple[str, int, int]],
) -> List[List[Event]]:
    """Cleans and assigns events.

    Args:
        events (List[Event]): A list of Event objects
        entence_entities (List[List[Entity]]): A list of sentence entity lists.
        sentences (List[Tuple[str, int, int]]): A list of sentences.

    Returns:
        List[List[Event]]: a list of sentence event lists.
    """
    sentence_events = [[] for _ in range(len(sentences))]
    # assign each event mention to the sentence where it appears
    for event in events:
        start, end = event.trigger.start, event.trigger.end
        for i, (_, s, e) in enumerate(sentences):
            sent_entities = sentence_entities[i]
            if start >= s and end <= e:
                # clean the argument list
                arguments = []
                for argument in event.arguments:
                    # entity_id = argument.entity_id
                    mention_id = argument.mention_id
                    for entity in sent_entities:
                        if entity.mention_id == mention_id:
                            arguments.append(argument)
                            break
                event_cleaned = Event(
                    event.event_id,
                    event.mention_id,
                    event.event_type,
                    event.event_subtype,
                    trigger=event.trigger.copy(),
                    arguments=arguments,
                )
                sentence_events[i].append(event_cleaned)

    # remove overlapping events
    sentence_events_cleaned = [[] for _ in range(len(sentences))]
    for i, events in enumerate(sentence_events):
        if not events:
            continue
        events.sort(key=lambda x: (x.trigger.end - x.trigger.start), reverse=True)
        chars = [0] * max([x.trigger.end for x in events])
        for event in events:
            overlap = False
            for j in range(event.trigger.start, event.trigger.end):
                if chars[j] == 1:
                    overlap = True
                    break
            if not overlap:
                chars[event.trigger.start : event.trigger.end] = [1] * (event.trigger.end - event.trigger.start)
                sentence_events_cleaned[i].append(event)
        sentence_events_cleaned[i].sort(key=lambda x: x.trigger.start)

    return sentence_events_cleaned


def process_relation(
    relations: List[Relation],
    sentence_entities: List[List[Entity]],
    sentences: List[Tuple[str, int, int]],
) -> List[List[Relation]]:
    """Cleans and assigns relations

    Args:
        relations (List[Relation]): a list of Relation instances.
        sentence_entities (List[List[Entity]]): a list of sentence entity lists.
        sentences (List[Tuple[str, int, int]]): a list of sentences.

    Returns:
        List[List[Relation]]: a list of sentence relation lists.
    """
    sentence_relations = [[] for _ in range(len(sentences))]
    for relation in relations:
        mention_id1 = relation.arg1.mention_id
        mention_id2 = relation.arg2.mention_id
        for i, entities in enumerate(sentence_entities):
            arg1_in_sent = any(mention_id1 == e.mention_id for e in entities)
            arg2_in_sent = any(mention_id2 == e.mention_id for e in entities)
            if arg1_in_sent and arg2_in_sent:
                sentence_relations[i].append(relation)
                break
            elif arg1_in_sent != arg2_in_sent:
                break
    return sentence_relations


def tokenize(
    sentence: Tuple[str, int, int],
    entities: List[Entity],
    events: List[Event],
    language: str = "english",
) -> List[Tuple[int, int, str]]:
    """Tokenizes a sentence.
    Each sentence is first split into chunks that are entity/event spans or words
    between two spans. After that, word tokenization is performed on each chunk.

    Args:
        sentence (Tuple[str, int, int]): Sentence tuple (text, start, end)
        entities (List[Entity]): A list of Entity instances.
        events (List[Event]): A list of Event instances.

    Returns:
        List[Tuple[int, int, str]]: a list of token tuples. Each tuple consists
        of three elements, start offset, end offset, and token text.
    """
    text, start, end = sentence
    text = mask_escape(text)

    # split the sentence into chunks
    splits = {0, len(text)}
    for entity in entities:
        splits.add(entity.start - start)
        splits.add(entity.end - start)
    for event in events:
        splits.add(event.trigger.start - start)
        splits.add(event.trigger.end - start)
    splits = sorted(splits)
    chunks = [(splits[i], splits[i + 1], text[splits[i] : splits[i + 1]]) for i in range(len(splits) - 1)]

    # tokenize each chunk
    chunks = [(s, e, t, wordpunct_tokenize(t, language=language)) for s, e, t in chunks]

    # merge chunks and add word offsets
    tokens = []
    for chunk_start, chunk_end, chunk_text, chunk_tokens in chunks:
        last = 0
        chunk_tokens_ = []
        for token in chunk_tokens:
            token_start = chunk_text[last:].find(token)
            if token_start == -1:
                raise ValueError("Cannot find token {} in {}".format(token, text))
            token_end = token_start + len(token)
            chunk_tokens_.append(
                (
                    token_start + start + last + chunk_start,
                    token_end + start + last + chunk_start,
                    unmask_escape(token),
                )
            )
            last += token_end
        tokens.extend(chunk_tokens_)
    return tokens


def convert(sgm_file: str, apf_file: str, time_and_val: bool = False, language: str = "english") -> Document:
    """Converts a document.

    Args:
        sgm_file (str): path to a SGM file.
        apf_file (str): path to a APF file.
        time_and_val (bool, optional): extracts times and values or not.
            Defaults to False.
        language (str, optional): document language. Available options: english,
            chinese. Defaults to 'english'.

    Returns:
        Document: a Document instance.
    """
    sentences = read_sgm_file(sgm_file, language=language)
    doc_id, source, entities, relations, events = read_apf_file(apf_file, time_and_val=time_and_val)

    # Reivse sentences
    if doc_id in DOCS_TO_REVISE_SENT:
        sentences = revise_sentences(sentences, doc_id)

    # Process entities, relations, and events
    sentence_entities = process_entities(entities, sentences)
    sentence_relations = process_relation(relations, sentence_entities, sentences)
    sentence_events = process_events(events, sentence_entities, sentences)

    # Tokenization
    sentence_tokens = [
        tokenize(s, ent, evt, language=language) for s, ent, evt in zip(sentences, sentence_entities, sentence_events)
    ]

    # Convert span character offsets to token indices
    sentence_objs = []
    for i, (toks, ents, evts, rels, sent) in enumerate(
        zip(
            sentence_tokens,
            sentence_entities,
            sentence_events,
            sentence_relations,
            sentences,
        )
    ):
        for entity in ents:
            entity.char_offsets_to_token_offsets(toks)
        for event in evts:
            event.trigger.char_offsets_to_token_offsets(toks)
        sent_id = "{}-{}".format(doc_id, i)
        sentence_objs.append(
            Sentence(
                start=sent[1],
                end=sent[2],
                text=sent[0],
                sent_id=sent_id,
                tokens=[t for _, _, t in toks],
                entities=ents,
                relations=rels,
                events=evts,
            )
        )
    return Document(doc_id, sentence_objs)


def convert_batch(
    input_path: str,
    output_path: str,
    time_and_val: bool = False,
    language: str = "english",
):
    """Converts a batch of documents.

    Args:
        input_path (str): path to the input directory. Usually, it is the path
            to the LDC2006T06/data/English or LDC2006T06/data/Chinese folder.
        output_path (str): path to the output JSON file.
        time_and_val (bool, optional): extracts times and values or not.
            Defaults to False.
        language (str, optional): document language. Available options: english,
            chinese. Defaults to 'english'.
    """
    if language == "english":
        sgm_files = glob.glob(os.path.join(input_path, "**", "timex2norm", "*.sgm"))
    elif language == "chinese":
        sgm_files = glob.glob(os.path.join(input_path, "**", "adj", "*.sgm"))
    else:
        raise ValueError("Unknown language: {}".format(language))
    print("Converting the dataset to JSON format")
    print("#SGM files: {}".format(len(sgm_files)))
    progress = tqdm.tqdm(total=len(sgm_files))

    with open(output_path, "w", encoding="utf-8") as w:
        for sgm_file in sgm_files:
            progress.update(1)
            apf_file = sgm_file.replace(".sgm", ".apf.xml")
            doc = convert(sgm_file, apf_file, time_and_val=time_and_val, language=language)
            w.write(json.dumps(doc.to_dict()) + "\n")
    progress.close()


def convert_to_oneie(input_path: str, output_path: str):
    """Converts files to OneIE format.

    Args:
        input_path (str): path to the input file.
        output_path (str): path to the output file.
    """
    print("Converting the dataset to OneIE format")
    with open(input_path, "r", encoding="utf-8") as r, open(output_path, "w", encoding="utf-8") as w:
        for line in r:
            doc = json.loads(line)
            for sentence in doc["sentences"]:
                tokens = sentence["tokens"]
                # pieces = [tokenizer.tokenize(t) for t in tokens]
                # token_lens = [len(x) for x in pieces]
                # if 0 in token_lens:
                #     skip_num += 1
                #     continue
                # pieces = [p for ps in pieces for p in ps]
                # if len(pieces) == 0:
                #     skip_num += 1
                #     continue

                entity_text = {e["mention_id"]: e["text"] for e in sentence["entities"]}
                # update argument text
                for relation in sentence["relations"]:
                    arg1, arg2 = relation["arg1"], relation["arg2"]
                    arg1["text"] = entity_text[arg1["mention_id"]]
                    arg2["text"] = entity_text[arg2["mention_id"]]
                for event in sentence["events"]:
                    for arg in event["arguments"]:
                        arg["text"] = entity_text[arg["mention_id"]]

                # entities
                entities = []
                for entity in sentence["entities"]:
                    entities.append(
                        {
                            "id": entity["mention_id"],
                            "text": entity["text"],
                            "entity_type": entity["entity_type"] if entity["mention_type"] != "TIME" else "TIME",
                            "mention_type": entity["mention_type"],
                            "entity_subtype": entity["entity_subtype"],
                            "start": entity["start"],
                            "end": entity["end"],
                        }
                    )
                # relations
                relations = []
                for relation in sentence["relations"]:
                    relations.append(
                        {
                            "id": relation["relation_id"],
                            "relation_type": relation["relation_type"],
                            "relation_subtype": "{}:{}".format(
                                relation["relation_type"], relation["relation_subtype"]
                            ),
                            "arguments": [
                                {
                                    "entity_id": relation["arg1"]["mention_id"],
                                    "text": relation["arg1"]["text"],
                                    "role": relation["arg1"]["role"],
                                },
                                {
                                    "entity_id": relation["arg2"]["mention_id"],
                                    "text": relation["arg2"]["text"],
                                    "role": relation["arg2"]["role"],
                                },
                            ],
                        }
                    )

                # events
                events = []
                for event in sentence["events"]:
                    events.append(
                        {
                            "id": event["mention_id"],
                            "event_type": "{}:{}".format(event["event_type"], event["event_subtype"]),
                            "trigger": event["trigger"],
                            "arguments": [
                                {
                                    "entity_id": arg["mention_id"],
                                    "text": arg["text"],
                                    "role": arg["role"],
                                }
                                for arg in event["arguments"]
                            ],
                        }
                    )

                sent_obj = {
                    "doc_id": doc["doc_id"],
                    "sent_id": sentence["sent_id"],
                    "tokens": tokens,
                    "sentence": sentence["text"],
                    "entity_mentions": entities,
                    "relation_mentions": relations,
                    "event_mentions": events,
                }
                w.write(json.dumps(sent_obj) + "\n")


def convert_to_event_only(input_path: str, output_path: str):
    """Converts files to event-only format.

    Args:
        input_path (str): path to the input file.
        output_path (str): path to the output file.
        tokenizer (PreTrainedTokenizer): wordpiece tokenizer.
    """
    print("Converting the dataset to event-only format...")
    skip_num = 0
    with open(input_path, "r", encoding="utf-8") as r, open(output_path, "w", encoding="utf-8") as w:
        for line in r:
            doc = json.loads(line)
            for sentence in doc["sentences"]:
                tokens = sentence["tokens"]

                entity_text = {e["mention_id"]: e["text"] for e in sentence["entities"]}
                entity_span = {e["mention_id"]: {"start": e["start"], "end": e["end"]} for e in sentence["entities"]}

                ## update argument text

                for event in sentence["events"]:
                    event_type = event["event_subtype"].upper()
                    cleaned_arguments = []

                    for arg in event["arguments"]:
                        arg["text"] = entity_text[arg["mention_id"]]
                        arg["start"] = entity_span[arg["mention_id"]]["start"]
                        arg["end"] = entity_span[arg["mention_id"]]["end"]
                        arg["role"] = simplify_arg_role_name(arg["role"])

                        if event_type in arg_name_mapping:
                            if arg["role"] in arg_name_mapping[event_type]:
                                new_role = arg_name_mapping[event_type][arg["role"]]
                                if new_role is None:  # arg type isn't in ontology at all
                                    continue  # delete it from data
                                else:  # arg type is in ontology, but misnamed in data
                                    arg["role"] = new_role  # update its name

                        cleaned_arguments.append(
                            {
                                "text": arg["text"],
                                "role": arg["role"],
                                "start": arg["start"],
                                "end": arg["end"],
                            }
                        )
                    event["arguments"] = cleaned_arguments

                # events

                events = []
                for event in sentence["events"]:
                    events.append(
                        {
                            "event_type": "{}:{}".format(event["event_type"], event["event_subtype"]),
                            "trigger": event["trigger"],
                            "arguments": event["arguments"],
                        }
                    )

                sent_obj = {
                    "doc_id": doc["doc_id"],
                    "sent_id": sentence["sent_id"],
                    "tokens": tokens,
                    "sentence": sentence["text"],
                    "event_mentions": events,
                }
                w.write(json.dumps(sent_obj) + "\n")
    print("skip num: {}".format(skip_num))


def simplify_arg_role_name(role_name: str):
    """
    Converts the name of the argument role to the simple form (e.g. "Time-Within" to
    "Time").
    """
    cols = role_name.split("-")
    if len(cols) > 1 and cols[0] != "Time":
        print(cols)
    return cols[0]


def split_data(input_file: str, output_dir: str, split_path: str):
    """Splits the input file into train/dev/test sets.

    Args:
        input_file (str): path to the input file.
        output_dir (str): path to the output directory.
        split_path (str): path to the split directory that contains three files,
            train.doc.txt, dev.doc.txt, and test.doc.txt . Each line in these
            files is a document ID.
    """
    print("Splitting the dataset into train/dev/test sets")
    train_docs, dev_docs, test_docs = set(), set(), set()
    # load doc ids
    with open(os.path.join(split_path, "train.doc.txt")) as r:
        train_docs.update(r.read().strip("\n").split("\n"))
    with open(os.path.join(split_path, "dev.doc.txt")) as r:
        dev_docs.update(r.read().strip("\n").split("\n"))
    with open(os.path.join(split_path, "test.doc.txt")) as r:
        test_docs.update(r.read().strip("\n").split("\n"))

    # split the dataset
    with open(input_file, "r", encoding="utf-8") as r, open(
        os.path.join(output_dir, "train.sentence.json"), "w"
    ) as w_train, open(os.path.join(output_dir, "dev.sentence.json"), "w") as w_dev, open(
        os.path.join(output_dir, "test.sentence.json"), "w"
    ) as w_test:
        for line in r:
            inst = json.loads(line)
            doc_id = inst["doc_id"]
            if doc_id in train_docs:
                w_train.write(line)
            elif doc_id in dev_docs:
                w_dev.write(line)
            elif doc_id in test_docs:
                w_test.write(line)


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("-i", "--input", help="Path to the input folder")
    parser.add_argument("-o", "--output", help="Path to the output folder")
    parser.add_argument("-s", "--split", default=None, help="Path to the split folder")
    parser.add_argument("-l", "--lang", default="english", help="Document language")
    parser.add_argument("--time_and_val", action="store_true", help="Extracts times and values")

    args = parser.parse_args()
    if args.lang not in ["chinese", "english"]:
        raise ValueError("Unsupported language: {}".format(args.lang))
    input_dir = os.path.join(args.input, args.lang.title())

    # Convert to doc-level JSON format
    json_path = os.path.join(args.output, "{}.json".format(args.lang))
    convert_batch(input_dir, json_path, time_and_val=args.time_and_val, language=args.lang)

    # Convert to event-only format
    sentence_path = os.path.join(args.output, "{}.sentence.json".format(args.lang))
    convert_to_oneie(json_path, sentence_path)

    # Split the data
    if args.split:
        split_data(sentence_path, args.output, args.split)
