from typing import List, Type

from src.tasks.utils_typing import Entity, Event, dataclass


"""Entity definitions

The entity defitions are extracted from the KAIROS project guidelines.
"""


@dataclass
class Abstract(Entity):
    """{wikievents_ner_abstract}"""

    span: str


@dataclass
class BodyPart(Entity):
    """{wikievents_ner_bodypart}"""

    span: str


@dataclass
class CommercialProduct(Entity):
    """{wikievents_ner_commercialproduct}"""

    span: str


@dataclass
class Facility(Entity):
    """{wikievents_ner_facility}"""

    span: str


@dataclass
class GPE(Entity):
    """{wikievents_ner_gpe}"""

    span: str


@dataclass
class Information(Entity):
    """{wikievents_ner_information}"""

    span: str


@dataclass
class Location(Entity):
    """{wikievents_ner_location}"""

    span: str


@dataclass
class MedicalHealthIssue(Entity):
    """{wikievents_ner_medicalhealthissue}"""

    span: str


@dataclass
class Money(Entity):
    """{wikievents_ner_money}"""

    span: str


@dataclass
class Organization(Entity):
    """{wikievents_ner_organization}"""

    span: str


@dataclass
class Person(Entity):
    """{wikievents_ner_person}"""

    span: str


@dataclass
class SideOfConflict(Entity):
    """{wikievents_ner_side_of_conflict}"""

    span: str


@dataclass
class JobTitle(Entity):
    """{wikievents_ner_job_title}"""

    span: str


@dataclass
class Numeric(Entity):
    """{wikievents_ner_numeric}"""

    span: str


@dataclass
class Vehicle(Entity):
    """{wikievents_ner_vehicle}"""

    span: str


@dataclass
class Weapon(Entity):
    """{wikievents_ner_weapon}"""

    span: str


ENTITY_DEFINITIONS: List[Type] = [
    Abstract,
    BodyPart,
    CommercialProduct,
    Facility,
    GPE,
    Information,
    Location,
    MedicalHealthIssue,
    Money,
    Organization,
    Person,
    SideOfConflict,
    JobTitle,
    Numeric,
    Vehicle,
    Weapon,
]


@dataclass
class ArtifactExistanceEvent(Event):
    """{wikievents_ee_artifact_existance}"""

    mention: str


@dataclass
class CognitiveEvent(Event):
    """{wikievents_ee_cognitive}"""

    mention: str


@dataclass
class ConflictEvent(Event):
    """{wikievents_ee_conflict}"""

    mention: str


@dataclass
class ContactEvent(Event):
    """{wikievents_ee_contact}"""

    mention: str


@dataclass
class ControlEvent(Event):
    """{wikievents_ee_control}"""

    mention: str


@dataclass
class DisasterEvent(Event):
    """{wikievents_ee_disaster}"""

    mention: str


@dataclass
class GenericCrimeEvent(Event):
    """{wikievents_ee_generic_crime}"""

    mention: str


@dataclass
class JusticeEvent(Event):
    """{wikievents_ee_justice}"""

    mention: str


@dataclass
class LifeEvent(Event):
    """{wikievents_ee_life}"""

    mention: str


@dataclass
class MedicalEvent(Event):
    """{wikievents_ee_medical}"""

    mention: str


@dataclass
class MovementTransportEvent(Event):
    """{wikievents_ee_movement_transport}"""

    mention: str


@dataclass
class PersonnelEvent(Event):
    """{wikievents_ee_personnel}"""

    mention: str


@dataclass
class TransactionEvent(Event):
    """{wikievents_ee_transaction}"""

    mention: str


COARSE_EVENT_DEFINITIONS: List[Type] = [
    ArtifactExistanceEvent,
    CognitiveEvent,
    ConflictEvent,
    ContactEvent,
    ControlEvent,
    DisasterEvent,
    GenericCrimeEvent,
    JusticeEvent,
    LifeEvent,
    MedicalEvent,
    MovementTransportEvent,
    PersonnelEvent,
    TransactionEvent,
]


@dataclass
class DamageDestroy(ArtifactExistanceEvent):
    """{wikievents_eae_damage_destroy}"""

    mention: str  # The text span that most clearly expresses (triggers) the event
    agent: List[str]  # The person damaging the artifact
    artifact: List[str]  # The artifact being damaged
    instrument: List[str]  # The object used to damage the artifact
    place: List[str]  # Where the event occurred


@dataclass
class DisableDefuse(ArtifactExistanceEvent):
    """{wikievents_eae_disable_defuse}"""

    mention: str  # The text span that most clearly expresses (triggers) the event
    agent: List[str]  # The person disabling, defusing or deactivating the artifact
    artifact: List[str]  # The artifact being disabled
    instrument: List[str]  # The object used to disable, defuse or deactivating the artifact
    place: List[str]  # Where the event occurred


@dataclass
class Dismantle(ArtifactExistanceEvent):
    """{wikievents_eae_dismantle}"""

    mention: str  # # The text span that most clearly expresses (triggers) the event
    agent: List[str]  # The person dismantling the artifact
    artifact: List[str]  # The artifact being dismantled into components
    components: List[str]  # The components that originally composed the artifact
    place: List[str]  # Where the event occurred


@dataclass
class ManufactureAssemble(ArtifactExistanceEvent):
    """{wikievents_eae_manufacture_assemble}"""

    mention: str  # The text span that most clearly expresses (triggers) the event
    agent: List[str]  # The person manufacturing or assembling the artifact
    artifact: List[str]  # The artifact being manufactured or assembled
    components: List[str]  # The components that compose the artifact
    instrument: List[str]  # The object use to manufacture or assemble the artifact
    place: List[str]  # Where the event occurred
