GUIDELINES = {
    "harveyner_point": {
        "en": [
            "Refers to a location that is a building, a landmark, an intersection of two roads, an intersection of a"
            " river with a lake/reservoir/ocean, or a specifc address. A section of a road/river between two"
            " detailed/precise locations should be considered as a point. A road passing through a small area can be"
            " designated as a point. Ignore generic company/franchise names like HEB, Kroger etc. unless it is"
            " accompanied with a precise location, for example, HEB at Kirkwood Drive. However, non-franchised small"
            " businesses with only one unique location are considered as a point. Ignore any locations in the Twitter"
            " username, like @HoustonABC. However, if the @ does not refer to a Twitter account name, 3338 please"
            " recognize the location. For example, I am @ XXX High School, “XXX High School” will be considered as a"
            " point."
        ]
    },
    "harveyner_area": {
        "en": [
            "Refers to all the named entities of cities, neighborhoods, super neighborhoods, geographic divisions etc."
            " The following locations, Lake Houston, Barker Reservoir, and Addick’s Reservoir, are annotated as areas"
            " due to their signifcant size while all other lakes/reservoirs are considered as points."
        ]
    },
    "harveyner_road": {
        "en": [
            "Refers to a road/avenue/street or a section of a road/avenue/street when the tweet does not provide an"
            " exact location on that road. A road intersecting a very large area cannot be a point and must be denoted"
            " as a stretch of a road."
        ]
    },
    "harveyner_river": {
        "en": [
            "Refers to a river or a section of a river when the tweet does not imply there is an intersection between"
            " the river and other places. If the distance between the two points is very large, it might be considered"
            " as a stretch of a river."
        ]
    },
}
