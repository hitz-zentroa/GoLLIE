from typing import List

from ..utils_typing import Entity, dataclass


"""Entity definitions

In the absence of public guidelines, the guidelines have been defined by the CoLLIE authors.
Dataset available at: https://groups.csail.mit.edu/sls/downloads/restaurant/

"""


@dataclass
class Rating(Entity):
    """{mit_rating}"""

    span: str  # {mit_rating_examples}


@dataclass
class Amenity(Entity):
    """{mit_amenity}"""

    span: str  # {mit_amenity_examples}


@dataclass
class Location(Entity):
    """{mit_location}"""

    span: str  # {mit_location_examples}


@dataclass
class RestaurantName(Entity):
    """{mit_restaurantname}"""

    span: str  # {mit_restaurantname_examples}


@dataclass
class Price(Entity):
    """{mit_price}"""

    span: str  # {mit_price_examples}


@dataclass
class Hours(Entity):
    """{mit_hours}"""

    span: str  # {mit_hours_examples}


@dataclass
class Dish(Entity):
    """{mit_dish}"""

    span: str  # {mit_dish_examples}


@dataclass
class Cuisine(Entity):
    """{mit_cuisine}"""

    span: str  # {mit_cuisine_examples}


ENTITY_DEFINITIONS: List[Entity] = [Rating, Amenity, Location, RestaurantName, Price, Hours, Dish, Cuisine]

# __all__ = list(map(str, [*ENTITY_DEFINITIONS]))
