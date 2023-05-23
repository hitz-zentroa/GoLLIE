from src.tasks.utils_typing import Entity


"""Entity definitions

The entity defitions are extracted from the KAIROS project guidelines

"""


class Abstract(Entity):
    """{wikievents_ner_abstract}"""

    span: str


class BodyPart(Entity):
    """{wikievents_ner_bodypart}"""

    span: str


class CommercialProduct(Entity):
    """{wikievents_ner_commercialproduct}"""

    span: str


class Facility(Entity):
    """{wikievents_ner_facility}"""

    span: str


class GPE(Entity):
    """{wikievents_ner_gpe}"""

    span: str


class Information(Entity):
    """{wikievents_ner_information}"""

    span: str


class Location(Entity):
    """{wikievents_ner_location}"""

    span: str


class MedicalHealthIssue(Entity):
    """{wikievents_ner_medicalhealthissue}"""

    span: str


class Money(Entity):
    """{wikievents_ner_money}"""

    span: str


class Organization(Entity):
    """{wikievents_ner_organization}"""

    span: str
