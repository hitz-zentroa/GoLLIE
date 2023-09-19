from typing import List

from ..utils_typing import Entity, dataclass


"""Entity definitions

The entity definitions are derived from the official CrossNER corpus guidelines:
https://arxiv.org/pdf/2012.04373.pdf

"""


@dataclass
class MusicGenre(Entity):
    """{crossner_music_musicgenre}"""

    span: str  # {crossner_music_musicgenre_examples}


@dataclass
class Song(Entity):
    """{crossner_music_song}"""

    span: str  # {crossner_music_song_examples}


@dataclass
class Band(Entity):
    """{crossner_music_band}"""

    span: str  # {crossner_music_band_examples}


@dataclass
class Album(Entity):
    """{crossner_music_album}"""

    span: str  # {crossner_music_album_examples}


@dataclass
class MusicalArtist(Entity):
    """{crossner_music_musicalartist}"""

    span: str  # {crossner_music_musicalartist_examples}


@dataclass
class MusicalInstrument(Entity):
    """{crossner_music_musicalinstrument}"""

    span: str  # {crossner_music_musicalinstrument_examples}


@dataclass
class Award(Entity):
    """{crossner_music_award}"""

    span: str  # {crossner_music_award_examples}


@dataclass
class Event(Entity):
    """{crossner_music_event}"""

    span: str  # {crossner_music_event_examples}


@dataclass
class Country(Entity):
    """{crossner_music_country}"""

    span: str  # {crossner_music_country_examples}


@dataclass
class Location(Entity):
    """{crossner_music_location}"""

    span: str  # {crossner_music_location_examples}


@dataclass
class Organization(Entity):
    """{crossner_music_organization}"""

    span: str  # {crossner_music_organization_examples}


@dataclass
class Person(Entity):
    """{crossner_music_person}"""

    span: str  # {crossner_music_person_examples}


@dataclass
class Other(Entity):
    """{crossner_music_miscellaneous}"""

    span: str  # {crossner_music_miscellaneous_examples}


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
    Other,
]

ENTITY_DEFINITIONS_MUSIC_woMISC: List[Entity] = [
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
]

# __all__ = list(map(str, [*ENTITY_DEFINITIONS]))
