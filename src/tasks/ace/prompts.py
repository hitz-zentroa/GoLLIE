from dataclasses import dataclass
from typing import Any, List

from ..utils import Entity


@dataclass
class Person(Entity):
    """Each distinct person or set of people mentioned in a document refers
    to an entity of type Person. For example, people may be specified by name
    (“John Smith”), occupation (“the butcher”), family relation (“dad”),
    pronoun (“he”), etc., or by some combination of these.
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


ENTITY_DEFINITIONS: List[Any] = [Person, Organization, GPE, Location, Facility]
