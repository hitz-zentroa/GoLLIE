from typing import Tuple, Union

from src.tasks.ace.prompts import (
    ENTITY_DEFINITIONS,
    EVENT_DEFINITIONS,
    GPE,
    RELATION_DEFINITIONS,
    VALUE_DEFINITIONS,
    Acquit,
    Appeal,
    ArrestJail,
    Attack,
    BeBorn,
    Business,
    ChargeIndict,
    CitizenResidentReligionEthnicity,
    ContactInfo,
    Convict,
    Crime,
    DeclareBankruptcy,
    Demonstrate,
    Die,
    Divorce,
    Elect,
    Employment,
    EndOrg,
    EndPosition,
    Execute,
    Extradite,
    Facility,
    Family,
    Fine,
    Founder,
    Injure,
    InvestorShareholder,
    JobTitle,
    LastingPersonal,
    Located,
    Location,
    Marry,
    Meet,
    Membership,
    MergeOrg,
    Near,
    Nominate,
    Numeric,
    OrgLocationOrigin,
    Organization,
    Ownership,
    Pardon,
    Person,
    PhoneWrite,
    ReleaseParole,
    Sentence,
    SentenceAct,
    SportsAffiliation,
    StartOrg,
    StartPosition,
    StudentAlum,
    Subsidiary,
    Sue,
    Time,
    TransferMoney,
    TransferOwnership,
    Transport,
    TrialHearing,
    UserOwnerInventorManufacturer,
    Vehicle,
    Weapon,
    Geographical,
)
from ..utils_data import DatasetLoader, Sampler

import json
import inspect


class ACEDatasetLoader(DatasetLoader):
    """
    A `DatasetLoader` for the ACE05 dataset.

    Args:
        path (`str`):
            The location of the dataset directory.
        group_by (`str`, optional):
            Whether to group the texts by sentence or documents. Defaults to "sentence".

    Raises:
        `ValueError`:
            raised when a not defined value found.
    """

    ENTITY_TO_CLASS_MAPPING = {
        "FAC": Facility,
        "GPE": GPE,
        "LOC": Location,
        "ORG": Organization,
        "PER": Person,
        "VEH": Vehicle,
        "WEA": Weapon,
    }
    VALUE_TO_CLASS_MAPPING = {
        "Contact-Info": ContactInfo,
        "Crime": Crime,
        "Job-Title": JobTitle,
        "Numeric": Numeric,
        "Sentence": Sentence,
        "TIME": Time,
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
                        "doc_id": line["doc_id"],
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


class ACESampler(Sampler):
    """
    A data `Sampler` for the ACE05 dataset.

    Args:
        dataset_loader (`ACEDatasetLoader`):
            The dataset loader that contains the data information.
        task (`str`, optional):
            The task to sample. It must be one of the following: NER, VER, RE, EE.
            Defaults to `None`.
        split (`str`, optional):
            The split to sample. It must be one of the following: "train", "dev" or
            "test". Depending on the split the sampling strategy differs. Defaults to
            `"train"`.
        parallel_instances (`Union[int, Tuple[int, int]]`, optional):
            The number of sentences sampled in parallel. Options:

                * **`int`**: The amount of elements that will be sampled in parallel.
                * **`tuple`**: The range of elements that will be sampled in parallel.

            Defaults to 1.
        max_guidelines (`int`, optional):
            The number of guidelines to append to the example at the same time. If `-1`
            is given then all the guidelines are appended. Defaults to `-1`.
        guideline_dropout (`float`, optional):
            The probability to dropout a guideline definition for the given example. This
            is only applied on training. Defaults to `0.0`.
        seed (`float`, optional):
            The seed to sample the examples. Defaults to `0`.
        prompt_template (`str`, optional):
            The path to the prompt template. Defaults to `"templates/prompt.txt"`.
        ensure_positives_on_train (bool, optional):
            Whether to ensure that the guidelines of annotated examples are not removed.
            Defaults to `True`.
        dataset_name (str, optional):
            The name of the dataset. Defaults to `None`.
        scorer (`str`, optional):
           The scorer class import string. Defaults to `None`.
        sample_only_gold_guidelines (`bool`, optional):
            Whether to sample only guidelines of present annotations. Defaults to `False`.
    """

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
        ensure_positives_on_train: bool = True,
        dataset_name: str = None,
        scorer: str = None,
        sample_only_gold_guidelines: bool = False,
        **kwargs,
    ) -> None:
        assert task in [
            "NER",
            "VER",
            "RE",
            "EE",
        ], f"{task} must be either 'NER', 'VER', 'RE', 'EE'."

        task_definitions, task_target = {
            "NER": (ENTITY_DEFINITIONS, "entities"),
            "VER": (VALUE_DEFINITIONS, "values"),
            "RE": (RELATION_DEFINITIONS, "relations"),
            "EE": (EVENT_DEFINITIONS, "events"),
        }[task]

        super().__init__(
            dataset_loader=dataset_loader,
            task=task,
            split=split,
            parallel_instances=parallel_instances,
            max_guidelines=max_guidelines,
            guideline_dropout=guideline_dropout,
            seed=seed,
            prompt_template=prompt_template,
            ensure_positives_on_train=ensure_positives_on_train,
            sample_only_gold_guidelines=sample_only_gold_guidelines,
            dataset_name=dataset_name,
            scorer=scorer,
            task_definitions=task_definitions,
            task_target=task_target,
            **kwargs,
        )
