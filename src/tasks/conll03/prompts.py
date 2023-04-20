from typing import List

from ..utils_typing import Entity, dataclass


"""Entity definitions

The entity definitions are derived from the official ConLL2003 guidelines:
https://www.clips.uantwerpen.be/conll2003/ner/
Based on: Nancy Chinchor, Erica Brown, Lisa Ferro, Patty Robinson,
           "1999 Named Entity Task Definition". MITRE and SAIC, 1999.
"""


@dataclass
class Person(Entity):
    """Persons: first, middle and last names of people, animals and fictional
            characters
    aliases"""

    span: str


@dataclass
class Organization(Entity):
    """Organizations: companies (press agencies, studios, banks, stock
               markets, manufacturers, cooperatives)
    subdivisions of companies (newsrooms)
    brands
    political movements (political parties, terrorist
              organisations)
    government bodies (ministries, councils, courts, political unions
               of countries (e.g. the {\\it U.N.}))
    publications (magazines, newspapers, journals)
    musical companies (bands, choirs, opera companies, orchestras
    public organisations (schools, universities, charities
    other collections of people (sports clubs, sports
              teams, associations, theaters companies,
              religious orders, youth organisations
    """

    span: str


@dataclass
class Location(Entity):
    """Locations: roads (streets, motorways)
    trajectories
    regions (villages, towns, cities, provinces, countries, continents,
             dioceses, parishes)
    structures (bridges, ports, dams)
    natural locations (mountains, mountain ranges, woods,
                       rivers, wells, fields, valleys, gardens,
                       nature reserves, allotments, beaches,
                       national parks)
    public places (squares, opera houses, museums, schools,
                   markets, airports, stations, swimming pools,
                   hospitals, sports facilities, youth centers,
                   parks, town halls, theaters, cinemas, galleries,
                   camping grounds, NASA launch pads, club
                   houses, universities, libraries, churches,
                   medical centers, parking lots, playgrounds,
                   cemeteries)
    commercial places (chemists, pubs, restaurants, depots,
                       hostels, hotels, industrial parks,
                       nightclubs, music venues)
    assorted buildings (houses, monasteries, creches, mills,
                        army barracks, castles, retirement
                        homes, towers, halls, rooms, vicarages,
                        courtyards)
    abstract ``places'' (e.g. {\\it the free world})
    """

    span: str


@dataclass
class Miscellaneous(Entity):
    """Miscellaneous: words of which one part is a location, organisation,
              miscellaneous, or person
    adjectives and other words derived from a word
              which is location, organisation, miscellaneous, or
              person
    religions
    political ideologies
    nationalities
    languages
    programs
    events (conferences, festivals, sports competitions,
              forums, parties, concerts)
    wars
    sports related names (league tables, leagues, cups
    titles (books, songs, films, stories, albums, musicals,
              TV programs)
    slogans
    eras in time
    types (not brands) of objects (car types, planes,
              motorbikes)"""

    span: str


ENTITY_DEFINITIONS: List[Entity] = [
    Person,
    Organization,
    Location,
    Miscellaneous,
]


__all__ = list(map(str, [*ENTITY_DEFINITIONS]))
