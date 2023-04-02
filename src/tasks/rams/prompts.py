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
    """A DamageDestroy (conflict) Event occurs when an Artifact is damaged or destroyed
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

    The possible Event subtypes: "Corresponde", "Meet" or None.
    """

    mention: str  # The text span that most clearly expresses (triggers) the event
    subtype: Union[str, None]  # Possible event subtype
    participants: List[str]  # The participants of the discussion
    place: List[str]  # Where the event takes place


@dataclass
class FuneralVigil(Event):
    """A FuneralVigil (contact) Event occurs when some Participants communicate
    during a funeral or vigil for Deceased at some Place.

    The possible Event subtypes: "Meet" or None.
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

    The possible Event subtypes: "Broadcast" or None.
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

    The possible Event subtypes: "Correspondence", "Meet" or None.
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

    The possible Event subtypes: "Correspondence", "Meet" or None.
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

    The possible Event subtypes: "Broadcast" or None.
    """

    mention: str  # The text span that most clearly expresses (triggers) the event
    subtype: Union[str, None]  # Possible event subtype
    communicator: List[str]  # The communicator of the public statement
    recipient: List[str]  # The recipient of the statement
    topic: List[str]  # The topic of the public statement
    place: List[str]  # Where the event takes place


@dataclass
class RequestAdvice(Event):
    """A RequestAdvice (contact) Event occurs when a Communicator requests something
    or gives advice about a Topic to a Recipient at some Place.

    The possible Event subtypes: "Broadcast", "Correspondence", "Meet" or None.
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

    The possible Event subtypes: "Broadcast", "Correspondence", "Meet" or None.
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

    The possible Event subtypes: "Accept", "RejectNullify", "Violate" or None.
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

    The only possible event subtype is: "GenericCrime".
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

    The possible Event subtypes: "Merge", "Start", None.
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

    The possible Event subtypes: "CastVote", "PreventVote", None.
    """

    mention: str  # The text span that most clearly expresses (triggers) the event
    subtype: Union[str, None]  # Possible event subtype
    voter: List[str]  # The person or entity who votes.
    candidate: List[str]  # The candidate, entity being voted.
    ballot: List[str]  # The ballot
    result: List[str]  # The result of the ballot
    preventer: List[str]  # Only in "PreventVote". The vote preventer.
    place: List[str]  # Where the evnet takes place


@dataclass
class SensoryObserve(Event):
    """A SensoryObserve (inspection) Event occurs when a Observer observed, inspected or
    monitored a ObservedEntity in some Place.

    The possible Event subtypes: "InspectPeopleOrganization", "MonitorElection",
    "PhysicalInvestigateInspect" or None.
    """

    mention: str  # The text span that most clearly expresses (triggers) the event
    subtype: Union[str, None]  # Possible event subtype
    observer: List[str]  # The observer entity
    observed_entity: List[str]  # The observed entity
    place: List[str]  # Where the evnet takes place
