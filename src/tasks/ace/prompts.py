from dataclasses import dataclass
from typing import List

from ..utils import Entity, Relation

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
