from typing import Dict, List, Type

from src.tasks.utils_typing import Entity, Event, dataclass


"""Entity definitions

The entity defitions are extracted from the KAIROS project guidelines.
"""


@dataclass
class Abstract(Entity):
    """{wikievents_ner_abstract}"""

    span: str  # {wikievents_ner_abstract_examples}


@dataclass
class BodyPart(Entity):
    """{wikievents_ner_bodypart}"""

    span: str  # {wikievents_ner_bodypart_examples}


@dataclass
class CommercialProduct(Entity):
    """{wikievents_ner_commercialproduct}"""

    span: str  # {wikievents_ner_commercialproduct_examples}


@dataclass
class Facility(Entity):
    """{wikievents_ner_facility}"""

    span: str  # {wikievents_ner_facility_examples}


@dataclass
class GPE(Entity):
    """{wikievents_ner_gpe}"""

    span: str  # {wikievents_ner_gpe_examples}


@dataclass
class Information(Entity):
    """{wikievents_ner_information}"""

    span: str  # {wikievents_ner_information_examples}


@dataclass
class Location(Entity):
    """{wikievents_ner_location}"""

    span: str  # {wikievents_ner_location_examples}


@dataclass
class MedicalHealthIssue(Entity):
    """{wikievents_ner_medicalhealthissue}"""

    span: str  # {wikievents_ner_medicalhealthissue_examples}


@dataclass
class Money(Entity):
    """{wikievents_ner_money}"""

    span: str  # {wikievents_ner_money_examples}


@dataclass
class Organization(Entity):
    """{wikievents_ner_organization}"""

    span: str  # {wikievents_ner_organization_examples}


@dataclass
class Person(Entity):
    """{wikievents_ner_person}"""

    span: str  # {wikievents_ner_person_examples}


@dataclass
class SideOfConflict(Entity):
    """{wikievents_ner_side_of_conflict}"""

    span: str  # {wikievents_ner_side_of_conflict_examples}


@dataclass
class JobTitle(Entity):
    """{wikievents_ner_job_title}"""

    span: str  # {wikievents_ner_job_title_examples}


@dataclass
class Numeric(Entity):
    """{wikievents_ner_numeric}"""

    span: str  # {wikievents_ner_numeric_examples}


@dataclass
class Vehicle(Entity):
    """{wikievents_ner_vehicle}"""

    span: str  # {wikievents_ner_vehicle_examples}


@dataclass
class Weapon(Entity):
    """{wikievents_ner_weapon}"""

    span: str  # {wikievents_ner_weapon_examples}


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
    """The text span that triggers the event.
    {wikievents_ee_artifact_existance_examples}
    """


@dataclass
class CognitiveEvent(Event):
    """{wikievents_ee_cognitive}"""

    mention: str
    """The text span that triggers the event.
    {wikievents_ee_cognitive_examples}
    """


@dataclass
class ConflictEvent(Event):
    """{wikievents_ee_conflict}"""

    mention: str
    """The text span that triggers the event.
    {wikievents_ee_conflict_examples}
    """


@dataclass
class ContactEvent(Event):
    """{wikievents_ee_contact}"""

    mention: str
    """The text span that triggers the event.
    {wikievents_ee_contact_examples}
    """


@dataclass
class ControlEvent(Event):
    """{wikievents_ee_control}"""

    mention: str
    """The text span that triggers the event.
    {wikievents_ee_control_examples}
    """


@dataclass
class DisasterEvent(Event):
    """{wikievents_ee_disaster}"""

    mention: str
    """The text span that triggers the event.
    {wikievents_ee_disaster_examples}
    """


@dataclass
class GenericCrimeEvent(Event):
    """{wikievents_ee_generic_crime}"""

    mention: str
    """The text span that triggers the event.
    {wikievents_ee_generic_crime_examples}
    """


@dataclass
class JusticeEvent(Event):
    """{wikievents_ee_justice}"""

    mention: str
    """The text span that triggers the event.
    {wikievents_ee_justice_examples}
    """


@dataclass
class LifeEvent(Event):
    """{wikievents_ee_life}"""

    mention: str
    """The text span that triggers the event.
    {wikievents_ee_life_examples}
    """


@dataclass
class MedicalEvent(Event):
    """{wikievents_ee_medical}"""

    mention: str
    """The text span that triggers the event.
    {wikievents_ee_medical_examples}
    """


@dataclass
class MovementTransportEvent(Event):
    """{wikievents_ee_movement_transport}"""

    mention: str
    """The text span that triggers the event.
    {wikievents_ee_transport_examples}
    """


@dataclass
class PersonnelEvent(Event):
    """{wikievents_ee_personnel}"""

    mention: str
    """The text span that triggers the event.
    {wikievents_ee_personnel_examples}
    """


@dataclass
class TransactionEvent(Event):
    """{wikievents_ee_transaction}"""

    mention: str
    """The text span that triggers the event.
    {wikievents_ee_transaction_examples}
    """


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
    instrument: List[str]  # The object used to dismantle the artifact
    place: List[str]  # Where the event occurred


@dataclass
class ManufactureAssemble(ArtifactExistanceEvent):
    """{wikievents_eae_manufacture_assemble}"""

    mention: str  # The text span that most clearly expresses (triggers) the event
    agent: List[str]  # The person manufacturing or assembling the artifact
    artifact: List[str]  # The artifact being manufactured or assembled
    components: List[str]  # The components that compose the artifact
    place: List[str]  # Where the event occurred


@dataclass
class IdentifyCategorize(CognitiveEvent):
    """{wikievents_eae_identify_categorize}"""

    mention: str  # The text span that most clearly expresses (triggers) the event
    agent: List[str]  # The person identifying the object
    object: List[str]  # The identifyied object
    role: List[str]  # The role or categorization of the object
    place: List[str]  # Where the event occurred


@dataclass
class Inspection(CognitiveEvent):
    """{wikievents_eae_inspection}"""

    mention: str  # The text span that most clearly expresses (triggers) the event
    agent: List[str]  # The person observing the entity
    entity: List[str]  # The entity being observed
    instrument: List[str]  # The instrument used to observe the entity
    place: List[str]  # Where the event occurred


@dataclass
class Research(CognitiveEvent):
    """{wikievents_eae_research}"""

    mention: str  # The text span that most clearly expresses (triggers) the event
    agent: List[str]  # The person conducting the research
    subject: List[str]  # The subject being researched
    place: List[str]  # Where the event occurred


@dataclass
class TeachingTrainingLearning(CognitiveEvent):
    """{wikievents_eae_teaching_training_learning}"""

    mention: str  # The text span that most clearly expresses (triggers) the event
    agent: List[str]  # The person who teaches or trains
    patient: List[str]  # The person who is being taught or trained


@dataclass
class Attack(ConflictEvent):
    """{wikievents_eae_attack}"""

    mention: str  # The text span that most clearly expresses (triggers) the event
    agent: List[str]  # The entity attacking (the attacker)
    target: List[str]  # The entity being attacked (the victim)
    instrument: List[str]  # The object used to attack
    explosive_device: List[str]  # The explosive device used to attack (if any)
    place: List[str]  # Where the event occurred


@dataclass
class Defeat(ConflictEvent):
    """{wikievents_eae_defeat}"""

    mention: str  # The text span that most clearly expresses (triggers) the event
    victor: List[str]  # The entity defeating (the defeater)
    defeated: List[str]  # The entity being defeated (the defeated)
    place: List[str]  # Where the event occurred


@dataclass
class Demonstrate(ConflictEvent):
    """{wikievents_eae_demonstrate}"""

    mention: str  # The text span that most clearly expresses (triggers) the event
    demonstrator: List[str]  # The entity demonstrating
    regulator: List[str]  #  The entity regulating the demonstration
    topic: List[str]  # The topic of the demonstration
    target: List[str]  # The entity being demonstrated against


@dataclass
class Contact(ContactEvent):
    """{wikievents_eae_contact}"""

    mention: str  # The text span that most clearly expresses (triggers) the event
    participants: List[str]  # The entities in contact
    instrument: List[str]  # The object used to contact
    topic: List[str]  # The topic of the contact
    place: List[str]  # Where the event occurred


@dataclass
class RequestCommand(ContactEvent):
    """{wikievents_eae_request_command}"""

    mention: str  # The text span that most clearly expresses (triggers) the event
    communicator: List[str]  # The entity communicating
    receptor: List[str]  # The entity receiving the communication
    topic: List[str]  # The topic of the communication
    place: List[str]  # Where the event occurred


@dataclass
class ThreatenCoerce(ContactEvent):
    """{wikievents_eae_threaten_coerce}"""

    mention: str  # The text span that most clearly expresses (triggers) the event
    communicator: List[str]  # The entity threatening
    recipient: List[str]  # The entity being threatened
    place: List[str]  # Where the event occurred


@dataclass
class ImpedeInterfereWith(ControlEvent):
    """{wikievents_eae_impede_interfere_with}"""

    mention: str  # The text span that most clearly expresses (triggers) the event
    impeder: List[str]  # The entity impeding
    place: List[str]  # Where the event occurred


@dataclass
class Crash(DisasterEvent):
    """{wikievents_eae_crash}"""

    mention: str  # The text span that most clearly expresses (triggers) the event
    vehicle: List[str]  # The vehicle being driven
    object: List[str]  # The object crashed into
    place: List[str]  # Where the event occurred


@dataclass
class DiseaseOutbreak(DisasterEvent):
    """{wikievents_eae_disease_outbreak}"""

    mention: str  # The text span that most clearly expresses (triggers) the event
    disease: List[str]  # The disease being outbreak
    victim: List[str]  # The entity being infected
    place: List[str]  # Where the event occurred


@dataclass
class GenericCrime(GenericCrimeEvent):
    """{wikievents_eae_generic_crime}"""

    mention: str  # The text span that most clearly expresses (triggers) the event
    perpetrator: List[str]  # The entity perpetrating the crime
    victim: List[str]  # The entity being perpetrator
    place: List[str]  # Where the event occurred


@dataclass
class Acquit(JusticeEvent):
    """{wikievents_eae_acquit}"""

    mention: str  # The text span that most clearly expresses (triggers) the event
    defendant: List[str]  # The entity being acquitted


@dataclass
class ArrestJailDetain(JusticeEvent):
    """{wikievents_eae_arrest_jail_detain}"""

    mention: str  # The text span that most clearly expresses (triggers) the event
    jailer: List[str]  # The entity jailing
    detainee: List[str]  # The entity being detained
    place: List[str]  # Where the event occurred


@dataclass
class ChargeIndict(JusticeEvent):
    """{wikievents_eae_charge_indict}"""

    mention: str  # The text span that most clearly expresses (triggers) the event
    defendant: List[str]  # The entity being charged or indicted
    prosecutor: List[str]  # The entity prosecuting
    judge_court: List[str]  # The entity charging or indicting
    crime: List[str]  # The crime being charged
    place: List[str]  # Where the event occurred


@dataclass
class Convict(JusticeEvent):
    """{wikievents_eae_convict}"""

    mention: str  # The text span that most clearly expresses (triggers) the event
    judge_court: List[str]  # The entity convicting
    defendant: List[str]  # The entity being convicted
    place: List[str]  # Where the event occurred


@dataclass
class InvestigateCrime(JusticeEvent):
    """{wikievents_eae_investigate_crime}"""

    mention: str  # The text span that most clearly expresses (triggers) the event
    investigator: List[str]  # The entity investigating
    defendant: List[str]  # The entity being investigated
    crime: List[str]  # The crime being investigated
    place: List[str]  # Where the event occurred


@dataclass
class ReleaseParole(JusticeEvent):
    """{wikievents_eae_release_parole}"""

    mention: str  # The text span that most clearly expresses (triggers) the event
    judge_court: List[str]  # The entity releasing
    defendant: List[str]  # The entity being released
    place: List[str]  # Where the event occurred


@dataclass
class Sentence(JusticeEvent):
    """{wikievents_eae_sentence}"""

    mention: str  # The text span that most clearly expresses (triggers) the event
    judge_court: List[str]  # The entity sentence
    defendant: List[str]  # The entity being sentence
    place: List[str]  # Where the event occurred


@dataclass
class TrialHearing(JusticeEvent):
    """{wikievents_eae_trial_hearing}"""

    mention: str  # The text span that most clearly expresses (triggers) the event
    prosecutor: List[str]  # The entity prosecuting
    defendant: List[str]  # The entity being prosecuted
    judge_court: List[str]  # The entity trialing
    place: List[str]  # Where the event occurred


@dataclass
class Die(LifeEvent):
    """{wikievents_eae_die}"""

    mention: str  # The text span that most clearly expresses (triggers) the event
    victim: List[str]  # The entity being killed
    killer: List[str]  # The entity killing the victim
    place: List[str]  # Where the event occurred


@dataclass
class Infect(LifeEvent):
    """{wikievents_eae_infect}"""

    mention: str  # The text span that most clearly expresses (triggers) the event
    victim: List[str]  # The entity being infected


@dataclass
class Injure(LifeEvent):
    """{wikievents_eae_injure}"""

    mention: str  # The text span that most clearly expresses (triggers) the event
    victim: List[str]  # The entity being injured
    injurer: List[str]  #  The entity injuring the victim
    instrument: List[str]  # The instrument used to injure the victim
    body_part: List[str]  # The body part injured
    place: List[str]  # Where the event occurred


@dataclass
class Intervention(MedicalEvent):
    """{wikievents_eae_intervention}"""

    mention: str  # The text span that most clearly expresses (triggers) the event
    treater: List[str]  # The entity performing the intervention
    patient: List[str]  # The entity being intervened upon
    place: List[str]  # Where the event occurred


@dataclass
class Evacuation(MovementTransportEvent):
    """{wikievents_eae_evacuation}"""

    mention: str  # The text span that most clearly expresses (triggers) the event
    transporter: List[str]  # The entity transporting
    passenger_artifact: List[str]  # The entity being transported
    origin: List[str]  # The origin of the event
    destination: List[str]  # The destination of the event


@dataclass
class IllegalTransportation(MovementTransportEvent):
    """{wikievents_eae_illegal_transportation}"""

    mention: str  # The text span that most clearly expresses (triggers) the event
    transporter: List[str]  # The entity transporting
    passenger_artifact: List[str]  # The entity being transported
    vehicle: List[str]  # The vehicle used
    origin: List[str]  # The origin of the event
    destination: List[str]  # The destination of the event


@dataclass
class PreventPassage(MovementTransportEvent):
    """{wikievents_eae_prevent_passage}"""

    mention: str  # The text span that most clearly expresses (triggers) the event
    transporter: List[str]  # The entity transporting
    passenger_artifact: List[str]  # The entity being transported
    vehicle: List[str]  # The vehicle used
    preventer: List[str]  # The transportation preventer
    origin: List[str]  # The origin of the event
    destination: List[str]  # The destination of the event


@dataclass
class Transportation(MovementTransportEvent):
    """{wikievents_eae_transportation}"""

    mention: str  # The text span that most clearly expresses (triggers) the event
    transporter: List[str]  # The entity transporting
    passenger_artifact: List[str]  # The entity being transported
    vehicle: List[str]  # The vehicle used
    origin: List[str]  # The origin of the event
    destination: List[str]  # The destination of the event


@dataclass
class EndPosition(PersonnelEvent):
    """{wikievents_eae_end_position}"""

    mention: str  # The text span that most clearl expresses (triggers) the event
    employee: List[str]  # The person ending the job
    organization: List[str]  # Place of employment


@dataclass
class StartPosition(PersonnelEvent):
    """{wikievents_eae_start_position}"""

    mention: str  # The text span that most clearl expresses (triggers) the event
    employee: List[str]  # The person starting the job
    organization: List[str]  # Place of employment
    position: List[str]  # The position started
    place: List[str]  # Where the event occurred


@dataclass
class Donation(TransactionEvent):
    """{wikievents_eae_donation}"""

    mention: str  # The text span that most clearl expresses (triggers) the event
    giver: List[str]  # The entity donating
    recipient: List[str]  # The entity receiving the money
    artifact_money: List[str]  # The artifact or money given


@dataclass
class ExchangeBuySell(TransactionEvent):
    """{wikievents_eae_exchange_buy_sell}"""

    mention: str  # The text span that most clearl expresses (triggers) the event
    giver: List[str]  # The entity selling
    recipient: List[str]  # The entity buying
    adquired_entity: List[str]  # The entity being bought or sold
    payment_barter: List[str]  # The artifact or money given


EVENT_DEFINITIONS: List[Type] = [
    DamageDestroy,
    DisableDefuse,
    Dismantle,
    ManufactureAssemble,
    IdentifyCategorize,
    Inspection,
    Research,
    TeachingTrainingLearning,
    Attack,
    Defeat,
    Demonstrate,
    Contact,
    RequestCommand,
    ThreatenCoerce,
    ImpedeInterfereWith,
    Crash,
    DiseaseOutbreak,
    GenericCrime,
    Acquit,
    ArrestJailDetain,
    ChargeIndict,
    Convict,
    InvestigateCrime,
    ReleaseParole,
    Sentence,
    TrialHearing,
    Die,
    Infect,
    Injure,
    Intervention,
    Evacuation,
    IllegalTransportation,
    PreventPassage,
    Transportation,
    EndPosition,
    StartPosition,
    Donation,
    ExchangeBuySell,
]

FINE_TO_COARSE_EVENTS: Dict[Type, Type] = {_def: _def.__base__ for _def in EVENT_DEFINITIONS}
COARSE_TO_FINE_EVENTS: Dict[Type, List[Type]] = {}
for fine, coarse in FINE_TO_COARSE_EVENTS.items():
    if coarse not in COARSE_TO_FINE_EVENTS:
        COARSE_TO_FINE_EVENTS[coarse] = []
    COARSE_TO_FINE_EVENTS[coarse].append(fine)
