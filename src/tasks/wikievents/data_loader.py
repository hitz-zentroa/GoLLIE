import inspect
import json

from src.tasks.wikievents.prompts import (
    GPE,
    Abstract,
    Acquit,
    ArrestJailDetain,
    ArtifactExistanceEvent,
    Attack,
    BodyPart,
    ChargeIndict,
    CognitiveEvent,
    CommercialProduct,
    ConflictEvent,
    Contact,
    ContactEvent,
    ControlEvent,
    Convict,
    Crash,
    DamageDestroy,
    Defeat,
    Demonstrate,
    Die,
    DisableDefuse,
    DisasterEvent,
    DiseaseOutbreak,
    Dismantle,
    Donation,
    EndPosition,
    Evacuation,
    ExchangeBuySell,
    Facility,
    GenericCrime,
    GenericCrimeEvent,
    IdentifyCategorize,
    IllegalTransportation,
    ImpedeInterfereWith,
    Infect,
    Information,
    Injure,
    Inspection,
    Intervention,
    InvestigateCrime,
    JobTitle,
    JusticeEvent,
    LifeEvent,
    Location,
    ManufactureAssemble,
    MedicalEvent,
    MedicalHealthIssue,
    Money,
    MovementTransportEvent,
    Numeric,
    Organization,
    Person,
    PersonnelEvent,
    PreventPassage,
    ReleaseParole,
    RequestCommand,
    Research,
    Sentence,
    SideOfConflict,
    StartPosition,
    TeachingTrainingLearning,
    ThreatenCoerce,
    TransactionEvent,
    Transportation,
    TrialHearing,
    Vehicle,
    Weapon,
)

from ..utils_data import DatasetLoader


class WikiEventsDatasetLoader(DatasetLoader):
    ENTITY_TO_CLASS_MAPPING = {
        "ABS": Abstract,
        "BOD": BodyPart,
        "COM": CommercialProduct,
        "FAC": Facility,
        "GPE": GPE,
        "INF": Information,
        "LOC": Location,
        "MHI": MedicalHealthIssue,
        "MON": Money,
        "ORG": Organization,
        "PER": Person,
        "SID": SideOfConflict,
        "TTL": JobTitle,
        "VAL": Numeric,
        "VEH": Vehicle,
        "WEA": Weapon,
    }

    _EVENT_CONSTANTS_MAPPING = {
        "trigger": "mention",
        "Place": "place",
    }

    EVENT_TO_CLASS_MAPPING = {
        "ArtifactExistence.DamageDestroyDisableDismantle.Damage": {
            "coarse": ArtifactExistanceEvent,
            "class": DamageDestroy,
            "Artifact": "artifact",
            "Instrument": "instrument",
            "Damager": "agent",
        },
        "ArtifactExistence.DamageDestroyDisableDismantle.Destroy": {
            "coarse": ArtifactExistanceEvent,
            "class": DamageDestroy,
            "Artifact": "artifact",
            "Destroyer": "agent",
            "Instrument": "instrument",
        },
        "ArtifactExistence.DamageDestroyDisableDismantle.DisableDefuse": {
            "coarse": ArtifactExistanceEvent,
            "class": DisableDefuse,
            "Artifact": "artifact",
            "Disabler": "agent",
            "Instrument": "instrument",
        },
        "ArtifactExistence.DamageDestroyDisableDismantle.Dismantle": {
            "coarse": ArtifactExistanceEvent,
            "class": Dismantle,
            "Artifact": "artifact",
            "Components": "components",
            "Dismantler": "agent",
            "Instrument": "instrument"
        },
        "ArtifactExistence.DamageDestroyDisableDismantle.Unspecified": {
            "coarse": ArtifactExistanceEvent,
            "class": DamageDestroy,
            "Artifact": "artifact",
            "Instrument": "instrument",
            "DamagerDestroyer": "agent",
        },
        "ArtifactExistence.ManufactureAssemble.Unspecified": {
            "coarse": ArtifactExistanceEvent,
            "class": ManufactureAssemble,
            "Artifact": "artifact",
            "Components": "components",
            "ManufacturerAssembler": "agent",
        },
        "Cognitive.IdentifyCategorize.Unspecified": {
            "coarse": CognitiveEvent,
            "class": IdentifyCategorize,
            "IdentifiedObject": "object",
            "IdentifiedRole": "role",
            "Identifier": "agent",
        },
        "Cognitive.Inspection.SensoryObserve": {
            "coarse": CognitiveEvent,
            "class": Inspection,
            "Instrument": "instrument",
            "ObservedEntity": "entity",
            "Observer": "agent",
        },
        "Cognitive.Research.Unspecified": {
            "coarse": CognitiveEvent,
            "class": Research,
            "Researcher": "agent",
            "Subject": "subject",
        },
        "Cognitive.TeachingTrainingLearning.Unspecified": {
            "coarse": CognitiveEvent,
            "class": TeachingTrainingLearning,
            "Learner": "patient",
            "TeacherTrainer": "agent",
        },
        "Conflict.Attack.DetonateExplode": {
            "coarse": ConflictEvent,
            "class": Attack,
            "Attacker": "agent",
            "ExplosiveDevice": "explosive_device",
            "Instrument": "instrument",
            "Target": "target",
        },
        "Conflict.Attack.Unspecified": {
            "coarse": ConflictEvent,
            "class": Attack,
            "Attacker": "agent",
            "Instrument": "instrument",
            "Target": "target",
        },
        "Conflict.Defeat.Unspecified": {
            "coarse": ConflictEvent,
            "class": Defeat,
            "Defeated": "defeated",
            "Victor": "victor",
        },
        "Conflict.Demonstrate.DemonstrateWithViolence": {
            "coarse": ConflictEvent,
            "class": Demonstrate,
            "Demonstrator": "demonstrator",
            "Regulator": "Regulator",
        },
        "Conflict.Demonstrate.Unspecified": {
            "coarse": ConflictEvent,
            "class": Demonstrate,
            "Demonstrator": "demonstrator",
            "Target": "target",
            "Topic": "topic",
        },
        "Contact.Contact.Broadcast": {
            "coarse": ContactEvent,
            "class": Contact,
            "Communicator": "participants",
            "Instrument": "instrument",
            "Recipient": "participants",
            "Topic": "topic",
        },
        "Contact.Contact.Correspondence": {
            "coarse": ContactEvent,
            "class": Contact,
            "Participant": "participants",
            "Topic": "topic",
        },
        "Contact.Contact.Meet": {
            "coarse": ContactEvent,
            "class": Contact,
            "Participant": "participants",
            "Topic": "topic",
        },
        "Contact.Contact.Unspecified": {
            "coarse": ContactEvent,
            "class": Contact,
            "Participant": "participants",
            "Topic": "topic",
        },
        "Contact.RequestCommand.Broadcast": {
            "coarse": ContactEvent,
            "class": RequestCommand,
            "Communicator": "communicator",
            "Recipient": "receptor",
            "Topic": "topic",
        },
        "Contact.RequestCommand.Correspondence": {
            "coarse": ContactEvent,
            "class": RequestCommand,
            "Communicator": "communicator",
            "Recipient": "receptor",
            "Topic": "topic",
        },
        "Contact.RequestCommand.Meet": {
            "coarse": ContactEvent,
            "class": RequestCommand,
            "Communicator": "communicator",
            "Recipient": "receptor",
            "Topic": "topic",
        },
        "Contact.RequestCommand.Unspecified": {
            "coarse": ContactEvent,
            "class": RequestCommand,
            "Communicator": "communicator",
            "Recipient": "receptor",
            "Topic": "topic",
        },
        "Contact.ThreatenCoerce.Broadcast": {
            "coarse": ContactEvent,
            "class": ThreatenCoerce,
            "Communicator": "communicator",
            "Recipient": "recipient",
        },
        "Contact.ThreatenCoerce.Correspondence": {
            "coarse": ContactEvent,
            "class": ThreatenCoerce,
            "Communicator": "communicator",
            "Recipient": "recipient",
        },
        "Contact.ThreatenCoerce.Unspecified": {
            "coarse": ContactEvent,
            "class": ThreatenCoerce,
            "Communicator": "communicator",
            "Recipient": "recipient",
        },
        "Control.ImpedeInterfereWith.Unspecified": {
            "coarse": ControlEvent,
            "class": ImpedeInterfereWith,
            "Impeder": "impeder",
        },
        "Disaster.Crash.Unspecified": {
            "coarse": DisasterEvent,
            "class": Crash,
            "CrashObject": "object",
            "Vehicle": "vehicle",
        },
        "Disaster.DiseaseOutbreak.Unspecified": {
            "coarse": DisasterEvent,
            "class": DiseaseOutbreak,
            "Disease": "disease",
            "Victim": "victim",
        },
        "GenericCrime.GenericCrime.GenericCrime": {
            "coarse": GenericCrimeEvent,
            "class": GenericCrime,
            "Perpetrator": "perpetrator",
            "Victim": "victim",
        },
        "Justice.Acquit.Unspecified": {"coarse": JusticeEvent, "class": Acquit, "Defendant": "defendant"},
        "Justice.ArrestJailDetain.Unspecified": {
            "coarse": JusticeEvent,
            "class": ArrestJailDetain,
            "Detainee": "detainee",
            "Jailer": "jailer",
        },
        "Justice.ChargeIndict.Unspecified": {
            "coarse": JusticeEvent,
            "class": ChargeIndict,
            "Defendant": "defendant",
            "JudgeCourt": "judge_court",
            "Prosecutor": "prosecutor",
        },
        "Justice.Convict.Unspecified": {
            "coarse": JusticeEvent,
            "class": Convict,
            "Defendant": "defendant",
            "JudgeCourt": "judge_court",
        },
        "Justice.InvestigateCrime.Unspecified": {
            "coarse": JusticeEvent,
            "class": InvestigateCrime,
            "Defendant": "defendant",
            "Investigator": "investigator",
            "ObservedEntity": "crime",
            "Observer": "investigator",
        },
        "Justice.ReleaseParole.Unspecified": {
            "coarse": JusticeEvent,
            "class": ReleaseParole,
            "Defendant": "defendant",
            "JudgeCourt": "judge_court",
        },
        "Justice.Sentence.Unspecified": {
            "coarse": JusticeEvent,
            "class": Sentence,
            "Defendant": "defendant",
            "JudgeCourt": "judge_court",
        },
        "Justice.TrialHearing.Unspecified": {
            "coarse": JusticeEvent,
            "class": TrialHearing,
            "Defendant": "defendant",
            "JudgeCourt": "judge_court",
            "Prosecutor": "prosecutor",
        },
        "Life.Die.Unspecified": {
            "coarse": LifeEvent,
            "class": Die,
            "Killer": "killer",
            "Victim": "victim",
        },
        "Life.Infect.Unspecified": {"coarse": LifeEvent, "class": Infect, "Victim": "victim"},
        "Life.Injure.Unspecified": {
            "coarse": LifeEvent,
            "class": Injure,
            "BodyPart": "body_part",
            "Injurer": "injurer",
            "Instrument": "instrument",
            "Victim": "victim",
        },
        "Medical.Intervention.Unspecified": {
            "coarse": MedicalEvent,
            "class": Intervention,
            "Patient": "patient",
            "Treater": "treater",
        },
        "Movement.Transportation.Evacuation": {
            "coarse": MovementTransportEvent,
            "class": Evacuation,
            "Destination": "destination",
            "Origin": "origin",
            "PassengerArtifact": "passenger_artifact",
            "Transporter": "transporter",
        },
        "Movement.Transportation.IllegalTransportation": {
            "coarse": MovementTransportEvent,
            "class": IllegalTransportation,
            "Destination": "destination",
            "PassengerArtifact": "passenger_artifact",
            "Transporter": "transporter",
            "Vehicle": "vehicle",
        },
        "Movement.Transportation.PreventPassage": {
            "coarse": MovementTransportEvent,
            "class": PreventPassage,
            "Destination": "destination",
            "Origin": "origin",
            "PassengerArtifact": "passenger_artifact",
            "Preventer": "preventer",
            "Transporter": "transporter",
            "Vehicle": "vehicle",
        },
        "Movement.Transportation.Unspecified": {
            "coarse": MovementTransportEvent,
            "class": Transportation,
            "Destination": "destination",
            "Origin": "origin",
            "PassengerArtifact": "passenger_artifact",
            "Transporter": "transporter",
            "Vehicle": "vehicle",
        },
        "Personnel.EndPosition.Unspecified": {
            "coarse": PersonnelEvent,
            "class": EndPosition,
            "Employee": "employee",
            "PlaceOfEmployment": "organization",
        },
        "Personnel.StartPosition.Unspecified": {
            "coarse": PersonnelEvent,
            "class": StartPosition,
            "Employee": "employee",
            "PlaceOfEmployment": "organization",
            "Position": "position",
        },
        "Transaction.Donation.Unspecified": {
            "coarse": TransactionEvent,
            "class": Donation,
            "ArtifactMoney": "artifact_money",
            "Giver": "giver",
            "Recipient": "recipient",
        },
        "Transaction.ExchangeBuySell.Unspecified": {
            "coarse": TransactionEvent,
            "class": ExchangeBuySell,
            "AcquiredEntity": "adquired_entity",
            "Giver": "giver",
            "PaymentBarter": "payment_barter",
            "Recipient": "recipient",
        },
    }

    def __init__(self, path: str, group_by: str = "sentence", **kwargs) -> None:
        assert group_by in [
            "sentence",
            "document",
        ], "`group_by` must be either 'sentence' or 'document'."

        self.elements = {}

        with open(path, "rt", encoding="utf-8") as in_f:
            for line in in_f:
                line = json.loads(line.strip())

                sent_id = line["doc_id"]
                doc_id = "_".join(sent_id.split("_")[:-1])
                key = doc_id if group_by == "document" else sent_id
                if key not in self.elements:
                    self.elements[key] = {
                        "id": key,
                        "doc_id": doc_id,
                        "text": "",
                        "entities": [],
                        "events": [],
                        "arguments": [],
                        "gold": [],
                    }

                entities = [
                    self.ENTITY_TO_CLASS_MAPPING[entity["entity_type"]](span=entity["text"])
                    for entity in line["entity_mentions"]
                    if entity["entity_type"] in self.ENTITY_TO_CLASS_MAPPING
                ]

                events, arguments = [], []
                for event in line["event_mentions"]:
                    if event["event_type"] not in self.EVENT_TO_CLASS_MAPPING:
                        continue
                    info = self.EVENT_TO_CLASS_MAPPING[event["event_type"]]
                    _inst = {param: [] for param in inspect.signature(info["class"]).parameters.keys()}
                    _inst["mention"] = event["trigger"]["text"]
                    for argument in event["arguments"]:
                        if "OOR" in argument["role"]:
                            continue
                        elif argument["role"] in info:
                            name = info[argument["role"]]
                            _inst[name].append(argument["text"])
                        elif argument["role"] in self._EVENT_CONSTANTS_MAPPING:
                            name = self._EVENT_CONSTANTS_MAPPING[argument["role"]]
                            if name not in _inst:
                                continue
                            _inst[name].append(argument["text"])
                        else:
                            raise ValueError(f"Argument {event['event_type']}:{argument['role']} not found!")

                    events.append(info["coarse"](mention=_inst["mention"]))
                    arguments.append(info["class"](**_inst))

                self.elements[key]["text"] += " " + line["text"].strip()
                self.elements[key]["entities"] += entities
                self.elements[key]["events"] += events
                self.elements[key]["arguments"] += arguments
                self.elements[key]["gold"] += entities  # Is not used anyway

