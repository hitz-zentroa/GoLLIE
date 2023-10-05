GUIDELINES = {
    "crossner_politics_person": {"en": ["Refers to an individual's name that is not a politician."]},
    "crossner_politics_organization": {
        "en": ["Refers to a structured group, institution, company, or association that is not a political party."]
    },
    "crossner_politics_location": {
        "en": [
            "Refers to a specific geographical or structural location. This includes but is not limited"
            " to: places (e.g., parks, landmarks), bridges, cities, towns, villages, areas and other distinct regions."
        ]
    },
    "crossner_politics_politician": {
        "en": [
            "Refers to a person who is actively engaged in politics, holding a public office, involved in political"
            " activities or part of a political party. "
            "If a person entity is identified as a politician, annotate that person's name as a politician entity."
        ]
    },
    "crossner_politics_politicalparty": {
        "en": [
            "A political party is an organization that coordinates candidates to compete in a particular country's"
            " elections. Also annotate acronyms of political parties."
        ]
    },
    "crossner_politics_election": {
        "en": [
            "Refers to an organized process in which individuals vote to choose a candidate or make a"
            " decision. If an event mentioned in the text pertains to an election, annotate it as an election entity."
        ]
    },
    "crossner_politics_event": {
        "en": [
            "Refers to a significant occurrence or happening. Such as wars, conferences, summits, conventions, etc."
        ]
    },
    "crossner_politics_country": {"en": ["Refers to a sovereign nation."]},
    "crossner_politics_miscellaneous": {
        "en": ["Refers to named entities that are not included in any other category."]
    },
    "crossner_naturalscience_scientist": {
        "en": [
            "Refers to a person who is studying or has expert knowledge of one or more of the natural or physical"
            " sciences."
        ]
    },
    "crossner_naturalscience_person": {"en": ["Refers to an individual's name that is not a scientist."]},
    "crossner_naturalscience_university": {
        "en": [
            "Refers to an educational institution of higher learning. Label organizations that are universities as"
            " 'university' entities."
        ]
    },
    "crossner_naturalscience_organization": {
        "en": [
            "Refers to a structured group, institution, company, or association. This category covers a"
            " diverse range of organizations, including businesses, non-profits, educational institutions, and"
            " government agencies."
        ]
    },
    "crossner_naturalscience_country": {"en": ["Refers to a sovereign nation."]},
    "crossner_naturalscience_location": {
        "en": [
            "Refers to a specific geographical or structural location. This includes but is not limited"
            " to: places (e.g., parks, landmarks), bridges, cities, towns, villages, areas and other distinct regions."
        ]
    },
    "crossner_naturalscience_discipline": {
        "en": [
            "Refers to a specialized field of study or research within the domains of natural science. Also label"
            " words such as biology, chemistry, astrophysics, mathematics or physics. This also includes specific"
            " branches such as quantum chemistry."
        ]
    },
    "crossner_naturalscience_enzyme": {
        "en": [
            " Refers to a specialized protein that acts as a biological catalyst, facilitating chemical reactions"
            " within organisms. If a protein is an enzyme, annotate it as an enzyme entity."
        ]
    },
    "crossner_naturalscience_protein": {
        "en": [
            "Refers to a complex biological molecule composed of amino acids, essential for various biological"
            " functions."
        ]
    },
    "crossner_naturalscience_chemicalelement": {
        "en": [
            "Refers to a fundamental substance characterized by its atomic number and unique properties, as found in"
            " the periodic table."
        ]
    },
    "crossner_naturalscience_chemicalcompound": {
        "en": [
            "Refers to a substance formed by combining two or more elements in fixed proportions, with distinct"
            " chemical properties."
        ]
    },
    "crossner_naturalscience_astronomicalobject": {
        "en": ["Refers to a celestial entity such as a star, planet, galaxy, or nebula, present in space."]
    },
    "crossner_naturalscience_academicjournal": {
        "en": [
            "Refers to a periodical publication containing scholarly articles and research findings related to natural"
            " science disciplines."
        ]
    },
    "crossner_naturalscience_event": {
        "en": ["Refers to a significant occurrence or happening. Such as festivals, sports events, conferences, etc."]
    },
    "crossner_naturalscience_award": {
        "en": [
            "Refers to a recognition or distinction presented to individuals or organizations for significant"
            " contributions within the natural science domain."
        ]
    },
    "crossner_naturalscience_theory": {
        "en": [
            "Refers to a scientifically established principle or explanation that describes natural phenomena within"
            " the scope of biology, chemistry, or astrophysics, such as orbital resonance. This encompasses laws and"
            " theories like the Ptolemaic planetary theories."
        ]
    },
    "crossner_naturalscience_miscellaneous": {
        "en": ["Refers to named entities that are not included in any other category."]
    },
    "crossner_music_musicgenre": {
        "en": [
            "Refers to a distinct category or style of music, characterized by its unique characteristics, themes, and"
            " instrumentation. Include regional musics typical of a certain place."
        ]
    },
    "crossner_music_song": {
        "en": [
            "Refers to a distinct category or style of music, characterized by its unique characteristics, themes, and"
            " instrumentation."
        ]
    },
    "crossner_music_band": {
        "en": [
            "Refers to a distinct category or style of music, characterized by its unique characteristics, themes, and"
            " instrumentation."
        ]
    },
    "crossner_music_album": {
        "en": ["Refers to a collection of songs or musical compositions released as a single package"]
    },
    "crossner_music_musicalartist": {
        "en": [
            "Refers to an individual actively involved in the creation, performance, or production of music. If a"
            " person is a singer, composer, or songwriter, annotate them as a musical artist entity instead of a"
            " person entity"
        ]
    },
    "crossner_music_musicalinstrument": {
        "en": ["Refers to a device or tool used to produce musical sounds, such as a piano, guitar, or drum."]
    },
    "crossner_music_award": {
        "en": ["Refers to a device or tool used to produce musical sounds, such as a piano, guitar, or drum."]
    },
    "crossner_music_event": {
        "en": ["Refers to a music-related occurrence or happening, such as a concert, festival, or competition."]
    },
    "crossner_music_country": {"en": ["Refers to a sovereign nation."]},
    "crossner_music_location": {
        "en": [
            "Refers to a specific geographical or structural location. This includes but is not limited"
            " to: places (e.g., parks, landmarks), bridges, cities, towns, villages, areas and other distinct regions."
        ]
    },
    "crossner_music_organization": {
        "en": [
            "Refers to a structured group, institution, company, or association. This category covers a"
            " diverse range of organizations, including businesses, non-profits, educational institutions, and"
            " government agencies."
        ]
    },
    "crossner_music_person": {"en": ["Refers to an individual's name that is not a musical artist."]},
    "crossner_music_miscellaneous": {"en": ["Refers to named entities that are not included in any other category."]},
    "crossner_literature_book": {
        "en": [
            "Refers to a published work of literature, typically consisting of written content bound in a physical or"
            " digital format."
        ]
    },
    "crossner_literature_writer": {
        "en": [
            " Refers to an individual actively engaged in the creation of literary works, including writers,"
            " novelists, scriptwriters, poets, and other literary artists. If a person is involved in"
            " literature-related roles, annotate them as a writer entity instead of a person entity."
        ]
    },
    "crossner_literature_award": {
        "en": [
            "Refers to a recognition or honor bestowed upon individuals or works of literature for notable"
            " achievements. "
        ]
    },
    "crossner_literature_poem": {
        "en": [
            "Refers to a literary composition characterized by its structured form, rhythm, and often heightened"
            " language. "
        ]
    },
    "crossner_literature_event": {
        "en": [
            "Refers to a significant occurrence or happening. Such as wars, conferences, festivals, sport events, etc."
        ]
    },
    "crossner_literature_magazine": {
        "en": ["Refers to a periodical publication that features articles, stories, and various literary works."]
    },
    "crossner_literature_literarygenre": {
        "en": [
            "Refers to categories in literature defined by unique artistic techniques, themes, content, and lengths."
            " Label words such as poetry, essay or novel as well as content categories like Science Fiction, Fantasy,"
            " and Fiction. It also encompasses culturally influenced genres, such as Nordic countries poetry."
        ]
    },
    "crossner_literature_person": {"en": ["Refers to an individual's name that is not a writer."]},
    "crossner_literature_location": {
        "en": [
            "Refers to a specific geographical or structural location. This includes but is not limited"
            " to: places (e.g., parks, landmarks), bridges, cities, towns, villages, areas and other distinct regions."
        ]
    },
    "crossner_literature_organization": {
        "en": [
            "Refers to a structured group, institution, company, or association. This category covers a"
            " diverse range of organizations, including businesses, non-profits, educational institutions, and"
            " government agencies."
        ]
    },
    "crossner_literature_country": {"en": ["Refers to a sovereign nation."]},
    "crossner_literature_miscellaneous": {
        "en": ["Refers to named entities that are not included in any other category."]
    },
    "crossner_ai_field": {
        "en": [
            "Refers to a specific research area or subfield within Artificial Intelligence. Also annotate acronyms"
            " such as NLP."
        ]
    },
    "crossner_ai_task": {
        "en": [
            "Refers to a particular research task or problem within a specific AI research field. Annotate the name of"
            " the specific task, such as machine translation or object detection."
        ]
    },
    "crossner_ai_product": {
        "en": [
            "Refers to a product, system, or toolkit related to Artificial Intelligence. This includes specific"
            " AI-enabled products (e.g., robots like Pepper), systems (e.g., facial recognition systems), and toolkits"
            " (e.g., Tensorflow and PyTorch)."
        ]
    },
    "crossner_ai_algorithm": {
        "en": [
            "Refers to an algorithmic procedure or computational model used in Artificial Intelligence research. This"
            " category includes algorithms (e.g., decision trees) and models (e.g., CNN and LSTM)."
        ]
    },
    "crossner_ai_researcher": {
        "en": [
            "Refers to an individual engaged in research activities within the field of Artificial Intelligence (AI),"
            " including professors, Ph.D. students, and researchers in academia, research institutions, and companies."
            " If a person is involved in AI research, label them as a researcher entity instead of a person entity."
        ]
    },
    "crossner_ai_metric": {
        "en": [
            "Refers to evaluation metrics used to assess the performance of AI models and algorithms. Annotate"
            " specific metrics like F1-score."
        ]
    },
    "crossner_ai_university": {
        "en": [
            "Refers to an educational institution of higher learning. Label organizations that are universities as"
            " 'university'' entities."
        ]
    },
    "crossner_ai_country": {"en": ["Refers to a sovereign nation."]},
    "crossner_ai_person": {"en": ["Refers to an individual's name that is not a researcher."]},
    "crossner_ai_organization": {
        "en": [
            "Refers to a structured group, institution, company, or association. This category covers a"
            " diverse range of organizations, including businesses, non-profits, educational institutions, and"
            " government agencies."
        ]
    },
    "crossner_ai_location": {
        "en": [
            "Refers to a specific geographical or structural location. This includes but is not limited"
            " to: places (e.g., parks, landmarks), bridges, cities, towns, villages, areas and other distinct regions."
        ]
    },
    "crossner_ai_programminglanguage": {
        "en": [
            "Refers to a programming language used in the development of AI applications and research. Annotate the"
            " name of the programming language, such as Java and Python."
        ]
    },
    "crossner_ai_conference": {
        "en": [
            "Refers to a research conference or journal in the field of Artificial Intelligence. This category"
            " includes conferences where AI research is presented and published."
        ]
    },
    "crossner_ai_miscellaneous": {"en": ["Refers to named entities that are not included in any other category."]},
}
