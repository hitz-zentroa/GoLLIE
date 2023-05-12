import inspect
import json
from typing import Tuple, Union

from src.tasks.rams.guidelines import GUIDELINES
from src.tasks.rams.prompts import (
    EVENT_DEFINITIONS,
    AccidentCrash,
    Agreement,
    ArrestJailDetain,
    ArtifactFailure,
    Attack,
    Collaborate,
    CommandOrder,
    CommitmentPromiseExpressIntent,
    Convene,
    Coup,
    DamageDestroy,
    Demonstrate,
    Die,
    Discussion,
    DiseaseOutbreak,
    Elect,
    EndPossition,
    FireExplosion,
    Formation,
    FuneralVigil,
    GenericCrime,
    InitiateJudicialProcess,
    Injure,
    InvestigateCrime,
    JudicialConsequences,
    Legislate,
    ManufactureArtifact,
    MediaStatement,
    MedicalIntervention,
    Negotiate,
    Prevarication,
    PublicStatementInPerson,
    RequestAdvice,
    SensoryObserve,
    Shortage,
    Spy,
    StartPossition,
    TargetAimAt,
    ThreatenCoerce,
    Transaction,
    TransferMoney,
    TransferOwnership,
    TransportArtifact,
    TransportPerson,
    Vote,
    Yield,
)

from ..utils_data import DatasetLoader, Sampler


class RAMSDatasetLoader(DatasetLoader):
    """
    A `DatasetLoader` for the RAMS dataset.

    Args:
        path (`str`):
            The location of the dataset directory.

    Raises:
        `ValueError`:
            raised when a not defined value found.
    """

    _EVENT_CONSTANTS_MAPPING = {"n/a": None, "place": "place"}
    EVENT_TO_CLASS_MAPPING = {
        "artifactexistence.artifactfailure": {
            "class": ArtifactFailure,
            "subtypes": {"mechanicalfailure": "MechanicalFailure"},
            "mechanicalartifact": "artifact",
            "instrument": "instrument",
        },
        "artifactexistence.damagedestroy": {
            "class": DamageDestroy,
            "subtypes": {"damage": "Damage", "destroy": "Destroy"},
            "damagerdestroyer": "agent",
            "damager": "agent",
            "destroyer": "agent",
            "artifact": "artifact",
            "instrument": "instrument",
        },
        "artifactexistence.shortage": {
            "class": Shortage,
            "subtypes": {"shortage": "Shortage"},
            "experiencer": "experiencer",
            "supply": "supply",
        },
        "conflict.attack": {
            "class": Attack,
            "subtypes": {
                "airstrikemissilestrike": "AirStrikeMissileStrike",
                "biologicalchemicalpoisonattack": "BiologicalChemicalPoisonAttack",
                "bombing": "Bombing",
                "firearmattack": "FireArmAttack",
                "hanging": "Hanging",
                "invade": "Invade",
                "selfdirectedbattle": "SelfDirectedBattle",
                "setfire": "SetFire",
                "stabbing": "Stabbing",
                "stealrobhijack": "StealRobHijack",
                "strangling": "Strangling",
            },
            "attacker": "attacker",
            "target": "target",
            "instrument": "instrument",
            "artifact": "artifact",
        },
        "conflict.coup": {
            "class": Coup,
            "subtypes": {"coup": "Coup"},
            "deposedentity": "deposed_entity",
            "deposingentity": "deposing_entity",
        },
        "conflict.demonstrate": {
            "class": Demonstrate,
            "subtypes": {"marchprotestpoliticalgathering": "MarchProtestPoliticalGathering"},
            "demonstrator": "demonstrator",
        },
        "conflict.yield": {
            "class": Yield,
            "subtypes": {"retreat": "Retreat", "surrender": "Surrender"},
            "yielder": "agent",
            "retreater": "agent",
            "surrenderer": "agent",
            "recipient": "recipient",
            "origin": "origin",
            "destination": "destination",
        },
        "contact.collaborate": {
            "class": Collaborate,
            "subtypes": {"correspondence": "Correspondence", "meet": "Meet"},
            "participant": "participants",
        },
        "contact.commandorder": {
            "class": CommandOrder,
            "subtypes": {
                "broadcast": "Broadcast",
                "correspondence": "Correspondence",
                "meet": "Meet",
            },
            "communicator": "communicator",
            "recipient": "recipient",
            "topic": "topic",
        },
        "contact.commitmentpromiseexpressintent": {
            "class": CommitmentPromiseExpressIntent,
            "subtypes": {
                "broadcast": "Broadcast",
                "correspondence": "Correspondence",
                "meet": "Meet",
            },
            "communicator": "communicator",
            "recipient": "recipient",
            "topic": "topic",
        },
        "contact.discussion": {
            "class": Discussion,
            "subtypes": {"correspondence": "Correspondence", "meet": "Meet"},
            "participant": "participants",
        },
        "contact.funeralvigil": {
            "class": FuneralVigil,
            "subtypes": {"meet": "Meet"},
            "participant": "participants",
            "deceased": "deceased",
        },
        "contact.mediastatement": {
            "class": MediaStatement,
            "subtypes": {"broadcast": "Broadcast"},
            "communicator": "communicator",
            "recipient": "recipient",
        },
        "contact.negotiate": {
            "class": Negotiate,
            "subtypes": {"correspondence": "Correspondence", "meet": "Meet"},
            "participant": "participants",
            "topic": "topic",
        },
        "contact.prevarication": {
            "class": Prevarication,
            "subtypes": {
                "broadcast": "Broadcast",
                "correspondence": "Correspondence",
                "meet": "Meet",
            },
            "communicator": "communicator",
            "recipient": "recipient",
            "topic": "topic",
        },
        "contact.publicstatementinperson": {
            "class": PublicStatementInPerson,
            "subtypes": {"broadcast": "Broadcast"},
            "communicator": "communicator",
            "recipient": "recipient",
        },
        "contact.requestadvise": {
            "class": RequestAdvice,
            "subtypes": {
                "broadcast": "Broadcast",
                "correspondence": "Correspondence",
                "meet": "Meet",
            },
            "communicator": "communicator",
            "recipient": "recipient",
            "topic": "topic",
        },
        "contact.threatencoerce": {
            "class": ThreatenCoerce,
            "subtypes": {
                "broadcast": "Broadcast",
                "correspondence": "Correspondence",
                "meet": "Meet",
            },
            "communicator": "communicator",
            "recipient": "recipient",
            "topic": "topic",
        },
        "disaster.accidentcrash": {
            "class": AccidentCrash,
            "subtypes": {"accidentcrash": "AccidentCrash"},
            "driverpassenger": "driver_or_passengers",
            "vehicle": "vehicle",
            "crashobject": "crash_object",
        },
        "disaster.diseaseoutbreak": {
            "class": DiseaseOutbreak,
            "subtypes": {"diseaseoutbreak": "DiseaseOutbreak"},
            "disease": "disease",
            "victim": "victim",
        },
        "disaster.fireexplosion": {
            "class": FireExplosion,
            "subtypes": {"fireexplosion": "FireExplosion"},
            "fireexplosionobject": "fire_explosion_object",
            "instrument": "instrument",
        },
        "genericcrime.genericcrime": {
            "class": GenericCrime,
            "subtypes": {"genericcrime": "GenericCrime"},
            "perpetrator": "perpetrator",
            "victim": "victim",
        },
        "government.agreements": {
            "class": Agreement,
            "subtypes": {
                "acceptagreementcontractceasefire": "Accept",
                "rejectnullifyagreementcontractceasefire": "RejectNullify",
                "violateagreement": "Violate",
            },
            "participant": "participants",
            "rejecternullifier": "rejecter_nullifier",
            "violator": "violator",
            "otherparticipant": "other_participant",
        },
        "government.convene": {
            "class": Convene,
            "subtypes": {"convene": "Convene"},
            "convener": "convener",
            "convenedthing": "convened_entity",
        },
        "government.formation": {
            "class": Formation,
            "subtypes": {"mergegpe": "Merge", "startgpe": "Start"},
            "gpe": "gpe",
            "founder": "founder",
            "participant": "participants",
        },
        "government.legislate": {
            "class": Legislate,
            "subtypes": {"legislate": "Legislate"},
            "governmentbody": "government_body",
            "law": "law",
        },
        "government.spy": {
            "class": Spy,
            "subtypes": {"spy": "Spy"},
            "spy": "spy",
            "observedentity": "observed_entity",
            "beneficiary": "beneficiary",
        },
        "government.vote": {
            "class": Vote,
            "subtypes": {"castvote": "CastVote", "violationspreventvote": "PreventVote"},
            "voter": "voter",
            "candidate": "candidate",
            "ballot": "ballot",
            "result": "result",
            "preventer": "preventer",
        },
        "inspection.sensoryobserve": {
            "class": SensoryObserve,
            "subtypes": {
                "inspectpeopleorganization": "InspectPeopleOrganization",
                "monitorelection": "MonitorElection",
                "physicalinvestigateinspect": "PhysicalInvestigateInspect",
            },
            "observer": "observer",
            "observedentity": "observed_entity",
            "monitor": "observer",
            "monitoredentity": "observed_entity",
            "inspector": "observer",
            "inspectedentity": "observed_entity",
        },
        "inspection.targetaimat": {
            "class": TargetAimAt,
            "subtypes": {"targetaimat": "TargetAimAt"},
            "targeter": "targeter",
            "target": "target",
            "instrument": "instrument",
        },
        "justice.arrestjaildetain": {
            "class": ArrestJailDetain,
            "subtypes": {"arrestjaildetain": "ArrestJailDetain"},
            "jailer": "jailer",
            "detainee": "detainee",
            "crime": "crime",
        },
        "justice.initiatejudicialprocess": {
            "class": InitiateJudicialProcess,
            "subtypes": {"chargeindict": "ChargeIndict", "trialhearing": "TrialHearing"},
            "prosecutor": "prosecutor",
            "defendant": "defendant",
            "judgecourt": "judge_court",
            "crime": "crime",
        },
        "justice.investigate": {
            "class": InvestigateCrime,
            "subtypes": {"investigatecrime": "InvestigateCrime"},
            "investigator": "investigator",
            "defendant": "defendant",
            "crime": "crime",
        },
        "justice.judicialconsequences": {
            "class": JudicialConsequences,
            "subtypes": {
                "convict": "Convict",
                "execute": "Execute",
                "extradite": "Extradite",
            },
            "judgecourt": "judge_court",
            "defendant": "defendant",
            "crime": "crime",
            "executioner": "judge_court",
            "extraditer": "judge_court",
            "origin": "origin",
            "destination": "destination",
        },
        "life.die": {
            "class": Die,
            "subtypes": {
                "deathcausedbyviolentevents": "Violent",
                "nonviolentdeath": "NonViolent",
            },
            "victim": "victim",
            "killer": "killer",
            "medicalissue": "medical_issue",
            "instrument": "instrument",
        },
        "life.injure": {
            "class": Injure,
            "subtypes": {
                "illnessdegradationhungerthirst": "HungerThirst",
                "illnessdegradationphysical": "Physical",
                "illnessdegredationsickness": "Sickness",
                "injurycausedbyviolentevents": "Violent",
            },
            "victim": "victim",
            "injurer": "injurer",
            "medicalissue": "medical_issue",
            "disease": "disease",
            "instrument": "instrument",
        },
        "manufacture.artifact": {
            "class": ManufactureArtifact,
            "subtypes": {
                "build": "Build",
                "createintellectualproperty": "IntellectualProperty",
                "createmanufacture": "CreateManufacture",
            },
            "manufacturer": "manufacturer",
            "artifact": "artifact",
            "instrument": "instrument",
        },
        "medical.intervention": {
            "class": MedicalIntervention,
            "subtypes": {"intervention": "Intervention"},
            "treater": "treater",
            "patient": "patient",
            "medicalissue": "medical_issue",
            "instrument": "instrument",
        },
        "movement.transportartifact": {
            "class": TransportArtifact,
            "subtypes": {
                "bringcarryunload": "BringCarryUnload",
                "disperseseparate": "DisperseSeparate",
                "fall": "Fall",
                "grantentry": "GrantEntry",
                "hide": "Hide",
                "lossofcontrol": "LostOfControl",
                "nonviolentthrowlaunch": "NonViolentThrowLaunch",
                "prevententry": "PreventEntry",
                "preventexit": "PreventExit",
                "receiveimport": "ReceiveImport",
                "sendsupplyexport": "SendSupplyExport",
                "smuggleextract": "SmuggleExtract",
            },
            "transporter": "transporter",
            "artifact": "artifact",
            "vehicle": "vehicle",
            "origin": "origin",
            "destination": "destination",
            "hidingplace": "hidding_place",
            "controller": "transporter",
            "controlledthing": "artifact",
            "preventer": "preventer",
        },
        "movement.transportperson": {
            "class": TransportPerson,
            "subtypes": {
                "bringcarryunload": "BringCarryUnload",
                "disperseseparate": "DisperseSeparate",
                "evacuationrescue": "EvacuationRescue",
                "fall": "Fall",
                "grantentryasylum": "GrantedAsylum",
                "hide": "Hide",
                "prevententry": "PreventEntry",
                "preventexit": "PreventExit",
                "selfmotion": "SelfMotion",
                "smuggleextract": "SmuggleExtract",
            },
            "transporter": "transporter",
            "passenger": "passenger",
            "vehicle": "vehicle",
            "origin": "origin",
            "destination": "destination",
            "granter": "granter",
            "hidingplace": "hidding_place",
            "preventer": "preventer",
        },
        "personnel.elect": {
            "class": Elect,
            "subtypes": {"winelection": "WinElection"},
            "voter": "voter",
            "candidate": "candidate",
        },
        "personnel.endposition": {
            "class": EndPossition,
            "subtypes": {"firinglayoff": "FiringLayOff", "quitretire": "QuitRetire"},
            "employee": "employee",
            "placeofemployment": "organization",
        },
        "personnel.startposition": {
            "class": StartPossition,
            "subtypes": {"hiring": "Hiring"},
            "employee": "employee",
            "placeofemployment": "organization",
        },
        "transaction.transaction": {
            "class": Transaction,
            "subtypes": {
                "embargosanction": "EmbargoSanction",
                "giftgrantprovideaid": "GiftGrantProvideAid",
                "transfercontrol": "TransferControl",
            },
            "participant": "participants",
            "beneficiary": "beneficiary",
            "preventer": "preventer",
            "giver": "giver",
            "recipient": "recipient",
            "artifactmoney": "artifact",
            "territoryorfacility": "artifact",
        },
        "transaction.transfermoney": {
            "class": TransferMoney,
            "subtypes": {
                "borrowlend": "BorrowLend",
                "embargosanction": "EmbargoSanction",
                "giftgrantprovideaid": "GiftGrantProvideAid",
                "payforservice": "PayForService",
                "purchase": "Purchase",
            },
            "giver": "giver",
            "recipient": "recipient",
            "beneficiary": "beneficiary",
            "money": "money",
            "preventer": "preventer",
        },
        "transaction.transferownership": {
            "class": TransferOwnership,
            "subtypes": {
                "borrowlend": "BorrowLend",
                "embargosanction": "EmbargoSanction",
                "giftgrantprovideaid": "GiftGrantProvideAid",
                "purchase": "Purchase",
            },
            "giver": "giver",
            "recipient": "recipient",
            "beneficiary": "beneficiary",
            "artifact": "artifact",
            "preventer": "preventer",
        },
    }

    def __init__(self, path: str, **kwargs) -> None:
        self.elements = {}

        with open(path, "rt") as in_f:
            for line in in_f:
                line = json.loads(line.strip())
                key = line["doc_key"]
                tokens = [token for sentence in line["sentences"] for token in sentence]
                text = " ".join(tokens)
                events = []
                for event in line["evt_triggers"]:
                    trigger_start, trigger_end = event[:2]
                    event_type = event[-1][0][0].split(".")
                    _event_full_type = ".".join(event_type[:2])

                    info = self.EVENT_TO_CLASS_MAPPING[_event_full_type]
                    _inst = {param: [] for param in inspect.signature(info["class"]).parameters.keys()}
                    _inst["mention"] = " ".join(tokens[trigger_start : trigger_end + 1])

                    # Find the correct event subtype
                    if event_type[-1] in info["subtypes"]:
                        value = info["subtypes"][event_type[-1]]
                    elif event_type[-1] in self._EVENT_CONSTANTS_MAPPING:
                        value = self._EVENT_CONSTANTS_MAPPING[event_type[-1]]
                    else:
                        raise ValueError(f"Event subtype {event_type[-1]} not found!")
                    _inst["subtype"] = value

                    # Find the arguments of the event
                    for argument in line["gold_evt_links"]:
                        if argument[0] != [trigger_start, trigger_end]:
                            continue

                        arg_text = " ".join(tokens[argument[1][0] : argument[1][1] + 1])
                        role = argument[-1][11:]
                        if role in info:
                            value = info[role]
                        elif role in self._EVENT_CONSTANTS_MAPPING:
                            value = self._EVENT_CONSTANTS_MAPPING[role]
                        else:
                            raise ValueError(f"Argument {event_type}:{role} not found!")

                        try:
                            _inst[value].append(arg_text)
                        except KeyError:
                            raise KeyError(f"{event_type}-{value}")

                    events.append(info["class"](**_inst))

                self.elements[key] = {"id": key, "doc_id": key, "text": text, "labels": events, "gold": events}


class RAMSSampler(Sampler):
    """
    A data `Sampler` for the RAMS dataset.

    Args:
        dataset_loader (`RAMSDatasetLoader`):
            The dataset loader that contains the data information.
        task (`str`, optional):
            The task to sample. It can only be EAE. Defaults to `"EAE"`.
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
            The path to the prompt template. Defaults to `"templates/prompt_eae.txt"`.
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
        dataset_loader: RAMSDatasetLoader,
        task: str = "EAE",
        split: str = "train",
        parallel_instances: Union[int, Tuple[int, int]] = 1,
        max_guidelines: int = -1,
        guideline_dropout: float = 0.0,
        seed: float = 0,
        prompt_template: str = "templates/prompt_eae.txt",
        ensure_positives_on_train: bool = True,
        dataset_name: str = None,
        scorer: str = None,
        sample_only_gold_guidelines: bool = True,
        **kwargs,
    ) -> None:
        assert task in [
            "EAE",
        ], f"{task} must be 'EAE'."

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
            task_definitions=EVENT_DEFINITIONS,
            task_target="labels",
            definitions=GUIDELINES,
            **kwargs,
        )
