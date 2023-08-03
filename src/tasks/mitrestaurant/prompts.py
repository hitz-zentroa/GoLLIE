from typing import List

from ..utils_typing import Entity, dataclass


"""Entity definitions

In the absence of public guidelines, the guidelines have been defined by the CoLLIE authors.
Dataset available at: https://groups.csail.mit.edu/sls/downloads/restaurant/

"""


@dataclass
class Rating(Entity):
    """{mit_rating}"""

    span: str


@dataclass
class Amenity(Entity):
    """{mit_amenity}"""

    span: str


@dataclass
class Location(Entity):
    """{mit_location}"""

    span: str


@dataclass
class RestaurantName(Entity):
    """{mit_restaurantname}"""

    span: str


@dataclass
class Price(Entity):
    """{mit_price}"""

    span: str


@dataclass
class Hours(Entity):
    """{mit_hours}"""

    span: str


@dataclass
class Dish(Entity):
    """{mit_dish}"""

    span: str


@dataclass
class Cuisine(Entity):
    """{mit_cuisine}"""

    span: str


ENTITY_DEFINITIONS: List[Entity] = [Rating, Amenity, Location, RestaurantName, Price, Hours, Dish, Cuisine]

# __all__ = list(map(str, [*ENTITY_DEFINITIONS]))
