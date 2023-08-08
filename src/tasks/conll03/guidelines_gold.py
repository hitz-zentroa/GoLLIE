GUIDELINES = {
    "ner_person": {"en": ["first, middle and last names of people, animals and fictional characters aliases."]},
    "ner_organization": {
        "en": [
            "Companies (press agencies, studios, banks, stock\n"
            "markets, manufacturers, cooperatives) subdivisions of companies (newsrooms)\n"
            "brands political movements (political parties, terrorist organisations)\n"
            "government bodies (ministries, councils, courts, political unions of countries\n"
            "(e.g. the {\\it U.N.})) publications (magazines, newspapers, journals)\n"
            "musical companies (bands, choirs, opera companies, orchestras\n"
            "public organisations (schools, universities, charities other collections\n"
            "of people (sports clubs, sports teams, associations, theaters companies,\n"
            "religious orders, youth organisations.\n"
        ]
    },
    "ner_location": {
        "en": [
            "Roads (streets, motorways) trajectories regions (villages, towns, cities, provinces,\n"
            "countries, continents, dioceses, parishes) structures (bridges, ports, dams) natural locations\n"
            "(mountains, mountain ranges, woods, rivers, wells, fields, valleys, gardens, nature reserves,\n"
            "allotments, beaches, national parks) public places (squares, opera houses, museums, schools, markets,\n"
            "airports, stations, swimming pools, hospitals, sports facilities, youth centers, parks, town halls,\n"
            "theaters, cinemas, galleries, camping grounds, NASA launch pads, club houses, universities, libraries,\n"
            "churches, medical centers, parking lots, playgrounds, cemeteries) commercial places (chemists, pubs,\n"
            "restaurants, depots, hostels, hotels, industrial parks, nightclubs, music venues) assorted buildings\n"
            "(houses, monasteries, creches, mills, army barracks, castles, retirement homes, towers, halls, rooms,\n"
            "vicarages, courtyards) abstract ``places'' (e.g. {\\it the free world})\n"
        ]
    },
    "ner_miscellaneous": {
        "en": [
            "Words of which one part is a location, organisation, miscellaneous, or person adjectives\n"
            "and other words derived from a word which is location, organisation, miscellaneous, or person\n"
            "religions political ideologies nationalities languages programs events (conferences, festivals,\n"
            "sports competitions, forums, parties, concerts) wars sports related names (league tables, leagues,\n"
            "cups titles (books, songs, films, stories, albums, musicals, TV programs) slogans eras in time types\n"
            "(not brands) of objects (car types, planes, motorbikes)\n"
        ]
    },
}

EXAMPLES = {
    "ner_location_examples": {
        "en": ["U.S.", "Germany", "Britain", "Australia", "England", "France", "Spain", "Italy", "LONDON", "China"]
    },
    "ner_organization_examples": {
        "en": ["Reuters", "U.N.", "NEW YORK", "CHICAGO", "PUK", "OSCE", "EU", "NATO", "European Union", "Honda"]
    },
    "ner_person_examples": {
        "en": [
            "Clinton",
            "Dole",
            "Arafat",
            "Yeltsin",
            "Lebed",
            "Dutroux",
            "Wasim Akram",
            "Waqar Younis",
            "Mushtaq Ahmed",
            "Mother Teresa",
        ]
    },
    "ner_miscellaneous_examples": {
        "en": ["Russian", "German", "British", "French", "Dutch", "GMT", "Israeli", "English", "Iraqi", "European"]
    },
}
