GUIDELINES = {
    "ace_gpe": {
        "en": [
            "Geo-Political Entities are composite entities comprised of a population, a government, a physical\n"
            "location, and a nation (or province, state, country, city, etc.).\n"
        ]
    },
    "ace_acquit": {
        "en": [
            "An Acquit Event occurs whenever a trial ends but fails to produce a conviction. This will include cases\n"
            "where the charges are dropped by the Prosecutor.\n"
        ]
    },
    "ace_agentartifactrelationrelation": {
        "en": [
            "The AgentArtifact Relation applies when an agent owns an artifact, has possession of an artifact, uses\n"
            "an artifact, or caused an artifact to come into being. Note: if the `arg2` is an Organization, use\n"
            "OrganizationAffiliation when `arg1` is a Person or PartWhole when `arg1` is an Organization or GPE.\n"
        ]
    },
    "ace_appeal": {
        "en": ["An Appeal Event occurs whenever the decision of a court is taken to a higher court for review."]
    },
    "ace_arrestjail": {
        "en": [
            "A Jail Event occurs whenever the movement of a Person is constrained by a state actor (a GPE, its\n"
            "Organization subparts, or its Person representatives).\n"
        ]
    },
    "ace_attack": {
        "en": [
            "An Attack Event is defined as a violent physical act causing harm or damage. Attack Events include any\n"
            "such Event not covered by the Injure or Die subtypes, including Events where there is no stated agent.\n"
        ]
    },
    "ace_beborn": {"en": ["A BeBorn Event occurs whenever a Person Entity is given birth to."]},
    "ace_business": {
        "en": [
            "The Business Relation captures the connection between two entities in any professional relationship.\n"
            "Both arguments must be entities of type Person.\n"
        ]
    },
    "ace_businessevent": {
        "en": [
            "A BusinessEvent refers to actions related to Organizations such as: creating, merging, declaring\n"
            "bankruptcy or ending organizations (including government agencies).\n"
        ]
    },
    "ace_chargeindict": {
        "en": [
            "A Charge Event occurs whenever a Person, Organization or GPE is accused of a crime by a state actor\n"
            "(GPE, an Organization subpart of a GPE or a Person representing a GPE).\n"
        ]
    },
    "ace_citizenresidentreligionethnicity": {
        "en": [
            "CitizenResidentReligionEthnicity describes the relation between a Person entity and (1) the GPE in\n"
            "which they have citizenship, (2) the GPE or Location in which they live, the religious Organization or\n"
            "Person entity with which they have affiliation and (3) the GPE or PER entity that indicates their\n"
            "ethnicity.\n"
        ]
    },
    "ace_conflictevent": {
        "en": [
            "A ConflictEvent refers to either violent physical acts causing harm or damage, but are not covered by\n"
            "Life events (conflicts, clashes, fighting, gunfire, ...) or demonstrations (protests, sit-ins,\n"
            "strikes, riots, ...).\n"
        ]
    },
    "ace_contactevent": {
        "en": [
            "A ContactEvent occurs whenever two or more entities (persons or organization's representatives) come\n"
            "together at a single location and interact with one another face-to-face or directly enages in\n"
            "discussion via written or telephone communication.\n"
        ]
    },
    "ace_contactinfo": {
        "en": [
            "A ContactInfo value refers to contact information values such as telephone numbers, emails, addresses.\n"
            "For example: 'mich...@sumptionandwyland.com', ...\n"
        ]
    },
    "ace_convict": {
        "en": [
            "A Convict Event occurs whenever a Try Event ends with a successful prosecution of the Defendant. In\n"
            "other words, a Person, Organization or GPE Entity is convicted whenever that Entity has been found\n"
            "guilty of a Crime.\n"
        ]
    },
    "ace_crime": {
        "en": [
            "A Crime value refers to the specific reason (crime) that a Person entity can be judged or sentenced\n"
            "for. For example: 'raping', 'murder', 'drug', ...\n"
        ]
    },
    "ace_declarebankruptcy": {
        "en": [
            "A DeclareBankruptcy Event will occur whenever an Entity officially requests legal protection from debt\n"
            "collection due to an extremely negative balance sheet.\n"
        ]
    },
    "ace_demonstrate": {
        "en": [
            "A Demonstrate Event occurs whenever a large number of people come together in a public area to protest\n"
            "or demand some sort of official action. Demonstrate Events include, but are not limited to,\n"
            "protests, sit-ins, strikes, and riots.\n"
        ]
    },
    "ace_die": {
        "en": [
            "A Die Event occurs whenever the life of a Person Entity ends. Die Events can be accidental, intentional\n"
            "or self-inflicted\n"
        ]
    },
    "ace_divorce": {
        "en": [
            "A Divorce Event occurs whenever two people are officially divorced under the legal definition of\n"
            "divorce. We do not include separations or church annulments.\n"
        ]
    },
    "ace_elect": {
        "en": [
            "An Elect Event occurs whenever a candidate wins an election designed to determine the Person argument\n"
            "of a StartPosition Event.\n"
        ]
    },
    "ace_employment": {
        "en": [
            "Employment captures the relationship between Persons and their employers. This Relation is only\n"
            "taggable when it can be reasonably assumed that the Person is paid by the ORG or GPE.\n"
        ]
    },
    "ace_endorg": {
        "en": [
            "An EndOrg Event occurs whenever an Organization ceases to exist (in other words 'goes out of\n"
            "business').\n"
        ]
    },
    "ace_endposition": {
        "en": [
            "An EndPosition Event occurs whenever a Person Entity stops working for (or changes offices within) an\n"
            "Organization or GPE.\n"
        ]
    },
    "ace_execute": {
        "en": [
            "An Execute Event occurs whenever the life of a Person is taken by a state actor (a GPE, its\n"
            "Organization subparts, or Person representatives).\n"
        ]
    },
    "ace_extradite": {
        "en": [
            "An Extradite Event occurs whenever a Person is sent by a state actor from one Place (normally the GPE\n"
            "associated with the state actor, but sometimes a Facility under its control) to another place\n"
            "(Location, GPE or Facility) for the purposes of legal proceedings there.\n"
        ]
    },
    "ace_facility": {
        "en": [
            "A facility is a functional, primarily man-made structure. These include buildings and similar\n"
            "facilities designed for human habitation, such as houses, factories, stadiums, office buildings, ...\n"
            "Roughly speaking, facilities are artifacts falling under the domains of architecture and civil\n"
            "engineering.\n"
        ]
    },
    "ace_family": {
        "en": [
            "The Family Relation captures the connection between one entity and another with which it is in any\n"
            "familial relationship. Both arguments must be entities of type Person.\n"
        ]
    },
    "ace_fine": {
        "en": [
            "A Fine Event takes place whenever a state actor issues a financial punishment to a GPE, Person or\n"
            "Organization Entity, typically as a result of court proceedings.\n"
        ]
    },
    "ace_founder": {
        "en": [
            "Founder captures the relationship between an agent (Person, Organization, or GPE) and an Organization\n"
            "or GPE established or set up by that agent.\n"
        ]
    },
    "ace_genaffiliationrelation": {
        "en": [
            "The GenAffiliation Relation describes the citizen, resident, religion or ethnicity relation when the\n"
            "`arg1` is a Person. When the `arg1` is an Organization, the relation describes where it is located,\n"
            "based or does business.\n"
        ]
    },
    "ace_geographical": {
        "en": [
            "The Geographical relation captures the location of a Facility, Location, or GPE in or at or as a part\n"
            "of another Facility, Location, or GPE.\n"
        ]
    },
    "ace_injure": {
        "en": [
            "An Injure Event occurs whenever a Person Entity experiences physical harm. Injure Events can be\n"
            "accidental, intentional or self-inflicted.\n"
        ]
    },
    "ace_investorshareholder": {
        "en": [
            "InvestorShareholder captures the relationship between an agent (Person, Organization, or GPE) and an\n"
            "Organization in which the agent has invested or in which the agent owns shares/stock. Please note that\n"
            "agents may invest in GPEs.\n"
        ]
    },
    "ace_jobtitle": {
        "en": [
            "A JobTitle value refers to the name of the job or position of a Person entity in a Organization. For\n"
            "example: 'co-chief executive', 'move coordinator', 'interim ED', ...\n"
        ]
    },
    "ace_justiceevent": {
        "en": [
            "A JusticeEvent refers to any judicial action such as: arresting, jailing, releasing, granting parole,\n"
            "trial starting, hearing, charging, indicting, suing, convicting, sentencing, fine, executing,\n"
            "extraditing, adquiting, appealing or pardoning a Person entity.\n"
        ]
    },
    "ace_lastingpersonal": {
        "en": [
            "Lasting-Personal captures relationships that meet the following conditions: (1) The relationship must\n"
            "involve personal contact (or a reasonable assumption thereof). (2) There must be some indication or\n"
            "expectation that the relationship exists outside of a particular cited interaction. Both arguments\n"
            "must be entities of type Person.\n"
        ]
    },
    "ace_lifeevent": {
        "en": ["A LifeEvent occurs whenever a Person Entity borns, dies, gets married, divorced or gets injured."]
    },
    "ace_located": {
        "en": [
            "The Located relation captures the physical location of an entity. This relation is restricted to\n"
            "people. In other words, `arg1` in Located relations can only be occupied by mentions of Entities of\n"
            "type Person.\n"
        ]
    },
    "ace_location": {
        "en": [
            "Places defined on a geographical or astronomical basis which are mentioned in a document and do not\n"
            "constitute a political entity give rise to Location entities. These include, for example, the solar\n"
            "system, Mars, the Hudson River, Mt. Everest, and Death Valley.\n"
        ]
    },
    "ace_marry": {
        "en": ["Marry Events are official Events, where two people are married under the legal definition."]
    },
    "ace_meet": {
        "en": [
            "A Meet Event occurs whenever two or more Entities come together at a single location and interact with\n"
            "one another face-to-face. Meet Events include talks, summits, conferences, meetings, visits, and any\n"
            "other Event where two or more parties get together at some location.\n"
        ]
    },
    "ace_membership": {
        "en": [
            "Membership captures the relationship between an agent and an organization of which the agent is a\n"
            "member. Organizations and GPEs can be members of other Organizations (such as NATO or the UN).\n"
        ]
    },
    "ace_mergeorg": {
        "en": [
            "A MergeOrg Event occurs whenever two or more Organization Entities come together to form a new\n"
            "Organization Entity. This Event applies to any kind of Organization, including government agencies. It\n"
            "also includes joint venture.\n"
        ]
    },
    "ace_movementevent": {
        "en": [
            "A TransportEvent occurs whenever an Artifact (Weapon or Vehicle) or a Person is moved from one Place\n"
            "(GPE, Facility, Location) to another. This event requires the explicit mention of the Artifact or\n"
            "Person.\n"
        ]
    },
    "ace_near": {
        "en": [
            "Near indicates that an entity is explicitly near another entity, but neither entity is a part of the\n"
            "other or located in/at the other.\n"
        ]
    },
    "ace_nominate": {
        "en": [
            "A Nominate Event occurs whenever a Person is proposed for a StartPosition Event by the appropriate\n"
            "Person, through official channels.\n"
        ]
    },
    "ace_numeric": {
        "en": [
            "A Numeric value refers to relevant numbers, amounts, etc. For example: 'billions of dollars', '50\n"
            "percent', '100%', ...\n"
        ]
    },
    "ace_organization": {
        "en": [
            "Each organization or set of organizations mentioned in a document gives rise to an entity of type\n"
            "Organization. Typical examples are businesses, government units, sports teams, and formally organized\n"
            "music groups.\n"
        ]
    },
    "ace_organizationaffiliationrelation": {
        "en": [
            "The OrganizationAffiliation Relation describes the relations between a Person (or other Organizations)\n"
            "and a related Organization. This relation includes: employment, ownership, founder, student or alumn,\n"
            "sport affiliation, inverstor or shareholder and membership relations.\n"
        ]
    },
    "ace_orglocationorigin": {
        "en": [
            "OrgLocationOrigin captures the relationship between an organization and the Location or GPE where it is\n"
            "located, based, or does business. Note: Subsidiary trumps this relation for government organizations.\n"
        ]
    },
    "ace_ownership": {
        "en": [
            "Ownership captures the relationship between a Person and an Organization owned by that Person. If the\n"
            "`arg2` is not an Organization, use the Agent-Artifact relation.\n"
        ]
    },
    "ace_pardon": {
        "en": [
            "A Pardon Event occurs whenever a head-of-state or their appointed representative lifts a sentence\n"
            "imposed by the judiciary.\n"
        ]
    },
    "ace_partwholerelation": {
        "en": [
            "The PartWhole Relation refers to the semantic relation between two entities that are parts of a larger\n"
            "whole or vice versa. For example, the relation between a country and its states, or between a company\n"
            "and its subsidiaries, are instances of PartWhole relations.\n"
        ]
    },
    "ace_person": {
        "en": [
            "Each distinct person or set of people mentioned in a document refers to an entity of type Person. For\n"
            'example, people may be specified by name ("John Smith"), occupation ("the butcher"), family relation\n'
            '("dad"), pronoun ("he"), etc., or by some combination of these.'
        ]
    },
    "ace_personalsocialrelation": {
        "en": [
            "The Personal-Social Relation describe the relationship between people. Both arguments must be entities\n"
            "of type Person. Please note: The arguments of these Relations are not ordered. The Relations are\n"
            "symmetric.\n"
        ]
    },
    "ace_personnelevent": {
        "en": [
            "A PersonnelEvent occurs when a Person entity changes its job position (JobTitle entity) with respect an\n"
            "Organization entity. It includes when a person starts working, ends working, changes offices within,\n"
            "gets nominated or is elected for a position in a Organization.\n"
        ]
    },
    "ace_phonewrite": {
        "en": [
            "A PhoneWrite Event occurs when two or more people directly engage in discussion which does not take\n"
            "place 'face-to-face'. To make this Event less open-ended, we limit it to written or telephone\n"
            "communication where at least two parties are specified.\n"
        ]
    },
    "ace_physicalrelation": {
        "en": [
            "The Physical Relation captures the physical location relation of entities such as: a Person entity\n"
            "located in a Facility, Location or GPE; or two entities that are near, but neither entity is a part of\n"
            "the other or located in/at the other.\n"
        ]
    },
    "ace_releaseparole": {
        "en": [
            "A Release Event occurs whenever a state actor (GPE, Organization subpart, or Person representative)\n"
            "ends its custody of a Person Entity.\n"
        ]
    },
    "ace_sentence": {
        "en": [
            "A Sentence value refers to sentences decided by a court or judge for a specific crime. For example:\n"
            "'124 years in prison', 'a sentence', 'death'...\n"
        ]
    },
    "ace_sentenceact": {
        "en": [
            "A SentenceAct Event takes place whenever the punishment (particularly incarceration) for the Defendant\n"
            "of a Try Event is issued by a state actor (a GPE, an Organization subpart or a Person representing\n"
            "them)\n"
        ]
    },
    "ace_sportsaffiliation": {
        "en": [
            "Sports-Affiliation captures the relationship between a player, coach, manager, or assistant and his or\n"
            "her affiliation with a sports organization (including sports leagues or divisions as well as\n"
            "individual sports teams).\n"
        ]
    },
    "ace_startorg": {"en": ["A StartOrg Event occurs whenever a new Organization is created."]},
    "ace_startposition": {
        "en": [
            "A StartPosition Event occurs whenever a Person Entity begins working for (or changes offices within) an\n"
            "Organization or GPE. This includes government officials starting their terms, whether elected or\n"
            "appointed.\n"
        ]
    },
    "ace_studentalum": {
        "en": [
            "StudentAlum captures the relationship between a Person and an educational institution the Person\n"
            "attends or attended.\n"
        ]
    },
    "ace_subsidiary": {
        "en": [
            "Subsidiary captures the ownership, administrative, and other hierarchical relationships between\n"
            "organizations and between organizations and GPEs.\n"
        ]
    },
    "ace_sue": {
        "en": [
            "A Sue Event occurs whenever a court proceeding has been initiated for the purposes of determining the\n"
            "liability of a Person, Organization or GPE accused of committing a crime or neglecting a commitment.\n"
        ]
    },
    "ace_time": {
        "en": [
            "A Time value refers to a specific time frame. Usually known as time expressions. For example: '4\n"
            "years', 'today', 'December', 'future', ...\n"
        ]
    },
    "ace_transactionevent": {
        "en": [
            "A TransactionEvent refers to buying, selling, loaning, borrowing, giving, or receving of Artifacts or\n"
            "Organizations; or giving, receiving, borrowing, or lending Money.\n"
        ]
    },
    "ace_transfermoney": {
        "en": [
            "TransferMoney Events refer to the giving, receiving, borrowing, or lending money when it is not in the\n"
            "context of purchasing something. The canonical examples are: (1) people giving money to organizations\n"
            "(and getting nothing tangible in return); and (2) organizations lending money to people or other orgs.\n"
        ]
    },
    "ace_transferownership": {
        "en": [
            "TransferOwnership Events refer to the buying, selling, loaning, borrowing, giving, or receiving of\n"
            "artifacts or organizations.\n"
        ]
    },
    "ace_transport": {
        "en": [
            "A Transport Event occurs whenever an Artifact (Weapon or Vehicle) or a Person is moved from one Place\n"
            "(GPE, Facility, Location) to another.\n"
        ]
    },
    "ace_trialhearing": {
        "en": [
            "A Trial Event occurs whenever a court proceeding has been initiated for the purposes of determining the\n"
            "guilt or innocence of a Person, Organization or GPE accused of committing a crime.\n"
        ]
    },
    "ace_userownerinventormanufacturer": {
        "en": [
            "This Relation applies when an agent owns an artifact, has possession of an artifact, uses an artifact,\n"
            "or caused an artifact to come into being. Note: if `arg2` is an Organization, use Ownership relation\n"
            "(arg1=PER) or Subsidiary relation (arg1=ORG or GPE).\n"
        ]
    },
    "ace_vehicle": {
        "en": [
            "A Vehicle entity refers to vehicles that are used for transportation. The vehicles can transport either\n"
            "persons or artifacts. For example: 'car', 'plane', 'cabin', ...\n"
        ]
    },
    "ace_weapon": {
        "en": [
            "A Weapon entity refers to instruments that can be used to deal physical damage, destroy something or\n"
            "kill someone. For example: 'bomb', 'm-16s', 'missile', ...\n"
        ]
    },
}

EXAMPLES = {
    "ace_lifeevent_examples": {
        "en": [
            "wounded",
            "divorce",
            "birth",
            "born",
            "marriage",
            "married",
            "suicide",
            "killing",
            "injured",
            "died",
            "killed",
        ]
    },
    "ace_movementevent_examples": {
        "en": ["travel", "arrived", "going", "moving", "take", "went", "get", "trip", "come", "go"]
    },
    "ace_transactionevent_examples": {
        "en": [
            "donate",
            "received",
            "paying",
            "seize",
            "contributions",
            "donations",
            "captured",
            "bought",
            "paid",
            "pay",
        ]
    },
    "ace_businessevent_examples": {
        "en": [
            "started",
            "open",
            "create",
            "closing",
            "merged",
            "merging",
            "set up",
            "founded",
            "merger",
            "bankruptcy",
        ]
    },
    "ace_conflictevent_examples": {
        "en": ["terrorism", "combat", "hit", "fight", "bombing", "fire", "attacks", "fighting", "attack", "war"]
    },
    "ace_contactevent_examples": {
        "en": ["meetings", "conference", "talked", "met", "letters", "summit", "call", "meet", "talks", "meeting"]
    },
    "ace_personnelevent_examples": {
        "en": [
            "won",
            "appoint",
            "retired",
            "fired",
            "appointed",
            "resigned",
            "elected",
            "former",
            "elections",
            "election",
        ]
    },
    "ace_justiceevent_examples": {
        "en": [
            "parole",
            "sued",
            "sentenced",
            "appeal",
            "charged",
            "sentence",
            "arrested",
            "convicted",
            "charges",
            "trial",
        ]
    },
    "ace_person_examples": {
        "en": ["I", "you", "they", "troops", "forces", "people", "who", "officials", "we", "them"]
    },
    "ace_organization_examples": {
        "en": [
            "they",
            "military",
            "company",
            "CNN",
            "U.N.",
            "companies",
            "police",
            "administration",
            "court",
            "government",
        ]
    },
    "ace_gpe_examples": {
        "en": ["Iraq", "U.S.", "they", "country", "Baghdad", "city", "US", "coalition", "Israel", "British"]
    },
    "ace_location_examples": {
        "en": ["world", "area", "there", "where", "here", "mars", "areas", "border", "planet", "region"]
    },
    "ace_facility_examples": {
        "en": ["home", "airport", "base", "there", "hospital", "house", "prison", "room", "bridge", "road"]
    },
    "ace_weapon_examples": {
        "en": ["weapons", "gun", "missiles", "nuclear", "artillery", "bomb", "arms", "granades", "explosive", "knife"]
    },
    "ace_vehicle_examples": {
        "en": ["ship", "car", "aircraft", "tank", "plane", "bus", "vehicle", "boat", "helicopter", "truck"]
    },
    "ace_time_examples": {
        "en": [
            "Tuesday",
            "Monday",
            "tonight",
            "new",
            "this morning",
            "yesterday",
            "right now",
            "former",
            "today",
            "now",
        ]
    },
    "ace_numeric_examples": {
        "en": [
            "$800 million",
            "$30 million",
            "60 percent",
            "$2 million",
            "$500 billion",
            "billions of dollars",
            "40%",
            "$90 million",
            "100%",
            "$250,000",
        ]
    },
    "ace_jobtitle_examples": {
        "en": [
            "a pastor",
            "a counselor",
            "Presidential",
            "Vice President",
            "Governor of uh New Jersey",
            "head of Homeland Security",
            "president",
            "governor",
            "the Shah of Iran",
            "the CEO",
        ]
    },
    "ace_crime_examples": {
        "en": [
            "corruption",
            "theft",
            "receiving bribes",
            "killing",
            "insider trading",
            "attempted murder",
            "treason",
            "obstruction of justice",
            "sodomy",
            "murder",
        ]
    },
    "ace_sentence_examples": {
        "en": [
            "prison for life",
            "the maximum sentence",
            "a death penalty",
            "more than seven years in prison",
            "death",
            "five years probation",
            "100 lashes",
            "life",
            "life in prison",
            "the death penalty",
        ]
    },
    "ace_contactinfo_examples": {
        "en": [
            "911",
            "www.werkheiserfordelegate.com",
            "770-239-X X X X",
            "DKo...@hotmail.com",
            "a...@yahoo.com",
            "cnn.com/wolf",
            "www.vitac.com",
            "am@cnn.com",
        ]
    },
}
