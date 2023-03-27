from dataclasses import dataclass
from typing import List

from ..utils_typing import Entity, Event, Value, Relation

"""Entity definitions

The entity definitions are derived from the oficial ACE guidelines:
https://www.ldc.upenn.edu/sites/www.ldc.upenn.edu/files/english-entities-guidelines-v6.6.pdf
"""


@dataclass
class Person(Entity):
    """Each distinct person or set of people mentioned in a document refers
    to an entity of type Person. For example, people may be specified by name
    ("John Smith"), occupation ("the butcher"), family relation ("dad"),
    pronoun ("he"), etc., or by some combination of these.
    """

    span: str


@dataclass
class Organization(Entity):
    """Each organization or set of organizations mentioned in a document gives
    rise to an entity of type Organization. Typical examples are businesses,
    government units, sports teams, and formally organized music groups.
    """

    span: str


@dataclass
class GPE(Entity):
    """Geo-Political Entities are composite entities comprised of a population,
    a government, a physical location, and a nation (or province, state,
    country, city, etc.).
    """

    span: str


@dataclass
class Location(Entity):
    """Places defined on a geographical or astronomical basis which are
    mentioned in a document and do not constitute a political entity give rise
    to Location entities. These include, for example, the solar system, Mars,
    the Hudson River, Mt. Everest, and Death Valley.
    """

    span: str


@dataclass
class Facility(Entity):
    """A facility is a functional, primarily man-made structure. These include
    buildings and similar facilities designed for human habitation, such as
    houses, factories, stadiums, office buildings, ... Roughly speaking,
    facilities are artifacts falling under the domains of architecture and
    civil engineering.
    """

    span: str


ENTITY_DEFINITIONS: List[Entity] = [Person, Organization, GPE, Location, Facility]


"""Value definitions

The following "entities" are not defined on the ACE schema, however, they are
annotated as time expressions or value/numeric data.
"""


@dataclass
class Time(Value):
    """A Time value refers to a specific time frame. Usually known as time
    expressions. For example: '4 years', 'today', 'December', 'future', ...
    """

    span: str


@dataclass
class Numeric(Value):
    """A Numeric value refers to relevant numbers, amounts, etc. For example:
    'billions of dollars', '50 percent', '100%', ...
    """

    span: str


@dataclass
class JobTitle(Value):
    """A JobTitle value refers to the name of the job or position of a Person
    entity in a Organization. For example: 'co-chief executive', 'move coordinator',
    'interim ED', ...
    """

    span: str


@dataclass
class Weapon(Value):
    """A Weapon value refers to instruments that can be used to deal physical damage,
    destroy something or kill someone. For example: 'bomb', 'm-16s', 'missile', ...
    """

    span: str


@dataclass
class Crime(Value):
    """A Crime value refers to the specific reason (crime) that a Person entity can
    be judged or sentenced for. For example: 'raping', 'murder', 'drug', ...
    """

    span: str


@dataclass
class Sentence(Value):
    """A Sentence value refers to sentences decided by a court or judge for a
    specific crime. For example: '124 years in prison', 'a sentence', 'death'...
    """

    span: str


@dataclass
class ContactInfo(Value):
    """A ContactInfo value refers to contact information values such as telephone
    numbers, emails, addresses. For example: 'mich...@sumptionandwyland.com', ...
    """

    span: str


@dataclass
class Vehicle(Value):
    """A Vehicle value refers to vehicles that are used for transportation. The
    vehicles can transport either persons or artifacts. For example: 'car', 'plane',
    'cabin', ...
    """

    span: str


VALUE_DEFINITIONS: List[Value] = [
    Time,
    Numeric,
    JobTitle,
    Weapon,
    Crime,
    Sentence,
    ContactInfo,
]


"""Relation definitions

The relations definitions are derived from the oficial ACE guidelines:
https://www.ldc.upenn.edu/sites/www.ldc.upenn.edu/files/english-relations-guidelines-v6.2.pdf
"""


@dataclass
class Located(Relation):
    """The Located relation captures the physical location of an entity. This
    relation is restricted to people. In other words, `arg1` in Located
    relations can only be occupied by mentions of Entities of type Person.
    """

    arg1: str
    arg2: str


@dataclass
class Near(Relation):
    """Near indicates that an entity is explicitly near another entity, but
    neither entity is a part of the other or located in/at the other.
    """

    arg1: str
    arg2: str


@dataclass
class Geographical(Relation):
    """The Geographical relation captures the location of a Facility, Location,
    or GPE in or at or as a part of another Facility, Location, or GPE.
    """

    arg1: str
    arg2: str


@dataclass
class Subsidiary(Relation):
    """Subsidiary captures the ownership, administrative, and other hierarchical
    relationships between organizations and between organizations and GPEs.
    """

    arg1: str
    arg2: str


@dataclass
class Business(Relation):
    """The Business Relation captures the connection between two entities in any
    professional relationship. Both arguments must be entities of type Person.
    """

    arg1: str
    arg2: str


@dataclass
class Family(Relation):
    """The Family Relation captures the connection between one entity and another
    with which it is in any familial relationship. Both arguments must be entities
    of type Person.
    """

    arg1: str
    arg2: str


@dataclass
class LastingPersonal(Relation):
    """Lasting-Personal captures relationships that meet the following conditions:
    (1) The relationship must involve personal contact (or a reasonable assumption
    thereof).
    (2) There must be some indication or expectation that the relationship exists
    outside of a particular cited interaction.
    Both arguments must be entities of type Person.
    """

    arg1: str
    arg2: str


@dataclass
class Employment(Relation):
    """Employment captures the relationship between Persons and their employers.
    This Relation is only taggable when it can be reasonably assumed that the
    Person is paid by the ORG or GPE.
    """

    arg1: str
    arg2: str


@dataclass
class Ownership(Relation):
    """Ownership captures the relationship between a Person and an Organization
    owned by that Person. If the `arg2` is not an Organization, use the
    Agent-Artifact relation.
    """

    arg1: str
    arg2: str


@dataclass
class Founder(Relation):
    """Founder captures the relationship between an agent (Person, Organization,
    or GPE) and an Organization or GPE established or set up by that agent.
    """

    arg1: str
    arg2: str


@dataclass
class StudentAlum(Relation):
    """StudentAlum captures the relationship between a Person and an educational
    institution the Person attends or attended.
    """

    arg1: str
    arg2: str


@dataclass
class SportsAffiliation(Relation):
    """Sports-Affiliation captures the relationship between a player, coach, manager,
    or assistant and his or her affiliation with a sports organization (including
    sports leagues or divisions as well as individual sports teams).
    """

    arg1: str
    arg2: str


@dataclass
class InvestorShareholder(Relation):
    """InvestorShareholder captures the relationship between an agent (Person,
    Organization, or GPE) and an Organization in which the agent has invested or in
    which the agent owns shares/stock. Please note that agents may invest in
    GPEs.
    """

    arg1: str
    arg2: str


@dataclass
class Membership(Relation):
    """Membership captures the relationship between an agent and an organization of
    which the agent is a member. Organizations and GPEs can be members of other
    Organizations (such as NATO or the UN).
    """

    arg1: str
    arg2: str


@dataclass
class UserOwnerInventorManufacturer(Relation):
    """This Relation applies when an agent owns an artifact, has possession of an
    artifact, uses an artifact, or caused an artifact to come into being. Note:
    if `arg2` is an Organization, use Ownership relation (arg1=PER) or Subsidiary
    relation (arg1=ORG or GPE).
    """

    arg1: str
    arg2: str


@dataclass
class CitizenResidentReligionEthnicity(Relation):
    """CitizenResidentReligionEthnicity describes the relation between a Person
    entity and (1) the GPE in which they have citizenship, (2) the GPE or Location
    in which they live, the religious Organization or Person entity with which they
    have affiliation and (3) the GPE or PER entity that indicates their ethnicity.
    """

    arg1: str
    arg2: str


@dataclass
class OrgLocationOrigin(Relation):
    """OrgLocationOrigin captures the relationship between an organization and the
    Location or GPE where it is located, based, or does business. Note: Subsidiary
    trumps this relation for government organizations.
    """

    arg1: str
    arg2: str


RELATION_DEFINITIONS: List[Relation] = [
    Located,
    Near,
    Geographical,
    Subsidiary,
    Business,
    Family,
    LastingPersonal,
    Employment,
    Ownership,
    Founder,
    StudentAlum,
    SportsAffiliation,
    InvestorShareholder,
    Membership,
    UserOwnerInventorManufacturer,
    CitizenResidentReligionEthnicity,
    OrgLocationOrigin,
]

"""Event definitions

The events definitions are derived from the oficial ACE guidelines:
https://www.ldc.upenn.edu/sites/www.ldc.upenn.edu/files/english-events-guidelines-v5.4.3.pdf
"""


@dataclass
class BeBorn(Event):
    """A BeBorn Event occurs whenever a Person Entity is given birth to"""

    mention: str  # The text span that most clearly expresses (triggers) the event
    person: List[str]  # The person who is born
    time: List[str]  # When the birth takes place
    place: List[str]  # Where the birth takes place


@dataclass
class Marry(Event):
    """Marry Events are official Events, where two people are married under the
    legal definition.
    """

    mention: str  # The text span that most clearly expresses (triggers) the event
    person: List[str]  # The people who are married
    time: List[str]  # When the marriage takes place
    place: List[str]  # Where the marriage takes place


@dataclass
class Divorce(Event):
    """A DIVORCE Event occurs whenever two people are officially divorced under the
    legal definition of divorce. We do not include separations or church annulments.
    """

    mention: str  # The text span that most clearly expresses (triggers) the event
    person: List[str]  # The people who are divorced
    time: List[str]  # When the divorce takes place
    place: List[str]  # Where the divorce takes place


@dataclass
class Injure(Event):
    """An Injure Event occurs whenever a Person Entity experiences physical harm.
    Injure Events can be accidental, intentional or self-inflicted.
    """

    mention: str  # The text span that most clearly expresses (triggers) the event
    agent: List[str]  # The attacking agent / The one that enacts the harm
    victim: List[str]  # The harmed person(s)
    instrument: List[str]  # The device used to inflict the harm
    time: List[str]  # When the injuring takes place
    place: List[str]


@dataclass
class Die(Event):
    """A Die Event occurs whenever the life of a Person Entity ends. Die Events
    can be accidental, intentional or self-inflicted
    """

    mention: str  # The text span that most clearly expresses (triggers) the event
    agent: List[str]  # (Optional) The attacking agent / The killer
    victim: List[str]  # The person(s) who died
    instrument: List[str]  # The device used to kill
    time: List[str]  # When the death takes place
    place: List[str]  # Where the death takes place


@dataclass
class Transport(Event):
    """A Transport Event occurs whenever an Artifact (Weapon or Vehicle) or a
    Person is moved from one Place (GPE, Facility, Location) to another.
    """

    mention: str  # The text span that most clearly expresses (triggers) the event
    agent: List[str]  # The agent responsible for the transport Event
    artifact: List[str]  # The person doing the traveling or the artifact being traveled
    vehicle: List[str]  # The vehicle used to transport the person or artifact
    price: List[str]  # The price of transporting the person or artifact
    origin: List[str]  # Where the transporting originated
    destination: List[str]  # Where the transporting is directed
    time: List[str]  # When the transporting takes place


@dataclass
class TransferOwnership(Event):
    """TransferOwnership Events refer to the buying, selling, loaning,
    borrowing, giving, or receiving of artifacts or organizations.
    """

    mention: str  # The text span that most clearly expresses (triggers) the event
    buyer: List[str]  # The buying agent
    seller: List[str]  # The selling agent
    beneficiary: List[str]  # The agent that benefits from the transaction
    artifact: List[str]  # The item or Organization that was bought or sold
    price: List[str]  # The sale price of the artifact
    time: List[str]  # When the sale takes place
    place: List[str]  # Where the sale takes place


@dataclass
class TransferMoney(Event):
    """TransferMoney Events refer to the giving, receiving, borrowing, or
    lending money when it is not in the context of purchasing something. The
    canonical examples are: (1) people giving money to organizations (and getting
    nothing tangible in return); and (2) organizations lending money to people or
    other orgs.
    """

    mention: str  # The text span that most clearly expresses (triggers) the event
    giver: List[str]  # The donating agent
    recipient: List[str]  # The recipient agent
    beneficiary: List[str]  # The agent that benefits from the transfer
    money: List[str]  # The amount given, donated or loaned
    time: List[str]  # When the amount is transferred
    place: List[str]  # Where the transation takes place


@dataclass
class StartOrg(Event):
    """A StartOrg Event occurs whenever a new Organization is created."""

    mention: str  # The text span that most clearly expresses (triggers) the event
    agent: List[str]  # The agent responsible for the StattOrg Event (the founder)
    org: List[str]  # The organization that is started
    time: List[str]  # When the Event takes place
    place: List[str]  # Where the Event takes place


@dataclass
class MergeOrg(Event):
    """A MergeOrg Event occurs whenever two or more Organization Entities
    come together to form a new Organization Entity. This Event applies to any
    kind of Organization, including government agencies. It also includes joint
    venture
    """

    mention: str  # The text span that most clearly expresses (triggers) the event
    org: List[str]  # The organization(s) that are merged
    time: List[str]  # When the merger takes place
    place: List[str]  # Where the merger takes place


@dataclass
class DeclareBankruptcy(Event):
    """A DeclareBankruptcy Event will occur whenever an Entity officially
    requests legal protection from debt collection due to an extremely negative
    balance sheet.
    """

    mention: str  # The text span that most clearly expresses (triggers) the event
    org: List[str]  # The Organization declaring bankruptcy
    time: List[str]  # When the bankruptcy is declared
    place: List[str]  # Where the declaration takes place


@dataclass
class EndOrg(Event):
    """An EndOrg Event occurs whenever an Organization ceases to exist (in
    other words 'goes out of business').
    """

    mention: str  # The text span that most clearly expresses (triggers) the event
    org: List[str]  # The Organization that is ended
    time: List[str]  # When the Event takes place
    place: List[str]  # Where the Event takes place


@dataclass
class Attack(Event):
    """An Attack Event is defined as a violent physical act causing harm or damage.
    Attack Events include any such Event not covered by the Injure or Die
    subtypes, including Events where there is no stated agent.
    """

    mention: str  # The text span that most clearly expresses (triggers) the event
    attacker: List[str]  # The attacking/instigating agent
    target: List[str]  # The target of the attack (including unintended targets)
    instrument: List[str]  # The instrument used in the attack
    time: List[str]  # When the attack takes place
    place: List[str]  # Where the attack takes place


@dataclass
class Demonstrate(Event):
    """A Demonstrate Event occurs whenever a large number of people come
    together in a public area to protest or demand some sort of official action.
    Demonstrate Events include, but are not limited to, protests, sit-ins, strikes,
    and riots.
    """

    mention: str  # The text span that most clearly expresses (triggers) the event
    entity: List[str]  # The demonstrating agent
    time: List[str]  # When the demonstration takes place
    place: List[str]  # Where the demonstration takes place


@dataclass
class Meet(Event):
    """A Meet Event occurs whenever two or more Entities come together at a single
    location and interact with one another face-to-face. Meet Events include talks,
    summits, conferences, meetings, visits, and any other Event where two or more
    parties get together at some location.
    """

    mention: str  # The text span that most clearly expresses (triggers) the event
    entity: List[str]  # The agents who are meeting
    time: List[str]  # When the meeting takes place
    place: List[str]  # Where the meeting takes place


@dataclass
class PhoneWrite(Event):
    """A PhoneWrite Event occurs when two or more people directly engage in
    discussion which does not take place 'face-to-face'. To make this Event less
    open-ended, we limit it to written or telephone communication where at least two
    parties are specified.
    """

    mention: str  # The text span that most clearly expresses (triggers) the event
    entity: List[str]  # The communicating agents
    time: List[str]  # When the communication takes place


@dataclass
class StartPosition(Event):
    """A StartPosition Event occurs whenever a Person Entity begins working
    for (or changes offices within) an Organization or GPE. This includes
    government officials starting their terms, whether elected or appointed.
    """

    mention: str  # The text span that most clearly expresses (triggers) the event
    person: List[str]  # The employee
    entity: List[str]  # The employer
    position: List[str]  # The JobTitle for the position being started
    time: List[str]  # When the employment relationship begins
    place: List[str]  # Where the employment relationship begins


@dataclass
class EndPosition(Event):
    """An EndPosition Event occurs whenever a Person Entity stops working for
    (or changes offices within) an Organization or GPE.
    """

    mention: str  # The text span that most clearly expresses (triggers) the event
    person: List[str]  # The employee
    entity: List[str]  # The employer
    position: List[str]  # The JobTitle for the position being ended
    time: List[str]  # When the employment relationship ends
    place: List[str]  # Where the employment relationship ends


@dataclass
class Nominate(Event):
    """A Nominate Event occurs whenever a Person is proposed for a StartPosition
    Event by the appropriate Person, through official channels.
    """

    mention: str  # The text span that most clearly expresses (triggers) the event
    person: List[str]  # The person(s) nominated
    agent: List[str]  # The nominating agent
    position: List[str]  # The JobTitle for the position being nominated to
    time: List[str]  # When the nomination takes place
    place: List[str]  # Where the nomination takes place


@dataclass
class Elect(Event):
    """An Elect Event occurs whenever a candidate wins an election designed to
    determine the Person argument of a StartPosition Event.
    """

    mention: str  # The text span that most clearly expresses (triggers) the event
    person: List[str]  # The person elected
    entity: List[str]  # The voting agent(s)
    position: List[str]  # The JobTitle for the position being nominated to
    time: List[str]  # When the election takes place
    place: List[str]  # Where the election takes place


@dataclass
class ArrestJail(Event):
    """A Jail Event occurs whenever the movement of a Person is constrained by a
    state actor (a GPE, its Organization subparts, or its Person representatives).
    """

    mention: str  # The text span that most clearly expresses (triggers) the event
    person: List[str]  # The person who is jailed or arrested
    agent: List[str]  # The jailer or the arresting agent
    crime: List[str]  # The Crime for which the Person is being jailed or arrested
    time: List[str]  # When the person is arrested or sent to jail
    place: List[str]  # Where the person is arrested or where they are in jail


@dataclass
class ReleaseParole(Event):
    """A Release Event occurs whenever a state actor (GPE, Organization
    subpart, or Person representative) ends its custody of a Person Entity.
    """

    mention: str  # The text span that most clearly expresses (triggers) the event
    person: List[str]  # The person who is released
    entity: List[str]  # The former captor agent(s)
    crime: List[str]  # The Crime for which the released Person was being held
    time: List[str]  # When the release takes place
    place: List[str]  # Where the release takes place


@dataclass
class TrialHearing(Event):
    """A Trial Event occurs whenever a court proceeding has been initiated for the
    purposes of determining the guilt or innocence of a Person, Organization
    or GPE accused of committing a crime.
    """

    mention: str  # The text span that most clearly expresses (triggers) the event
    defendant: List[str]  # The agent on trial
    prosecutor: List[str]  # The prosecuting agent
    adjudicator: List[str]  # The judge or court
    crime: List[str]  # The Crime for which the Defendant is being tried
    time: List[str]  # When the trial takes place
    place: List[str]  # Where the trial takes place


@dataclass
class ChargeIndict(Event):
    """A Charge Event occurs whenever a Person, Organization or GPE is
    accused of a crime by a state actor (GPE, an Organization subpart of a GPE
    or a Person representing a GPE).
    """

    mention: str  # The text span that most clearly expresses (triggers) the event
    defendant: List[str]  # The agent that is indicted
    prosecutor: List[str]  # The agent bringing charges or executing the indictment
    adjudicator: List[str]  # The judge our court
    crime: List[str]  # The Crime for which the Defendant is being indicted
    time: List[str]  # When the indictment takes place
    place: List[str]  # When the indictment takes place


@dataclass
class Sue(Event):
    """A Sue Event occurs whenever a court proceeding has been initiated for the
    purposes of determining the liability of a Person, Organization or GPE
    accused of committing a crime or neglecting a commitment.
    """

    mention: str  # The text span that most clearly expresses (triggers) the event
    plaintiff: List[str]  # The suing agent
    defendant: List[str]  # The agent being sued
    adjudicator: List[str]  # The judge or court
    crime: List[str]  # The Crime (or offense) for which the Defendant is being sued
    time: List[str]  # When the suit takes place
    place: List[str]  # Where the suit takes place


@dataclass
class Convict(Event):
    """A Convict Event occurs whenever a Try Event ends with a successful
    prosecution of the Defendant. In other words, a Person,
    Organization or GPE Entity is convicted whenever that Entity has been found
    guilty of a Crime.
    """

    mention: str  # The text span that most clearly expresses (triggers) the event
    defendant: List[str]  # The convicted agent(s)
    adjudicator: List[str]  # The judge or court
    crime: List[str]  # The Crime for which the Defendant has been convicted
    time: List[str]  # When the conviction takes place
    place: List[str]  # Where the conviction takes place


@dataclass
class SentenceAct(Event):
    """A SentenceAct Event takes place whenever the punishment (particularly
    incarceration) for the Defendant of a Try Event is issued by a state
    actor (a GPE, an Organization subpart or a Person representing them)
    """

    mention: str  # The text span that most clearly expresses (triggers) the event
    defendant: List[str]  # The agent who is sentenced
    adjudicator: List[str]  # The judge or court
    crime: List[str]  # The Crime for which the Person is being sentenced
    sentence: List[str]  # The sentence
    time: List[str]  # The time of the sentencing Event
    place: List[str]  # Where the sentencing takes place


@dataclass
class Fine(Event):
    """A Fine Event takes place whenever a state actor issues a financial punishment
    to a GPE, Person or Organization Entity, typically as a result of court
    proceedings.
    """

    mention: str  # The text span that most clearly expresses (triggers) the event
    entity: List[str]  # The Entity that was fined
    adjudicator: List[str]  # The Entity doing the finding
    money: List[str]  # The amount of the fine
    crime: List[str]  # The Crime (or offence) for which the Entity is being fined
    time: List[str]  # When the fining Event takes place
    place: List[str]  # Where the fining Event takes place


@dataclass
class Execute(Event):
    """An Execute Event occurs whenever the life of a Person is taken by a state
    actor (a GPE, its Organization subparts, or Person representatives).
    """

    mention: str  # The text span that most clearly expresses (triggers) the event
    person: List[str]  # The person executed
    agent: List[str]  # The agent responsible for carrying out the execution
    crime: List[str]  # The Crime for which the Person is being executed
    time: List[str]  # When te execution takes place
    place: List[str]  # Where the execution takes place


@dataclass
class Extradite(Event):
    """An Extradite Event occurs whenever a Person is sent by a state actor from
    one Place (normally the GPE associated with the state actor, but sometimes a
    Facility under its control) to another place (Location, GPE or Facility) for
    the purposes of legal proceedings there.
    """

    mention: str  # The text span that most clearly expresses (triggers) the event
    agent: List[str]  # The extraditing agent
    person: List[str]  # The person being extradited
    destination: List[str]  # Where the person is extradited to, the destination
    origin: List[str]  # The original location of the person being extradited
    crime: List[str]  # The Crime for which the Person is being extradited
    time: List[str]  # When the extradition takes place


@dataclass
class Acquit(Event):
    """An Acquit Event occurs whenever a trial ends but fails to produce a conviction.
    This will include cases where the charges are dropped by the Prosecutor.
    """

    mention: str  # The text span that most clearly expresses (triggers) the event
    defendant: List[str]  # The agent being acquitted
    adjudicator: List[str]  # The judge or court
    crime: List[str]  # The Crime of which the Defendant is being acquitted
    time: List[str]  # When the acquittal takes place
    place: List[str]  # Where the acquittal takes place


@dataclass
class Pardon(Event):
    """A Pardon Event occurs whenever a head-of-state or their appointed
    representative lifts a sentence imposed by the judiciary.
    """

    mention: str  # The text span that most clearly expresses (triggers) the event
    defendant: List[str]  # The agent being pardoned
    adjudicator: List[str]  # The state official who does the pardoning
    crime: List[str]  # The Crime of which the Defendant is being pardoned
    time: List[str]  # When the pardon takes place
    place: List[str]  # Where the pardon takes place


@dataclass
class Appeal(Event):
    """An Appeal Event occurs whenever the decision of a court is taken to a higher
    court for review.
    """

    mention: str  # The text span that most clearly expresses (triggers) the event
    defendant: List[str]  # The defendant
    prosecutor: List[str]  # The prosecuting agent
    adjudicator: List[str]  # The judge or court
    crime: List[str]  # The Crime which is the subject of the appeal
    time: List[str]  # When the appeal takes place
    place: List[str]  # Where the appeal takes place


EVENT_DEFINITIONS: List[Event] = [
    BeBorn,
    Marry,
    Divorce,
    Injure,
    Die,
    Transport,
    TransferOwnership,
    TransferMoney,
    StartOrg,
    MergeOrg,
    DeclareBankruptcy,
    EndOrg,
    Attack,
    Demonstrate,
    Meet,
    PhoneWrite,
    StartPosition,
    EndPosition,
    Nominate,
    Elect,
    ArrestJail,
    ReleaseParole,
    TrialHearing,
    ChargeIndict,
    Sue,
    Convict,
    SentenceAct,
    Fine,
    Execute,
    Extradite,
    Acquit,
    Pardon,
    Appeal,
]
