from typing import Any, Dict, Union
from ..utils_typing import DatasetLoader
from .prompts import *

import json


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

    def __init__(self, path: str, group_by: str = "sentence") -> None:
        assert group_by in [
            "sentence",
            "document",
        ], "`group_by` must be either 'sentence' or document'."

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
