from typing import List, Union

from ..utils_typing import Event, dataclass

"""Event definitions

The oficial guidelines are not public. All event definitions are taken from:
https://github.com/raspberryice/gen-arg/blob/main/aida_ontology_cleaned.csv
"""


@dataclass
class ArtifactFailure(Event):
    """An ArtifactFailure Event occurs whenever a (mechanical) Artifact failed
    due to some Instrument at some Place.

    The possible Event subtypes are: "MechanicalFailure" or None.
    """

    mention: str  # The text span that most clearly expresses (triggers) the event
    subtype: Union[str, None]  # Possible event subtype.
    artifact: List[str]  # The artifact involved
    instrument: List[str]  # The reason (instrument) for the artifact fail
    place: List[str]  # Where the fail occurred


@dataclass
class DamageDestroy(Event):
    """A DamageDestroy Event occurs when an Artifact is damaged or destroyed by
    some Agent (damager or destroyer) using an Instrument at some Place.

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
    """An Attack Event occurs when an Attacker attacks a Target with some
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
    """A Coup Event occurs when a DeposedEntity was desposed by a DeposingEntity
    at some Place.

    The only possible event subtype is: "Coup".
    """

    mention: str  # The text span that most clearly expresses (triggers) the event
    subtype: Union[str, None]  # Possible event subtype
    deposed_entity: List[str]  # The entity being deposed
    deposing_entity: List[str]  # The deposing entity
    place: List[str]  # Where the event takes place


@dataclass
class Demonstrate(Event):
    """A Demonstrate Event occurs when a Demonstrator(s) protest in some Place.

    The possible Event subtypes are: "MarchProtestPoliticalGathering" or None.
    """

    mention: str  # The text span that most clearly expresses (triggers) the event
    subtype: Union[str, None]  # Possible event subtype
    demonstrator: List[str]  # The Demonstrators that take part in the protest
    place: List[str]  # Where the protest takes place


@dataclass
class Yield(Event):
    """A Yield (conflict) Event occurs when an Agent (yielder or surrender)
    yields or surrenders to a Recipient in some Place. But also, when an Agent
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
    communicates (remotely or face-to-face) in some Place.

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
    """A Discussion (contact) Event occurs when some Participants discuss in some
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
    during a funeral or vigil for Deceased in some Place.

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
    something on media to some Recipients in some Place.

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
    a negotiation about some Topic in some Place.

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
    some Topic to a Recipient in some Place.

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
    a public statement to a Recipient in some Place.

    The possible Event subtypes: "Broadcast" or None.
    """

    mention: str  # The text span that most clearly expresses (triggers) the event
    subtype: Union[str, None]  # Possible event subtype
    communicator: List[str]  # The communicator of the public statement
    recipient: List[str]  # The recipient of the statement
    topic: List[str]  # The topic of the public statement
    place: List[str]  # Where the event takes place
