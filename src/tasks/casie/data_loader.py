import inspect
import json
from typing import Tuple, Union

from src.tasks.casie.guidelines import GUIDELINES
from src.tasks.casie.guidelines_gold import EXAMPLES
from src.tasks.casie.prompts_eae import (
    EAE_EVENT_DEFINITIONS,
)
from src.tasks.casie.prompts_eae import (
    DatabreachAttack as EAEDatabreachAttack,
)
from src.tasks.casie.prompts_eae import PhisingAttack as EAEPhisingAttack
from src.tasks.casie.prompts_eae import RansomAttack as EAERansomAttack
from src.tasks.casie.prompts_eae import (
    VulnerabilityDiscover as EAEVulnerabilityDiscover,
)
from src.tasks.casie.prompts_eae import (
    VulnerabilityPatch as EAEVulnerabilityPatch,
)
from src.tasks.casie.prompts_ed import (
    ED_EVENT_DEFINITIONS,
    DatabreachAttack,
    PhisingAttack,
    RansomAttack,
    VulnerabilityDiscover,
    VulnerabilityPatch,
)
from src.tasks.utils_data import DatasetLoader, Sampler


class CASIEDatasetLoader(DatasetLoader):
    _EVENT_CONSTANTS_MAPPING = {
        "trigger": "mention",
        "Time": "time",
        "Place": "place",
        "Attacker": "attacker",
        "Tool": "tool",
        "Victim": "victim",
        "Damage-Amount": "damage_amount",
        "Vulnerability": "vulnerability",
        "Vulnerable_System": "vulnerable_system",
        "Vulnerable_System_Owner": "system_owner",
        "Vulnerable_System_Version": "system_version",
        "Supported_Platform": "supported_platform",
    }
    EVENT_TO_CLASS_MAPPING = {
        "Attack:Databreach": {
            "ed_class": DatabreachAttack,
            "eae_class": EAEDatabreachAttack,
            "Attack-Pattern": "attack_pattern",
            "Compromised-Data": "compromised_data",
            "Number-of-Data": "number_of_data",
            "Number-of-Victim": "number_of_victim",
            "Purpose": "purpose",
        },
        "Attack:Phising": {
            "ed_class": PhisingAttack,
            "eae_class": EAEPhisingAttack,
            "Attack-Pattern": "pattern",
            "Purpose": "purpose",
            "Trusted-Entity": "trusted_entity",
        },
        "Attack:Ransom": {
            "ed_class": RansomAttack,
            "eae_class": EAERansomAttack,
            "Attack-Pattern": "pattern",
            "Payment-Method": "payment_method",
            "Price": "price",
        },
        "Vulnerability:Discover": {
            "ed_class": VulnerabilityDiscover,
            "eae_class": EAEVulnerabilityDiscover,
            "CVE": "cve",
            "Capabilities": "used_for",
            "Discoverer": "discoverer",
            "Supported_Platform": "supported_platform",
        },
        "Vulnerability:Patch": {
            "ed_class": VulnerabilityPatch,
            "eae_class": EAEVulnerabilityPatch,
            "CVE": "cve",
            "Issues-Addressed": "issues_addressed",
            "Patch": "patch",
            "Patch-Number": "patch_number",
            "Releaser": "releaser",
        },
    }

    def __init__(self, path: str, **kwargs) -> None:
        self.elements = {}

        with open(path, "rt") as in_f:
            for line in in_f:
                line = json.loads(line.strip())

                key = line["sent_id"]
                if key not in self.elements:
                    self.elements[key] = {
                        "id": key,
                        "doc_id": key.split(":")[0],
                        "text": "",
                        "events": [],
                        "arguments": [],
                        "gold": [],
                    }

                events, arguments = [], []
                for event in sorted(line["events"], key=lambda x: x["trigger"]["start"]):
                    if event["type"] not in self.EVENT_TO_CLASS_MAPPING:
                        continue
                    info = self.EVENT_TO_CLASS_MAPPING[event["type"]]
                    _inst = {param: [] for param in inspect.signature(info["eae_class"]).parameters.keys()}
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
                            raise ValueError(f"Argument {event['type']}:{argument['role']} not found!")

                    events.append(info["ed_class"](mention=_inst["mention"]))
                    arguments.append(info["eae_class"](**_inst))

                self.elements[key]["text"] += " " + line["text"].strip()
                self.elements[key]["events"] += events
                self.elements[key]["arguments"] += arguments
                self.elements[key]["gold"] += events


class CASIESampler(Sampler):
    """
    A data `Sampler` for the CASIE dataset.

    Args:
        dataset_loader (`CASIEDatasetLoader`):
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
            Defaults to `False`.
        dataset_name (str, optional):
            The name of the dataset. Defaults to `None`.
        scorer (`str`, optional):
           The scorer class import string. Defaults to `None`.
        sample_only_gold_guidelines (`bool`, optional):
            Whether to sample only guidelines of present annotations. Defaults to `False`.
    """

    def __init__(
        self,
        dataset_loader: CASIEDatasetLoader,
        task: str = None,
        split: str = "train",
        parallel_instances: Union[int, Tuple[int, int]] = 1,
        max_guidelines: int = -1,
        guideline_dropout: float = 0.0,
        seed: float = 0,
        ensure_positives_on_train: bool = False,
        dataset_name: str = None,
        scorer: str = None,
        sample_only_gold_guidelines: bool = False,
        **kwargs,
    ) -> None:
        assert task in [
            "EE",
            "EAE",
        ], f"{task} must be either 'EE', 'EAE'."

        task_definitions, task_target, task_template = {
            "EE": (ED_EVENT_DEFINITIONS, "events", "templates/prompt.txt"),
            "EAE": (EAE_EVENT_DEFINITIONS, "arguments", "templates/prompt_ace_eae.txt"),
        }[task]

        kwargs.pop("prompt_template")

        super().__init__(
            dataset_loader=dataset_loader,
            task=task,
            split=split,
            parallel_instances=parallel_instances,
            max_guidelines=max_guidelines,
            guideline_dropout=guideline_dropout,
            seed=seed,
            prompt_template=task_template,
            ensure_positives_on_train=ensure_positives_on_train,
            sample_only_gold_guidelines=sample_only_gold_guidelines,
            dataset_name=dataset_name,
            scorer=scorer,
            task_definitions=task_definitions,
            task_target=task_target,
            is_coarse_to_fine=False,
            coarse_to_fine=None,
            fine_to_coarse=None,
            definitions=GUIDELINES,
            examples=EXAMPLES,
            **kwargs,
        )
