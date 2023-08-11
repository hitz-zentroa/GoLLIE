from typing import Dict, List, Type

from ..utils_typing import Entity, Event, Relation, dataclass


"""Entity definitions

The entity definitions are derived from the official ACE guidelines:
https://www.ldc.upenn.edu/sites/www.ldc.upenn.edu/files/english-entities-guidelines-v6.6.pdf
"""


@dataclass
class Person(Entity):
    """{ace_person}"""

    span: str  # {ace_person_examples}


@dataclass
class Organization(Entity):
    """{ace_organization}"""

    span: str  # {ace_organization_examples}


@dataclass
class GPE(Entity):
    """{ace_gpe}"""

    span: str  # {ace_gpe_examples}


@dataclass
class Location(Entity):
    """{ace_location}"""

    span: str  # {ace_location_examples}


@dataclass
class Facility(Entity):
    """{ace_facility}"""

    span: str  # {ace_facility_examples}


@dataclass
class Weapon(Entity):
    """{ace_weapon}"""

    span: str  # {ace_weapon_examples}


@dataclass
class Vehicle(Entity):
    """{ace_vehicle}"""

    span: str  # {ace_vehicle_examples}


ENTITY_DEFINITIONS: List[Type] = [
    Person,
    Organization,
    GPE,
    Location,
    Facility,
    Weapon,
    Vehicle,
]


"""Value definitions

The following "entities" are not defined on the ACE schema, however, they are
annotated as time expressions or value/numeric data.
"""


@dataclass
class Time(Entity):
    """{ace_time}"""

    span: str  # {ace_time_examples}


@dataclass
class Numeric(Entity):
    """{ace_numeric}"""

    span: str  # {ace_numeric_examples}


@dataclass
class JobTitle(Entity):
    """{ace_jobtitle}"""

    span: str  # {ace_jobtitle_examples}


@dataclass
class Crime(Entity):
    """{ace_crime}"""

    span: str  # {ace_crime_examples}


@dataclass
class Sentence(Entity):
    """{ace_sentence}"""

    span: str  # {ace_sentence_examples}


@dataclass
class ContactInfo(Entity):
    """{ace_contactinfo}"""

    span: str  # {ace_contactinfo_examples}


VALUE_DEFINITIONS: List[Type] = [
    Time,
    Numeric,
    JobTitle,
    Crime,
    Sentence,
    ContactInfo,
]


"""Relation definitions

The relations definitions are derived from the oficial ACE guidelines:
https://www.ldc.upenn.edu/sites/www.ldc.upenn.edu/files/english-relations-guidelines-v6.2.pdf
"""


@dataclass
class PhysicalRelation(Relation):
    """{ace_physicalrelation}"""

    arg1: str
    arg2: str


@dataclass
class PartWholeRelation(Relation):
    """{ace_partwholerelation}"""

    arg1: str
    arg2: str


@dataclass
class PersonalSocialRelation(Relation):
    """{ace_personalsocialrelation}"""

    arg1: str
    arg2: str


@dataclass
class OrganizationAffiliationRelation(Relation):
    """{ace_organizationaffiliationrelation}"""

    arg1: str
    arg2: str


@dataclass
class AgentArtifactRelationRelation(Relation):
    """{ace_agentartifactrelationrelation}"""

    arg1: str
    arg2: str


@dataclass
class GenAffiliationRelation(Relation):
    """{ace_genaffiliationrelation}"""

    arg1: str
    arg2: str


COARSE_RELATION_DEFINITIONS: List[Type] = [
    PhysicalRelation,
    PartWholeRelation,
    PersonalSocialRelation,
    OrganizationAffiliationRelation,
    AgentArtifactRelationRelation,
    GenAffiliationRelation,
]


@dataclass
class Located(PhysicalRelation):
    """{ace_located}"""

    arg1: str
    arg2: str


@dataclass
class Near(PhysicalRelation):
    """{ace_near}"""

    arg1: str
    arg2: str


@dataclass
class Geographical(PartWholeRelation):
    """{ace_geographical}"""

    arg1: str
    arg2: str


@dataclass
class Subsidiary(PartWholeRelation):
    """{ace_subsidiary}"""

    arg1: str
    arg2: str


@dataclass
class Business(PersonalSocialRelation):
    """{ace_business}"""

    arg1: str
    arg2: str


@dataclass
class Family(PersonalSocialRelation):
    """{ace_family}"""

    arg1: str
    arg2: str


@dataclass
class LastingPersonal(PersonalSocialRelation):
    """{ace_lastingpersonal}"""

    arg1: str
    arg2: str


@dataclass
class Employment(OrganizationAffiliationRelation):
    """{ace_employment}"""

    arg1: str
    arg2: str


@dataclass
class Ownership(OrganizationAffiliationRelation):
    """{ace_ownership}"""

    arg1: str
    arg2: str


@dataclass
class Founder(OrganizationAffiliationRelation):
    """{ace_founder}"""

    arg1: str
    arg2: str


@dataclass
class StudentAlum(OrganizationAffiliationRelation):
    """{ace_studentalum}"""

    arg1: str
    arg2: str


@dataclass
class SportsAffiliation(OrganizationAffiliationRelation):
    """{ace_sportsaffiliation}"""

    arg1: str
    arg2: str


@dataclass
class InvestorShareholder(OrganizationAffiliationRelation):
    """{ace_investorshareholder}"""

    arg1: str
    arg2: str


@dataclass
class Membership(OrganizationAffiliationRelation):
    """{ace_membership}"""

    arg1: str
    arg2: str


@dataclass
class UserOwnerInventorManufacturer(AgentArtifactRelationRelation):
    """{ace_userownerinventormanufacturer}"""

    arg1: str
    arg2: str


@dataclass
class CitizenResidentReligionEthnicity(GenAffiliationRelation):
    """{ace_citizenresidentreligionethnicity}"""

    arg1: str
    arg2: str


@dataclass
class OrgLocationOrigin(GenAffiliationRelation):
    """{ace_orglocationorigin}"""

    arg1: str
    arg2: str


RELATION_DEFINITIONS: List[Type] = [
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

FINE_TO_COARSE_RELATIONS: Dict[Type, Type] = {_def: _def.__base__ for _def in RELATION_DEFINITIONS}
COARSE_TO_FINE_RELATIONS: Dict[Type, List[Type]] = {}
for fine, coarse in FINE_TO_COARSE_RELATIONS.items():
    if coarse not in COARSE_TO_FINE_RELATIONS:
        COARSE_TO_FINE_RELATIONS[coarse] = []
    COARSE_TO_FINE_RELATIONS[coarse].append(fine)

"""Event definitions

The events definitions are derived from the oficial ACE guidelines:
https://www.ldc.upenn.edu/sites/www.ldc.upenn.edu/files/english-events-guidelines-v5.4.3.pdf
"""


@dataclass
class LifeEvent(Event):
    """{ace_lifeevent}"""

    mention: str
    """The text span that most clearly expresses the event.
        {ace_lifeevent_examples}
    """


@dataclass
class MovementEvent(Event):
    """{ace_movementevent}"""

    mention: str
    """The text span that most clearly expresses the event.
        {ace_movementevent_examples}
    """


@dataclass
class TransactionEvent(Event):
    """{ace_transactionevent}"""

    mention: str
    """The text span that most clearly expresses the event.
        {ace_transactionevent_examples}
    """


@dataclass
class BusinessEvent(Event):
    """{ace_businessevent}"""

    mention: str
    """The text span that most clearly expresses the event.
        {ace_businessevent_examples}
    """


@dataclass
class ConflictEvent(Event):
    """{ace_conflictevent}"""

    mention: str
    """The text span that most clearly expresses the event.
        {ace_conflictevent_examples}
    """


@dataclass
class ContactEvent(Event):
    """{ace_contactevent}"""

    mention: str
    """The text span that most clearly expresses the event.
        {ace_contactevent_examples}
    """


@dataclass
class PersonnelEvent(Event):
    """{ace_personnelevent}"""

    mention: str
    """The text span that most clearly expresses the event.
        {ace_personnelevent_examples}
    """


@dataclass
class JusticeEvent(Event):
    """{ace_justiceevent}"""

    mention: str
    """The text span that most clearly expresses the event.
        {ace_justiceevent_examples}
    """


COARSE_EVENT_DEFINITIONS: List[Type] = [
    LifeEvent,
    MovementEvent,
    TransactionEvent,
    BusinessEvent,
    ConflictEvent,
    ContactEvent,
    PersonnelEvent,
    JusticeEvent,
]


@dataclass
class BeBorn(LifeEvent):
    """A BeBorn Event occurs whenever a Person Entity is given birth to."""

    mention: str  # The text span that most clearly expresses (triggers) the event
    person: List[str]  # The person who is born
    time: List[str]  # When the birth takes place
    place: List[str]  # Where the birth takes place


@dataclass
class Marry(LifeEvent):
    """{ace_marry}"""

    mention: str  # The text span that most clearly expresses (triggers) the event
    person: List[str]  # The people who are married
    time: List[str]  # When the marriage takes place
    place: List[str]  # Where the marriage takes place


@dataclass
class Divorce(LifeEvent):
    """{ace_divorce}"""

    mention: str  # The text span that most clearly expresses (triggers) the event
    person: List[str]  # The people who are divorced
    time: List[str]  # When the divorce takes place
    place: List[str]  # Where the divorce takes place


@dataclass
class Injure(LifeEvent):
    """{ace_injure}"""

    mention: str  # The text span that most clearly expresses (triggers) the event
    agent: List[str]  # The attacking agent / The one that enacts the harm
    victim: List[str]  # The harmed person(s)
    instrument: List[str]  # The device used to inflict the harm
    time: List[str]  # When the injuring takes place
    place: List[str]


@dataclass
class Die(LifeEvent):
    """{ace_die}"""

    mention: str  # The text span that most clearly expresses (triggers) the event
    agent: List[str]  # (Optional) The attacking agent / The killer
    victim: List[str]  # The person(s) who died
    instrument: List[str]  # The device used to kill
    time: List[str]  # When the death takes place
    place: List[str]  # Where the death takes place


@dataclass
class Transport(MovementEvent):
    """{ace_transport}"""

    mention: str  # The text span that most clearly expresses (triggers) the event
    agent: List[str]  # The agent responsible for the transport Event
    artifact: List[str]  # The person doing the traveling or the artifact being traveled
    vehicle: List[str]  # The vehicle used to transport the person or artifact
    price: List[str]  # The price of transporting the person or artifact
    origin: List[str]  # Where the transporting originated
    destination: List[str]  # Where the transporting is directed
    time: List[str]  # When the transporting takes place


@dataclass
class TransferOwnership(TransactionEvent):
    """{ace_transferownership}"""

    mention: str  # The text span that most clearly expresses (triggers) the event
    buyer: List[str]  # The buying agent
    seller: List[str]  # The selling agent
    beneficiary: List[str]  # The agent that benefits from the transaction
    artifact: List[str]  # The item or Organization that was bought or sold
    price: List[str]  # The sale price of the artifact
    time: List[str]  # When the sale takes place
    place: List[str]  # Where the sale takes place


@dataclass
class TransferMoney(TransactionEvent):
    """{ace_transfermoney}"""

    mention: str  # The text span that most clearly expresses (triggers) the event
    giver: List[str]  # The donating agent
    recipient: List[str]  # The recipient agent
    beneficiary: List[str]  # The agent that benefits from the transfer
    money: List[str]  # The amount given, donated or loaned
    time: List[str]  # When the amount is transferred
    place: List[str]  # Where the transation takes place


@dataclass
class StartOrg(BusinessEvent):
    """{ace_startorg}"""

    mention: str  # The text span that most clearly expresses (triggers) the event
    agent: List[str]  # The agent responsible for the StattOrg Event (the founder)
    org: List[str]  # The organization that is started
    time: List[str]  # When the Event takes place
    place: List[str]  # Where the Event takes place


@dataclass
class MergeOrg(BusinessEvent):
    """{ace_mergeorg}"""

    mention: str  # The text span that most clearly expresses (triggers) the event
    org: List[str]  # The organization(s) that are merged
    time: List[str]  # When the merger takes place
    place: List[str]  # Where the merger takes place


@dataclass
class DeclareBankruptcy(BusinessEvent):
    """{ace_declarebankruptcy}"""

    mention: str  # The text span that most clearly expresses (triggers) the event
    org: List[str]  # The Organization declaring bankruptcy
    time: List[str]  # When the bankruptcy is declared
    place: List[str]  # Where the declaration takes place


@dataclass
class EndOrg(BusinessEvent):
    """{ace_endorg}"""

    mention: str  # The text span that most clearly expresses (triggers) the event
    org: List[str]  # The Organization that is ended
    time: List[str]  # When the Event takes place
    place: List[str]  # Where the Event takes place


@dataclass
class Attack(ConflictEvent):
    """{ace_attack}"""

    mention: str  # The text span that most clearly expresses (triggers) the event
    attacker: List[str]  # The attacking/instigating agent
    target: List[str]  # The target of the attack (including unintended targets)
    instrument: List[str]  # The instrument used in the attack
    time: List[str]  # When the attack takes place
    place: List[str]  # Where the attack takes place


@dataclass
class Demonstrate(ConflictEvent):
    """{ace_demonstrate}"""

    mention: str  # The text span that most clearly expresses (triggers) the event
    entity: List[str]  # The demonstrating agent
    time: List[str]  # When the demonstration takes place
    place: List[str]  # Where the demonstration takes place


@dataclass
class Meet(ContactEvent):
    """{ace_meet}"""

    mention: str  # The text span that most clearly expresses (triggers) the event
    entity: List[str]  # The agents who are meeting
    time: List[str]  # When the meeting takes place
    place: List[str]  # Where the meeting takes place


@dataclass
class PhoneWrite(ContactEvent):
    """{ace_phonewrite}"""

    mention: str  # The text span that most clearly expresses (triggers) the event
    entity: List[str]  # The communicating agents
    time: List[str]  # When the communication takes place


@dataclass
class StartPosition(PersonnelEvent):
    """{ace_startposition}"""

    mention: str  # The text span that most clearly expresses (triggers) the event
    person: List[str]  # The employee
    entity: List[str]  # The employer
    position: List[str]  # The JobTitle for the position being started
    time: List[str]  # When the employment relationship begins
    place: List[str]  # Where the employment relationship begins


@dataclass
class EndPosition(PersonnelEvent):
    """{ace_endposition}"""

    mention: str  # The text span that most clearly expresses (triggers) the event
    person: List[str]  # The employee
    entity: List[str]  # The employer
    position: List[str]  # The JobTitle for the position being ended
    time: List[str]  # When the employment relationship ends
    place: List[str]  # Where the employment relationship ends


@dataclass
class Nominate(PersonnelEvent):
    """{ace_nominate}"""

    mention: str  # The text span that most clearly expresses (triggers) the event
    person: List[str]  # The person(s) nominated
    agent: List[str]  # The nominating agent
    position: List[str]  # The JobTitle for the position being nominated to
    time: List[str]  # When the nomination takes place
    place: List[str]  # Where the nomination takes place


@dataclass
class Elect(PersonnelEvent):
    """{ace_elect}"""

    mention: str  # The text span that most clearly expresses (triggers) the event
    person: List[str]  # The person elected
    entity: List[str]  # The voting agent(s)
    position: List[str]  # The JobTitle for the position being nominated to
    time: List[str]  # When the election takes place
    place: List[str]  # Where the election takes place


@dataclass
class ArrestJail(JusticeEvent):
    """{ace_arrestjail}"""

    mention: str  # The text span that most clearly expresses (triggers) the event
    person: List[str]  # The person who is jailed or arrested
    agent: List[str]  # The jailer or the arresting agent
    crime: List[str]  # The Crime for which the Person is being jailed or arrested
    time: List[str]  # When the person is arrested or sent to jail
    place: List[str]  # Where the person is arrested or where they are in jail


@dataclass
class ReleaseParole(JusticeEvent):
    """{ace_releaseparole}"""

    mention: str  # The text span that most clearly expresses (triggers) the event
    person: List[str]  # The person who is released
    entity: List[str]  # The former captor agent(s)
    crime: List[str]  # The Crime for which the released Person was being held
    time: List[str]  # When the release takes place
    place: List[str]  # Where the release takes place


@dataclass
class TrialHearing(JusticeEvent):
    """{ace_trialhearing}"""

    mention: str  # The text span that most clearly expresses (triggers) the event
    defendant: List[str]  # The agent on trial
    prosecutor: List[str]  # The prosecuting agent
    adjudicator: List[str]  # The judge or court
    crime: List[str]  # The Crime for which the Defendant is being tried
    time: List[str]  # When the trial takes place
    place: List[str]  # Where the trial takes place


@dataclass
class ChargeIndict(JusticeEvent):
    """{ace_chargeindict}"""

    mention: str  # The text span that most clearly expresses (triggers) the event
    defendant: List[str]  # The agent that is indicted
    prosecutor: List[str]  # The agent bringing charges or executing the indictment
    adjudicator: List[str]  # The judge our court
    crime: List[str]  # The Crime for which the Defendant is being indicted
    time: List[str]  # When the indictment takes place
    place: List[str]  # When the indictment takes place


@dataclass
class Sue(JusticeEvent):
    """{ace_sue}"""

    mention: str  # The text span that most clearly expresses (triggers) the event
    plaintiff: List[str]  # The suing agent
    defendant: List[str]  # The agent being sued
    adjudicator: List[str]  # The judge or court
    crime: List[str]  # The Crime (or offense) for which the Defendant is being sued
    time: List[str]  # When the suit takes place
    place: List[str]  # Where the suit takes place


@dataclass
class Convict(JusticeEvent):
    """{ace_convict}"""

    mention: str  # The text span that most clearly expresses (triggers) the event
    defendant: List[str]  # The convicted agent(s)
    adjudicator: List[str]  # The judge or court
    crime: List[str]  # The Crime for which the Defendant has been convicted
    time: List[str]  # When the conviction takes place
    place: List[str]  # Where the conviction takes place


@dataclass
class SentenceAct(JusticeEvent):
    """{ace_sentenceact}"""

    mention: str  # The text span that most clearly expresses (triggers) the event
    defendant: List[str]  # The agent who is sentenced
    adjudicator: List[str]  # The judge or court
    crime: List[str]  # The Crime for which the Person is being sentenced
    sentence: List[str]  # The sentence
    time: List[str]  # The time of the sentencing Event
    place: List[str]  # Where the sentencing takes place


@dataclass
class Fine(JusticeEvent):
    """{ace_fine}"""

    mention: str  # The text span that most clearly expresses (triggers) the event
    entity: List[str]  # The Entity that was fined
    adjudicator: List[str]  # The Entity doing the finding
    money: List[str]  # The amount of the fine
    crime: List[str]  # The Crime (or offence) for which the Entity is being fined
    time: List[str]  # When the fining Event takes place
    place: List[str]  # Where the fining Event takes place


@dataclass
class Execute(JusticeEvent):
    """{ace_execute}"""

    mention: str  # The text span that most clearly expresses (triggers) the event
    person: List[str]  # The person executed
    agent: List[str]  # The agent responsible for carrying out the execution
    crime: List[str]  # The Crime for which the Person is being executed
    time: List[str]  # When te execution takes place
    place: List[str]  # Where the execution takes place


@dataclass
class Extradite(JusticeEvent):
    """{ace_extradite}"""

    mention: str  # The text span that most clearly expresses (triggers) the event
    agent: List[str]  # The extraditing agent
    person: List[str]  # The person being extradited
    destination: List[str]  # Where the person is extradited to, the destination
    origin: List[str]  # The original location of the person being extradited
    crime: List[str]  # The Crime for which the Person is being extradited
    time: List[str]  # When the extradition takes place


@dataclass
class Acquit(JusticeEvent):
    """{ace_acquit}"""

    mention: str  # The text span that most clearly expresses (triggers) the event
    defendant: List[str]  # The agent being acquitted
    adjudicator: List[str]  # The judge or court
    crime: List[str]  # The Crime of which the Defendant is being acquitted
    time: List[str]  # When the acquittal takes place
    place: List[str]  # Where the acquittal takes place


@dataclass
class Pardon(JusticeEvent):
    """{ace_pardon}"""

    mention: str  # The text span that most clearly expresses (triggers) the event
    defendant: List[str]  # The agent being pardoned
    adjudicator: List[str]  # The state official who does the pardoning
    crime: List[str]  # The Crime of which the Defendant is being pardoned
    time: List[str]  # When the pardon takes place
    place: List[str]  # Where the pardon takes place


@dataclass
class Appeal(JusticeEvent):
    """{ace_appeal}"""

    mention: str  # The text span that most clearly expresses (triggers) the event
    defendant: List[str]  # The defendant
    prosecutor: List[str]  # The prosecuting agent
    adjudicator: List[str]  # The judge or court
    crime: List[str]  # The Crime which is the subject of the appeal
    time: List[str]  # When the appeal takes place
    place: List[str]  # Where the appeal takes place


EVENT_DEFINITIONS: List[Type] = [
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

FINE_TO_COARSE_EVENTS: Dict[Type, Type] = {_def: _def.__base__ for _def in EVENT_DEFINITIONS}
COARSE_TO_FINE_EVENTS: Dict[Type, List[Type]] = {}
for fine, coarse in FINE_TO_COARSE_EVENTS.items():
    if coarse not in COARSE_TO_FINE_EVENTS:
        COARSE_TO_FINE_EVENTS[coarse] = []
    COARSE_TO_FINE_EVENTS[coarse].append(fine)

# __all__ = list(map(str, [*ENTITY_DEFINITIONS, *RELATION_DEFINITIONS, *EVENT_DEFINITIONS]))
