from typing import List

from ..utils_typing import Entity, dataclass


"""Entity definitions

In the absence of public guidelines, the guidelines have been defined by the CoLLIE authors.
Dataset available at: https://groups.csail.mit.edu/sls/downloads/movie/

"""


@dataclass
class Actor(Entity):
    """{mit_actor}"""

    span: str  # {mit_actor_examples}


@dataclass
class Character(Entity):
    """{mit_character}"""

    span: str  # {mit_character_examples}


@dataclass
class Director(Entity):
    """{mit_director}"""

    span: str  # {mit_director_examples}


@dataclass
class Genre(Entity):
    """{mit_genre}"""

    span: str  # {mit_genre_examples}


@dataclass
class Plot(Entity):
    """{mit_plot}"""

    span: str  # {mit_plot_examples}


@dataclass
class Rating(Entity):
    """{mit_rating}"""

    span: str  # {mit_rating_examples}


@dataclass
class RatingsAverage(Entity):
    """{mit_ratings_average}"""

    span: str  # {mit_ratings_average_examples}


@dataclass
class Review(Entity):
    """{mit_review}"""

    span: str  # {mit_review_examples}


@dataclass
class Song(Entity):
    """{mit_song}"""

    span: str  # {mit_song_examples}


@dataclass
class Tittle(Entity):
    """{mit_title}"""

    span: str  # {mit_title_examples}


@dataclass
class Trailer(Entity):
    """{mit_trailer}"""

    span: str  # {mit_trailer_examples}


@dataclass
class Year(Entity):
    """{mit_year}"""

    span: str  # {mit_year_examples}


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
