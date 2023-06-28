import json
from collections import defaultdict
from typing import Tuple, Union

import rich

from src.tasks.tacred.guidelines import GUIDELINES
from src.tasks.tacred.prompts import TEMPLATE_DEFINITIONS, OrganizationTemplate, PersonTemplate

from ..utils_data import DatasetLoader, Sampler
from ..utils_typing import Relation, Template, dataclass


@dataclass
class NoneRelation(Relation):
    arg1: str
    arg2: str


class TACREDDatasetLoader(DatasetLoader):
    """
    A `DatasetLoader` for the TACRED dataset.

    Args:
        path (`str`):
            The location of the dataset directory.

    Raises:
        `ValueError`:
            raised when a not defined value found.
    """

    TEMPLATE_TO_CLASS_MAPPING = {
        "PERSON": {
            "class": PersonTemplate,
            "per:alternate_names": "alternate_names",
            "per:date_of_birth": "date_of_birth",
            "per:age": "age",
            "per:country_of_birth": "country_of_birth",
            "per:stateorprovince_of_birth": "state_or_province_of_birth",
            "per:city_of_birth": "city_of_birth",
            "per:origin": "origin",
            "per:date_of_death": "date_of_death",
            "per:country_of_death": "country_of_death",
            "per:stateorprovince_of_death": "state_or_province_of_death",
            "per:city_of_death": "city_of_death",
            "per:cause_of_death": "cause_of_death",
            "per:countries_of_residence": "countries_of_residence",
            "per:stateorprovinces_of_residence": "states_or_provinces_of_residence",
            "per:cities_of_residence": "cities_of_residence",
            "per:schools_attended": "schools_attended",
            "per:title": "title",
            "per:employee_of": "employee_or_member_of",
            "per:religion": "religion",
            "per:spouse": "spouse",
            "per:children": "children",
            "per:parents": "parents",
            "per:siblings": "siblings",
            "per:other_family": "other_family",
            "per:charges": "charges",
        },
        "ORGANIZATION": {
            "class": OrganizationTemplate,
            "org:alternate_names": "alternate_names",
            "org:political/religious_affiliation": "political_or_religious_affiliation",
            "org:top_members/employees": "top_members_employees",
            "org:number_of_employees/members": "number_of_employees_members",
            "org:members": "members",
            "org:member_of": "member_of",
            "org:subsidiaries": "subsidiaries",
            "org:parents": "parents",
            "org:founded_by": "founded_by",
            "org:founded": "date_founded",
            "org:dissolved": "date_dissolved",
            "org:country_of_headquarters": "country_of_headquarters",
            "org:stateorprovince_of_headquarters": "state_or_province_of_headquarters",
            "org:city_of_headquarters": "city_of_headquarters",
            "per:cities_of_residence": "city_of_headquarters",  # Bug on data
            "org:shareholders": "shareholders",
            "org:website": "website",
        },
    }

    def __init__(self, path: str, **kwargs) -> None:
        self.elements = {}
        with open(path, "rt", encoding="utf-8") as in_f:
            data = json.load(in_f)

        data_by_sentence = defaultdict(list)
        for line in data:
            text = " ".join(line["token"])
            data_by_sentence[text].append(line)

        for text, instances in data_by_sentence.items():
            text = text.replace("-LRB-", "(").replace("-RRB-", ")").replace("-LSB-", "[").replace("-RSB-", "]")
            templates = {}
            for inst in instances:
                if inst["relation"] == "no_relation":
                    continue

                subj = (
                    " ".join(inst["token"][inst["subj_start"] : inst["subj_end"] + 1])
                    .replace("-LRB-", "(")
                    .replace("-RRB-", ")")
                    .replace("-LSB-", "[")
                    .replace("-RSB-", "]")
                )
                if f"{subj}-{inst['subj_type']}" not in templates:
                    _info = self.TEMPLATE_TO_CLASS_MAPPING[inst["subj_type"]]
                    templates[f"{subj}-{inst['subj_type']}"] = {"query": subj, "_info": _info}
                _info = templates[f"{subj}-{inst['subj_type']}"]["_info"]

                obj = (
                    " ".join(inst["token"][inst["obj_start"] : inst["obj_end"] + 1])
                    .replace("-LRB-", "(")
                    .replace("-RRB-", ")")
                    .replace("-LSB-", "[")
                    .replace("-RSB-", "]")
                )
                slot_name = _info[inst["relation"]]
                if slot_name not in templates[f"{subj}-{inst['subj_type']}"]:
                    templates[f"{subj}-{inst['subj_type']}"][slot_name] = []

                templates[f"{subj}-{inst['subj_type']}"][slot_name].append(obj)

            key = str(hash(text))
            labels, gold = [], []
            for temp in templates.values():
                _info = temp.pop("_info")
                try:
                    template: Template = _info["class"](**temp)
                except Exception as e:
                    rich.print(_info)
                    rich.print(temp)
                    raise e
                template.assert_typing_constraints()
                labels.append(template)
                gold.append(template.query)

            self.elements[key] = {
                "id": key,
                "doc_id": instances[0]["docid"],
                "text": text,
                "labels": labels,
                "gold": labels,
            }

        assert len(self.elements) == len(data_by_sentence), "The hash function failed."


class TACREDSampler(Sampler):
    """
    A data `Sampler` for the TACRED dataset.

    Args:
        dataset_loader (`TACREDDatasetLoader`):
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
        dataset_loader: TACREDDatasetLoader,
        task: str = None,
        split: str = "train",
        parallel_instances: Union[int, Tuple[int, int]] = 1,
        max_guidelines: int = -1,
        guideline_dropout: float = 0.0,
        seed: float = 0,
        prompt_template: str = "templates/prompt_tacred.txt",
        ensure_positives_on_train: bool = True,
        dataset_name: str = None,
        scorer: str = None,
        sample_only_gold_guidelines: bool = False,
        **kwargs,
    ) -> None:
        assert task in [
            "SF",
        ], f"{task} can only be 'SF'."

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
            task_definitions=TEMPLATE_DEFINITIONS,
            task_target="labels",
            definitions=GUIDELINES,
            **kwargs,
        )
