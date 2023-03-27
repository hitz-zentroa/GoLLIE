import math
from typing import Any, Dict, Tuple, Union
from jinja2 import Template
from ..utils_typing import DatasetLoader, Sampler
from .prompts import *

import json
import inspect
import random
from copy import deepcopy


class ACEDatasetLoader(DatasetLoader):
    ENTITY_TO_CLASS_MAPPING = {
        "FAC": Facility,
        "GPE": GPE,
        "LOC": Location,
        "ORG": Organization,
        "PER": Person,
    }
    VALUE_TO_CLASS_MAPPING = {
        "Contact-Info": ContactInfo,
        "Crime": Crime,
        "Job-Title": JobTitle,
        "Numeric": Numeric,
        "Sentence": Sentence,
        "TIME": Time,
        "VEH": Vehicle,
        "WEA": Weapon,
    }
    RELATION_TO_CLASS_MAPPING = {
        "ART:User-Owner-Inventor-Manufacturer": UserOwnerInventorManufacturer,
        "GEN-AFF:Citizen-Resident-Religion-Ethnicity": CitizenResidentReligionEthnicity,
        "GEN-AFF:Org-Location": OrgLocationOrigin,
        "ORG-AFF:Employment": Employment,
        "ORG-AFF:Founder": Founder,
        "ORG-AFF:Investor-Shareholder": InvestorShareholder,
        "ORG-AFF:Membership": Membership,
        "ORG-AFF:Ownership": Ownership,
        "ORG-AFF:Sports-Affiliation": SportsAffiliation,
        "ORG-AFF:Student-Alum": StudentAlum,
        "PART-WHOLE:Artifact": (
            Geographical
        ),  # There is no definition for Artifact relation on the guidelines
        "PART-WHOLE:Geographical": Geographical,
        "PART-WHOLE:Subsidiary": Subsidiary,
        "PER-SOC:Business": Business,
        "PER-SOC:Family": Family,
        "PER-SOC:Lasting-Personal": LastingPersonal,
        "PHYS:Located": Located,
        "PHYS:Near": Near,
    }
    _EVENT_CONSTANTS_MAPPING = {
        "trigger": "mention",
        "Place": "place",
        "Time-After": "time",
        "Time-At-Begginning": "time",
        "Time-At-Beginning": "time",  # A bug on the data
        "Time-At-End": "time",
        "Time-Before": "time",
        "Time-Ending": "time",
        "Time-Holds": "time",
        "Time-Starting": "time",
        "Time-Within": "time",
    }
    EVENT_TO_CLASS_MAPPING = {
        "Business:Declare-Bankruptcy": {
            "class": DeclareBankruptcy,
            "Org": "org",
        },
        "Business:End-Org": {
            "class": EndOrg,
            "Org": "org",
        },
        "Business:Merge-Org": {
            "class": MergeOrg,
            "Org": "org",
        },
        "Business:Start-Org": {"class": StartOrg, "Agent": "agent", "Org": "org"},
        "Conflict:Attack": {
            "class": Attack,
            "Agent": "attacker",
            "Attacker": "attacker",
            "Instrument": "instrument",
            "Target": "target",
            "Victim": "target",
        },
        "Conflict:Demonstrate": {
            "class": Demonstrate,
            "Entity": "entity",
        },
        "Contact:Meet": {
            "class": Meet,
            "Entity": "entity",
        },
        "Contact:Phone-Write": {
            "class": PhoneWrite,
            "Entity": "entity",
        },
        "Justice:Acquit": {
            "class": Acquit,
            "Adjudicator": "adjudicator",
            "Crime": "crime",
            "Defendant": "defendant",
        },
        "Justice:Appeal": {
            "class": Appeal,
            "Adjudicator": "adjudicator",
            "Crime": "crime",
            "Plaintiff": "prosecutor",
        },
        "Justice:Arrest-Jail": {
            "class": ArrestJail,
            "Agent": "agent",
            "Crime": "crime",
            "Person": "person",
        },
        "Justice:Charge-Indict": {
            "class": ChargeIndict,
            "Adjudicator": "adjudicator",
            "Crime": "crime",
            "Defendant": "defendant",
            "Prosecutor": "prosecutor",
        },
        "Justice:Convict": {
            "class": Convict,
            "Adjudicator": "adjudicator",
            "Crime": "crime",
            "Defendant": "defendant",
        },
        "Justice:Execute": {
            "class": Execute,
            "Agent": "agent",
            "Crime": "crime",
            "Person": "person",
        },
        "Justice:Extradite": {
            "class": Extradite,
            "Agent": "agent",
            "Destination": "destination",
            "Origin": "origin",
            "Person": "person",
        },
        "Justice:Fine": {
            "class": Fine,
            "Adjudicator": "adjudicator",
            "Crime": "crime",
            "Entity": "entity",
            "Money": "money",
        },
        "Justice:Pardon": {
            "class": Pardon,
            "Adjudicator": "adjudicator",
            "Defendant": "defendant",
            "Crime": "crime",
        },
        "Justice:Release-Parole": {
            "class": ReleaseParole,
            "Crime": "crime",
            "Entity": "entity",
            "Person": "person",
        },
        "Justice:Sentence": {
            "class": SentenceAct,
            "Adjudicator": "adjudicator",
            "Crime": "crime",
            "Defendant": "defendant",
            "Sentence": "sentence",
        },
        "Justice:Sue": {
            "class": Sue,
            "Adjudicator": "adjudicator",
            "Crime": "crime",
            "Defendant": "defendant",
            "Plaintiff": "plaintiff",
        },
        "Justice:Trial-Hearing": {
            "class": TrialHearing,
            "Adjudicator": "adjudicator",
            "Crime": "crime",
            "Defendant": "defendant",
            "Prosecutor": "prosecutor",
        },
        "Life:Be-Born": {
            "class": BeBorn,
            "Person": "person",
        },
        "Life:Die": {
            "class": Die,
            "Agent": "agent",
            "Instrument": "instrument",
            "Person": "victim",
            "Victim": "victim",
        },
        "Life:Divorce": {
            "class": Divorce,
            "Person": "person",
        },
        "Life:Injure": {
            "class": Injure,
            "Agent": "agent",
            "Instrument": "instrument",
            "Victim": "victim",
        },
        "Life:Marry": {
            "class": Marry,
            "Person": "person",
        },
        "Movement:Transport": {
            "class": Transport,
            "Agent": "agent",
            "Artifact": "artifact",
            "Destination": "destination",
            "Origin": "origin",
            "Place": "destination",
            "Vehicle": "vehicle",
            "Victim": "artifact",  # MMMmmm WTF
            "Price": "price",
        },
        "Personnel:Elect": {
            "class": Elect,
            "Entity": "entity",
            "Person": "person",
            "Position": "position",
        },
        "Personnel:End-Position": {
            "class": EndPosition,
            "Entity": "entity",
            "Person": "person",
            "Position": "position",
        },
        "Personnel:Nominate": {
            "class": Nominate,
            "Agent": "agent",
            "Person": "person",
            "Position": "position",
        },
        "Personnel:Start-Position": {
            "class": StartPosition,
            "Entity": "entity",
            "Person": "person",
            "Position": "position",
        },
        "Transaction:Transfer-Money": {
            "class": TransferMoney,
            "Beneficiary": "beneficiary",
            "Giver": "giver",
            "Money": "money",
            "Recipient": "recipient",
        },
        "Transaction:Transfer-Ownership": {
            "class": TransferOwnership,
            "Artifact": "artifact",
            "Beneficiary": "beneficiary",
            "Buyer": "buyer",
            "Price": "price",
            "Seller": "seller",
        },
    }

    def __init__(self, path: str, group_by: str = "sentence", **kwargs) -> None:
        assert group_by in [
            "sentence",
            "document",
        ], "`group_by` must be either 'sentence' or 'document'."

        self.elements = {}

        with open(path, "rt") as in_f:
            for line in in_f:
                line = json.loads(line.strip())

                key = line["sent_id"] if group_by == "sentence" else line["doc_id"]
                if key not in self.elements:
                    self.elements[key] = {
                        "id": key,
                        "text": "",
                        "entities": [],
                        "values": [],
                        "relations": [],
                        "events": [],
                    }

                entities = [
                    self.ENTITY_TO_CLASS_MAPPING[entity["entity_type"]](
                        span=entity["text"]
                    )
                    for entity in line["entity_mentions"]
                    if entity["entity_type"] in self.ENTITY_TO_CLASS_MAPPING
                ]
                values = [
                    self.VALUE_TO_CLASS_MAPPING[entity["entity_type"]](
                        span=entity["text"]
                    )
                    for entity in line["entity_mentions"]
                    if entity["entity_type"] in self.VALUE_TO_CLASS_MAPPING
                ]
                relations = [
                    self.RELATION_TO_CLASS_MAPPING[rel["relation_subtype"]](
                        arg1=rel["arguments"][0]["text"],
                        arg2=rel["arguments"][1]["text"],
                    )
                    for rel in line["relation_mentions"]
                    if rel["relation_subtype"] in self.RELATION_TO_CLASS_MAPPING
                ]
                events = []
                for event in line["event_mentions"]:
                    if event["event_type"] not in self.EVENT_TO_CLASS_MAPPING:
                        continue
                    info = self.EVENT_TO_CLASS_MAPPING[event["event_type"]]
                    _inst = {
                        param: []
                        for param in inspect.signature(info["class"]).parameters.keys()
                    }
                    _inst["mention"] = event["trigger"]["text"]
                    for argument in event["arguments"]:
                        if argument["role"] in info:
                            name = info[argument["role"]]
                            _inst[name].append(argument["text"])
                        elif argument["role"] in self._EVENT_CONSTANTS_MAPPING:
                            name = self._EVENT_CONSTANTS_MAPPING[argument["role"]]
                            if name not in _inst:
                                continue
                            _inst[name].append(argument["text"])
                        else:
                            raise ValueError(
                                f"Argument {event['event_type']}:{argument['role']} not"
                                " found!"
                            )

                    events.append(info["class"](**_inst))

                self.elements[key]["text"] += " " + line["sentence"].strip()
                self.elements[key]["entities"] += entities
                self.elements[key]["values"] += values
                self.elements[key]["relations"] += relations
                self.elements[key]["events"] += events

    def __iter__(self):
        for elem in self.elements.values():
            yield elem

    def __getitem__(self, idx: Union[int, str]) -> Dict[str, Any]:
        if isinstance(idx, int):
            return list(self.elements.values())[idx]  # Not very efficient
        else:
            return self.elements[idx]


class ACESampler(Sampler):
    def __init__(
        self,
        dataset_loader: ACEDatasetLoader,
        task: str = None,
        split: str = "train",
        parallel_instances: Union[int, Tuple[int, int]] = 1,
        max_guidelines: int = -1,
        guideline_dropout: float = 0.0,
        seed: float = 0,
        prompt_template: str = "templates/prompt.txt",
        ensure_positives_on_train: bool = False,
        **kwargs,
    ) -> None:
        self.loader = dataset_loader
        assert task in [
            "NER",
            "VER",
            "RE",
            "EE",
        ], f"{task} must be either 'NER', 'VER', 'RE', 'EE'."
        self.task = task
        assert split in [
            "train",
            "dev",
            "test",
        ], f"{split} must be either 'train', 'dev' or 'test'."
        self.split = split
        if isinstance(parallel_instances, int):
            parallel_instances = (1, 1)
        self.parallel_instances = tuple(parallel_instances)
        self.guideline_dropout = guideline_dropout
        self.seed = seed
        self.task_definitions, self.task_target = {
            "NER": (ENTITY_DEFINITIONS, "entities"),
            "VER": (VALUE_DEFINITIONS, "values"),
            "RE": (RELATION_DEFINITIONS, "relations"),
            "EE": (EVENT_DEFINITIONS, "events"),
        }[self.task]
        if max_guidelines < 0 or max_guidelines > len(self.task_definitions):
            self.max_guidelines = len(self.task_definitions)
        else:
            self.max_guidelines = max_guidelines

        with open(prompt_template, "rt") as f:
            self.template = Template(f.read())

    def __iter__(self):
        random.seed(self.seed)
        guidelines = [definition for definition in self.task_definitions]
        instances = []
        total_inst = random.randint(*self.parallel_instances)
        for elem in self.loader:
            if len(instances) == total_inst:
                random.shuffle(guidelines)
                splits = math.ceil(len(guidelines) / self.max_guidelines)
                for i in range(splits):
                    _guidelines = guidelines[
                        i * self.max_guidelines : (i + 1) * self.max_guidelines
                    ]
                    # Apply guideline dropout
                    if self.split == "train":
                        _guidelines = [
                            definition
                            for definition in _guidelines
                            if random.random() > self.guideline_dropout
                        ]
                    _text = " ".join([inst["text"] for inst in instances]).strip()
                    _ann = [
                        ann
                        for inst in instances
                        for ann in inst[self.task_target]
                        if type(ann) in _guidelines
                    ]
                    yield {
                        "ids": [inst["id"] for inst in instances],
                        "labels": [ann.__repr__() for ann in _ann],
                        "text": self.template.render(
                            guidelines=[
                                inspect.getsource(definition)
                                for definition in _guidelines
                            ],
                            text=_text,
                            annotations=_ann,
                        ),
                    }
                instances = []
                total_inst = random.randint(*self.parallel_instances)

            instances.append(elem)

        if len(instances):
            random.shuffle(guidelines)
            splits = math.ceil(len(guidelines) / self.max_guidelines)
            for i in range(splits):
                _guidelines = guidelines[
                    i * self.max_guidelines : (i + 1) * self.max_guidelines
                ]
                # Apply guideline dropout
                if self.split == "train":
                    _guidelines = [
                        definition
                        for definition in _guidelines
                        if random.random() > self.guideline_dropout
                    ]
                _text = " ".join([inst["text"] for inst in instances]).strip()
                _ann = [
                    ann
                    for inst in instances
                    for ann in inst[self.task_target]
                    if type(ann) in _guidelines
                ]
                yield {
                    "ids": [inst["id"] for inst in instances],
                    "labels": [ann.__repr__() for ann in _ann],
                    "text": self.template.render(
                        guidelines=[
                            inspect.getsource(definition) for definition in _guidelines
                        ],
                        text=_text,
                        annotations=_ann,
                    ),
                }
