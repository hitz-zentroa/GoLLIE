from typing import List, Union

from ..utils_typing import Event, dataclass

"""Event definitions

The oficial guidelines are not public. All event definitions are taken from:
https://github.com/raspberryice/gen-arg/blob/main/aida_ontology_cleaned.csv
"""


@dataclass
class ArtifactFailure(Event):
    """An ArtifactFailure (artifact) Event occurs whenever a (mechanical) Artifact
    failed due to some Instrument at some Place.

    The possible Event subtypes are: "MechanicalFailure" or None.
    """

    mention: str  # The text span that most clearly expresses (triggers) the event
    subtype: Union[str, None]  # Possible event subtype.
    artifact: List[str]  # The artifact involved
    instrument: List[str]  # The reason (instrument) for the artifact fail
    place: List[str]  # Where the fail occurred


@dataclass
class DamageDestroy(Event):
    """A DamageDestroy (artifact) Event occurs when an Artifact is damaged or destroyed
    by some Agent (damager or destroyer) using an Instrument at some Place.

    The possible Event subtypes are: "Damage", "Destroy" or None.
    """

    mention: str  # The text span that most clearly expresses (triggers) the event
    subtype: Union[str, None]  # Possible event subtype.
    agent: List[str]  # The damager or destroyer
    artifact: List[str]  # The damaged or destroyed artifact
    instrument: List[str]  # The instrument used for damaging or destroying
    place: List[str]  # Where the event takes place


@dataclass
class Shortage(Event):
    """A Shortage (artifact) Event occurs when a Experiencer experienced a shortage of
    Supply in some Place.

    The only possible event subtype is: "Shortage".
    """

    mention: str  # The text span that most clearly expresses (triggers) the event
    subtype: Union[str, None]  # Possible event subtype.
    experiencer: List[str]  # The entity experiencing the shortage of supply
    supply: List[str]  # The entity being supplied
    place: List[str]  # Where the event takes place


@dataclass
class Attack(Event):
    """An Attack (conflict) Event occurs when an Attacker attacks a Target with some
    Instrument at some Place.

    The possible Event subtypes are: "AirStrikeMissileStrike",
    "BiologicalChemicalPoisonAttack", "Bombing", "FireArmAttack", "Hanging",
    "Invade", "SelfDirectedBattle", "SetFire", "Stabbing", "StealRobHijack",
    "Strangling" or None.
    """

    mention: str  # The text span that most clearly expresses (triggers) the event
    subtype: Union[str, None]  # Possible event subtype
    attacker: List[str]  # The attacker
    target: List[str]  # The target of the attack
    instrument: List[str]  # The instrument used in the attack
    place: List[str]  # Where the event takes place
    artifact: List[str]  # Only in "StealRobHijack". The artifact being stolen, ...


@dataclass
class Coup(Event):
    """A Coup (conflict) Event occurs when a DeposedEntity was desposed by a
    DeposingEntity at some Place.

    The only possible event subtype is: "Coup".
    """

    mention: str  # The text span that most clearly expresses (triggers) the event
    subtype: Union[str, None]  # Possible event subtype
    deposed_entity: List[str]  # The entity being deposed
    deposing_entity: List[str]  # The deposing entity
    place: List[str]  # Where the event takes place


@dataclass
class Demonstrate(Event):
    """A Demonstrate (conflict) Event occurs when a Demonstrator(s) protest at some
    Place.

    The possible Event subtypes are: "MarchProtestPoliticalGathering" or None.
    """

    mention: str  # The text span that most clearly expresses (triggers) the event
    subtype: Union[str, None]  # Possible event subtype
    demonstrator: List[str]  # The Demonstrators that take part in the protest
    place: List[str]  # Where the protest takes place


@dataclass
class Yield(Event):
    """A Yield (conflict) Event occurs when an Agent (yielder or surrender)
    yields or surrenders to a Recipient at some Place. But also, when an Agent
    (retreater) retreats from Origin to some Destination.

    The possible Event subtypes are: "Surrender", "Retreat" or None
    """

    mention: str  # The text span that most clearly expresses (triggers) the event
    subtype: Union[str, None]  # Possible event subtype
    agent: List[str]  # The yielder, surrender or retreater agent
    recipient: List[str]  # To who/where the agent yields or surrenders
    place: List[str]  # Where the event takes place
    origin: List[str]  # Only in "Retreat". From where the agent is retreated.
    destination: List[str]  # Only in "Retreat". To where the agent is retreated.


@dataclass
class Collaborate(Event):
    """A Collaborate (contact) Event occurs when some Participants
    communicates (remotely or face-to-face) at some Place.

    The possible Event subtypes are: "Correspondence", "Meet" or None.
    """

    mention: str  # The text span that most clearly expresses (triggers) the event
    subtype: Union[str, None]  # Possible event subtype
    participants: List[str]  # The participants of the Event
    place: List[str]  # Where the Event takes place


@dataclass
class CommandOrder(Event):
    """A CommandOrder (contact) Event occurs when a Communicator communicates
    with/to Recipient about a Topic at some Place.

    The possible Event subtypes are: "Broadcast", "Correspondence", "Meet"
    or None.
    """

    mention: str  # The text span that most clearly expresses (triggers) the event
    subtype: Union[str, None]  # Possible event subtype
    communicator: List[str]  # The Communicator agent
    recipient: List[str]  # The recipient of the communication event
    topic: List[str]  # The topic of the communication
    place: List[str]  # Where the Event takes place


@dataclass
class CommitmentPromiseExpressIntent(Event):
    """A CommitmentPromiseExpressIntent (contact) Event occurs when a Communicator
    commits, promises, expresses an intent to Recipient about a Topic at some Place.

    The possible Event subtypes are: "Broadcast", "Correspondence", "Meet" or None.
    """

    mention: str  # # The text span that most clearly expresses (triggers) the event
    subtype: Union[str, None]  # Possible event subtype
    communicator: List[str]  # The Communicator agent
    recipient: List[str]  # The recipient of the communication event
    topic: List[str]  # The topic of the communication
    place: List[str]  # Where the event takes place


@dataclass
class Discussion(Event):
    """A Discussion (contact) Event occurs when some Participants discuss at some
    place.

    The possible Event subtypes are: "Correspondence", "Meet" or None.
    """

    mention: str  # The text span that most clearly expresses (triggers) the event
    subtype: Union[str, None]  # Possible event subtype
    participants: List[str]  # The participants of the discussion
    place: List[str]  # Where the event takes place


@dataclass
class FuneralVigil(Event):
    """A FuneralVigil (contact) Event occurs when some Participants communicate
    during a funeral or vigil for Deceased at some Place.

    The possible Event subtypes are: "Meet" or None.
    """

    mention: str  # The text span that most clearly expresses (triggers) the event
    subtype: Union[str, None]  # Possible event subtype
    participants: List[str]  # The participants of the communicative event
    deceased: List[str]  # The deceased person(s)
    place: List[str]  # Where the event takes place


@dataclass
class MediaStatement(Event):
    """A MediaStatement (contact) Event occurs when a Communicator communicates
    something on media to some Recipients at some Place.

    The possible Event subtypes are: "Broadcast" or None.
    """

    mention: str  # The text span that most clearly expresses (triggers) the event
    subtype: Union[str, None]  # Possible event subtype
    communicator: List[str]  # The communication agent
    recipient: List[str]  # The recipient of the communication event
    place: List[str]  # Where the event takes place


@dataclass
class Negotiate(Event):
    """A Negotiate (contact) Event occurs when some Participants participate on
    a negotiation about some Topic at some Place.

    The possible Event subtypes are: "Correspondence", "Meet" or None.
    """

    mention: str  # The text span that most clearly expresses (triggers) the event
    subtype: Union[str, None]  # Possible event subtype
    participants: List[str]  # The participants of the negotiation
    topic: List[str]  # The topic of the negotiation
    place: List[str]  # Where the event takes place


@dataclass
class Prevarication(Event):
    """A Prevarication (contact) Event occurs when a Communicator prevaricate about
    some Topic to a Recipient at some Place.

    The possible Event subtypes are: "Broadcast", "Correspondence", "Meet" or None.
    """

    mention: str  # The text span that most clearly expresses (triggers) the event
    subtype: Union[str, None]  # Possible event subtype
    communicator: List[str]  # The communicator of the prevarication
    recipient: List[str]  # The recipient of the communication event
    topic: List[str]  # The topic of the prevarication
    place: List[str]  # Where the event takes place


@dataclass
class PublicStatementInPerson(Event):
    """A PublicStatementInPerson (contact) Event occurs when a Communicator gives
    a public statement to a Recipient at some Place.

    The possible Event subtypes are: "Broadcast" or None.
    """

    mention: str  # The text span that most clearly expresses (triggers) the event
    subtype: Union[str, None]  # Possible event subtype
    communicator: List[str]  # The communicator of the public statement
    recipient: List[str]  # The recipient of the statement
    place: List[str]  # Where the event takes place


@dataclass
class RequestAdvice(Event):
    """A RequestAdvice (contact) Event occurs when a Communicator requests something
    or gives advice about a Topic to a Recipient at some Place.

    The possible Event subtypes are: "Broadcast", "Correspondence", "Meet" or None.
    """

    mention: str  # The text span that most clearly expresses (triggers) the event
    subtype: Union[str, None]  # Possible event subtype
    communicator: List[str]  # The communicator of the request or advice
    recipient: List[str]  # The recipient of the request or advice
    topic: List[str]  # The topic requested or adviced
    place: List[str]  # Where the event takes place


@dataclass
class ThreatenCoerce(Event):
    """A ThreatenCoerce (contact) Event occurs when a Communicator threats or coerces
    a Recipient about a Topic at some Place.

    The possible Event subtypes are: "Broadcast", "Correspondence", "Meet" or None.
    """

    mention: str  # The text span that most clearly expresses (triggers) the event
    subtype: Union[str, None]  # Possible event subtype
    communicator: List[str]  # The threatening or coercing agent
    recipient: List[str]  # The threatened or coerced entity
    topic: List[str]  # The topic of the threat or coerce
    place: List[str]  # Where the event takes place


@dataclass
class AccidentCrash(Event):
    """An AccidentCrash (disaster) Event occurs when a Driver/Passenger in a
    Vehicle crashes into CrashObject at some place.

    The only possible event subtype is: "AccidentCrash".
    """

    mention: str  # The text span that most clearly expresses (triggers) the event
    subtype: Union[str, None]  # Possible event subtype
    driver_or_passengers: List[str]  # The driven/passengers of the vehicle
    vehicle: List[str]  # The crashed vehicle
    crash_object: List[str]  # The object to which the vehicle crashed
    place: List[str]  # Where the event takes place


@dataclass
class DiseaseOutbreak(Event):
    """A DiseaseOutbreak (disaster) Event occurs when a Disease broke out
    among some Victims at some Place.

    The only possible event subtype is: "DiseaseOutbreak".
    """

    mention: str  # The text span that most clearly expresses (triggers) the event
    subtype: Union[str, None]  # Possible event subtype
    disease: List[str]  # The disease of the outbreak
    victim: List[str]  # The victims of the outbreak
    place: List[str]  # Where the event takes place


@dataclass
class FireExplosion(Event):
    """A FireExplosion (disaster) Event occurs when a FireExplosionObject caught fire
    or exploded from an Instrument at some Place.

    The only possible event subtype is: "FireExplosion".
    """

    mention: str  # The text span that most clearly expresses (triggers) the event
    subtype: Union[str, None]  # Possible event subtype
    fire_explosion_object: List[str]  # The object that caught fire or exploded
    instrument: List[str]  # The instrument used to generate the explosion
    place: List[str]  # Where the event takes place


@dataclass
class GenericCrime(Event):
    """A GenericCrime (crime) Event occurs when a Perpetrator commits a crime against
    a Victim at some Place.

    The only possible event subtype is: "GenericCrime".
    """

    mention: str  # The text span that most clearly expresses (triggers) the event
    subtype: Union[str, None]  # Possible event subtype
    perpetrator: List[str]  # The person commiting the crime
    victim: List[str]  # The victim of the crime
    place: List[str]  # Where the event takes place


@dataclass
class Agreement(Event):
    """An Agreement (government) Event occurs when a Participant signed, rejected,
    nullified or violated an agreement at some Place.

    The possible Event subtypes are: "Accept", "RejectNullify", "Violate" or None.
    """

    mention: str  # The text span that most clearly expresses (triggers) the event
    subtype: Union[str, None]  # Possible event subtype
    participants: List[str]  # Only in "Accept" or None. List of participants
    rejecter_nullifier: List[str]  # Only in "RejectNullify". The rejecter or nullifier.
    violator: List[str]  # Only in "Violate". The agreement violator.
    other_participant: List[str]  # Only in "RejectNullify" or "Violate". The rest.
    place: List[str]  # Where the event takes place


@dataclass
class Convene(Event):
    """A Convene (government) Event occurs when a Convener convened a ConvenedEntity
    at some Place.

    The only possible event subtype is: "Convene".
    """

    mention: str  # The text span that most clearly expresses (triggers) the event
    subtype: Union[str, None]  # Possible event subtype
    convener: List[str]  # The convener
    convened_entity: List[str]  # The convened entity
    place: List[str]  # Where the event takes place


@dataclass
class Formation(Event):
    """A Formation (government) Event occurs when some Participant (GPEs) are merged or
    when a GPE is formed/started by a Founder at some Place.

    The possible Event subtypes are: "Merge", "Start", None.
    """

    mention: str  # The text span that most clearly expresses (triggers) the event
    subtype: Union[str, None]  # Possible event subtype
    gpe: List[str]  # Only in "Start" or None. The founded Geo-Political entity
    participants: List[str]  # Only in "Merge". The merged participants.
    founder: List[str]  # Only in "Start" or None. The founder of the GPE.
    place: List[str]  # Where the event takes place


@dataclass
class Legislate(Event):
    """A Legislate (government) Event occurs when a Government legislature enacted
    a Law in some Place.

    The only possible event subtype is: "Legislate".
    """

    mention: str  # The text span that most clearly expresses (triggers) the event
    subtype: Union[str, None]  # Possible event subtype
    government_body: List[str]  # The Government body that enacted the law
    law: List[str]  # The law enacted by the government
    place: List[str]  # Where the event takes place


@dataclass
class Spy(Event):
    """An Spy (government) Event occurs when a Spy spied on a ObservedEntity to the
    benefit of a Beneficiary in some Place.

    The only possible event subtype is: "Spy".
    """

    mention: str  # The text span that most clearly expresses (triggers) the event
    subtype: Union[str, None]  # Possible event subtype
    spy: List[str]  # The spying entity
    observed_entity: List[str]  # The entity being observed (spied)
    beneficiary: List[str]  # The entity that benefits from the information
    place: List[str]  # Where the event takes place


@dataclass
class Vote(Event):
    """A Vote (government) Event occurs when a Voter votes for a Candidate on a
    Ballot with a Result in some Place. This event also handles the situations when
    a Preventer prevents a Voter for voting.

    The possible Event subtypes are: "CastVote", "PreventVote", None.
    """

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
    """A SensoryObserve (inspection) Event occurs when a Observer observed, inspected or
    monitored a ObservedEntity in some Place.

    The possible Event subtypes are: "InspectPeopleOrganization", "MonitorElection",
    "PhysicalInvestigateInspect" or None.
    """

    mention: str  # The text span that most clearly expresses (triggers) the event
    subtype: Union[str, None]  # Possible event subtype
    observer: List[str]  # The observer entity
    observed_entity: List[str]  # The observed entity
    place: List[str]  # Where the event takes place


@dataclass
class TargetAimAt(Event):
    """A TargetAimAt (inspection) Event occurs when a Targeter physically targeted a
    Target with a Instrument at some Place.

    The only possible event subtype is: "TargetAimAt".
    """

    mention: str  # The text span that most clearly expresses (triggers) the event
    subtype: Union[str, None]  # Possible event subtype
    targeter: List[str]  # The agent of the event
    target: List[str]  # The entity being physically targeted
    instrument: List[str]  # The instrument used
    place: List[str]  # Where the event takes place


@dataclass
class ArrestJailDetain(Event):
    """An ArrestJailDetain (justice) Event occurs when a Jailer arrested or jailed
    a Detainee for a Crime at some Place.

    The only possible event subtype is: "ArrestJailDetain".
    """

    mention: str  # The text span that most clearly expresses (triggers) the event
    subtype: Union[str, None]  # Possible event subtype
    jailer: List[str]  # The person who arrested or jailed the detainee
    detainee: List[str]  # The person being arrested or jailed
    crime: List[str]  # The reason (crime) for the arresting or jailing
    place: List[str]  # Where the event takes place


@dataclass
class InitiateJudicialProcess(Event):
    """An InitiateJudicialProcess (justice) Event occurs when a Prosecutor charged,
    indicted, tried or initiated a judicial process pertaining to a Defendant before
    a JudgeCourt for a Crime in some Place.

    The possible Event subtypes are: "ChargeIndict", "TrialHearing" or None.
    """

    mention: str  # The text span that most clearly expresses (triggers) the event
    subtype: Union[str, None]  # Possible event subtype
    prosecutor: List[str]  # The prosecutor entity
    defendant: List[str]  # The defendant of the process
    judge_court: List[str]  # The judge or court in charge
    crime: List[str]  # The crime
    place: List[str]  # Where the event takes place


@dataclass
class InvestigateCrime(Event):
    """An InvestigateCrime (justice) Event occurs when a Investigator investigated
    a Defendant for a Crime in some Place.

    The possible Event subtypes are: "InvestigateCrime" or None.
    """

    mention: str  # The text span that most clearly expresses (triggers) the event
    subtype: Union[str, None]  # Possible event subtype
    investigator: List[str]  # The investigator of the crime
    defendant: List[str]  # The person investigated
    crime: List[str]  # The crime investigated
    place: List[str]  # Where the event takes place


@dataclass
class JudicialConsequences(Event):
    """A JudicialConsequence (justice) Event occurs when a JudgeCourt decided
    the consequences, convicted, executed or extradited a Defendant for a Crime
    in some Place.

    The possible Event subtypes are: "Convict", "Execute", "Extradite" or None.
    """

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
    """A Die (life) Event occurs when a Victim died in some Place. The reason
    of the death can be: killed by a Killer or by a MedicalIssue, with or without
    an Instrument.

    The possible Event subtypes are: "Violent", "NonViolent" or None.
    """

    mention: str  # The text span that most clearly expresses (triggers) the event
    subtype: Union[str, None]  # Possible event subtype
    victim: List[str]  # The person who died
    killer: List[str]  # If any, the killer
    medical_issue: List[str]  # If died by medicall issues, the issue
    instrument: List[str]  # If killed with an instrument, the instrument
    place: List[str]  # Where the event takes place


@dataclass
class Injure(Event):
    """An Injure (life) Event occurs when a Victim is injured in some Place. The
    reasons can be: have extreme hunger or thirst, some physical degradation and
    sickness or illness by some MedicalIssue either infected by some Disease or imposed
    by some Injurer. The injures can be caused by some Instrument.

    The possible Event subtypes are: "HungerThirst", "Physical", "Sickness",
    "Violent" or None
    """

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
    """A ManufactureArtifact (manufacture) Event occurs when a Manufacturer
    manufactured, created or produced an Artifact using an Instrument at
    some Place.

    The possible Event subtypes are: "Build", "IntellectualProperty",
    "CreateManufacture" or None.
    """

    mention: str  # The text span that most clearly expresses (triggers) the event
    subtype: Union[str, None]  # Possible event subtype
    manufacturer: List[str]  # The entity that created the artifact
    artifact: List[str]  # The artifact being created
    instrument: List[str]  # The instrument used to create the artifact
    place: List[str]  # Where the event takes place


@dataclass
class MedicalIntervention(Event):
    """A MedicalIntervention (medical) Event occurs when a Treater treated
    a Patient for a MedicalIssue by means of some Instrument at some
    Place.

    The only possible event subtype is: "Intervention".
    """

    mention: str  # The text span that most clearly expresses (triggers) the event
    subtype: Union[str, None]  # Possible event subtype
    treater: List[str]  # The entity in charge of the intervention
    patient: List[str]  # The treated entity
    medical_issue: List[str]  # The reason for the intervention
    instrument: List[str]  # The instrument used on the intervention
    place: List[str]  # Where the event takes place


@dataclass
class TransportArtifact(Event):
    """A TransportArtifact (transport) Event occurs when a Transporter transports
    an Artifact from the Origin to the Destination in some Vehicle. For some cases
    a Preventer entity can prevent the Transporter to transport the Artifact.

    The possible Event subtypes are: "BringCarryUnload", "DisperseSeparate",
    "Fall", "GrantEntry", "Hide", "LostOfControl", "NonViolentThrowLaunch",
    "PreventEntry", "PreventExit", "ReceiveImport", "SendSupplyExport",
    "SmuggleExtract" or None.
    """

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
    """A TransportPerson (transport) Event occurs when a Transporter transports
    itself or a Passanger from the Origin to the Destination in some Vehicle. For
    some cases a Preventer entity can prevent the Transporter to transport itself or
    the Passenger.

    The possible Event subtypes are: "BringCarryUnload", "DisperseSeparate",
    "EvacuationRescue", "Fall", "GrantedAsylum", "Hide", "PreventEntry",
    "PreventExit", "SelfMotion", "SmuggleExtract" or None.
    """

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
    """An Elect (personnel) Event occurs when a Voter elects a Candidate in some
    Place.

    The possible Event subtypes are: "WinElection" or None.
    """

    mention: str  # The text span that most clearly expresses (triggers) the event
    subtype: Union[str, None]  # Possible event subtype
    voter: List[str]  # The entity who elects the candidate
    candidate: List[str]  # The candidate being elected
    place: List[str]  # Where the event takes place


@dataclass
class EndPossition(Event):
    """An EndPossition (personnel) Event occurs when an Employee stops working on
    a Organization in some Place.

    The possible Event subtypes are: "FiringLayOff", "QuitRetire" or None.
    """

    mention: str  # The text span that most clearly expresses (triggers) the event
    subtype: Union[str, None]  # Possible event subtype
    employee: List[str]  # The entity that has stopped working for the organization
    organization: List[str]  # The organization to which the employee worked for
    place: List[str]  # Where the event takes place


@dataclass
class StartPossition(Event):
    """An StartPossition (personnel) Event occurs when an Employee starts working on
    a Organization in some Place.

    The possible Event subtypes are: "Hiring" or None.
    """

    mention: str  # The text span that most clearly expresses (triggers) the event
    subtype: Union[str, None]  # Possible event subtype
    employee: List[str]  # The entity that has started working on the organization
    organization: List[str]  # The organization to which the employee works
    place: List[str]  # Where the event takes place


@dataclass
class Transaction(Event):
    """A Transaction (transaction) Event occurs when a transaction of some Artifact
    occurred between some Participants for the benefit of a Beneficiary at some Place.
    The Participants can be characterized into Giver and Recipient. There can be a
    preventer that prevents the transaction to occur.

    The possible Event subtypes are: "EmbargoSanction", "GiftGrantProvideAid",
    "TransferControl" or None.
    """

    mention: str  # The text span that most clearly expresses (triggers) the event
    subtype: Union[str, None]  # Possible event subtype
    participants: List[str]  # Only if subtype is None. The participants.
    giver: List[str]  # The entity giving the artifact
    recipient: List[str]  # The entity receiving the artifact
    beneficiary: List[
        str
    ]  # The entity that benefits from the transaction (other than recipient)
    artifact: List[str]  # The entity being transferred (artifact, money or territory)
    preventer: List[
        str
    ]  # Only in "EmbargoSanction". The entity that prevents the transaction.
    place: List[str]  # Where the event takes place


@dataclass
class TransferMoney(Event):
    """A TransferMoney (transaction) Event occurs when a Giver gives Money to a
    Recipient for the benefit of Beneficiary in some Place. There can be a
    preventer that prevents the transaction to occur.

    The possible Event subtypes are: "BorrowLend", "EmbargoSanction",
    "GiftGrantProvideAid", "PayForService", "Purchase" or None.
    """

    mention: str  # The text span that most clearly expresses (triggers) the event
    subtype: Union[str, None]  # Possible event subtype
    giver: List[str]  # The entity giving the money
    recipient: List[str]  # The entity receiving the money
    beneficiary: List[
        str
    ]  # The entity that benefits from the transaction (other than recipient)
    money: List[str]  # The money amount
    preventer: List[
        str
    ]  # Only in "EmbargoSanction". The entity that prevents the transaction.
    place: List[str]  # Where the event takes place


@dataclass
class TransferOwnership(Event):
    """A TransferMoney (transaction) Event occurs when a Giver gives some Artifact to a
    Recipient for the benefit of Beneficiary in some Place. There can be a
    preventer that prevents the transaction to occur.

    The possible Event subtypes are: "BorrowLend", "EmbargoSanction",
    "GiftGrantProvideAid", "Purchase" or None.
    """

    mention: str  # The text span that most clearly expresses (triggers) the event
    subtype: Union[str, None]  # Possible event subtype
    giver: List[str]  # The entity giving the artifact
    recipient: List[str]  # The entity receiving the artifact
    beneficiary: List[
        str
    ]  # The entity that benefits from the transaction (other than recipient)
    artifact: List[str]  # The artifact being transferred
    preventer: List[
        str
    ]  # Only in "EmbargoSanction". The entity that prevents the transaction.
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
