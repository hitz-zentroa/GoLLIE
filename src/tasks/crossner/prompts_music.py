from typing import List

from ..utils_typing import Entity, dataclass


"""Entity definitions

The entity definitions are derived from the official CrossNER corpus guidelines:
https://arxiv.org/pdf/2012.04373.pdf

"""


@dataclass
class MusicGenre(Entity):
    """{crossner_music_musicgenre}"""

    span: str


@dataclass
class Song(Entity):
    """{crossner_music_song}"""

    span: str


@dataclass
class Band(Entity):
    """{crossner_music_band}"""

    span: str


@dataclass
class Album(Entity):
    """{crossner_music_album}"""

    span: str


@dataclass
class MusicalArtist(Entity):
    """{crossner_music_musicalartist}"""

    span: str


@dataclass
class MusicalInstrument(Entity):
    """{crossner_music_musicalinstrument}"""

    span: str


@dataclass
class Award(Entity):
    """{crossner_music_award}"""

    span: str


@dataclass
class Event(Entity):
    """{crossner_music_event}"""

    span: str


@dataclass
class Country(Entity):
    """{crossner_music_country}"""

    span: str


@dataclass
class Location(Entity):
    """{crossner_music_location}"""

    span: str


@dataclass
class Organization(Entity):
    """{crossner_music_organization}"""

    span: str


@dataclass
class Person(Entity):
    """{crossner_music_person}"""

    span: str


@dataclass
class Miscellaneous(Entity):
    """{crossner_music_miscellaneous}"""

    span: str


ENTITY_DEFINITIONS_MUSIC: List[Entity] = [
    MusicGenre,
    Song,
    Band,
    Album,
    MusicalArtist,
    MusicalInstrument,
    Award,
    Event,
    Country,
    Location,
    Organization,
    Person,
    Miscellaneous,
]

# __all__ = list(map(str, [*ENTITY_DEFINITIONS]))
