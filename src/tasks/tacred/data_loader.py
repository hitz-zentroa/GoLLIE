import json
from collections import defaultdict
from typing import Tuple, Union

from src.tasks.tacred.prompts import (
    RELATION_DEFINITIONS,
    OrganizationAlternateName,
    OrganizationCityOfHeadquarters,
    OrganizationCountryOfHeadquarters,
    OrganizationDateDissolved,
    OrganizationDateFounded,
    OrganizationFoundedBy,
    OrganizationMember,
    OrganizationMemberOf,
    OrganizationNumberOfEmployeesMembers,
    OrganizationParent,
    OrganizationPoliticalReligiousAffiliation,
    OrganizationShareholders,
    OrganizationStateOrProvinceOfHeadquarters,
    OrganizationSubsidiary,
    OrganizationTopMembersEmployees,
    OrganizationWebsite,
    PersonAge,
    PersonAlternateNames,
    PersonCauseOfDeath,
    PersonCharges,
    PersonChildren,
    PersonCityOfBirth,
    PersonCityOfDeath,
    PersonCityOfResidence,
    PersonCountryOfBirth,
    PersonCountryOfDeath,
    PersonCountryOfResidence,
    PersonDateOfBirth,
    PersonDateOfDeath,
    PersonEmployeeOrMemberOf,
    PersonOrigin,
    PersonOtherFamily,
    PersonParents,
    PersonReligion,
    PersonSchoolAttended,
    PersonSiblings,
    PersonSpouse,
    PersonStateOrProvinceOfBirth,
    PersonStateOrProvinceOfDeath,
    PersonStateOrProvinceOfResidence,
    PersonTitle,
)

from ..utils_data import DatasetLoader, Sampler
from ..utils_typing import Relation, dataclass
from src.tasks.tacred.guidelines import GUIDELINES


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

    RELATION_TO_CLASS_MAPPING = {
        "no_relation": NoneRelation,
        "org:alternate_names": OrganizationAlternateName,
        "org:city_of_headquarters": OrganizationCityOfHeadquarters,
        "org:country_of_headquarters": OrganizationCountryOfHeadquarters,
        "org:dissolved": OrganizationDateDissolved,
        "org:founded": OrganizationDateFounded,
        "org:founded_by": OrganizationFoundedBy,
        "org:member_of": OrganizationMemberOf,
        "org:members": OrganizationMember,
        "org:number_of_employees/members": OrganizationNumberOfEmployeesMembers,
        "org:parents": OrganizationParent,
        "org:political/religious_affiliation": OrganizationPoliticalReligiousAffiliation,
        "org:shareholders": OrganizationShareholders,
        "org:stateorprovince_of_headquarters": OrganizationStateOrProvinceOfHeadquarters,
        "org:subsidiaries": OrganizationSubsidiary,
        "org:top_members/employees": OrganizationTopMembersEmployees,
        "org:website": OrganizationWebsite,
        "per:age": PersonAge,
        "per:alternate_names": PersonAlternateNames,
        "per:cause_of_death": PersonCauseOfDeath,
        "per:charges": PersonCharges,
        "per:children": PersonChildren,
        "per:cities_of_residence": PersonCityOfResidence,
        "per:city_of_birth": PersonCityOfBirth,
        "per:city_of_death": PersonCityOfDeath,
        "per:countries_of_residence": PersonCountryOfResidence,
        "per:country_of_birth": PersonCountryOfBirth,
        "per:country_of_death": PersonCountryOfDeath,
        "per:date_of_birth": PersonDateOfBirth,
        "per:date_of_death": PersonDateOfDeath,
        "per:employee_of": PersonEmployeeOrMemberOf,
        "per:origin": PersonOrigin,
        "per:other_family": PersonOtherFamily,
        "per:parents": PersonParents,
        "per:religion": PersonReligion,
        "per:schools_attended": PersonSchoolAttended,
        "per:siblings": PersonSiblings,
        "per:spouse": PersonSpouse,
        "per:stateorprovince_of_birth": PersonStateOrProvinceOfBirth,
        "per:stateorprovince_of_death": PersonStateOrProvinceOfDeath,
        "per:stateorprovinces_of_residence": PersonStateOrProvinceOfResidence,
        "per:title": PersonTitle,
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
            relations = []
            for inst in instances:
                subj = (
                    " ".join(inst["token"][inst["subj_start"] : inst["subj_end"] + 1])
                    .replace("-LRB-", "(")
                    .replace("-RRB-", ")")
                    .replace("-LSB-", "[")
                    .replace("-RSB-", "]")
                )
                obj = (
                    " ".join(inst["token"][inst["obj_start"] : inst["obj_end"] + 1])
                    .replace("-LRB-", "(")
                    .replace("-RRB-", ")")
                    .replace("-LSB-", "[")
                    .replace("-RSB-", "]")
                )
                relation_cls = self.RELATION_TO_CLASS_MAPPING[inst["relation"]]

                relation = relation_cls(arg1=subj, arg2=obj)
                relation.subj_type = inst["subj_type"]
                relation.subj_type = inst["obj_type"]
                relations.append(relation)

            key = str(hash(text))
            self.elements[key] = {
                "id": key,
                "doc_id": instances[0]["docid"],
                "text": text,
                "labels": [rel for rel in relations if not isinstance(rel, NoneRelation)],
                "gold": relations,
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
            "RE",
        ], f"{task} can only be 'RE'."

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
            task_definitions=RELATION_DEFINITIONS,
            task_target="labels",
            definitions=GUIDELINES,
            **kwargs,
        )
