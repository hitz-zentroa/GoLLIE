GUIDELINES = {
    "harveyner_point": {
        "en": [
            "Refers to a location that is a building, a landmark, an intersection of two roads, an intersection of a"
            " river with a lake/reservoir/ocean, or a specifc address. Ignore generic company/franchise names unless"
            " it is accompanied with a precise location, for example, HEB at Kirkwood Drive. However, non-franchised"
            " small businesses with only one unique location are considered as a point. Ignore any locations in the"
            " Twitter username, unless @ does not refer to a Twitter account name. For example, I am @ XXX High"
            " School."
        ]
    },
    "harveyner_area": {
        "en": [
            "Refers to all the named entities of cities, neighborhoods, super neighborhoods, geographic divisions etc."
            " The following locations, Lake Houston, Barker Reservoir, and Addick’s Reservoir, are annotated as areas"
            " due to their significant size while all other lakes/reservoirs are not considered as areas."
        ]
    },
    "harveyner_road": {
        "en": [
            "Refers to a road/avenue/street or a section of a road/avenue/street when the tweet does not provide an"
            " exact location on that road."
        ]
    },
    "harveyner_river": {
        "en": [
            "Refers to a river or a section of a river when the tweet does not imply there is an intersection between"
            " the river and other places."
        ]
    },
}

EXAMPLES = {
    "harveyner_point_examples": {
        "en": [
            "GRB",
            "GEORGE R. BROWN",
            "Lakewood Church",
            "Bayou Oaks",
            "Northgate Subdivision S of toll road",
            "TerryHS",
            "GRB Convention Center",
            "@GRBCC",
            "Addicks",
            "TERRY HIGH SCHOOL",
        ]
    },
    "harveyner_area_examples": {
        "en": [
            "Sienna Plantation",
            "Galveston",
            "Addicks",
            "Barker",
            "Fort Bend",
            "Chambers",
            "Fort Bend County",
            "Pecan Grove",
            "Brazoria",
            "Dickinson",
        ]
    },
    "harveyner_river_examples": {
        "en": [
            "Buffalo Bayou",
            "Brazos River",
            "Brays Bayou",
            "Cypress Creek",
            "Spring Creek",
            "Addicks",
            "Colorado River",
            "San Jacinto",
            "WhiteOakBayou",
            "Brazos",
        ]
    },
    "harveyner_road_examples": {
        "en": ["Barker Cypress", "I-10", "US 290 WB", "SH-71", "I-45", "105", "59", "Fry", "US-59 South", "Summer St"]
    },
}
