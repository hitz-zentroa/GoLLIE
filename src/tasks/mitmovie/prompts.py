from typing import List

from ..utils_typing import Entity, dataclass


"""Entity definitions

In the absence of public guidelines, the guidelines have been defined by the CoLLIE authors.
Dataset available at: https://groups.csail.mit.edu/sls/downloads/movie/

"""


@dataclass
class Actor(Entity):
    """{mit_actor}"""

    span: str


@dataclass
class Character(Entity):
    """{mit_character}"""

    span: str


@dataclass
class Director(Entity):
    """{mit_director}"""

    span: str


@dataclass
class Genre(Entity):
    """{mit_genre}"""

    span: str


@dataclass
class Plot(Entity):
    """{mit_plot}"""

    span: str


@dataclass
class Rating(Entity):
    """{mit_rating}"""

    span: str


@dataclass
class RatingsAverage(Entity):
    """{mit_ratings_average}"""

    span: str


@dataclass
class Review(Entity):
    """{mit_review}"""

    span: str


@dataclass
class Song(Entity):
    """{mit_song}"""

    span: str


@dataclass
class Tittle(Entity):
    """{mit_title}"""

    span: str


@dataclass
class Trailer(Entity):
    """{mit_trailer}"""

    span: str


@dataclass
class Year(Entity):
    """{mit_year}"""

    span: str


ENTITY_DEFINITIONS: List[Entity] = [
    Actor,
    Character,
    Director,
    Genre,
    Plot,
    Rating,
    RatingsAverage,
    Review,
    Song,
    Tittle,
    Trailer,
    Year,
]

# __all__ = list(map(str, [*ENTITY_DEFINITIONS]))
