import inspect
import random

import black
import rich

from src.tasks.conll03.prompts import Organization


GUIDELINES = {
    "ner_person": {
        "en": ["Persons: first, middle and last names of people, animals and fictional\ncharacters aliases."]
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
}


guideline = {key: random.choice(value["en"]) for key, value in GUIDELINES.items()}

rich.print(guideline)

source = inspect.getsource(Organization)
rich.print(source)
source = source.format(**guideline)

source = black.format_str(source, mode=black.Mode())

print(source)
