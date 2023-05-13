GUIDELINES = {
    "ner_person": {
        "en": [
            "first, middle and last names of people, animals and fictional characters aliases.",
            '"Aliases for first, middle, and last names of individuals, animals, and fictional characters."',
            '"Nicknames, pseudonyms, and alter egos of individuals, creatures, and fictional personas."',
            (
                '"First, middle, and last names are also referred to as aliases of people, animals, and fictional'
                ' characters."'
            ),
            '"Aliases for the first, middle, and last names of people, animals, and fictional characters."',
        ]
    },
    "ner_organization": {
        "en": [
            (
                "Companies (press agencies, studios, banks, stock markets, manufacturers, cooperatives) subdivisions"
                " of \ncompanies (newsrooms) brands political movements (political parties, terrorist organisations)"
                " government bodies \n(ministries, councils, courts, political unions of countries (e.g. the {\\it"
                " U.N.})) publications (magazines, newspapers, \njournals) musical companies (bands, choirs, opera"
                " companies, orchestras public organisations (schools, universities, \ncharities other collections of"
                " people (sports clubs, sports teams, associations, theaters companies, religious orders, \nyouth"
                " organisations."
            ),
            (
                "There are various types of organizations, such as press agencies, studios, banks, stock markets,"
                " manufacturers, \ncooperatives, and government bodies, that have subdivisions or brands, and some of"
                " these organizations have political movements \nor publications. There are also musical companies,"
                " public organizations such as schools and universities, and other \ncollections of people such as"
                " sports clubs, religious orders, and youth organizations."
            ),
            (
                '"Various organizations such as press agencies, studios, banks, stock markets, manufacturers,'
                " cooperatives, \nnewsrooms, political parties, terrorist organizations, government bodies,"
                " ministries, councils, courts, political \nunions of countries (e.g. the UN), magazines, newspapers,"
                " journals, bands, choirs, opera companies, orchestras, public \norganizations (schools, universities,"
                " charities), other collections of people (sports clubs, sports teams, associations, \ntheaters,"
                ' religious orders, youth organizations are mentioned in the text."'
            ),
            (
                '"There are various types of organizations that can be considered as actors in the media ecosystem,'
                " including \ncompanies like press agencies, studios, banks, stock markets, manufacturers,"
                " cooperatives, as well as their subdivisions \nsuch as newsrooms, brands, political movements,"
                " government bodies, publications, musical companies, public \norganizations, and other collections of"
                " people like sports clubs, sports teams, associations, theaters, religious orders, and \nyouth"
                ' organizations."'
            ),
            (
                "There are various types of organizations that can be considered as sources of news, including press"
                " agencies, \nstudios, banks, stock markets, manufacturers, cooperatives, subdivisions of companies"
                " such as newsrooms, brands, \npolitical movements like political parties and terrorist organizations,"
                " government bodies like ministries, councils, \ncourts, and political unions of countries,"
                " publications like magazines, newspapers, and journals, musical companies \nlike bands, choirs, opera"
                " companies, and orchestras, public organizations such as schools, universities, charities, \nand"
                " other collections of people like sports clubs, sports teams, associations, theaters, companies,"
                " religious \norders, and youth organizations."
            ),
        ]
    },
    "ner_location": {
        "en": [
            (
                "Roads (streets, motorways) trajectories regions (villages, towns, cities, provinces, countries,"
                " continents, \ndioceses, parishes) structures (bridges, ports, dams) natural locations (mountains,"
                " mountain ranges, woods, rivers, \nwells, fields, valleys, gardens, nature reserves, allotments,"
                " beaches, national parks) public places (squares, opera \nhouses, museums, schools, markets,"
                " airports, stations, swimming pools, hospitals, sports facilities, youth centers, \nparks, town"
                " halls, theaters, cinemas, galleries, camping grounds, NASA launch pads, club houses, universities,"
                " \nlibraries, churches, medical centers, parking lots, playgrounds, cemeteries) commercial places"
                " (chemists, pubs, \nrestaurants, depots, hostels, hotels, industrial parks, nightclubs, music venues)"
                " assorted buildings (houses, monasteries, \ncreches, mills, army barracks, castles, retirement homes,"
                " towers, halls, rooms, vicarages, courtyards) abstract \n``places'' (e.g. {\\it the free world})"
            ),
            (
                'The term "places" encompasses a wide range of physical locations, including roads and motorways,'
                " regions such as \nvillages, towns, and countries, structures like bridges and ports, natural"
                " locations like rivers and forests, public places \nlike squares and parks, and commercial places"
                " like pubs and hotels. Additionally, there are assorted buildings like \nhouses, monasteries, and"
                ' factories, and abstract concepts like "the free world."'
            ),
            (
                "The following list includes various types of locations: roads and streets, regions such as villages,"
                " towns, and \ncountries, structures like bridges and ports, natural locations like mountains and"
                " rivers, public places like squares and \nparks, and commercial places like pubs and industrial"
                " parks. Additionally, there are assorted buildings like houses and \nmonasteries, and abstract places"
                ' like "the free world."'
            ),
            (
                "The following list includes various types of locations: roads and streets, regions such as villages,"
                " towns, and \ncountries, structures like bridges and ports, natural locations like mountains and"
                " rivers, public places like squares and \nhospitals, commercial places like pubs and hotels, and"
                " assorted buildings like houses and army barracks. Additionally, there \nare abstract places like"
                ' "the free world."'
            ),
            (
                "The following are various types of places: roads and streets, regions including villages, towns, and"
                " countries, \nstructures such as bridges and ports, natural locations like mountains, rivers, and"
                " forests, public places like squares, \nmuseums, and parks, commercial places like pubs and hotels,"
                " and assorted buildings like houses and monasteries. \nAdditionally, there are abstract places like"
                ' "the free world."'
            ),
        ]
    },
    "ner_miscellaneous": {
        "en": [
            (
                "Words of which one part is a location, organisation, miscellaneous, or person adjectives and other"
                " words derived \nfrom a word which is location, organisation, miscellaneous, or person religions"
                " political ideologies nationalities \nlanguages programs events (conferences, festivals, sports"
                " competitions, forums, parties, concerts) wars sports related \nnames (league tables, leagues, cups"
                " titles (books, songs, films, stories, albums, musicals, TV programs) slogans eras \nin time types"
                " (not brands) of objects (car types, planes, motorbikes)"
            ),
            (
                "This text describes a list of nouns that can be used to describe various things, including location,"
                " organizations, \nmiscellaneous items, and people. These nouns can be used to modify other words,"
                " such as adjectives derived from words that describe \nlocation, organizations, miscellaneous items,"
                " or people. Additionally, the text mentions specific types of events, such as \nconferences,"
                " festivals, sports competitions, forums, parties, concerts, and wars. It also mentions specific types"
                " of names, \nsuch as those related to sports leagues, cups, titles, and eras in time."
            ),
            (
                "The text describes a list of nouns that can be used in a sentence, including adjectives that describe"
                " places, \norganizations, miscellaneous things, and people, as well as nouns that refer to various"
                " types of religions, political ideologies, \nnationalities, languages, programs, events, and wars."
                " The list also includes nouns that refer to sports-related things, such as \nleagues, cups, and"
                " titles related to books, songs, films, stories, albums, musicals, and TV programs. Additionally, the"
                " \ntext includes nouns that describe different types of objects, such as car types, planes, and"
                " motorbikes, as well as nouns \nthat refer to different eras in time and types of objects."
            ),
            (
                "The text describes a list of nouns that can be used to describe various entities, including location,"
                " \norganizations, miscellaneous items, and people. These nouns can be derived from other words that"
                " refer to similar entities, such as \nreligions, political ideologies, nationalities, languages,"
                " programs, events, wars, sports-related names, and eras in \ntime. Examples of these nouns include"
                " adjectives, titles, slogans, and types of objects."
            ),
            (
                "The text describes a set of nouns that can be classified into various categories, including location"
                " and \norganization adjectives, religion and ideology nouns, nationality nouns, language nouns,"
                " program and event nouns, war nouns, \nsport-related nouns, and time period nouns. Examples of these"
                ' nouns include "location adjectives" like "New York City" or \n"organization adjectives" like "United'
                ' Nations," as well as "religion nouns" like "Christianity" and "political ideology \nnouns" like'
                ' "communism." Other examples include "nationality nouns" like "American" or "language nouns" like'
                ' \n"Spanish," as well as "program and event nouns" like "conference" or "festival," "war nouns" like'
                ' "World War II," \n"sport-related nouns" like "NBA," and "time period nouns" like "Renaissance."'
                ' Additionally, the text includes various slogans, \nlike "Make America Great Again," and eras in'
                ' time, like "21st century."'
            ),
        ]
    },
}
