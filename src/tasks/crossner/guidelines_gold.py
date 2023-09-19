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

EXAMPLES = {
    "crossner_politics_person_examples": {
        "en": [
            "Bennelong",
            "Zappa",
            "Tower",
            "Andrea Fischer",
            "Wyden",
            "Johann Karl Thilo",
            "Rowse",
            "Brooks",
            "Anawrahta",
            "Fidel",
        ]
    },
    "crossner_politics_organization_examples": {
        "en": [
            "NARAL Pro-Choice America",
            "Planned Parenthood",
            "National Right to Life Committee",
            "United Daughters of the Confederacy",
            "Sons of Confederate Veterans",
            "Parliament",
            "Amnesty International",
            "Human Rights Watch",
            "American Enterprise Institute",
            "American Academy of Arts and Sciences",
        ]
    },
    "crossner_politics_location_examples": {
        "en": ["Paris", "London", "Berlin", "Rome", "Dublin", "Cairo", "Amsterdam", "Colombo", "Montreal", "Texas"]
    },
    "crossner_politics_politician_examples": {
        "en": [
            "Bush",
            "Ronald Reagan",
            "Al Gore",
            "Joseph Stalin",
            "Richard Nixon",
            "Thomas Jefferson",
            "Johnson",
            "Genscher",
            "Kennedy",
            "Franklin D. Roosevelt",
        ]
    },
    "crossner_politics_politicalparty_examples": {
        "en": [
            "SPD",
            "National Party of Australia",
            "Sinn F\u00e9in",
            "FDP",
            "Liberal Party of Australia",
            "Liberal",
            "Progressive Conservative Party of Canada",
            "Serbian Radical Party",
            "National Alliance",
            "Forza Italia",
        ]
    },
    "crossner_politics_election_examples": {
        "en": [
            "1997 Irish general election",
            "1992 United States presidential election",
            "1920 United States presidential election",
            "2000 United States presidential election",
            "2008 United States presidential election",
            "1983 United Kingdom general election",
            "1987 United Kingdom general election",
            "1934 Australian federal election",
            "2019 Australian federal election",
            "2007 Australian federal election",
        ]
    },
    "crossner_politics_event_examples": {
        "en": [
            "Decembrist revolt",
            "1952 Republican National Convention",
            "1943 Tehran Conference",
            "World War II",
            "1983 Commonwealth heads of Government summit",
            "TM movement",
            "Tydings-Butler race",
            "War of Liberation",
            "War of the Sixth Coalition",
            "Civil War",
        ]
    },
    "crossner_politics_country_examples": {
        "en": [
            "U.S.",
            "India",
            "China",
            "Germany",
            "United States",
            "Soviet Union",
            "Egypt",
            "Ghana",
            "Australia",
            "Serbia",
        ]
    },
    "crossner_politics_miscellaneous_examples": {
        "en": [
            "Republican",
            "German",
            "Democrat",
            "Soviet",
            "Republicans",
            "Polish",
            "British",
            "Texas Republicans",
            "Australian",
            "Uyghur",
        ]
    },
    "crossner_music_musicgenre_examples": {
        "en": [
            "Hip hop music",
            "Pop music",
            "reggae",
            "Punk rock",
            "Celtic rock",
            "Soul music",
            "Samba",
            "rock",
            "Electronic music",
            "Sacred Harp",
        ]
    },
    "crossner_music_song_examples": {
        "en": [
            "Is That Love",
            "Tempted",
            "Clubland",
            "New Lace Sleeves",
            "The Lunatics ( Have Taken Over the Asylum )",
            "East Coast Killer",
            "West Coast Killer",
            "Layla",
            "Cross Road Blues",
            "Spoonman",
        ]
    },
    "crossner_music_band_examples": {
        "en": [
            "Backstreet Boys",
            "Spice Girls",
            "NSYNC",
            "LFO",
            "O-Town",
            "US5",
            "Black Sabbath",
            "Take That",
            "U2",
            "PUSA",
        ]
    },
    "crossner_music_album_examples": {
        "en": [
            "American Idiot",
            "Dookie",
            "Sun Ra Visits Planet Earth",
            "Interstellar Low Ways",
            "Super-Sonic Jazz",
            "We Travel the Space Ways",
            "The Nubians of Plutonia",
            "Jazz In Silhouette",
            "Tea for the Tillerman",
            "Teaser and the Firecat",
        ]
    },
    "crossner_music_musicalartist_examples": {
        "en": [
            "Elvis Costello",
            "Nas",
            "Madonna",
            "Debbie Gibson",
            "Tiffany",
            "Sun Ra",
            "Stevens",
            "Verni",
            "Skates",
            "Ellsworth",
        ]
    },
    "crossner_music_musicalinstrument_examples": {
        "en": [
            "piano accordion",
            "six-string guitar banjo",
            "guitar",
            "keyboard",
            "bass guitar",
            "drums",
            "bass",
        ]
    },
    "crossner_music_award_examples": {
        "en": [
            "Grammy Award",
            "Brit Awards",
            "MTV Video Music Award",
            "Academy Awards",
            "Grammy Award for Best Alternative Music Album",
            "Academy Award for Best Director",
            "Academy Award for Best Picture",
            "Grammy Award s",
            "Top New Male Vocalist",
            "American Music Awards",
        ]
    },
    "crossner_music_event_examples": {
        "en": [
            "2003 World Championships in Athletics",
            "Vocal Event of the Year",
            "World War II",
            "Saint Patrick 's Day",
            "the first wave of glam metal",
            "panto season",
            "G\u0175yl Gobaith Music Festival",
            "UAAP Season 71",
            "1973 Summer Universiade",
            "1986 Goodwill Games",
        ]
    },
    "crossner_music_country_examples": {
        "en": [
            "U.S.",
            "United States",
            "United Kingdom",
            "Australia",
            "Germany",
            "Poland",
            "Canada",
            "New Zealand",
            "Japan",
            "Ireland",
        ]
    },
    "crossner_music_location_examples": {
        "en": [
            "Europe",
            "Stade de France",
            "Paris",
            "Th\u00e9\u00e2tre de la Ville",
            "Bay Area",
            "Grand Ole Opry",
            "AccorHotels Arena",
            "Bataclan",
            "Casino de Paris",
            "Maple Leaf Gardens",
        ]
    },
    "crossner_music_organization_examples": {
        "en": [
            "Recording Industry Association of America",
            "Billboard",
            "BBC News",
            "Academy of Country Music",
            "Country Music Association",
            "Op\u00e9ra-Comique",
            "United Way of Canada",
            "Official Charts Company",
            "British Phonographic Industry",
            "ARIA",
        ]
    },
    "crossner_music_person_examples": {
        "en": [
            "Barney Bubbles",
            "St\u00e9phane Lafarge",
            "Bubbles",
            "Wolf-R\u00fcdiger M\u00fchlmann",
            "Glen Campbell",
            "Bobbie Gentry",
            "John Denver",
            "Olivia Newton-John",
            "Lou Pearlman",
            "Nichols",
        ]
    },
    "crossner_music_miscellaneous_examples": {
        "en": [
            "Irish-American",
            "European",
            "Les Troyens \u00e0 Carthage",
            "Didon",
            "\u00c9n\u00e9e",
            "Billboard",
            "British duo",
            "King of the Bai\u00e3o",
            "funk",
            "Billboard 200",
        ]
    },
    "crossner_literature_book_examples": {
        "en": [
            "The Plague of Doves",
            "A History of Warfare",
            "The Color Purple",
            "Rabbit at Rest",
            "The Fountainhead",
            "Atlas Shrugged",
            "The Little Prince",
            "Anabasis Alexandri",
            "Pro Archia Poeta",
            "Pantoum of the Great Depression",
        ]
    },
    "crossner_literature_writer_examples": {
        "en": [
            "John Keegan",
            "Leo Tolstoy",
            "John Steinbeck",
            "Yeats",
            "Jacobs",
            "Isaac Bashevis Singer",
            "Capp",
            "Kong Huan",
            "\u5b54\u6d63",
            "Kong Shao",
        ]
    },
    "crossner_literature_award_examples": {
        "en": [
            "Pulitzer Prize",
            "Nebula Award",
            "Hugo Award",
            "Academy Awards",
            "Nobel Prize in Literature",
            "National Book Critics Circle Award",
            "Grand Prix Sp\u00e9cial du Jury",
            "FIPRESCI prize",
            "Palme d 'Or",
            "Silver Bear for Best Actor",
        ]
    },
    "crossner_literature_poem_examples": {
        "en": [
            "Barbara Frietchie",
            "The Barefoot Boy",
            "Maud Muller",
            "Snow-Bound",
            "Shishupala Vadha",
            "Naishadha Charita",
            "Nai\u1e63adh\u012bya-carita",
            "Prick of Conscience",
            "At a Calvary near the Ancre",
            "There Will Come Soft Rains",
        ]
    },
    "crossner_literature_event_examples": {
        "en": [
            "World War II",
            "Cannes Film Festival",
            "47th Berlin International Film Festival",
            "Luge at the 1976 Winter Olympics",
            "Equestrian at the 1976 Summer Olympics",
            "Trojan War",
            "Black Arts Movement",
            "Ether 7 Festival",
            "Cold War",
        ]
    },
    "crossner_literature_magazine_examples": {
        "en": [
            "The New Yorker",
            "Simbolul",
            "Private Eye",
            "The Atlantic",
            "The Crisis",
            "The New York Times Magazine",
            "T Living",
            "Neue Rundschau",
            "The Magazine of Fantasy & Science Fiction",
            "New Statesman",
        ]
    },
    "crossner_literature_literarygenre_examples": {
        "en": [
            "poem",
            "poems",
            "novels",
            "novel",
            "science fiction",
            "anti-slavery writings",
            "Symbolism",
            "experimental poetry",
            "science fiction short stories",
            "Negro primitivism",
        ]
    },
    "crossner_literature_person_examples": {
        "en": [
            "Lindbergh",
            "Giacomo di Benincasa",
            "Baron Cohen",
            "Emperor Toghon Tem\u00fcr",
            "Princess Noguk",
            "Gongmin",
            "Marcel Janco",
            "Jim Broadbent",
            "Major",
            "Norman",
        ]
    },
    "crossner_literature_location_examples": {
        "en": [
            "London",
            "Chalcedon",
            "Charles Dickens Museum",
            "Charles Dickens Birthplace Museum",
            "Portsmouth",
            "Lincoln Center",
            "Beethovensaal",
            "Berlin",
            "Bristol",
            "The Thekla",
        ]
    },
    "crossner_literature_organization_examples": {
        "en": [
            "Science Fiction and Fantasy Writers of America",
            "The New York Times",
            "New York Times",
            "Food52",
            "Amnesty International",
            "S. Fischer Verlag",
            "Project Gutenberg",
            "Hollywood",
            "Royal Society of Literature",
            "National Space Society",
        ]
    },
    "crossner_literature_country_examples": {
        "en": [
            "Germany",
            "Han dynasty",
            "England",
            "Italy",
            "Yuan dynasty",
            "China",
            "Korea",
            "Mauretania",
            "United States",
            "Denmark",
        ]
    },
    "crossner_literature_miscellaneous_examples": {
        "en": [
            "American",
            "British",
            "English",
            "French",
            "Goryeo",
            "Mongolian-born",
            "Rabbit novel",
            "Objectivism",
            "Nazi",
            "Middle English",
        ]
    },
    "crossner_ai_field_examples": {
        "en": [
            "deep learning",
            "pattern recognition",
            "image processing",
            "reinforcement learning",
            "natural language processing",
            "machine learning",
            "unsupervised learning",
            "AI",
            "computer vision",
            "text mining",
        ]
    },
    "crossner_ai_task_examples": {
        "en": [
            "speech synthesis",
            "information retrieval",
            "Feature extraction",
            "dimension reduction",
            "speech recognition",
            "sentiment analysis",
            "Multimodal sentiment analysis",
            "face recognition",
            "handwriting recognition",
            "lip reading",
        ]
    },
    "crossner_ai_product_examples": {
        "en": [
            "MATLAB",
            "Programmable Universal Machine for Assembly",
            "industrial robot",
            "opinion-based recommender system",
            "Octave",
            "Google Translate",
            "SYSTRAN system",
            "BabelFish",
            "Babelfish",
            "RapidMiner",
        ]
    },
    "crossner_ai_algorithm_examples": {
        "en": [
            "principal component analysis",
            "linear discriminant analysis",
            "gradient descent",
            "Support vector machine",
            "recurrent neural network",
            "LSTM",
            "PCA",
            "LDA",
            "canonical correlation analysis",
            "CCA",
        ]
    },
    "crossner_ai_researcher_examples": {
        "en": [
            "J\u00fcrgen Schmidhuber",
            "Seymour Papert",
            "Victor Scheinman",
            "Scheinman",
            "X.Y. Feng",
            "H. Zhang",
            "Y.J. Ren",
            "P.H. Shang",
            "Y. Zhu",
            "Y.C. Liang",
            "Oscar Sainz",
            "Iker García-Ferrero",
        ]
    },
    "crossner_ai_metric_examples": {
        "en": [
            "mean squared error",
            "DCG",
            "maximum likelihood",
            "Recall-Oriented Understudy for Gisting Evaluation",
            "MSE",
            "noise floor measurement",
            "ROUGE",
            "Hinge loss",
            "hinge loss",
            "Sigmoid function Cross entropy loss",
        ]
    },
    "crossner_ai_university_examples": {
        "en": [
            "University of Toronto",
            "Cambridge",
            "University of Groningen",
            "MIT",
            "Brown University",
            "Carnegie Mellon University",
            "MPI Saarbruecken",
            "Stanford University",
            "University of California , San Diego",
            "\u00c9cole Centrale Paris",
            "University of the Basque Country",
        ]
    },
    "crossner_ai_country_examples": {
        "en": ["Netherlands", "Japan", "Germany", "Canada", "Australia", "Brazil", "China", "India", "Italy", "Korea"]
    },
    "crossner_ai_person_examples": {
        "en": ["Francis Ford Coppola", "Michael Jackson", "John Wayne", "Rita Hayworth", "Dean Martin", "Jerry Lewis"]
    },
    "crossner_ai_organization_examples": {
        "en": [
            "Unimation",
            "IAPR",
            "Audio Engineering Society",
            "National Science Foundation",
            "National Aeronautics and Space Administration",
            "NASA",
            "US Department of Energy",
            "US Department of Commerce NIST",
            "US Department of Defense",
            "Defense Advanced Research Projects Agency",
            "HiTZ: Basque Center for Language Technology",
            "IXA NLP Group",
        ]
    },
    "crossner_ai_location_examples": {
        "en": [
            "Chi\u0219in\u0103u",
            "Paris",
            "Montreal",
            "Scotiabank Theatre Toronto",
            "TIFF Bell Lightbox",
            "Moldavian SSR",
        ]
    },
    "crossner_ai_programminglanguage_examples": {
        "en": ["Java", "R", "CLIPS", "Python", "C + +", "GNU Octave", "Java 9", "java", "Perl", "ActiveX"]
    },
    "crossner_ai_conference_examples": {
        "en": [
            "AAAI",
            "1982 Association for the Advancement of Artificial Intelligence",
            "SIGGRAPH",
            "Symposium on Geometry Processing",
            "International Journal of Computer Vision",
            "IJCV",
            "IEEE Computer Society Conference on Computer Vision and Pattern Recognition",
            "CVPR",
            "International Conference on Machine Learning 2011 & 2012",
            "NIST ' s annual Document Understanding Conferences",
        ]
    },
    "crossner_ai_miscellaneous_examples": {
        "en": [
            "unsupervised methods",
            "topological properties",
            "audio signal",
            "eigenfaces",
            "intelligent agents",
            "graphical user interfaces",
            "Heuretics : Theoretical and Study of Heuristic Rules",
            "Best Paper award",
            "Johann Bernoulli Chair",
            "Toshiba Endowed Chair",
        ]
    },
    "crossner_naturalscience_scientist_examples": {
        "en": [
            "Werner Heisenberg",
            "Robert Boyle",
            "Hans Kramers",
            "Isaac Newton",
            "Galileo Galilei",
            "Carl Friedrich von Weizs\u00e4cker",
            "Walther Bothe",
            "August Kopff",
            "Wolf",
            "Edgar H. Booth",
        ]
    },
    "crossner_naturalscience_person_examples": {
        "en": [
            "Shenton",
            "Russell T Davies",
            "Aristotle",
            "Hall",
            "NeNe Leakes",
            "Nicki Minaj",
            "Rihanna",
            "Solange Knowles",
            "Beyonc\u00e9",
            "Sharkeisha",
        ]
    },
    "crossner_naturalscience_university_examples": {
        "en": [
            "University of Sydney",
            "Oxford",
            "Uppsala University",
            "University of Calcutta",
            "Odessa University",
            "Cambridge",
            "University of T\u00fcbingen",
            "University of G\u00f6ttingen",
            "Oak Ridge Associated Universities",
            "Heidelberg University",
        ]
    },
    "crossner_naturalscience_organization_examples": {
        "en": [
            "Royal Society",
            "American Academy of Arts and Sciences",
            "National Academy of Sciences",
            "International Union of Geodesy and Geophysics",
            "American Philosophical Society",
            "Cavendish Laboratory",
            "Royal Swedish Academy of Sciences",
            "American Association for the Advancement of Science",
            "University of Maryland Medical Center",
            "R Adams Cowley Shock Trauma Center",
        ]
    },
    "crossner_naturalscience_country_examples": {
        "en": [
            "Newfoundland Colony",
            "France",
            "United States",
            "Russia",
            "Japan",
            "UK",
            "England",
            "Italy",
            "Britain",
        ]
    },
    "crossner_naturalscience_location_examples": {
        "en": [
            "Cape of Good Hope",
            "Mumbai",
            "Heidelberg",
            "Royal Prince Alfred Hospital",
            "Sydney",
            "Annapolis",
            "MD",
            "Little Bay Copper Mine",
            "Thimble Tickle Bay",
            "Notre Dame Bay",
        ]
    },
    "crossner_naturalscience_discipline_examples": {
        "en": [
            "philosophy",
            "chemistry",
            "medicine",
            "electrodynamics",
            "spectroscopy",
            "geodesy",
            "geophysics",
            "Arts",
            "Literature of Belgium",
            "Electrical Engineering",
        ]
    },
    "crossner_naturalscience_enzyme_examples": {
        "en": [
            "RNA polymerase",
            "DNA methyltransferase",
            "DNA polymerase",
            "Spermidine synthase",
            "Alkaline phosphatase",
            "T7 RNA polymerase",
            "ribulose-1,5-bisphosphate carboxylase oxygenase",
            "RuBisCO",
            "ATP synthase",
            "Histone deacetylase",
        ]
    },
    "crossner_naturalscience_protein_examples": {
        "en": [
            "Argonaute",
            "Histone H3",
            "CYP1A1",
            "Green fluorescent protein",
            "glutamate binding protein",
            "GluBP",
            "Gamma-glutamyltransferase",
            "RNase inhibitor",
            "Histone",
            "nuclear proteins",
        ]
    },
    "crossner_naturalscience_chemicalelement_examples": {
        "en": [
            "sulfur",
            "copper",
            "hydrogen",
            "helium",
            "Nihonium",
            "americium",
            "europium",
            "curium",
            "gadolinium",
            "lead",
        ]
    },
    "crossner_naturalscience_chemicalcompound_examples": {
        "en": [
            "carbon dioxide",
            "Adenosine triphosphate",
            "Nitric oxide",
            "ROS",
            "cytosine",
            "Vespel",
            "neoprene",
            "nylon",
            "Corian",
            "Polytetrafluoroethylene",
        ]
    },
    "crossner_naturalscience_astronomicalobject_examples": {
        "en": ["Saturn", "Jupiter", "Venus", "Earth", "Uranus", "Mercury", "Neptune", "Mars", "Sun", "5145 Pholus"]
    },
    "crossner_naturalscience_academicjournal_examples": {
        "en": [
            "Angewandte Chemie",
            "The Astrophysical Journal",
            "Nature",
            "Chemical Reviews",
            "Accounts of Chemical Research",
            "The Astronomical Journal",
            "Cell",
            "Proceedings of the National Academy of Sciences of the United States of America",
            "Journal of Molecular Biology",
            "Annales de chimie et de physique",
        ]
    },
    "crossner_naturalscience_event_examples": {
        "en": [
            "2017 World Championships in Athletics",
            "Tomorrowland",
            "A State Of Trance",
            "Ultra Music Festival",
            "Electric Daisy Carnival",
            "Electric Zoo",
            "Gatecrasher",
            "Beyond Wonderland",
            "The men 's + 100 kg judo event",
            "2015 European Games",
        ]
    },
    "crossner_naturalscience_theory_examples": {
        "en": [
            "Protein-DNA interaction",
            "circular dichroism",
            "stem cell niche theory",
            "Nicolaus Copernicus heliocentric theory",
            "metaphysics",
            "methodology",
            "theory of evolution",
            "higher-order consciousness",
        ]
    },
    "crossner_naturalscience_award_examples": {
        "en": [
            "Nobel Prize in Physics",
            "Nobel Prize in Chemistry",
            "Fellow of the American Physical Society",
            "fellow of the Royal Society",
            "Copley Medal of the Royal Society",
            "Copley Medal",
            "Baronet MD Royal Society",
            "fellow of the Linnean Society of London",
            "Palit Professor of Physics",
            "Max Planck Medal",
        ]
    },
    "crossner_naturalscience_miscellaneous_examples": {
        "en": [
            "DNA",
            "Greeks",
            "Aryl hydrocarbon receptor repressor",
            "CRISPR",
            "Japanese",
            "American",
            "Arabidopsis thaliana",
            "DNA mismatch repair",
            "keratins",
            "Athletics",
        ]
    },
}
