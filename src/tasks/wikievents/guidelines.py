GUIDELINES = {
    "wikievents_ner_abstract": {
        "en": [
            (
                "Abstract, non-tangible artifacts such as software (e.g., programs, tool kits, apps, e-mail),"
                " measureable \nintellectual property, contracts, etc. (nb: does not include laws, which are LAW type)"
            ),
            (
                'Paraphrased text: "Intangible, abstract items like software (for example, programs, toolkits, apps,'
                " email), \nquantifiable intellectual property, contracts, and so on (excluding laws, which are a"
                " separate category)."
            ),
            (
                'Paraphrased text: "Intangible, abstract items like software (for example, programs, toolkits, apps,'
                " email), \nquantifiable intellectual property, contracts, and so on (excluding laws, which are part"
                " of the LEGAL type)."
            ),
            (
                'Paraphrased text: "Intangible, abstract items like software (for example, programs, toolkits, apps,'
                " email), \nintellectual property that can be quantified, agreements, and so on (exclusion: laws,"
                ' which are part of the LEGAL type)".'
            ),
            (
                "Abstract, intangible items like software (e.g., programs, toolkits, apps, email) and measurable"
                " intellectual \nproperty, such as contracts, etc. (excluding laws, which are a separate category)"
            ),
        ]
    },
    "wikievents_ner_bodypart": {
        "en": [
            "An identifiable, living part of a human's or animal's body, such as a eye, ear, neck, leg, etc.",
            "A recognizable, living component of a human or animal's body, like an eye, ear, neck, leg, and so on.",
            (
                "A distinguishable, living component of a human or animal body, such as an eye, ear, neck, leg, and"
                " so on."
            ),
            "A distinguishable, living component of a human or animal body, like an eye, ear, neck, leg, and so on.",
            "A distinct, living component of a human or animal's body, like an eye, ear, neck, or leg, for example.",
        ]
    },
    "wikievents_ner_commercialproduct": {
        "en": [
            (
                "A tangible product or article of trade for which someone pays or barters, or more generally, an"
                " artifact or a thing."
            ),
            (
                "A concrete item that is purchased or exchanged in a trade, or more broadly, a material object or"
                " article."
            ),
            "A concrete item that is bought or exchanged by someone, or more broadly, a material object or article.",
            (
                "A concrete item that is purchased or exchanged in a trade, or more broadly, a material object or"
                " article."
            ),
            (
                "A concrete item that is exchanged for money or another item of value, or more broadly, a material"
                " object or article."
            ),
        ]
    },
    "wikievents_ner_facility": {
        "en": [
            (
                "A functional, primarily man-made structure. Facilities are artifacts falling under the domains of"
                " architecture \nand civil engineering, including more temporary human constructs, such as police"
                " lines and checkpoints."
            ),
            (
                "A functional, predominantly human-created construction. Facilities encompass items classified under"
                " the \nfields of architecture and civil engineering, encompassing even temporary human creations,"
                " like police barriers and \ncheckpoints."
            ),
            (
                "A functional, predominantly human-created construction. Facilities are examples of architecture and"
                " civil \nengineering, encompassing even temporary human-made structures like police barricades and"
                " checkpoints."
            ),
            (
                "A functional, predominantly human-created construction. Facilities encompass items classified under"
                " the \nfields of architecture and civil engineering, as well as transient human-built structures,"
                " like police barriers and \ncheckpoints."
            ),
            (
                "An operational, predominantly human-created object. Facilities encompass items within the scope of"
                " \narchitecture and civil engineering, as well as transitory human creations, like police barriers"
                " and inspection stations."
            ),
        ]
    },
    "wikievents_ner_gpe": {
        "en": [
            (
                "Geopolitical entities such as countries, provinces, states, cities, towns, etc. GPEs are composite"
                " entities, \nconsisting of a physical location, a government, and a population. All three of these"
                " elements must be present for an entity to be \ntagged as a GPE. A GPE entity may be a single"
                " geopolitical entity or a group."
            ),
            (
                "Geopolitical entities, including nations, regions, cities, and towns, are complex entities that"
                " combine a \nspecific location, a governing body, and a population. For an entity to be categorized"
                " as a geopolitical entity, all three of \nthese components must be present. A geopolitical entity can"
                " be either a single, individual entity or a group."
            ),
            (
                "Geopolitical entities, including nations, provinces, states, cities, and towns, are composite"
                " structures \ncomprising a physical location, a governing body, and an inhabited population. For an"
                " entity to be classified as a geopolitical \nentity, all three of these components must be present. A"
                " geopolitical entity can exist as a single distinct entity or a group \nof related entities."
            ),
            (
                "Geopolitical entities, like nations, regions, states, cities, and towns, are composite structures,"
                " comprising a \nspecific location, a governing body, and an inhabiting population. In order to be"
                " categorized as a geopolitical entity, all \nthree of these components must be present. A"
                " geopolitical entity can exist as a single unit or as a group."
            ),
            (
                "Geopolitical entities, including nations, provinces, states, cities, and towns, are multifaceted"
                " entities that \ncomprise a physical location, a governing body, and an inhabiting population. For an"
                " entity to be classified as a \ngeopolitical entity, all three of these components must be present. A"
                " geopolitical entity can exist as a single unit or as a group."
            ),
        ]
    },
    "wikievents_ner_information": {
        "en": [
            (
                "An information object such as a field of study or topic of communication, including thoughts,"
                " opinions, etc."
            ),
            (
                "A subject matter, be it an academic discipline or a subject of discussion, encompassing ideas,"
                " perspectives, and so \non."
            ),
            (
                "A subject matter, encompassing academic disciplines or discussion content, encompassing thoughts and"
                " opinions \nas well."
            ),
            (
                "A subject matter, be it an academic discipline or a theme in communication, encompassing ideas,"
                " beliefs, and \nperspectives."
            ),
            (
                "A subject matter, be it an area of academic focus or a subject of communication encompassing thoughts"
                " and opinions."
            ),
        ]
    },
    "wikievents_ner_location": {
        "en": [
            "Geographical entities such as geographical areas and landmasses, bodies of water.",
            "Geographical features, including regions, landmasses, and bodies of water.",
            "Geographical features, including regions and landmasses, as well as water bodies.",
            "Geographical features, including regions, landmasses, and bodies of water.",
            "Geographical features, including regions, landmasses, and bodies of water.",
        ]
    },
    "wikievents_ner_medicalhealthissue": {
        "en": [
            (
                "Any medical condition or health issue, to include everything from disease to broken bones to fever to"
                " general ill \nhealth, medical errors, even natural causes"
            ),
            (
                "Any and all medical circumstances, encompassing everything from illnesses to fractures, fevers, and"
                " general \nunwellness, along with medical blunders, and even natural causes"
            ),
            (
                "Any and all medical circumstances or health problems, encompassing everything from illnesses to"
                " fractures, \nfevers, and general unwellness, medical blunders, even natural causes"
            ),
            (
                "Any and all medical situations or health problems, encompassing everything from illnesses to broken"
                " bones, \nfevers, and general unwellness, as well as medical blunders, and even natural causes"
            ),
            (
                "Any and all medical circumstances, encompassing everything from illnesses to fractures, fever, and"
                " overall poor \nhealth, as well as medical blunders, and even natural causes"
            ),
        ]
    },
    "wikievents_ner_money": {
        "en": [
            (
                "A monetary payment. The extent of a Money mention includes modifying quantifiers, the amount, and the"
                " currency \nunit, all of which can be optional."
            ),
            (
                "A financial compensation. The scope of a Money reference encompasses adjustable quantifiers, the"
                " payment amount, \nand the currency type, all of which can be discretionary."
            ),
            (
                "A financial compensation. The scope of a Money specification encompasses the adjustment of"
                " quantifiers, the \npayment amount, and the currency type, all of which can be optional elements."
            ),
            (
                "A financial compensation. The scope of a Money reference encompasses modifying determiners, the sum,"
                " and the \ncurrency denomination, all of which can be discretionary."
            ),
            (
                "A financial compensation. The scope of a Money reference encompasses modifying qualifiers, the sum,"
                " and the \ncurrency denomination, all of which can be optional."
            ),
        ]
    },
    "wikievents_ner_organization": {
        "en": [
            (
                "Corporations, agencies, and other groups of people defined by an established organizational"
                " structure. An ORG \nentity may be a single organization or a group. A key feature of an ORG is that"
                " it can change members without changing \nidentity."
            ),
            (
                "Organizations, such as corporations and government agencies, are classified as ORG entities, which"
                " can encompass \na wide range of groups characterized by a specific organizational framework. A"
                " notable attribute of an ORG entity is \nits ability to modify its membership without compromising"
                " its core identity."
            ),
            (
                "Organizations, bureaus, and other collectives characterized by a defined hierarchical arrangement. An"
                " ORG \nentity can encompass a single organization or a group. A crucial aspect of an ORG is its"
                " ability to modify its members without \naltering its core identity."
            ),
            (
                "Organizations, such as corporations and government agencies, are classified as ORG entities. These"
                " entities may \nconsist of a single organization or a group of people, and a defining characteristic"
                " is their ability to modify their \nmembership without compromising their core identity."
            ),
            (
                "Organizations, such as businesses and government agencies, are composed of individuals united under a"
                " specific \nstructure. An ORG entity can represent a single organization or a group of people. A"
                " defining characteristic of an ORG is its \nability to modify its membership without compromising its"
                " core identity."
            ),
        ]
    },
    "wikievents_ner_person": {
        "en": [
            "Person entities are limited to humans. A Person entity may be a single person or a group.",
            (
                'Paraphrase: "Person entities are exclusively reserved for humans. A Person entity can either'
                " represent an \nindividual or a group."
            ),
            (
                "Individual entities are exclusively reserved for humans. A Person entity can represent a single"
                " person or a group of \npeople."
            ),
            (
                "Paraphrase: Person entities are exclusively reserved for human individuals; a Person entity can"
                " either represent \na single person or a group of people."
            ),
            (
                'Paraphrase: "Person entities exclusively encompass human individuals; a Person entity can either'
                " represent a \nsingle person or a group."
            ),
        ]
    },
    "wikievents_ner_side_of_conflict": {
        "en": [
            (
                "The different sides of a conflict, such as philosophical, cultural, ideological, religious,"
                " political, guiding \nphilosophical movement or group orientation. This will encompass sides of the"
                " battle/conflict, sports fans when salient, and \nother such affiliations, in addition to religions,"
                " political parties, and other philosophies."
            ),
            (
                "Various aspects of a disagreement, including philosophical, cultural, ideological, religious,"
                " political, and \nguiding principles of movements or groups, are covered under this definition. It"
                " also encompasses opposing sides in a \nbattle or conflict, enthusiastic supporters of sports teams"
                " when their affiliation is significant, and any other similar \nallegiances, in addition to various"
                " faiths, political parties, and other belief systems."
            ),
            (
                "Various aspects of a disagreement, including philosophical, cultural, ideological, religious,"
                " political, and \nfactional perspectives, are covered under this definition. It encompasses opposing"
                " sides in battles or conflicts, as well as \nloyalty-driven associations like sports fanaticism when"
                " relevant, and other similar allegiances. Moreover, this encompasses \nvarious belief systems like"
                " religions, political parties, and other doctrines."
            ),
            (
                "Various aspects of a disagreement, including philosophical, cultural, ideological, religious,"
                " political, and \nprominent guiding principles or group inclinations, cover the opposing sides of a"
                " conflict, sports fanaticism when \nsignificant, and additional affiliations, as well as religious"
                " beliefs, political parties, and other philosophies."
            ),
            (
                "Various aspects of a disagreement, including philosophical, cultural, ideological, religious,"
                " political, and \nguiding belief systems or group inclinations, are covered under this definition. It"
                " encompasses opposing sides in a \nconflict, sports fan allegiances when significant, and other"
                " relevant affiliations, as well as different religious sects, \npolitical parties, and other"
                " doctrines."
            ),
        ]
    },
    "wikievents_ner_job_title": {
        "en": [
            "A person's title or job role.",
            "The specific position or occupation held by an individual.",
            "The position or occupation of an individual.",
            "A person's position or occupation.",
            "The specific position or occupation held by an individual.",
        ]
    },
    "wikievents_ner_numeric": {
        "en": [
            "A numerical value or non-numerical value such as an informational property such as color or make or URL.",
            (
                "A quantitative or non-quantitative attribute, including characteristics like color, type, or website"
                " address."
            ),
            "A quantitative or non-quantitative value, including properties like color, make, or web address.",
            "A quantitative or non-quantitative value, including properties like color, make, or website address.",
            (
                "A quantitative or non-quantitative value, including characteristics like color, make, or website"
                " address."
            ),
        ]
    },
    "wikievents_ner_vehicle": {
        "en": [
            (
                "A physical device primarily designed to move an object from one location to another, by (for example)"
                " carrying, \nflying, pulling, or pushing the transported object. Vehicle entities may or may not have"
                " their own power source."
            ),
            (
                "A tangible apparatus primarily intended to relocate an object from one place to another, such as by"
                " carrying, \nflying, pulling, or pushing the transported item. Vehicle entities may or may not"
                " possess their own energy source."
            ),
            (
                "A tangible apparatus principally intended to transfer an object from one place to another, such as by"
                " carrying, \nflying, pulling, or pushing the conveyed item. Vehicle entities can either possess or"
                " lack their own power source."
            ),
            (
                "A tangible apparatus principally intended to relocate an object from one place to another, such as by"
                " carrying, \nflying, pulling, or pushing the transported item. Vehicle entities may or may not"
                " possess their own power source."
            ),
            (
                "A tangible apparatus primarily intended to relocate an object from one place to another, such as by"
                " carrying, \nflying, pulling, or pushing the transported item. Vehicle entities can either possess or"
                " lack their own power source."
            ),
        ]
    },
    "wikievents_ner_weapon": {
        "en": [
            "A physical device that is primarily used as an instrument for physically harming or destroying entities.",
            (
                "A tangible apparatus primarily designed for the purpose of inflicting bodily harm or destruction on"
                " entities."
            ),
            (
                "A tangible object primarily designed for the purpose of inflicting physical injury or destruction"
                " upon beings."
            ),
            "A tangible appliance predominantly designed to inflict bodily injury or annihilation upon beings.",
            "A tangible object primarily designed to inflict or cause destruction upon living beings or objects.",
        ]
    },
    "wikievents_ee_artifact_existance": {
        "en": [
            (
                "Any event related to manufacturing, assembling, damagging, destroying, disabling, defusing, or"
                " dismantling an \nartifact or a thing."
            ),
            (
                "Any occurrence associated with the production, assembly, damage, destruction, disabling, disarming,"
                " or taking \napart of an artifact or an object."
            ),
            (
                "Any occurrence associated with the production, assembly, damage, destruction, disabling,"
                " deactivation, or \ndisassembly of an item or object."
            ),
            (
                "Any occurrence associated with the production, assembly, damage, destruction, disabling,"
                " deactivation, or \ndisassembly of an object or item."
            ),
            (
                "Any occurrence associated with the production, assembly, damage, destruction, disabling,"
                " deactivation, or \ndisassembly of an object or item."
            ),
        ]
    },
    "wikievents_ee_cognitive": {
        "en": [
            (
                "The act of establishing the identity of an entity or event, or establishing the relevant category"
                " that an entity or \nevent belongs to, such as being a suspect or a target or an attack. An"
                " observation or inspection event, with any target of \ninspection. Explicit mention of researching"
                " the answer to a question by analyzing literature or testing hypotheses through \nexperiments or"
                " reviewing opinions from experts in a field. The action of teaching a person or animal a particular"
                " skill or type of \nbehavior, where the learner does not have complete mastery of the skill until the"
                " end."
            ),
            (
                "The process of determining the origin or cause of an occurrence, categorizing it, and identifying its"
                " nature, such \nas distinguishing between a suspect, a target, or an attack. A systematic examination"
                " or assessment that involves \nstudying or evaluating any subject or object. The practice of"
                " investigating the solution to a question by studying various \nsources, conducting experiments, or"
                " seeking advice from experts in a given field, ultimately leading to the acquisition of a \nskill or"
                " behavior by a person or animal, even if mastery is not fully achieved."
            ),
            (
                "The process of determining the origin or nature of a person, occurrence, or object, as well as the"
                " classification it \nfalls under, such as being a person of interest, a goal, or the focus of an"
                " attack. A situation involving the examination or \nassessment of any subject or object. The act of"
                " investigating to reach a conclusion by examining various sources, such as \nliterature, experiments,"
                " or expert opinions within a specific domain. The practice of instructing an individual or animal in"
                " a \nparticular ability or behavior, where mastery is not fully achieved until the training is"
                " complete."
            ),
            (
                "The process of determining the origin or nature of a person, object, or event, and the classification"
                " of said entity \ninto a specific category, such as a suspect, target, or attack. A systematic"
                " examination or assessment that may involve \nany subject under scrutiny. The practice of"
                " investigating responses to inquiries by examining literary sources, \nconducting experimental"
                " investigations, or consulting expert perspectives within a given domain. The act of imparting"
                " \nknowledge or skill to an individual, whether human or animal, with the understanding that full"
                " mastery may not be achieved \nuntil the learning process is complete."
            ),
            (
                "The process of determining the origin or cause of a circumstance, categorizing it into appropriate"
                " groups such as \nsuspect, target, or assailant, and engaging in investigative actions or"
                " examinations with any relevant subject. \nAdditionally, the practice of investigating answers to"
                " inquiries by examining written works, testing hypotheses through \nexperimentation, or consulting"
                " expert opinions within a given field. Furthermore, the act of imparting knowledge or skills to an"
                " \nindividual or animal, where the learner's mastery of the skill is not yet complete by the end of"
                " the process."
            ),
        ]
    },
    "wikievents_ee_conflict": {
        "en": [
            (
                "An attack event, a violent physical act causing harm or damage. Defeat in a conflict or an election,"
                " but not a \ngame-style competition. A demonstration, march, protest, or political gathering."
            ),
            (
                "An assault occasion, a forceful physical act leading to injury or destruction. A loss in a contest or"
                " an election, \nthough not in a recreational competition. A display, march, protest, or political"
                " assembly."
            ),
            (
                "An act of aggression, a forceful physical action resulting in injury or destruction. A loss in a"
                " struggle or an \nelection, though not in a recreational contest. A public display, procession,"
                " protest, or political assembly."
            ),
            (
                "An assault occasion, a forceful physical act leading to injury or destruction. A loss in a"
                " disagreement or a voting \nprocess, though not in a recreational contest. A display, march, protest,"
                " or political assembly."
            ),
            (
                "An act of aggression, a forceful physical act that inflicts harm or damage. A loss in a struggle or"
                " an election, but not \nin a recreational contest. A public display of opposition, a march, a"
                " protest, or a political assembly."
            ),
        ]
    },
    "wikievents_ee_contact": {
        "en": [
            (
                "An event where two or more participants communicate over any medium, where the context does not"
                " distinguish the \nnature of the contact or whether the communication is in person or remote. Any"
                " communication over any medium where the \ncommunicator intentionally deceives the addressee or"
                " continue an ongoing deception, either by knowingly conveying false \ninformation, or conveying"
                " information with the intent of the addressee drawing the wrong conclusion, or omitting information."
                " A \nstatement making a request, appeal, command, or order, where the context does not distinguish"
                " whether the communication is \none-way or two-way, or whether it is in person or remote. A statement"
                " offering threat or coercion, where the context does not \ndistinguish whether the communication is"
                " one-way or two-way, or whether it is in person or remote."
            ),
            (
                "An occasion during which two or more individuals engage in communication through any means, without"
                " regard to \nwhether the interaction is face-to-face or remote, or whether the context distinguishes"
                " the type of contact. Any \ninteraction involving deceptive communication, intentionally misleading"
                " the recipient, either by knowingly providing \nfalse information, leading the recipient to the wrong"
                " conclusion, or withholding information. A statement that \nexpresses a request, appeal, command, or"
                " order, where the context does not differentiate between one-way or two-way \ncommunication, or"
                " whether the interaction is in person or remote. A statement that delivers a threat or coercion,"
                " without \ndifferentiating between one-way or two-way communication, or whether the interaction is in"
                " person or remote."
            ),
            (
                "An interaction involving two or more individuals utilizing any means of communication, where the"
                " circumstances do \nnot differentiate between face-to-face or remote communication or the type of"
                " medium used. Any communication process \nin which the sender intentionally misleads the recipient,"
                " either by deliberately providing false information, \nconveying information with the intention of"
                " leading the recipient astray, or withholding relevant information. A statement \nthat expresses a"
                " request, appeal, command, or order, where the context does not distinguish between one-way or"
                " two-way \ncommunication, or whether it occurs in person or at a distance. A statement that delivers"
                " a threat or coercion, where the context does \nnot differentiate between one-way or two-way"
                " communication, or whether it takes place in person or remotely."
            ),
            (
                "An interaction in which multiple participants engage in communication through any means, without"
                " regard to \nwhether the contact is in-person or remote. Any exchange of information through any"
                " medium that involves the intentional \ndeception of the recipient, either by knowingly providing"
                " false information, leading the recipient to the wrong conclusion, \nor withholding information. A"
                " statement that expresses a request, appeal, command, or order, without \ndifferentiating between"
                " one-way or two-way communication, or whether it occurs in-person or remotely. A statement that"
                " issues a \nthreat or employs coercion, without distinguishing between one-way or two-way"
                " communication, or whether it takes place \nin-person or remotely."
            ),
            (
                "An interaction in which two or more individuals engage in communication through any means, where the"
                " context fails \nto differentiate between face-to-face and remote communication or the nature of the"
                " contact. Any communication \nprocess, utilizing any medium, in which the communicator intentionally"
                " deceives the recipient, either by purposefully \nproviding false information, leading the recipient"
                " to the wrong conclusion, or withholding relevant information. A \nstatement that makes a request,"
                " appeal, command, or order, where the context does not specify whether the communication is"
                " \nunidirectional or bidirectional, or whether it occurs in person or at a distance. A statement that"
                " issues a threat or coercion, where \nthe context does not determine whether the communication is"
                " unidirectional or bidirectional, or whether it takes \nplace in person or remotely."
            ),
        ]
    },
    "wikievents_ee_control": {
        "en": [
            (
                "Explicit mention of an entity knowingly placing obstacles, not necessarily physical, that raise"
                " difficulties \nwith respect to the occurrence of a taggable, non-Movement event or process"
            ),
            (
                "Clear reference to a conscious effort by a party to intentionally introduce challenges that hinder"
                " the occurrence \nof a detectable, non-movement-related event or process"
            ),
            (
                "Clear reference to a conscious effort by a party to intentionally introduce challenges, which may not"
                " be strictly \nphysical in nature, that hinder the occurrence of a detectable, non-movement-related"
                " event or process."
            ),
            (
                "Clear reference to a specific entity intentionally creating challenges, which may not be purely"
                " physical in \nnature, that hinder the occurrence of a distinguishable, non-movement-related event or"
                " process."
            ),
            (
                "Clear reference to a specific entity intentionally creating impediments, which may not be purely"
                " physical in \nnature, that make it more challenging to facilitate a detectable, non-movement-related"
                " occurrence or process."
            ),
        ]
    },
    "wikievents_ee_disaster": {
        "en": [
            (
                "Vehicular collision or the crashing of any type of vehicle. Explicit mentions of an outbreak of a"
                " disease in an area, \nregion, or country. A damaging fire or explosion, either natural or caused but"
                " without the intent of attacking"
            ),
            (
                "Automobile collisions or the crashing of any kind of vehicle. Clear references to an epidemic of a"
                " disease breaking \nout in a specific location, region, or nation. A harmful fire or explosion,"
                " either occurring naturally or caused \nunintentionally, without any intent of attacking"
            ),
            (
                "Automotive collision, which involves the crashing of any kind of vehicle. Clear references to an"
                " epidemic of a \ndisease breaking out in a specific location, such as a region or country. A"
                " destructive fire or explosion, either resulting \nfrom natural causes or caused by accident without"
                " any intention of attacking"
            ),
            (
                "Automobile collision, which refers to the impact or crash of any kind of vehicle. Clear indications"
                " of an epidemic \nbreakout of an illness within a specific location, region, or nation. A harmful"
                " fire or blast, either resulting from natural \ncauses or human error, but not intended as an act of"
                " aggression."
            ),
            (
                "Car accidents or the crashing of any kind of vehicle. Clear references to an epidemic breaking out in"
                " a specific \nlocation, region, or nation. Destructive fires or explosions, either naturally"
                " occurring or caused unintentionally, \nwithout the intention of launching an attack"
            ),
        ]
    },
    "wikievents_ee_generic_crime": {
        "en": [
            (
                "For use as the crime argument in a Justice event when the crime event is not taggable as any other"
                " annotation ontology \nevent type."
            ),
            (
                "This statement serves as the foundation for the crime aspect in a Justice-centered event, when the"
                " crime event \nitself cannot be categorized under any other classification within the annotation"
                " ontology."
            ),
            (
                "This statement serves as the basis for the crime argument in a Justice event when the crime event"
                " cannot be \ncategorized under any other annotation ontology event type."
            ),
            (
                "This statement serves as the premise for a Justice event when the crime event cannot be categorized"
                " under any other \nannotation ontology event type."
            ),
            (
                "This statement serves as the basis for the crime argument in a Justice event when the crime event"
                " cannot be \ncategorized under any other type of annotation within an ontology."
            ),
        ]
    },
    "wikievents_ee_justice": {
        "en": [
            (
                "Any legal proceedings, such as a court case, a trial, or a hearing. Arresting, detaining, punishing,"
                " or otherwise \ndealing with a criminal or non-criminal person or entity."
            ),
            (
                "Any legal actions, including court cases, trials, or hearings, that involve apprehending,"
                " imprisoning, \npenalizing, or otherwise handling a criminal or non-criminal individual or"
                " organization."
            ),
            (
                "Any legal actions, including court cases, trials, or hearings, that involve apprehending, confining,"
                " \npenalizing, or otherwise managing a criminal or non-criminal individual or organization."
            ),
            (
                "Any legal actions, including court cases, trials, or hearings, that involve apprehending, confining,"
                " \npenalizing, or otherwise handling a criminal or non-criminal individual or entity."
            ),
            (
                "Any legal actions, including court cases, trials, and hearings, that involve apprehending,"
                " imprisoning, \npenalizing, or otherwise handling a criminal or non-criminal individual or entity."
            ),
        ]
    },
    "wikievents_ee_life": {
        "en": [
            (
                "An person or animal takes a substance into their body. The death of a person or animal. A person or"
                " animal experiencing \nphysical harm due to sickness or illness. A person or animal is infected with"
                " a pathogen. The physical injuring of a person or \nanimal."
            ),
            (
                "A person or animal ingests a substance, resulting in the demise of a person or animal, or physical"
                " harm caused by \nillness or disease. Additionally, a person or animal may be infected with a"
                " pathogen, ultimately leading to physical \ninjury."
            ),
            (
                "A person or animal ingests a substance, which can result in the death of an individual or animal, or"
                " cause them to \nexperience physical harm due to illness or sickness. Additionally, a person or"
                " animal may become infected with a pathogen, \nleading to physical injury."
            ),
            (
                "When an individual, whether human or animal, introduces a substance into their system, it can lead to"
                " unintended \nconsequences such as death, physical harm caused by illness or injury, or even pathogen"
                " infection, which can result in injury to \nthe person or animal."
            ),
            (
                "A person or animal ingests a substance, resulting in the demise of an individual or animal. A person"
                " or animal suffers \nfrom bodily harm due to illness or disease. A person or animal becomes afflicted"
                " with a pathogen. The act of physically \ninjuring a person or animal."
            ),
        ]
    },
    "wikievents_ee_medical": {
        "en": [
            (
                "A determination of the disease or medical condition that explains a person's or animal's symptoms and"
                " signs. Any \nkind of medical treatment or intervention for a person or an animal, often following a"
                " diagnosis of a medical condition. A \nperson or an animal is inoculated against a disease."
            ),
            (
                "A conclusive assessment of the illness or health issue that accounts for an individual's or animal's"
                " symptoms and \nindications. The administration of any therapeutic intervention or treatment method"
                " to a person or an animal, frequently \nsubsequent to a diagnosis of a medical condition. An"
                " individual or an animal is protected against an illness through \ninoculation."
            ),
            (
                "An assessment that identifies the illness or health issue responsible for an individual's or animal's"
                " symptoms and \nindications, often leading to a medical treatment or intervention. The process of"
                " protecting a person or animal from a specific \ndisease through immunization."
            ),
            (
                "An assessment that identifies the illness or health issue responsible for an individual's or animal's"
                " symptoms and \nindications, often leading to a corresponding medical treatment or intervention. The"
                " process of protecting a person or animal \nagainst a specific disease through the administration of"
                " a vaccine or other preventative measure."
            ),
            (
                "A conclusion regarding the illness or health issue that accounts for an individual's or animal's"
                " indications and \nmanifestations. The administration of any form of medical therapy or intervention"
                " to a person or animal, frequently subsequent to a \ndiagnosis of a medical condition. An individual"
                " or animal is protected against an illness through immunization."
            ),
        ]
    },
    "wikievents_ee_movement_transport": {
        "en": [
            (
                "Physical movement or transportation of a person or artifact between places, includes putting and"
                " placing objects \nin locations."
            ),
            (
                'Text: "The relocation of individuals or objects from one location to another, which involves'
                " positioning and \ndepositing items in various places."
            ),
            (
                "The process of relocating individuals or items from one location to another, which encompasses the"
                " act of \npositioning and depositing objects in various places."
            ),
            (
                "The action of relocating an individual or object from one location to another, which also involves"
                " positioning and \ndepositing items in various places."
            ),
            (
                "The action of relocating an individual or object from one location to another, which also involves"
                " positioning and \ndepositing items in specific places."
            ),
        ]
    },
    "wikievents_ee_personnel": {
        "en": [
            (
                "A person changing from one position to another in the same organization, with no indication of"
                " relative levels of the \npositions. A person starting or stoping working in a position."
            ),
            (
                "An individual shifting from one role to another within the same organization, without specifying the"
                " hierarchical \nrank of the positions. A person beginning or ceasing to work in a particular"
                " position."
            ),
            (
                "An individual transitioning between roles within the same organization, without specifying the"
                " hierarchical \nrelationship between the positions. Additionally, a person beginning or ending their"
                " tenure in a particular position."
            ),
            (
                "A person shifting from one role to another within the same organization, without specifying the"
                " hierarchical rank \nof the positions. A person who begins or ends their tenure in a particular"
                " position."
            ),
            (
                "An individual shifting from one role to another within the same organization, without specifying the"
                " positions' \nhierarchical relationship. A person beginning or ending their tenure in a particular"
                " position."
            ),
        ]
    },
    "wikievents_ee_transaction": {
        "en": [
            "A transaction involving the transfer of money, goods, or services between two or more parties.",
            "A transaction entailing the movement of funds, items, or services between two or more parties.",
            (
                "A transaction entails the exchange of funds, items, or services between two or more individuals or"
                " entities."
            ),
            "A transaction entails the exchange of funds, items, or services between a minimum of two parties.",
            (
                "A transaction is a process that involves the exchange of money, goods, or services between two or"
                " more individuals or \nentities."
            ),
        ]
    },
    "wikievents_eae_damage_destroy": {
        "en": [
            "The damaging or destruction of a thing.",
            "The act of causing harm or ruin to an object.",
            "The act of causing harm or ruin to an object.",
            "The act of causing harm or ruin to an object.",
            "The act of causing harm or ruin to an object.",
        ]
    },
    "wikievents_eae_disable_defuse": {
        "en": [
            (
                "Disabling the expected functioning of a mechanical device, or software, for example defusing or"
                " removing a fuse \nfrom an explosive."
            ),
            (
                "Temporarily neutralizing the intended operation of a mechanical apparatus or software, such as"
                " deactivating or \nremoving the fuse from an explosive."
            ),
            (
                "Temporarily impairing the typical operation of a mechanical appliance or computer program, such as"
                " deactivating \nor removing the fuse from an explosive."
            ),
            (
                "Impairing the typical operation of a mechanical apparatus or software, such as disarming or"
                " extracting a fuse from \nan explosive."
            ),
            (
                "Temporarily impairing the normal operation of a mechanical apparatus or software, such as disarming"
                " or extracting \na fuse from an explosive device."
            ),
        ]
    },
    "wikievents_eae_dismantle": {
        "en": [
            "Disassembling an artifact in such a way that it could be reassembled.",
            "Dismantling a complex item so that it can be put back together again.",
            "Dismantling a complex item so that it can be put back together again.",
            "Dismantling a complex item so that it can be put back together again.",
            "Dismantling a complex item so that it can be put back together again.",
        ]
    },
    "wikievents_eae_manufacture_assemble": {
        "en": [
            (
                "Physical action of building, assembling, manufacturing, putting things together, mixing, etc. (does"
                " not include \nthe creation of intellectual property)."
            ),
            (
                'Text: "The process of constructing, assembling, producing, joining components, blending, and so on'
                " (excludes the \ndevelopment of intellectual property)."
            ),
            (
                'Text: "The process of constructing, assembling, producing, joining components, blending, and so on,'
                " excluding \nthe generation of intellectual property."
            ),
            (
                'Text: "The process of constructing, assembling, producing, joining components, blending materials,'
                " and so on, \nexcluding the generation of intellectual property."
            ),
            (
                'Text: "The process of constructing, assembling, producing, joining components, blending materials,'
                " and so on, \nexcluding the generation of intellectual property."
            ),
        ]
    },
    "wikievents_eae_identify_categorize": {
        "en": [
            (
                "The act of establishing the identity of an entity or event, or establishing the relevant category"
                " that an entity or \nevent belongs to, such as being a suspect or a target or an attack."
            ),
            (
                "The process of determining the distinct characteristics or classification of a person or occurrence,"
                " including \ndifferentiating between roles such as a suspect, a target, or the object of an attack."
            ),
            (
                "The process of determining the distinct characteristics or classification of a person or occurrence,"
                " including \nwhether they are considered a suspect, a target, or the focus of an attack."
            ),
            (
                "The process of determining the distinct characteristics or classification of a person, occurrence, or"
                " object, \nincluding whether it is considered a suspect, a target, or the subject of an attack."
            ),
            (
                "The process of determining the distinct characteristics or classification of a person or occurrence,"
                " which may \ninvolve categorizing them as a possible perpetrator, objective, or aggressor."
            ),
        ]
    },
    "wikievents_eae_inspection": {
        "en": [
            "An observation or inspection event, with any target of inspection.",
            "A monitoring or examination instance, encompassing any subject matter being scrutinized.",
            "An instance of monitoring or examination, encompassing any subject matter being scrutinized.",
            "An instance of monitoring or examination, which can encompass any subject being scrutinized.",
            "An observation or examination occasion, encompassing any objective to be inspected.",
        ]
    },
    "wikievents_eae_research": {
        "en": [
            (
                "Explicit mention of researching the answer to a question by analyzing literature or testing"
                " hypotheses through \nexperiments or reviewing opinions from experts in a field."
            ),
            (
                "Clearly stating that the answer to a question can be found by examining written works, testing ideas"
                " through \nexperiments, or consulting expert perspectives in a specific domain."
            ),
            (
                "One such approach involves conducting an in-depth exploration of a subject by examining various"
                " sources of \ninformation, such as literature, conducting experiments to test hypotheses, and seeking"
                " the insights of experts in the field."
            ),
            (
                "Specific reference to the process of investigating the response to an inquiry by examining relevant"
                " literature, \ntesting proposed explanations through experiments, or consulting the perspectives of"
                " experienced professionals in a \ngiven domain."
            ),
            (
                "Clearly stating the process of discovering a response to an inquiry by examining relevant writings,"
                " testing \nproposed assumptions through experiments, or considering perspectives from knowledgeable"
                " individuals in a given domain."
            ),
        ]
    },
    "wikievents_eae_teaching_training_learning": {
        "en": [
            (
                "The action of teaching a person or animal a particular skill or type of behavior, where the learner"
                " does not have \ncomplete mastery of the skill until the end"
            ),
            (
                "The process of instructing an individual or animal in the development of a specific skill or"
                " behavior, during which \nthe learner progresses toward full proficiency throughout the learning"
                " experience"
            ),
            (
                "The process of instructing an individual or animal in the development of a specific skill or"
                " behavior, during which \nthe learner progresses toward full proficiency throughout the learning"
                " experience"
            ),
            (
                "The process of instructing an individual or animal in the development of a specific skill or"
                " behavior, during which \nthe learner progresses toward full proficiency throughout the learning"
                " experience"
            ),
            (
                "The process of instructing an individual or animal in the development of a specific skill or"
                " behavior, in which the \nlearner does not achieve total proficiency until the conclusion"
            ),
        ]
    },
    "wikievents_eae_attack": {
        "en": [
            "An attack event, a violent physical act causing harm or damage.",
            "An assault occasion, a forceful bodily action resulting in injury or destruction.",
            "An assault occasion, a forceful physical deed leading to injury or destruction.",
            "An assault occasion, a forceful physical action resulting in injury or destruction.",
            "An act of aggression, a forceful physical action resulting in injury or destruction.",
        ]
    },
    "wikievents_eae_defeat": {
        "en": [
            "Defeat in a conflict or an election, but not a game-style competition",
            "Loss in a confrontation or an election, but not in a game-like contest",
            "Losses in battles or elections, but not in game-like contests",
            "Loss in a clash or an election, but not in a game-like contest",
            "Loss in a confrontation or an election, but not in a game-like contest",
        ]
    },
    "wikievents_eae_demonstrate": {
        "en": [
            "A demonstration, march, protest, or political gathering.",
            "A display, procession, protest, or political assembly.",
            "A display, procession, protest, or political assembly.",
            "A display, procession, protest, or political assembly.",
            "A display, procession, protest, or assemblage of a political nature.",
        ]
    },
    "wikievents_eae_contact": {
        "en": [
            (
                "An event where two or more participants communicate over any medium, where the context does not"
                " distinguish the \nnature of the contact or whether the communication is in person or remote."
            ),
            (
                "An occasion in which multiple individuals engage in communication through any means, where the"
                " circumstances do \nnot differentiate between the type of contact or whether the interaction occurs"
                " in person or at a distance."
            ),
            (
                "An interaction in which multiple individuals engage, using any mode of communication, where the"
                " circumstances do \nnot specifically identify the type of contact or whether it is conducted in"
                " person or at a distance."
            ),
            (
                "An occurrence during which multiple individuals engage in communication through any means, in which"
                " the \ncircumstances do not differentiate between the type of contact or whether the interaction is"
                " face-to-face or remote."
            ),
            (
                "An interaction in which multiple individuals engage using any means of communication, where the"
                " circumstance does \nnot differentiate between the type of contact or whether it occurs in person or"
                " at a distance."
            ),
        ]
    },
    "wikievents_eae_prevarication": {
        "en": [
            (
                "Any communication over any medium where the communicator intentionally deceives the addressee or"
                " continue an \nongoing deception, either by knowingly conveying false information, or conveying"
                " information with the intent of the \naddressee drawing the wrong conclusion, or omitting"
                " information."
            ),
            (
                "Any form of communication, across any platform, in which the sender purposefully misleads the"
                " recipient, either by \ndeliberately providing false information, by conveying information with the"
                " aim of leading the recipient to an incorrect \nconclusion, or by withholding essential information."
            ),
            (
                "Any form of communication, across any platform, in which the sender purposefully misleads the"
                " recipient, either by \ndeliberately providing false information, by transmitting data with the"
                " objective of leading the recipient to an incorrect \nconclusion, or by withholding crucial"
                " information."
            ),
            (
                "Any form of communication, across any platform, in which the sender purposefully misleads the"
                " recipient, either by \ndeliberately providing false information, by convey"
            ),
            (
                "Any form of communication that involves a sender deliberately misleading the recipient, whether by"
                " purposefully \nproviding false information, leading the recipient to an incorrect conclusion, or"
                " withholding essential information."
            ),
        ]
    },
    "wikievents_eae_request_command": {
        "en": [
            (
                "A statement making a request, appeal, command, or order, where the context does not distinguish"
                " whether the \ncommunication is one-way or two-way, or whether it is in person or remote."
            ),
            (
                "A text that conveys a message seeking an action, entreaty, direction, or requirement, without"
                " differentiating \nbetween the type of communication exchange, whether it occurs in person or at a"
                " distance."
            ),
            (
                "A communication that conveys a request, plea, directive, or instruction, which does not specify"
                " whether the \ninteraction is unidirectional or bidirectional, or whether it occurs in person or at a"
                " distance."
            ),
            (
                "A communication that conveys a request, plea, directive, or instruction, which does not specify"
                " whether the \ninteraction is unidirectional or bidirectional, or whether it occurs in person or at a"
                " distance."
            ),
            (
                "A communication that conveys a request, appeal, directive, or instruction, which does not specify"
                " whether the \ncontext is one-way or two-way, or whether it occurs in person or at a distance."
            ),
        ]
    },
    "wikievents_eae_threaten_coerce": {
        "en": [
            (
                "A statement offering threat or coercion, where the context does not distinguish whether the"
                " communication is \none-way or two-way, or whether it is in person or remote."
            ),
            (
                "A declaration that implies either intimidation or compulsion, which fails to differentiate between"
                " whether the \ncommunication is unidirectional or bidirectional, or whether it occurs in-person or at"
                " a distance."
            ),
            (
                "A declaration that implies danger or compulsion, which does not clarify whether the communication is"
                " \nunidirectional or bidirectional, or if it occurs in person or at a distance."
            ),
            (
                "A declaration that implies either coercion or intimidation, which fails to differentiate between"
                " whether the \ncommunication is unidirectional or bidirectional, or whether it occurs in-person or"
                " via remote means."
            ),
            (
                "A declaration that implicitly or explicitly implies intimidation or compulsion, which fails to"
                " differentiate \nbetween unidirectional or bidirectional communication, or whether the interaction"
                " occurs in person or at a distance."
            ),
        ]
    },
    "wikievents_eae_impede_interfere_with": {
        "en": [
            (
                "Explicit mention of an entity knowingly placing obstacles, not necessarily physical, that raise"
                " difficulties \nwith respect to the occurrence of a taggable, non-Movement event or process."
            ),
            (
                "Specific reference to a conscious effort by a party to deliberately introduce challenges that impede"
                " the \nsuccessful execution of a distinguishable, non-movement-related event or process."
            ),
            (
                "Clear reference to a conscious act by a party intentionally creating challenges that hinder the"
                " occurrence of a \ndistinguishable, non-movement incident or procedure."
            ),
            (
                "Clear reference to a conscious entity intentionally creating challenges, which may not be purely"
                " physical in \nnature, that complicate the occurrence of a detectable, non-movement-related event or"
                " process."
            ),
            (
                "Clear reference to a specific entity intentionally creating challenges, which may not be solely"
                " physical in \nnature, that hinder the occurrence of a distinguishable, non-movement-related event or"
                " process."
            ),
        ]
    },
    "wikievents_eae_crash": {
        "en": [
            "Vehicular collision or the crashing of any type of vehicle.",
            "Automotive accident or the collision of any kind of vehicle.",
            "Automotive collision, which refers to the impact of any kind of vehicle.",
            "Automobile collision, which refers to the impact of any kind of vehicle.",
            "Automotive collision, which refers to the impact of any kind of vehicle.",
        ]
    },
    "wikievents_eae_disease_outbreak": {
        "en": [
            "Explicit mentions of an outbreak of a disease in an area, region, or country.",
            "Clear references to the occurrence of a widespread disease in a specific locale, region, or nation.",
            "Clear references to the occurrence of a disease outbreak within a specific locale, region, or nation.",
            "Clear references to the occurrence of a disease epidemic within a specific region or country.",
            "Clear references to the occurrence of a widespread disease within a specific area, region, or nation.",
        ]
    },
    "wikievents_eae_fire_explosion": {
        "en": [
            "A damaging fire or explosion, either natural or caused but without the intent of attacking.",
            (
                "A destructive fire or explosion, either stemming from natural causes or resulting from an"
                " unintentional act rather \nthan a deliberate attack."
            ),
            (
                "A destructive fire or explosion, either stemming from natural causes or human error, but not"
                " resulting from a \ndeliberate attack."
            ),
            (
                "A destructive fire or explosion, either occurring naturally or caused by human action but not with"
                " the purpose of \nlaunching an attack."
            ),
            (
                "A destructive fire or explosion, either due to natural causes or caused by an external factor but not"
                " as a result of a \ndeliberate attack."
            ),
        ]
    },
    "wikievents_eae_generic_crime": {
        "en": [
            (
                "For use as the crime argument in a Justice event when the crime event is not taggable as any other"
                " annotation ontology \nevent type."
            ),
            (
                "This text is intended for use as the crime argument in a Justice event when the crime event cannot be"
                " categorized under \nany other annotation ontology event type."
            ),
            (
                "This text is intended for use in the crime argument of a Justice event, when the crime event cannot"
                " be categorized \nunder any other annotation ontology event type."
            ),
            (
                "Use this text as the basis for the crime argument in a Justice event when the crime event cannot be"
                " categorized under \nany other type of annotation within an ontology."
            ),
            (
                "This text is intended for use in a Justice event when the crime event cannot be categorized under any"
                " other annotation \nontology event type."
            ),
        ]
    },
    "wikievents_eae_acquit": {
        "en": [
            (
                "An acquit event occurs whenever a trial ends but fails to produce a conviction, including cases where"
                " the charges are \ndropped by the prosecutor."
            ),
            (
                "An acquit event transpires whenever a judicial proceeding concludes without resulting in a"
                " conviction, \nencompassing instances in which the prosecutor chooses to abandon the charges."
            ),
            (
                "An acquit event transpires whenever a judicial proceeding concludes without resulting in a"
                " conviction, \nencompassing instances in which the prosecutor chooses to abandon the charges."
            ),
            (
                "An acquit event transpires whenever a judicial proceeding concludes without resulting in a"
                " conviction, \nencompassing instances in which the prosecutor chooses to abandon the charges."
            ),
            (
                "An acquit event transpires whenever a judicial proceeding concludes without resulting in a"
                " conviction, \nencompassing instances in which the prosecutor chooses to abandon the charges."
            ),
        ]
    },
    "wikievents_eae_arrest_jail_detain": {
        "en": [
            (
                "The detention, taking hostage, kidnapping, arrest, or jailing of an individual by government or"
                " non-government \nactors."
            ),
            "The act of confining, seizing, or imprisoning a person by government or non-government entities.",
            (
                "The act of detaining, seizing, abducting, or imprisoning a person by government or non-government"
                " entities."
            ),
            "The act of imprisoning, capturing, or confining a person by government or non-government entities.",
            "The act of confining, seizing, or imprisoning a person by government or non-government entities.",
        ]
    },
    "wikievents_eae_charge_indict": {
        "en": [
            "A government actor charging, accusing, or indicting a person, organization, or GPE of a crime.",
            (
                "An official from the government levies charges, makes accusations, or issues an indictment against an"
                " individual, \ngroup, or entity for engaging in illegal activities."
            ),
            (
                "A government official levies charges, makes accusations, or issues an indictment against an"
                " individual, group, or \ncorporate entity for engaging in illegal activities."
            ),
            (
                "When a government official files charges or levies accusations against an individual, group, or"
                " entity for \nengaging in illegal activities."
            ),
            (
                "An official from the government levies charges, makes accusations, or issues an indictment against an"
                " individual, \ngroup, or government-protected entity for engaging in unlawful activities."
            ),
        ]
    },
    "wikievents_eae_convict": {
        "en": [
            "A person, organization or GPE entity is convicted whenever that entity has been found guilty of a crime.",
            (
                "An individual, group, or governmental entity is deemed guilty of an offense whenever a judgment of"
                " conviction has \nbeen rendered against that party."
            ),
            (
                "Whenever an individual, group, or entity affiliated with a government or public enterprise is judged"
                " to have \ncommitted a crime, they are considered convicted."
            ),
            (
                "An individual, group, or global political entity is deemed guilty of an offense whenever a formal"
                " judgment of \nculpability has been levied against that entity."
            ),
            (
                "An individual, organization, or governmental entity is deemed guilty and convicted when a formal"
                " judgment of \nculpability has been rendered against that entity for committing a criminal act."
            ),
        ]
    },
    "wikievents_eae_investigate_crime": {
        "en": [
            "Legal, journalistic, and other investigations of crimes.",
            "Examining criminal activities through legal, journalistic, and other methodical inquiries.",
            "Examinations of criminal activities conducted by legal, journalistic, and other professional entities.",
            "Official, news-oriented, and additional probes into felonies.",
            "Official, journalistic, and various other inquiries into criminal acts.",
        ]
    },
    "wikievents_eae_release_parole": {
        "en": [
            (
                "A release-parole event occurs whenever a state actor (GPE, organization subpart, or person"
                " representative) ends \nits custody of a person entity because the sentence has ended, because the"
                " charges are dropped, or because parole has \nbeen granted."
            ),
            (
                "A release-on-parole situation takes place whenever a state actor, such as a governmental entity,"
                " organization, or \nan individual acting on their behalf, terminates their supervision of an"
                " individual due to the completion of their \nsentence, the dismissal of charges, or the granting of"
                " parole."
            ),
            (
                "A release-on-parole situation arises whenever a state figure (such as a government, organization, or"
                " individual \nacting on their behalf) terminates their supervision of an individual because their"
                " sentence has been completed, the \ncharges against them have been dismissed, or they have been"
                " granted parole."
            ),
            (
                "A release-on-parole situation arises whenever a state agent (such as a government, organization, or"
                " individual \nacting on their behalf) terminates the custody of an individual as a result of the"
                " completion of their sentence, the \nwithdrawal of charges, or the granting of parole."
            ),
            (
                "A release-on-parole situation arises whenever a state agent (such as a government, organization, or"
                " individual \nacting on their behalf) terminates their supervision of an individual, as a result of"
                " the completion of their sentence, the \ndismissal of charges, or the granting of parole."
            ),
        ]
    },
    "wikievents_eae_sentence": {
        "en": [
            (
                "A sentence event takes place whenever the punishment, particularly incarceration, for the defendant"
                " of a trial \nevent is issued by a state actor."
            ),
            (
                "A sentence occurrence happens whenever a state representative imposes the penalty, particularly"
                " imprisonment, \non the defendant in a legal case."
            ),
            (
                "A sentence occurrence happens whenever a state official imposes a penalty, particularly imprisonment,"
                " on the \ndefendant in a legal case."
            ),
            (
                "A sentence occurrence happens whenever the penalty, particularly imprisonment, imposed by a"
                " government official \non a defendant during a trial proceeding takes place."
            ),
            (
                "A sentence occurrence happens whenever the penalty, specifically imprisonment, imposed on the"
                " defendant in a \ntrial by a state representative is carried out."
            ),
        ]
    },
    "wikievents_eae_trial_hearing": {
        "en": [
            (
                "A trial event occurs whenever a court proceeding has been initiated for the purposes of determining"
                " the guilt or \ninnocence of a person, organization or GPE accused of committing a crime. A hearing"
                " event occurs whenever a state actor (GPE, \norganization subpart, or person representative)"
                " officially gathers to discuss some criminal legal matter."
            ),
            (
                "In the context of legal proceedings, a trial event takes place whenever a court case has been"
                " initiated to ascertain \nthe culpability or innocence of an individual, organization, or governing"
                " body accused of violating the law. A hearing \nevent, on the other hand, occurs whenever a"
                " representative of a state entity, such as a government, organization, or \nindividual, convenes for"
                " the purpose of discussing a matter related to criminal law."
            ),
            (
                "In the event of a trial, a legal process is initiated to assess the guilt or innocence of an"
                " individual, organization, \nor governing body accused of violating the law. Conversely, a hearing"
                " event takes place when a representative of the \nstate, be it a government entity, organization, or"
                " individual, convenes for the purpose of discussing a matter related to \ncriminal law."
            ),
            (
                "In the context of a court case, a trial event takes place whenever a legal proceeding is initiated to"
                " ascertain the \ninnocence or guilt of an individual, organization, or other party accused of"
                " violating the law. Conversely, a hearing event \noccurs whenever a representative of a state entity,"
                " such as a government, organization, or individual, convenes for the \npurpose of discussing a matter"
                " related to criminal law."
            ),
            (
                "In a trial event, a legal process is initiated to assess the guilt or innocence of an individual,"
                " organization, or GPE \naccused of violating the law. A hearing event, on the other hand, takes place"
                " when a representative of the state, such as a GPE, \norganization, or individual, convenes for an"
                " official discussion on a criminal legal matter."
            ),
        ]
    },
    "wikievents_eae_consume": {
        "en": [
            "An person or animal takes a substance into their body.",
            "A individual or creature ingests a substance within their physique.",
            "An individual, whether human or animal, ingests a substance within their body.",
            "An individual, whether human or animal, ingests a substance within their body.",
            "A person or animal ingests a substance within their body.",
        ]
    },
    "wikievents_eae_die": {
        "en": [
            "The death of a person or animal.",
            "The loss of life for an individual or animal.",
            "The loss of life for an individual or animal.",
            "The loss of life for an individual or animal.",
            "The loss of life for an individual or animal.",
        ]
    },
    "wikievents_eae_illness": {
        "en": [
            "A person or animal experiencing physical harm due to sickness or illness.",
            "An individual or animal undergoing bodily harm as a result of disease or illness.",
            "An individual or animal undergoing bodily harm as a result of illness or sickness.",
            "An individual or creature encountering bodily distress as a result of illness or disease.",
            "A individual or creature enduring bodily harm as a result of disease or ailment.",
        ]
    },
    "wikievents_eae_infect": {
        "en": [
            "A person or animal is infected with a pathogen.",
            (
                "An individual, whether human or animal, has been exposed to and is now hosting a particular"
                " disease-causing agent."
            ),
            (
                "An individual, whether human or animal, has been exposed to and is now hosting a particular"
                " disease-causing agent."
            ),
            "An individual, either human or animal, has been exposed to a harmful microorganism or substance.",
            "An individual, either human or animal, has been exposed to a harmful agent.",
        ]
    },
    "wikievents_eae_injure": {
        "en": [
            "The physical injuring of a person or animal.",
            "The act of causing bodily harm to a person or animal.",
            "The act of causing bodily harm to a person or animal.",
            "The act of causing bodily harm to a person or animal.",
            "The act of harming a person or animal through physical means.",
        ]
    },
    "wikievents_eae_diagnosis": {
        "en": [
            (
                "A determination of the disease or medical condition that explains a person's or animal's symptoms and"
                " signs."
            ),
            (
                "The process of identifying the specific illness or health issue that accounts for an individual's or"
                " animal's \nsymptoms and indications."
            ),
            (
                "A decision as to the illness or health issue that accounts for an individual's or animal's"
                " indications and \nmanifestations."
            ),
            (
                "A conclusive assessment of the illness or health issue that accounts for an individual's or animal's"
                " symptoms and \nindications."
            ),
            (
                "A conclusive determination of the health issue, whether a disease or medical condition, that accounts"
                " for the \nobservable symptoms and indicators experienced by an individual or animal."
            ),
        ]
    },
    "wikievents_eae_intervention": {
        "en": [
            (
                "Any kind of medical treatment or intervention for a person or an animal, often following a diagnosis"
                " of a medical \ncondition."
            ),
            (
                "Any form of therapeutic care or intervention implemented for an individual, whether human or animal,"
                " frequently \nafter a medical condition has been diagnosed."
            ),
            (
                "Medical treatment or intervention, which may include various procedures or therapies, is often"
                " provided to a \nperson or an animal following a diagnosis of an illness or medical condition."
            ),
            (
                "Any type of medical procedure or remedy administered to a person or animal, frequently after a"
                " diagnosis of an \nillness or condition."
            ),
            (
                "Medical care refers to any therapeutic intervention or treatment administered to a person or animal,"
                " frequently \nafter a diagnosis of an illness or health issue."
            ),
        ]
    },
    "wikievents_eae_vaccinate": {
        "en": [
            "A person or an animal is inoculated against a disease.",
            "An individual, whether human or animal, receives an inoculation to protect against a specific illness.",
            "An individual, whether human or animal, receives a protective immunization against an illness.",
            "An individual, whether human or animal, receives an inoculation to protect against a particular illness.",
            "An individual, whether human or animal, receives an inoculation to protect against a specific disease.",
        ]
    },
    "wikievents_eae_evacuation": {
        "en": [
            (
                "The movement of a person or animal (by an agent or via their own effort) from one place to another"
                " for evacuation \npurposes."
            ),
            (
                "The action of an individual or animal being relocated (by an influencer or through their own"
                " initiative) for the \npurpose of evacuation."
            ),
            (
                "The action of an individual or animal relocating to a safe area, whether assisted by another entity"
                " or \nself-initiated, during a time of emergency."
            ),
            (
                "The action of an individual or animal being relocated (whether by an external force or their own"
                " initiative) for the \npurpose of evacuation."
            ),
            (
                "The process of relocation for an individual or animal, whether facilitated by an external agent or"
                " self-initiated, \nin order to evacuate from a given location."
            ),
        ]
    },
    "wikievents_eae_grant_allow_passage": {
        "en": [
            "Explicit mention of granting or allowing entry or exit from a location.",
            "Specific reference to granting or permitting access to or egress from a particular place.",
            "Specific reference to permitting access or egress to or from a particular place.",
            "Specific reference to permitting access or egress to or from a particular place.",
            "Specific reference to granting or permitting access to or egress from a particular place.",
        ]
    },
    "wikievents_eae_illegal_transportation": {
        "en": [
            (
                "Explicit mention of illegal physical transporting of people or things between places, such as"
                " smuggling, \ntrafficking, illegal border crossings."
            ),
            (
                "Clear reference to unlawful movement of people or objects from one location to another, including"
                " smuggling, human \ntrafficking, and illegal border passage."
            ),
            (
                'Text: "Specific reference to unlawful movement of individuals or items between locations, including'
                " smuggling, \nhuman trafficking, and unauthorized border crossings."
            ),
            (
                'Text: "Specific references to the unauthorized movement of individuals or items from one location to'
                " another, \nincluding smuggling, human trafficking, and illegal border crossing."
            ),
            (
                'Text: "Clear references to unlawful movements of people or items from one location to another,'
                " including \nsmuggling, human trafficking, and illegal border crossings."
            ),
        ]
    },
    "wikievents_eae_prevent_passage": {
        "en": [
            "Explicit mention of preventing entry or exit from a location.",
            "Clear statement regarding the prohibition of entry or exit at a specific place.",
            "Clear statement regarding the restriction of access to or egress from a specific area.",
            'Text: "Specific reference to preventing access to or egress from a particular area.',
            "Specific reference to preventing access or egress at a particular site.",
        ]
    },
    "wikievents_eae_transportation": {
        "en": [
            (
                "Physical movement or transportation of a person or artifact between places, includes putting and"
                " placing objects \nin locations."
            ),
            (
                "The process of relocating an individual or object from one location to another, which entails"
                " positioning and \ndepositing items in specific places."
            ),
            (
                "The process of relocating individuals or items from one location to another, which involves"
                " positioning and \ndepositing objects in various places."
            ),
            (
                "The process of relocating individuals or objects from one location to another, which involves"
                " positioning and \ndepositing items in specific places."
            ),
            (
                "The process of relocating individuals or objects from one location to another, which involves"
                " positioning and \ndepositing items in specific places."
            ),
        ]
    },
    "wikievents_eae_change_job_location": {
        "en": [
            "A person continuing in the same role in a different location in the same organization.",
            "An individual who retains their position while relocating to a new site within the same organization.",
            (
                "An individual who remains in the same position but transfers to a distinct area within the same"
                " organization."
            ),
            "An individual who retains their position but relocates to a new site within the same organization.",
            (
                "An individual who remains in the same position but transitions to a different site within the same"
                " organization."
            ),
        ]
    },
    "wikievents_eae_change_job_title": {
        "en": [
            (
                "A person changing from one position to another in the same organization, with no indication of"
                " relative levels of the \npositions."
            ),
            (
                "A individual transitioning between two roles within the same organization, without any indication of"
                " the \npositions' respective hierarchical rankings."
            ),
            (
                "An individual transitioning between roles within the same organization, without any indication of the"
                " \nhierarchical relationship between the positions."
            ),
            (
                "An individual transitioning between two roles within the same organization, without any indication of"
                " the \npositions' hierarchical relationship."
            ),
            (
                "An individual transferring from one role to another within the same organization, without any"
                " indication of the \npositions' hierarchical relation."
            ),
        ]
    },
    "wikievents_eae_end_position": {
        "en": [
            (
                "A person stopping working in a position, with no indication that they are changing positions within"
                " the same \norganization."
            ),
            (
                "An individual ceasing to fulfill their role in a particular position, without any sign of"
                " transitioning to another \nrole within the same organization."
            ),
            (
                "An individual who ceases to work in a particular role, without any indication that they are"
                " transitioning to a \ndifferent role within the same organization."
            ),
            (
                "An individual ceasing their duties in a specific role, without any indication that they will be"
                " transitioning to \nanother role within the same company."
            ),
            (
                "An individual ceasing their duties in a specific role, without any indication that they will be"
                " transitioning to \nanother role within the same company."
            ),
        ]
    },
    "wikievents_eae_start_position": {
        "en": [
            (
                "A person starting working in a position, with no indication that they are changing positions within"
                " the same \norganization."
            ),
            (
                "An individual commences employment in a specific role, without any sign of transitioning to another"
                " role within the \nsame company."
            ),
            (
                "An individual commences employment in a specific role, without any hint that they are transitioning"
                " to another role \nwithin the same company."
            ),
            (
                "An individual commences employment within a specific role, without any signification of transitioning"
                " to another \nrole within the same company."
            ),
            (
                "An individual commences employment in a particular role, without any suggestion that they are"
                " transitioning to a \ndifferent role within the same company."
            ),
        ]
    },
    "wikievents_eae_aid_between_governments": {
        "en": [
            (
                "A voluntary transfer of resources from one GPE to another from the perspective of governments, often"
                " with strings \nattached."
            ),
            (
                "A willing allocation of assets from one government agency to another, as seen from the viewpoint of"
                " the governments, \nfrequently accompanied by specific conditions."
            ),
            (
                "A voluntary relocation of assets from one government agency to another, as seen from the viewpoint of"
                " governments, \nfrequently accompanied by specific conditions."
            ),
            (
                "A voluntary relocation of assets from one government agency to another, as seen from the viewpoint of"
                " governments, \nfrequently accompanied by specific conditions."
            ),
            (
                "A willing allocation of assets from one government entity to another, as seen from the viewpoint of"
                " governments, \nfrequently accompanied by specific conditions."
            ),
        ]
    },
    "wikievents_eae_donation": {
        "en": [
            (
                "The voluntary provision, donation, or extension of material aid in the form of assets or commodities"
                " (nb: use \nAidBetweenGovernments instead for GPE to GPE donations)."
            ),
            (
                "The voluntary offering, contribution, or expansion of tangible support in the form of resources or"
                " goods (note: use \nAidBetweenGovernments for aid donations between governments)."
            ),
            (
                "The voluntary supply, contribution, or allocation of tangible resources in the form of assets or"
                " goods (replace \nAidBetweenGovernments with AidBetweenGovernments for government-to-government"
                " donations)."
            ),
            (
                "The voluntary contribution, gift, or allocation of tangible resources, such as assets or goods,"
                " between entities \n(e.g., governments, organizations, or individuals)."
            ),
            (
                "The voluntary offer, contribution, or allocation of resources in the form of goods or services (note:"
                " use \nAidBetweenGovernments for government-to-government donations)."
            ),
        ]
    },
    "wikievents_eae_exchange_buy_sell": {
        "en": [
            (
                "A transaction transferring or obtaining money, ownership, possession, or control of something,"
                " applicable to any \ntype, nature, or method of acquisition including barter."
            ),
            (
                "A transaction involving the transfer or acquisition of funds, property, or control, encompassing all"
                " types, \nnatures, and methods of procurement, including bartering."
            ),
            (
                "A transaction involving the exchange or acquisition of assets, including money, ownership,"
                " possession, or \ncontrol, encompassing all types, natures, and methods of procurement, such as"
                " barter."
            ),
            (
                "A transaction involving the transfer or acquisition of assets, such as money, property, or control,"
                " encompassing \nall types, natures, and methods of procurement, including barter."
            ),
            (
                "A transaction involving the transfer or acquisition of money, property, or control, encompassing all"
                " types, \nnatures, and methods of procurement, including barter."
            ),
        ]
    },
}
