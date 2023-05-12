from ..utils_typing import Relation, dataclass


"""Relation definitions

The relation definitions are derived from the official TACRED guidelines:
https://tac.nist.gov/2014/KBP/ColdStart/guidelines/TAC_KBP_2014_Slot_Descriptions_V1.4.pdf
"""


@dataclass
class PersonAlternateNames(Relation):
    """{tacred_personalternatenames}"""

    arg1: str  # The original name
    arg2: str  # The alias


@dataclass
class PersonDateOfBirth(Relation):
    """{tacred_persondateofbirth}"""

    arg1: str  # The person
    arg2: str  # The birth date


@dataclass
class PersonAge(Relation):
    """{tacred_personage}"""

    arg1: str  # The person
    arg2: str  # The age


@dataclass
class PersonCountryOfBirth(Relation):
    """{tacred_personcountryofbirth}"""

    arg1: str  # The person
    arg2: str  # The country of birth


@dataclass
class PersonStateOrProvinceOfBirth(Relation):
    """{tacred_personstateorprovinceofbirth}"""

    arg1: str  # The person
    arg2: str  # The state or province


@dataclass
class PersonCityOfBirth(Relation):
    """{tacred_personcityofbirth}"""

    arg1: str  # The person
    arg2: str  # The city, town or village


@dataclass
class PersonOrigin(Relation):
    """{tacred_personorigin}"""

    arg1: str  # The person
    arg2: str  # The origin


@dataclass
class PersonDateOfDeath(Relation):
    """{tacred_persondateofdeath}"""

    arg1: str  # The person
    arg2: str  # The date of death


@dataclass
class PersonCountryOfDeath(Relation):
    """{tacred_personcountryofdeath}"""

    arg1: str  # The person
    arg2: str  # The country of death


@dataclass
class PersonStateOrProvinceOfDeath(Relation):
    """{tacred_personstateorprovinceofdeath}"""

    arg1: str  # The person
    arg2: str  # The state or province of death


@dataclass
class PersonCityOfDeath(Relation):
    """{tacred_personcityofdeath}"""

    arg1: str  # The person
    arg2: str  # The city, town or village


@dataclass
class PersonCauseOfDeath(Relation):
    """{tacred_personcauseofdeath}"""

    arg1: str  # The person
    arg2: str  # Cause of the death


@dataclass
class PersonCountryOfResidence(Relation):
    """{tacred_personcountryofresidence}"""

    arg1: str  # The person
    arg2: str  # The country


@dataclass
class PersonStateOrProvinceOfResidence(Relation):
    """{tacred_personstateorprovinceofresidence}"""

    arg1: str  # The person
    arg2: str  # The state or province


@dataclass
class PersonCityOfResidence(Relation):
    """{tacred_personcityofresidence}"""

    arg1: str  # The person
    arg2: str  # The city, town or village


@dataclass
class PersonSchoolAttended(Relation):
    """{tacred_personschoolattended}"""

    arg1: str  # The person
    arg2: str  # The school (college, high school, university, etc.)


@dataclass
class PersonTitle(Relation):
    """{tacred_persontitle}"""

    arg1: str  # The person
    arg2: str  # The position or title


@dataclass
class PersonEmployeeOrMemberOf(Relation):
    """{tacred_personemployeeormemberof}"""

    arg1: str  # The person
    arg2: str  # The organization or entity


@dataclass
class PersonReligion(Relation):
    """{tacred_personreligion}"""

    arg1: str  # The person
    arg2: str  # The religion to which the person belongs


@dataclass
class PersonSpouse(Relation):
    """{tacred_personspouse}"""

    arg1: str  # The person
    arg2: str  # The spouse (wife or husband)


@dataclass
class PersonChildren(Relation):
    """{tacred_personchildren}"""

    arg1: str  # The person (parent)
    arg2: str  # The child


@dataclass
class PersonParents(Relation):
    """{tacred_personparents}"""

    arg1: str  # The person (child)
    arg2: str  # The parent


@dataclass
class PersonSiblings(Relation):
    """{tacred_personsiblings}"""

    arg1: str  # The person
    arg2: str  # A sibling


@dataclass
class PersonOtherFamily(Relation):
    """{tacred_personotherfamily}"""

    arg1: str  # The person
    arg2: str  # The family member


@dataclass
class PersonCharges(Relation):
    """{tacred_personcharges}"""

    arg1: str  # The person
    arg2: str  # The crime


@dataclass
class OrganizationAlternateName(Relation):
    """{tacred_organizationalternatename}"""

    arg1: str  # The organization name
    arg2: str  # The alias


@dataclass
class OrganizationPoliticalReligiousAffiliation(Relation):
    """{tacred_organizationpoliticalreligiousaffiliation}"""

    arg1: str  # The organization
    arg2: str  # The affiliation


@dataclass
class OrganizationTopMembersEmployees(Relation):
    """{tacred_organizationtopmembersemployees}"""

    arg1: str  # The organization
    arg2: str  # The top member or employee


@dataclass
class OrganizationNumberOfEmployeesMembers(Relation):
    """{tacred_organizationnumberofemployeesmembers}"""

    arg1: str  # The organization
    arg2: str  # The number of members or employees


@dataclass
class OrganizationMember(Relation):
    """{tacred_organizationmember}"""

    arg1: str  # The organization
    arg2: str  # The organization member of the first


@dataclass
class OrganizationMemberOf(Relation):
    """{tacred_organizationmemberof}"""

    arg1: str  # The organization
    arg2: str  # The organization which the first is member of


@dataclass
class OrganizationSubsidiary(Relation):
    """{tacred_organizationsubsidiary}"""

    arg1: str  # The organization
    arg2: str  # The subsidiary


@dataclass
class OrganizationParent(Relation):
    """{tacred_organizationparent}"""

    arg1: str  # The organization
    arg2: str  # The parent organization


@dataclass
class OrganizationFoundedBy(Relation):
    """{tacred_organizationfoundedby}"""

    arg1: str  # The organization
    arg2: str  # The founder


@dataclass
class OrganizationDateFounded(Relation):
    """{tacred_organizationdatefounded}"""

    arg1: str  # The organization
    arg2: str  # The date


@dataclass
class OrganizationDateDissolved(Relation):
    """{tacred_organizationdatedissolved}"""

    arg1: str  # The organization
    arg2: str  # The date


@dataclass
class OrganizationCountryOfHeadquarters(Relation):
    """{tacred_organizationcountryofheadquarters}"""

    arg1: str  # The organization
    arg2: str  # The country


@dataclass
class OrganizationStateOrProvinceOfHeadquarters(Relation):
    """{tacred_organizationstateorprovinceofheadquarters}"""

    arg1: str  # The organization
    arg2: str  # The state or province


@dataclass
class OrganizationCityOfHeadquarters(Relation):
    """{tacred_organizationcityofheadquarters}"""

    arg1: str  # The organization
    arg2: str  # The city, town, ow village name


@dataclass
class OrganizationShareholders(Relation):
    """{tacred_organizationshareholders}"""

    arg1: str  # The organization
    arg2: str  # The shareholder


@dataclass
class OrganizationWebsite(Relation):
    """{tacred_organizationwebsite}"""

    arg1: str  # The organization
    arg2: str  # The website url


RELATION_DEFINITIONS = [
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
]
