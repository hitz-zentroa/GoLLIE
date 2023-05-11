GUIDELINES = {
    "ner_person": {
        "en": ["Persons: first, middle and last names of people, animals and fictional characters aliases."]
    },
    "ner_organization": {
        "en": [
            "Organizations: companies (press agencies, studios, banks, stock\n"
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
            "Locations: roads (streets, motorways) trajectories regions (villages, towns, cities, provinces,\n"
            " countries, continents, dioceses, parishes) structures (bridges, ports, dams) natural locations\n"
            " (mountains, mountain ranges, woods, rivers, wells, fields, valleys, gardens, nature reserves,\n"
            " allotments, beaches, national parks) public places (squares, opera houses, museums, schools, markets,\n"
            " airports, stations, swimming pools, hospitals, sports facilities, youth centers, parks, town halls,\n"
            " theaters, cinemas, galleries, camping grounds, NASA launch pads, club houses, universities, libraries,\n"
            " churches, medical centers, parking lots, playgrounds, cemeteries) commercial places (chemists, pubs,\n"
            " restaurants, depots, hostels, hotels, industrial parks, nightclubs, music venues) assorted buildings\n"
            " (houses, monasteries, creches, mills, army barracks, castles, retirement homes, towers, halls, rooms,\n"
            " vicarages, courtyards) abstract ``places'' (e.g. {\\it the free world})\n"
        ]
    },
    "ner_miscellaneous": {
        "en": [
            "Miscellaneous: words of which one part is a location, organisation, miscellaneous, or person adjectives\n"
            " and other words derived from a word which is location, organisation, miscellaneous, or person\n"
            " religions political ideologies nationalities languages programs events (conferences, festivals,\n"
            " sports competitions, forums, parties, concerts) wars sports related names (league tables, leagues,\n"
            " cups titles (books, songs, films, stories, albums, musicals, TV programs) slogans eras in time types\n"
            " (not brands) of objects (car types, planes, motorbikes)\n"
        ]
    },
}

# import inspect
# import random

# import black
# import rich

# from src.tasks.conll03.prompts import Organization

# guideline = {key: random.choice(value["en"]) for key, value in GUIDELINES.items()}

# rich.print(guideline)

# source = inspect.getsource(Organization)
# rich.print(source)
# source = source.format(**guideline)

# source = black.format_str(source, mode=black.Mode())

# print(source)
