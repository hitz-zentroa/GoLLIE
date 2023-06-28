from typing import List, Union

from ..utils_typing import Event, dataclass


"""Event definitions

The official guidelines are not public. All event definitions are taken from:
https://github.com/raspberryice/gen-arg/blob/main/aida_ontology_cleaned.csv
"""


@dataclass
class ArtifactFailure(Event):
    """{rams_artifactfailure}"""

    mention: str  # The text span that most clearly expresses (triggers) the event
    subtype: Union[str, None]  # Possible event subtype.
    artifact: List[str]  # The artifact involved
    instrument: List[str]  # The reason (instrument) for the artifact fail
    place: List[str]  # Where the fail occurred


@dataclass
class DamageDestroy(Event):
    """{rams_damagedestroy}"""

    mention: str  # The text span that most clearly expresses (triggers) the event
    subtype: Union[str, None]  # Possible event subtype.
    agent: List[str]  # The damager or destroyer
    artifact: List[str]  # The damaged or destroyed artifact
    instrument: List[str]  # The instrument used for damaging or destroying
    place: List[str]  # Where the event takes place


@dataclass
class Shortage(Event):
    """{rams_shortage}"""

    mention: str  # The text span that most clearly expresses (triggers) the event
    subtype: Union[str, None]  # Possible event subtype.
    experiencer: List[str]  # The entity experiencing the shortage of supply
    supply: List[str]  # The entity being supplied
    place: List[str]  # Where the event takes place


@dataclass
class Attack(Event):
    """{rams_attack}"""

    mention: str  # The text span that most clearly expresses (triggers) the event
    subtype: Union[str, None]  # Possible event subtype
    attacker: List[str]  # The attacker
    target: List[str]  # The target of the attack
    instrument: List[str]  # The instrument used in the attack
    place: List[str]  # Where the event takes place
    artifact: List[str]  # Only in "StealRobHijack". The artifact being stolen, ...


@dataclass
class Coup(Event):
    """{rams_coup}"""

    mention: str  # The text span that most clearly expresses (triggers) the event
    subtype: Union[str, None]  # Possible event subtype
    deposed_entity: List[str]  # The entity being deposed
    deposing_entity: List[str]  # The deposing entity
    place: List[str]  # Where the event takes place


@dataclass
class Demonstrate(Event):
    """{rams_demonstrate}"""

    mention: str  # The text span that most clearly expresses (triggers) the event
    subtype: Union[str, None]  # Possible event subtype
    demonstrator: List[str]  # The Demonstrators that take part in the protest
    place: List[str]  # Where the protest takes place


@dataclass
class Yield(Event):
    """{rams_yield}"""

    mention: str  # The text span that most clearly expresses (triggers) the event
    subtype: Union[str, None]  # Possible event subtype
    agent: List[str]  # The yielder, surrender or retreater agent
    recipient: List[str]  # To who/where the agent yields or surrenders
    place: List[str]  # Where the event takes place
    origin: List[str]  # Only in "Retreat". From where the agent is retreated.
    destination: List[str]  # Only in "Retreat". To where the agent is retreated.


@dataclass
class Collaborate(Event):
    """{rams_collaborate}"""

    mention: str  # The text span that most clearly expresses (triggers) the event
    subtype: Union[str, None]  # Possible event subtype
    participants: List[str]  # The participants of the Event
    place: List[str]  # Where the Event takes place


@dataclass
class CommandOrder(Event):
    """{rams_commandorder}"""

    mention: str  # The text span that most clearly expresses (triggers) the event
    subtype: Union[str, None]  # Possible event subtype
    communicator: List[str]  # The Communicator agent
    recipient: List[str]  # The recipient of the communication event
    topic: List[str]  # The topic of the communication
    place: List[str]  # Where the Event takes place


@dataclass
class CommitmentPromiseExpressIntent(Event):
    """{rams_commitmentpromiseexpressintent}"""

    mention: str  # # The text span that most clearly expresses (triggers) the event
    subtype: Union[str, None]  # Possible event subtype
    communicator: List[str]  # The Communicator agent
    recipient: List[str]  # The recipient of the communication event
    topic: List[str]  # The topic of the communication
    place: List[str]  # Where the event takes place


@dataclass
class Discussion(Event):
    """{rams_discussion}"""

    mention: str  # The text span that most clearly expresses (triggers) the event
    subtype: Union[str, None]  # Possible event subtype
    participants: List[str]  # The participants of the discussion
    place: List[str]  # Where the event takes place


@dataclass
class FuneralVigil(Event):
    """{rams_funeralvigil}"""

    mention: str  # The text span that most clearly expresses (triggers) the event
    subtype: Union[str, None]  # Possible event subtype
    participants: List[str]  # The participants of the communicative event
    deceased: List[str]  # The deceased person(s)
    place: List[str]  # Where the event takes place


@dataclass
class MediaStatement(Event):
    """{rams_mediastatement}"""

    mention: str  # The text span that most clearly expresses (triggers) the event
    subtype: Union[str, None]  # Possible event subtype
    communicator: List[str]  # The communication agent
    recipient: List[str]  # The recipient of the communication event
    place: List[str]  # Where the event takes place


@dataclass
class Negotiate(Event):
    """{rams_negotiate}"""

    mention: str  # The text span that most clearly expresses (triggers) the event
    subtype: Union[str, None]  # Possible event subtype
    participants: List[str]  # The participants of the negotiation
    topic: List[str]  # The topic of the negotiation
    place: List[str]  # Where the event takes place


@dataclass
class Prevarication(Event):
    """{rams_prevarication}"""

    mention: str  # The text span that most clearly expresses (triggers) the event
    subtype: Union[str, None]  # Possible event subtype
    communicator: List[str]  # The communicator of the prevarication
    recipient: List[str]  # The recipient of the communication event
    topic: List[str]  # The topic of the prevarication
    place: List[str]  # Where the event takes place


@dataclass
class PublicStatementInPerson(Event):
    """{rams_publicstatementinperson}"""

    mention: str  # The text span that most clearly expresses (triggers) the event
    subtype: Union[str, None]  # Possible event subtype
    communicator: List[str]  # The communicator of the public statement
    recipient: List[str]  # The recipient of the statement
    place: List[str]  # Where the event takes place


@dataclass
class RequestAdvice(Event):
    """{rams_requestadvice}"""

    mention: str  # The text span that most clearly expresses (triggers) the event
    subtype: Union[str, None]  # Possible event subtype
    communicator: List[str]  # The communicator of the request or advice
    recipient: List[str]  # The recipient of the request or advice
    topic: List[str]  # The topic requested or adviced
    place: List[str]  # Where the event takes place


@dataclass
class ThreatenCoerce(Event):
    """{rams_threatencoerce}"""

    mention: str  # The text span that most clearly expresses (triggers) the event
    subtype: Union[str, None]  # Possible event subtype
    communicator: List[str]  # The threatening or coercing agent
    recipient: List[str]  # The threatened or coerced entity
    topic: List[str]  # The topic of the threat or coerce
    place: List[str]  # Where the event takes place


@dataclass
class AccidentCrash(Event):
    """{rams_accidentcrash}"""

    mention: str  # The text span that most clearly expresses (triggers) the event
    subtype: Union[str, None]  # Possible event subtype
    driver_or_passengers: List[str]  # The driven/passengers of the vehicle
    vehicle: List[str]  # The crashed vehicle
    crash_object: List[str]  # The object to which the vehicle crashed
    place: List[str]  # Where the event takes place


@dataclass
class DiseaseOutbreak(Event):
    """{rams_diseaseoutbreak}"""

    mention: str  # The text span that most clearly expresses (triggers) the event
    subtype: Union[str, None]  # Possible event subtype
    disease: List[str]  # The disease of the outbreak
    victim: List[str]  # The victims of the outbreak
    place: List[str]  # Where the event takes place


@dataclass
class FireExplosion(Event):
    """{rams_fireexplosion}"""

    mention: str  # The text span that most clearly expresses (triggers) the event
    subtype: Union[str, None]  # Possible event subtype
    fire_explosion_object: List[str]  # The object that caught fire or exploded
    instrument: List[str]  # The instrument used to generate the explosion
    place: List[str]  # Where the event takes place


@dataclass
class GenericCrime(Event):
    """{rams_genericcrime}"""

    mention: str  # The text span that most clearly expresses (triggers) the event
    subtype: Union[str, None]  # Possible event subtype
    perpetrator: List[str]  # The person commiting the crime
    victim: List[str]  # The victim of the crime
    place: List[str]  # Where the event takes place


@dataclass
class Agreement(Event):
    """{rams_agreement}"""

    mention: str  # The text span that most clearly expresses (triggers) the event
    subtype: Union[str, None]  # Possible event subtype
    participants: List[str]  # Only in "Accept" or None. List of participants
    rejecter_nullifier: List[str]  # Only in "RejectNullify". The rejecter or nullifier.
    violator: List[str]  # Only in "Violate". The agreement violator.
    other_participant: List[str]  # Only in "RejectNullify" or "Violate". The rest.
    place: List[str]  # Where the event takes place


@dataclass
class Convene(Event):
    """{rams_convene}"""

    mention: str  # The text span that most clearly expresses (triggers) the event
    subtype: Union[str, None]  # Possible event subtype
    convener: List[str]  # The convener
    convened_entity: List[str]  # The convened entity
    place: List[str]  # Where the event takes place


@dataclass
class Formation(Event):
    """{rams_formation}"""

    mention: str  # The text span that most clearly expresses (triggers) the event
    subtype: Union[str, None]  # Possible event subtype
    gpe: List[str]  # Only in "Start" or None. The founded Geo-Political entity
    participants: List[str]  # Only in "Merge". The merged participants.
    founder: List[str]  # Only in "Start" or None. The founder of the GPE.
    place: List[str]  # Where the event takes place


@dataclass
class Legislate(Event):
    """{rams_legislate}"""

    mention: str  # The text span that most clearly expresses (triggers) the event
    subtype: Union[str, None]  # Possible event subtype
    government_body: List[str]  # The Government body that enacted the law
    law: List[str]  # The law enacted by the government
    place: List[str]  # Where the event takes place


@dataclass
class Spy(Event):
    """{rams_spy}"""

    mention: str  # The text span that most clearly expresses (triggers) the event
    subtype: Union[str, None]  # Possible event subtype
    spy: List[str]  # The spying entity
    observed_entity: List[str]  # The entity being observed (spied)
    beneficiary: List[str]  # The entity that benefits from the information
    place: List[str]  # Where the event takes place


@dataclass
class Vote(Event):
    """{rams_vote}"""

    mention: str  # The text span that most clearly expresses (triggers) the event
    subtype: Union[str, None]  # Possible event subtype
    voter: List[str]  # The person or entity who votes.
    candidate: List[str]  # The candidate, entity being voted.
    ballot: List[str]  # The ballot
    result: List[str]  # The result of the ballot
    preventer: List[str]  # Only in "PreventVote". The vote preventer.
    place: List[str]  # Where the event takes place


@dataclass
class SensoryObserve(Event):
    """{rams_sensoryobserve}"""

    mention: str  # The text span that most clearly expresses (triggers) the event
    subtype: Union[str, None]  # Possible event subtype
    observer: List[str]  # The observer entity
    observed_entity: List[str]  # The observed entity
    place: List[str]  # Where the event takes place


@dataclass
class TargetAimAt(Event):
    """{rams_targetaimat}"""

    mention: str  # The text span that most clearly expresses (triggers) the event
    subtype: Union[str, None]  # Possible event subtype
    targeter: List[str]  # The agent of the event
    target: List[str]  # The entity being physically targeted
    instrument: List[str]  # The instrument used
    place: List[str]  # Where the event takes place


@dataclass
class ArrestJailDetain(Event):
    """{rams_arrestjaildetain}"""

    mention: str  # The text span that most clearly expresses (triggers) the event
    subtype: Union[str, None]  # Possible event subtype
    jailer: List[str]  # The person who arrested or jailed the detainee
    detainee: List[str]  # The person being arrested or jailed
    crime: List[str]  # The reason (crime) for the arresting or jailing
    place: List[str]  # Where the event takes place


@dataclass
class InitiateJudicialProcess(Event):
    """{rams_initiatejudicialprocess}"""

    mention: str  # The text span that most clearly expresses (triggers) the event
    subtype: Union[str, None]  # Possible event subtype
    prosecutor: List[str]  # The prosecutor entity
    defendant: List[str]  # The defendant of the process
    judge_court: List[str]  # The judge or court in charge
    crime: List[str]  # The crime
    place: List[str]  # Where the event takes place


@dataclass
class InvestigateCrime(Event):
    """{rams_investigatecrime}"""

    mention: str  # The text span that most clearly expresses (triggers) the event
    subtype: Union[str, None]  # Possible event subtype
    investigator: List[str]  # The investigator of the crime
    defendant: List[str]  # The person investigated
    crime: List[str]  # The crime investigated
    place: List[str]  # Where the event takes place


@dataclass
class JudicialConsequences(Event):
    """{rams_judicialconsequences}"""

    mention: str  # The text span that most clearly expresses (triggers) the event
    subtype: Union[str, None]  # Possible event subtype
    judge_court: List[str]  # The judge, court, extraditer or executioner
    defendant: List[str]  # The defendant of the judicial process
    crime: List[str]  # The crime
    origin: List[str]  # Only in "Extradite". The location of origin
    destination: List[str]  # Only in "Extradite". The location of destination.
    place: List[str]  # Where the event takes place


@dataclass
class Die(Event):
    """{rams_die}"""

    mention: str  # The text span that most clearly expresses (triggers) the event
    subtype: Union[str, None]  # Possible event subtype
    victim: List[str]  # The person who died
    killer: List[str]  # If any, the killer
    medical_issue: List[str]  # If died by medicall issues, the issue
    instrument: List[str]  # If killed with an instrument, the instrument
    place: List[str]  # Where the event takes place


@dataclass
class Injure(Event):
    """{rams_injure}"""

    mention: str  # The text span that most clearly expresses (triggers) the event
    subtype: Union[str, None]  # Possible event subtype
    victim: List[str]  # The injured person
    medical_issue: List[str]  # If any, the medical issue
    disease: List[str]  # If any, the disease causing the medical issue
    injurer: List[str]  # If any, the agent causing the injure
    instrument: List[str]  # The instrument used to injure
    place: List[str]  # Where the event takes place


@dataclass
class ManufactureArtifact(Event):
    """{rams_manufactureartifact}"""

    mention: str  # The text span that most clearly expresses (triggers) the event
    subtype: Union[str, None]  # Possible event subtype
    manufacturer: List[str]  # The entity that created the artifact
    artifact: List[str]  # The artifact being created
    instrument: List[str]  # The instrument used to create the artifact
    place: List[str]  # Where the event takes place


@dataclass
class MedicalIntervention(Event):
    """{rams_medicalintervention}"""

    mention: str  # The text span that most clearly expresses (triggers) the event
    subtype: Union[str, None]  # Possible event subtype
    treater: List[str]  # The entity in charge of the intervention
    patient: List[str]  # The treated entity
    medical_issue: List[str]  # The reason for the intervention
    instrument: List[str]  # The instrument used on the intervention
    place: List[str]  # Where the event takes place


@dataclass
class TransportArtifact(Event):
    """{rams_transportartifact}"""

    mention: str  # The text span that most clearly expresses (triggers) the event
    subtype: Union[str, None]  # Possible event subtype
    transporter: List[str]  # The entity carrying the transport event
    artifact: List[str]  # The entity being transported
    vehicle: List[str]  # The vehicle used to transport the entity
    origin: List[str]  # The origin place
    destination: List[str]  # The destination place
    hidding_place: List[str]  # Only in "Hide". The place to hide the artifact.
    preventer: List[str]  # Only in "PreventEntry" and "PreventExit". The preventer.


@dataclass
class TransportPerson(Event):
    """{rams_transportperson}"""

    mention: str  # The text span that most clearly expresses (triggers) the event
    subtype: Union[str, None]  # Possible event subtype
    transporter: List[str]  # The entity carrying the transport event
    passenger: List[str]  # If any, the passenger transported
    vehicle: List[str]  # The vehicle used to transport the entity
    origin: List[str]  # The origin place
    destination: List[str]  # The destination place
    granter: List[str]  # Only in "GrantedAsylum". The granter of asylum permission
    hidding_place: List[str]  # Only in "Hide". The place to hide the passenger.
    preventer: List[str]  # Only in "PreventEntry" and "PreventExit". The preventer.


@dataclass
class Elect(Event):
    """{rams_elect}"""

    mention: str  # The text span that most clearly expresses (triggers) the event
    subtype: Union[str, None]  # Possible event subtype
    voter: List[str]  # The entity who elects the candidate
    candidate: List[str]  # The candidate being elected
    place: List[str]  # Where the event takes place


@dataclass
class EndPossition(Event):
    """{rams_endpossition}"""

    mention: str  # The text span that most clearly expresses (triggers) the event
    subtype: Union[str, None]  # Possible event subtype
    employee: List[str]  # The entity that has stopped working for the organization
    organization: List[str]  # The organization to which the employee worked for
    place: List[str]  # Where the event takes place


@dataclass
class StartPossition(Event):
    """{rams_startpossition}"""

    mention: str  # The text span that most clearly expresses (triggers) the event
    subtype: Union[str, None]  # Possible event subtype
    employee: List[str]  # The entity that has started working on the organization
    organization: List[str]  # The organization to which the employee works
    place: List[str]  # Where the event takes place


@dataclass
class Transaction(Event):
    """{rams_transaction}"""

    mention: str  # The text span that most clearly expresses (triggers) the event
    subtype: Union[str, None]  # Possible event subtype
    participants: List[str]  # Only if subtype is None. The participants.
    giver: List[str]  # The entity giving the artifact
    recipient: List[str]  # The entity receiving the artifact
    beneficiary: List[str]  # The entity that benefits from the transaction (other than recipient)
    artifact: List[str]  # The entity being transferred (artifact, money or territory)
    preventer: List[str]  # Only in "EmbargoSanction". The entity that prevents the transaction.
    place: List[str]  # Where the event takes place


@dataclass
class TransferMoney(Event):
    """{rams_transfermoney}"""

    mention: str  # The text span that most clearly expresses (triggers) the event
    subtype: Union[str, None]  # Possible event subtype
    giver: List[str]  # The entity giving the money
    recipient: List[str]  # The entity receiving the money
    beneficiary: List[str]  # The entity that benefits from the transaction (other than recipient)
    money: List[str]  # The money amount
    preventer: List[str]  # Only in "EmbargoSanction". The entity that prevents the transaction.
    place: List[str]  # Where the event takes place


@dataclass
class TransferOwnership(Event):
    """{rams_transferownership}"""

    mention: str  # The text span that most clearly expresses (triggers) the event
    subtype: Union[str, None]  # Possible event subtype
    giver: List[str]  # The entity giving the artifact
    recipient: List[str]  # The entity receiving the artifact
    beneficiary: List[str]  # The entity that benefits from the transaction (other than recipient)
    artifact: List[str]  # The artifact being transferred
    preventer: List[str]  # Only in "EmbargoSanction". The entity that prevents the transaction.
    place: List[str]  # Where the event takes place


EVENT_DEFINITIONS: List[Event] = [
    ArtifactFailure,
    DamageDestroy,
    Shortage,
    Attack,
    Coup,
    Demonstrate,
    Yield,
    Collaborate,
    CommandOrder,
    CommitmentPromiseExpressIntent,
    Discussion,
    FuneralVigil,
    MediaStatement,
    Negotiate,
    Prevarication,
    PublicStatementInPerson,
    RequestAdvice,
    ThreatenCoerce,
    AccidentCrash,
    DiseaseOutbreak,
    FireExplosion,
    GenericCrime,
    Agreement,
    Convene,
    Formation,
    Legislate,
    Spy,
    Vote,
    SensoryObserve,
    TargetAimAt,
    ArrestJailDetain,
    InitiateJudicialProcess,
    InvestigateCrime,
    JudicialConsequences,
    Die,
    Injure,
    ManufactureArtifact,
    MedicalIntervention,
    TransportArtifact,
    TransportPerson,
    Elect,
    EndPossition,
    StartPossition,
    Transaction,
    TransferMoney,
    TransferOwnership,
]

# __all__ = list(map(str, [*EVENT_DEFINITIONS]))
