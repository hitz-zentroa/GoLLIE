from ..utils_typing import Relation, dataclass


"""Relation definitions

The relation definitions are derived from the official TACRED guidelines:
https://tac.nist.gov/2014/KBP/ColdStart/guidelines/TAC_KBP_2014_Slot_Descriptions_V1.4.pdf
"""


@dataclass
class PersonAlternateNames(Relation):
    """The PersonAlaternateNames relation encodes names used to refer to the assigned
    person that are distinct from the "official" name. Alternate names may include
    aliases, stage names, alternate transliterations, abbreviations, alternate spellings,
    nicknames, or birth names.

    Verbalization: {arg1} is also known as {arg2}.
    """

    arg1: str  # The original name
    arg2: str  # The alias


@dataclass
class PersonDateOfBirth(Relation):
    """The PersonDateOfBirth relation encodes the date on which the assigned person was
    born.

    Verbalization: {arg1} was born on {arg2}.
    """

    arg1: str  # The person
    arg2: str  # The birth date


@dataclass
class PersonAge(Relation):
    """The PersonAge relation encondes the age of the assigned person.

    Verbalization: {arg1} is {arg2} years old.
    """

    arg1: str  # The person
    arg2: str  # The age


@dataclass
class PersonCountryOfBirth(Relation):
    """The PersonCountryOfBirth relation encodes the country in which the assigned person
    was born.

    Verbalization: {arg1} was born in {arg2}.
    """

    arg1: str  # The person
    arg2: str  # The country of birth


@dataclass
class PersonStateOrProvinceOfBirth(Relation):
    """The PersonStateOrProvinceOfBirth relation encodes the geopolitical (GPE) entity at
    state or province level in which the assigned person was born. The `arg2` slot must
    be filled with the name of a state or province.

    Verbalization: {arg1} was born in {arg2}.
    """

    arg1: str  # The person
    arg2: str  # The state or province


@dataclass
class PersonCityOfBirth(Relation):
    """The PersonCityOfBirth relation encodes the geopolitical (GPE) entity at the
    municipality level (city, town, or village) in which the assigned person was
    born. The `arg2` slot must be filled with the name of a city, town, or village.

    Verbalization: {arg1} was born in {arg2}.
    """

    arg1: str  # The person
    arg2: str  # The city, town or village


@dataclass
class PersonOrigin(Relation):
    """The PersonOrigin relation encodes the nationality and/or ethnicity of the assigned
    person.

    Verbalization: {arg2} is the nationality of {arg1}.
    """

    arg1: str  # The person
    arg2: str  # The origin


@dataclass
class PersonDateOfDeath(Relation):
    """The PersonDateOfDeath relation encodes the date of the assigned person's death.

    Verbalization: {arg1} died in {arg2}.
    """

    arg1: str  # The person
    arg2: str  # The date of death


@dataclass
class PersonCountryOfDeath(Relation):
    """The PersonCountryOfDeath relation encodes the country in which the assigned person
    died. The `arg2` slot must be filled with the name of a country.

    Verbalization: {arg1} died in {arg2}.
    """

    arg1: str  # The person
    arg2: str  # The country of death


@dataclass
class PersonStateOrProvinceOfDeath(Relation):
    """The PersonStateOrProvinceOfDeath relation encodes the geopolitical (GPE) entity at
    state or province level in which the assigned person died. The `arg2` slot must be
    filled with a state or province name.

    Verbalization: {arg1} died in {arg2}.
    """

    arg1: str  # The person
    arg2: str  # The state or province of death


@dataclass
class PersonCityOfDeath(Relation):
    """The PersonCityOfDeath relation encodes the geopolitical (GPE) entity at the level
    of city, town, village in which the assigned person died. The `arg2` slot must be
    filled with a city, town, or village name.

    Verbalization: {arg1} died in {arg2}.
    """

    arg1: str  # The person
    arg2: str  # The city, town or village


@dataclass
class PersonCauseOfDeath(Relation):
    """The PersonCauseOfDeath relation encodes the explicit cause of death for the
    assigned person.

    Verbalization: {arg2} is the cause of {arg1}'s death.
    """

    arg1: str  # The person
    arg2: str  # Cause of the death


@dataclass
class PersonCountryOfResidence(Relation):
    """The PersonCountryOfResidence relation encodes the country in which the assigned
    person has lived.

    Verbalization: {arg1} lives or has lived in {arg2}.
    """

    arg1: str  # The person
    arg2: str  # The country


@dataclass
class PersonStateOrProvinceOfResidence(Relation):
    """The PersonStateOrProvinceOfResidence relation encodes the geopolotical (GPE)
    entities at the state or province level in which the assigned person has lived. The
    `arg2` slot must be filled with state or province names.

    Verbalization: {arg1} lives or has lived in {arg2}.
    """

    arg1: str  # The person
    arg2: str  # The state or province


@dataclass
class PersonCityOfResidence(Relation):
    """The PersonCityOfResidence relations encodes the geopolitical (GPE) entities
    at the level of city, town, or village in which the assigned person has lived.
    The `arg2` slot must be filled with the name of a city, town, or village.

    Verbalization: {arg1} lives or has lived in {arg2}.
    """

    arg1: str  # The person
    arg2: str  # The city, town or village


@dataclass
class PersonSchoolAttended(Relation):
    """The PersonSchoolAttended relations encodes any school (college, high school,
    university, etc.) that the assigned person has attended.

    Verbalization: {arg1} studied in {arg2}.
    """

    arg1: str  # The person
    arg2: str  # The school (college, high school, university, etc.)


@dataclass
class PersonTitle(Relation):
    """The PersonTitle relation encodes the official or unofficial name(s) of the
    employment or membership position that have been held by the assigned person.
    The `arg2` slot must be filled with the name of the position or title.

    Verbalization: {arg1} is a {arg2}.
    """

    arg1: str  # The person
    arg2: str  # The position or title


@dataclass
class PersonEmployeeOrMemberOf(Relation):
    """The PersonEmployeeOrMemberOf relation encodes the organization or geopolitical
    (GPE) entities (governments) of which the assigned person has been an employee or
    member.

    Verbalization: {arg1} is a member of {arg2}.
    """

    arg1: str  # The person
    arg2: str  # The organization or entity


@dataclass
class PersonReligion(Relation):
    """The PersonReligion relation encodes the religion to which the assigned person has
    belonged. Former religions are also acceptable answers.

    Verbalization: {arg2} is the religion of {arg1}.
    """

    arg1: str  # The person
    arg2: str  # The religion to which the person belongs


@dataclass
class PersonSpouse(Relation):
    """The PersonSpouse relation encodes the spouse(s) of the assigned person. Former
    spouses are acceptable answers. This relation is bidirectional.

    Verbalization: {arg2} is the spouse of {arg1}.
    """

    arg1: str  # The person
    arg2: str  # The spouse (wife or husband)


@dataclass
class PersonChildren(Relation):
    """The PersonChildren relation encodes the children of the assigned person, including
    adopted and step-children.

    Verbalization: {arg2} is the child of {arg1}.
    """

    arg1: str  # The person (parent)
    arg2: str  # The child


@dataclass
class PersonParents(Relation):
    """The PersonParents relation encodes the parents of the assigned person. In addition
    to biological parents, step-parents and adoptive parents are also acceptable answers.

    Verbalization: {arg2} is the parent of {arg1}.
    """

    arg1: str  # The person (child)
    arg2: str  # The parent


@dataclass
class PersonSiblings(Relation):
    """The PersonSiblings relation encodes the brothers and sisters of the assigned person.
    In addition to full siblings, step-siblings and half-siblings are acceptable answers.
    Brothers- or sisters-in-law are not acceptable responses for PersonSiblings relation.

    Verbalization: {arg1} and {arg2} are siblings.
    """

    arg1: str  # The person
    arg2: str  # A sibling


@dataclass
class PersonOtherFamily(Relation):
    """The PersonOtherFamily relation encodes the family other than siblings, children, and
    spouse (or former spouse). Correct fillers for the `arg2` slot include brothers-in-law,
    sisters-in-law, grandparents, grandchildren, cousins, aunts, uncles, etc.

    Verbalization: {arg1} and {arg2} are family.
    """

    arg1: str  # The person
    arg2: str  # The family member


@dataclass
class PersonCharges(Relation):
    """The PersonCharges relation encodes the charges or crimes (alleged or convicted) of
    the assigned person.

    Verbalization: {arg1} was convicted for {arg2}.
    """

    arg1: str  # The person
    arg2: str  # The crime


@dataclass
class OrganizationAlternateName(Relation):
    """The OrganizationAlternateName relation encodes any name used to refer to the
    assigned organization that is distinct from the "official" name. Alternate names may
    include former names, aliases, alternate spellings, acronyms, abbreviations,
    translations or transliterations of names, and any official designators such as stock
    ticker code or airline call sign.

    Verbalization: {arg1} is also known as {arg2}.
    """

    arg1: str  # The organization name
    arg2: str  # The alias


@dataclass
class OrganizationPoliticalReligiousAffiliation(Relation):
    """The OrganizationPoliticalReligiousAffiliation relation encodes the ideological
    groups with which the organization is associated.

    Verbalization: {arg1} has political or religious affiliation with {arg2}.
    """

    arg1: str  # The organization
    arg2: str  # The affiliation


@dataclass
class OrganizationTopMembersEmployees(Relation):
    """The OrganizationTopMembersEmployees relation encodes the persons in high-level,
    leading positions at the assigned organization. Although the definition of 'leading
    position' is relatively broad, all Top Member/Employee positions should imply a level
    of decidion-making authority over the entire assigned organization.

    Verbalization: {arg1} is a high level member of {arg2}.
    """

    arg1: str  # The organization
    arg2: str  # The top member or employee


@dataclass
class OrganizationNumberOfEmployeesMembers(Relation):
    """The OrganizationNumberOfEmployeesMembers relation encodes the total number of
    people who are employed by or have membership in the associated organization.

    Verbalization: {arg1} employs nearly {arg2} people.
    """

    arg1: str  # The organization
    arg2: str  # The number of members or employees


@dataclass
class OrganizationMember(Relation):
    """The OrganizationMember relation encodes the organizations or geopolitical (GPE)
    entities that are members of the assigned organization (the inverse of
    OrganizationMemberOf). While similar to OrganizationSubsidiary, OrganizationMember
    is different because correct `arg2` fillers are distinct entities that are generally
    capable of autonomously ending their membership with the assigned organization.

    Verbalization: {arg2} is member of {arg1}.
    """

    arg1: str  # The organization
    arg2: str  # The organization member of the first


@dataclass
class OrganizationMemberOf(Relation):
    """The OrganizationMemberOf relation encodes the organizations or geopolitical (GPE)
    entities of which the assigned organization is a member itself (the inverse of
    OrganizationMember). For the `arg2` slot, the assigned organization is a distinct
    entity from the parent organization and is generally capable of autonomously ending
    the membership relation.

    Verbalization: {arg1} is member of {arg2}.
    """

    arg1: str  # The organization
    arg2: str  # The organization which the first is member of


@dataclass
class OrganizationSubsidiary(Relation):
    """The OrganizationSubsidiary relation encodes the organizations that are
    subsidiaries of the assigned organization (the inverse of OrganizationParent).
    Subsidiaries are subsumed under the assigned organization, rather than being distinct
    entities.

    Verbalization: {arg2} is a subsidiary or branch of {arg1}.
    """

    arg1: str  # The organization
    arg2: str  # The subsidiary


@dataclass
class OrganizationParent(Relation):
    """The OrganizationParent relation encodes the organizations or geopolitical (GPE)
    entities of which the assigned organization is a subsidiary (the inverse of
    OrganizationSubsidiary). While similar to OrganizationMemberOf, OrganizationParent
    is different because the assigned organization is subsumed under the parent
    organization(s), rather than being a distinct entity.

    Verbalization: {arg1} is a subsidiary or branch of {arg2}.
    """

    arg1: str  # The organization
    arg2: str  # The parent organization


@dataclass
class OrganizationFoundedBy(Relation):
    """The OrganizationFoundedBy relation encodes the person, organization or
    geopolitical (GPE) entity that founded the assigned organization.

    Verbalization: {arg1} was founded by {arg2}.
    """

    arg1: str  # The organization
    arg2: str  # The founder


@dataclass
class OrganizationDateFounded(Relation):
    """The OrganizationDateFounded relations encodes the date on which the assigned
    organization was founded.

    Verbalization: {arg1} was founded in {arg2}.
    """

    arg1: str  # The organization
    arg2: str  # The date


@dataclass
class OrganizationDateDissolved(Relation):
    """The OrganizationDateDissolved relation encodes the date on which the assigned
    organization was dissolved. When Companies merge to form a new entity, the original
    companies should be considered as dissolved.

    Verbalization: {arg1} dissolved in {arg2}.
    """

    arg1: str  # The organization
    arg2: str  # The date


@dataclass
class OrganizationCountryOfHeadquarters(Relation):
    """The OrganizationCountryOfHeadquarters relation encodes the country in which the
    headquarters of the assigned organization are located. The `arg2` slot must be filled
    with a country name.

    Verbalization: {arg1} is located in {arg2}.
    """

    arg1: str  # The organization
    arg2: str  # The country


@dataclass
class OrganizationStateOrProvinceOfHeadquarters(Relation):
    """The OrganizationStateOrProvinceOfHeadquarters relation encodes the location of
    the headquarters of the assigned organization at the state or province level. The
    `arg2` slot must be filled with a state or province name.

    Verbalization: {arg1} is located in {arg2}.
    """

    arg1: str  # The organization
    arg2: str  # The state or province


@dataclass
class OrganizationCityOfHeadquarters(Relation):
    """The OrganizationCityOfHeadquarters relation encodes the location of the
    headquarters of the assigned organization ath the city, town, or village level. The
    `arg2` slot must be filled with a city, town, or village name.

    Verbalization: {arg1} is located in {arg2}.
    """

    arg1: str  # The organization
    arg2: str  # The city, town, ow village name


@dataclass
class OrganizationShareholders(Relation):
    """The OrganizationShareholders relation encodes any organization, person, or
    geopolitical (GPE) entity that holds shares (majority or not) of the organization.
    Former shareholders are acceptable responses.

    Verbalization: {arg2} holds shares in {arg1}.
    """

    arg1: str  # The organization
    arg2: str  # The shareholder


@dataclass
class OrganizationWebsite(Relation):
    """The OrganizationWebsite relation encodes an official top level URL for the
    assigned organization's website.

    Verbalization: {arg2} is the website of {arg1}.
    """

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
