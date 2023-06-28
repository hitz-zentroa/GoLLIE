from typing import List, Optional

from ..utils_typing import Name, String, Template, Value, dataclass


"""Relation definitions

The relation definitions are derived from the official TACRED guidelines:
https://tac.nist.gov/2014/KBP/ColdStart/guidelines/TAC_KBP_2014_Slot_Descriptions_V1.4.pdf
"""


@dataclass
class PersonTemplate(Template):
    """{tacred_person}"""

    query: str  # The Person entity query
    alternate_names: Optional[List[Name]] = None
    """{tacred_person_alternate_names}"""
    date_of_birth: Optional[Value] = None
    """{tacred_person_date_of_birth}"""
    age: Optional[Value] = None
    """{tacred_person_age}"""
    country_of_birth: Optional[Name] = None
    """{tacred_person_country_of_birth}"""
    state_or_province_of_birth: Optional[Name] = None
    """{tacred_person_state_or_province_of_birth}"""
    city_of_birth: Optional[Name] = None
    """{tacred_person_city_of_birth}"""
    origin: Optional[List[Name]] = None
    """{tacred_person_origin}"""
    date_of_death: Optional[Value] = None
    """{tacred_person_date_of_death}"""
    country_of_death: Optional[Name] = None
    """{tacred_person_country_of_death}"""
    state_or_province_of_death: Optional[Name] = None
    """{tacred_person_state_or_province_of_death}"""
    city_of_death: Optional[Name] = None
    """{tacred_person_city_of_death}"""
    cause_of_death: Optional[String] = None
    """{tacred_person_cause_of_death}"""
    countries_of_residence: Optional[List[Name]] = None
    """{tacred_person_countries_of_residence}"""
    states_or_provinces_of_residence: Optional[List[Name]] = None
    """{tacred_person_states_or_provinces_of_residence}"""
    cities_of_residence: Optional[List[Name]] = None
    """{tacred_person_cities_of_residence}"""
    schools_attended: Optional[List[Name]] = None
    """{tacred_person_schools_attended}"""
    title: Optional[List[String]] = None
    """{tacred_person_title}"""
    employee_or_member_of: Optional[List[Name]] = None
    """{tacred_person_employee_or_member_of}"""
    religion: Optional[String] = None
    """{tacred_person_religion}"""
    spouse: Optional[List[Name]] = None
    """{tacred_person_spouse}"""
    children: Optional[List[Name]] = None
    """{tacred_person_children}"""
    parents: Optional[List[Name]] = None
    """{tacred_person_parents}"""
    siblings: Optional[List[Name]] = None
    """{tacred_person_siblings}"""
    other_family: Optional[List[Name]] = None
    """{tacred_person_other_family}"""
    charges: Optional[List[String]] = None
    """{tacred_person_charges}"""


@dataclass
class OrganizationTemplate(Template):
    """{tacred_organization_template}"""

    query: str  # The Organization entity query
    alternate_names: Optional[List[Name]] = None
    """{tacred_organization_alternate_names}"""
    political_or_religious_affiliation: Optional[List[Name]] = None
    """{tacred_organnization_political_or_religious_affiliation}"""
    top_members_employees: Optional[List[Name]] = None
    """{tacred_organization_top_members_employees}"""
    number_of_employees_members: Optional[Value] = None
    """{tacred_organization_number_of_employees_members}"""
    members: Optional[List[Name]] = None
    """{tacred_organization_members}"""
    member_of: Optional[List[Name]] = None
    """{tacred_organization_member_of}"""
    subsidiaries: Optional[List[Name]] = None
    """{tacred_organization_subsidiaries}"""
    parents: Optional[List[Name]] = None
    """{tacred_organization_parents}"""
    founded_by: Optional[List[Name]] = None
    """{tacred_organization_founded_by}"""
    date_founded: Optional[Value] = None
    """{tacred_organization_date_founded}"""
    date_dissolved: Optional[Value] = None
    """{tacred_organization_date_dissolved}"""
    country_of_headquarters: Optional[Name] = None
    """{tacred_organization_country_of_headquarters}"""
    state_or_province_of_headquarters: Optional[Name] = None
    """{tacred_organization_state_or_province_of_headquarters}"""
    city_of_headquarters: Optional[Name] = None
    """{tacred_organization_city_of_headquarters}"""
    shareholders: Optional[List[Name]] = None
    """{tacred_organization_shareholders}"""
    website: Optional[String] = None
    """{tacred_organization_website}"""


TEMPLATE_DEFINITIONS = [PersonTemplate, OrganizationTemplate]
