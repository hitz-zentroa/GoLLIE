from collections import defaultdict
import inspect
import json

from src.tasks.tacred.prompts import OrganizationAlternateName, OrganizationCityOfHeadquarters, OrganizationCountryOfHeadquarters, OrganizationDateDissolved, OrganizationDateFounded, OrganizationFoundedBy, OrganizationMember, OrganizationMemberOf, OrganizationNumberOfEmployeesMembers, OrganizationParent, OrganizationPoliticalReligiousAffiliation, OrganizationShareholders, OrganizationStateOrProvinceOfHeadquarters, OrganizationSubsidiary, OrganizationTopMembersEmployees, OrganizationWebsite, PersonAge, PersonAlternateNames, PersonCauseOfDeath, PersonCharges, PersonChildren, PersonCityOfBirth, PersonCityOfDeath, PersonCityOfResidence, PersonCountryOfResidence


from ..utils_data import DatasetLoader, Sampler
from ..utils_typing import Relation, dataclass

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
        "per:countries_of_residence": PersonCountryOfResidence
    }

    def __init__(self, path: str) -> None:
        
        self.elements = {}
        with open(path, 'rt', encoding="utf-8") as in_f:
            data = json.load(in_f)

        data_by_sentence = defaultdict(list)
        for line in data:
            text = " ".join(line['token'])
            data_by_sentence[text].append(line)
        
        for text, instances in data_by_sentence.items():
            text = text.replace("-LRB-", "(").replace("-RRB-", ")").replace("-LSB-", "[").replace("-RSB-", "]")
            relations, queries = [], set()
            for inst in instances:
                subj=" ".join(inst["token"][inst["subj_start"] : inst["subj_end"] + 1]).replace("-LRB-", "(").replace("-RRB-", ")").replace("-LSB-", "[").replace("-RSB-", "]")
                obj=" ".join(inst["token"][inst["subj_start"] : inst["subj_end"] + 1]).replace("-LRB-", "(").replace("-RRB-", ")").replace("-LSB-", "[").replace("-RSB-", "]")
                relation_cls = self.RELATION_TO_CLASS_MAPPING[inst['relation']]
                
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
                "gold": relations
            }
        
        assert len(self.elements) == len(data_by_sentence), "The hash function failed."