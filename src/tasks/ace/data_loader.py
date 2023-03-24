from typing import Any, Dict, Union
from ..utils_typing import DatasetLoader
from .prompts import *

import json
import inspect


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
        "Time-At-Beginning": "time", # A bug on the data
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

    def __init__(self, path: str, group_by: str = "sentence") -> None:
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
                events = []  # TODO: Load events once the prompts are defined
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
                            print(event['event_type'])
                            print(argument['role'])
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
