GUIDELINES = {
    "ace_gpe": {
        "en": [
            "Geo-Political Entities are composite entities comprised of a population, a government, a physical\nlocation, and a nation (or province, state, country, city, etc.).\n",
            'The term "Geo-Political Entities" refers to entities that are made up of a population, a government, a specific physical location, and a nation or region, such as a province, state, country, or city.',
            '"Geo-Political Entities are made up of a combination of a populace, a governing body, a specific location, and a nation (or province, state, city, etc.)."',
            "Geo-Political Entities are groups made up of a population, a governing body, a specific location, and a nation or region.",
            "Geo-Political Entities are made up of a combination of a populace, a governing body, a specific location, and a nation or region, which can be considered as a province, state, country, or city.",
        ]
    },
    "ace_acquit": {
        "en": [
            "An Acquit Event occurs whenever a trial ends but fails to produce a conviction. This will include cases\nwhere the charges are dropped by the Prosecutor.\n",
            "An Acquit Event takes place when a trial comes to an end without resulting in a conviction. This includes instances when the charges are dropped by the Prosecutor.",
            "An Acquit Event happens when a trial concludes without leading to a conviction. This includes instances when the charges are dismissed by the Prosecutor.",
            "An Acquit Event takes place when a trial concludes without resulting in a conviction. This can happen when the prosecutor decides to drop the charges.",
            "An Acquit Event takes place when a trial comes to an end without resulting in a conviction. This can include instances when the charges are dismissed by the Prosecutor.",
        ]
    },
    "ace_agentartifactrelationrelation": {
        "en": [
            "The AgentArtifact Relation applies when an agent owns an artifact, has possession of an artifact, uses\nan artifact, or caused an artifact to come into being. Note: if the `arg2` is an Organization, use\nOrganizationAffiliation when `arg1` is a Person or PartWhole when `arg1` is an Organization or GPE.\n",
            "The AgentArtifact Relation is applicable when an individual or entity, referred to as an agent, has ownership, possession, utilization, or creation responsibility for a particular artifact. It is important to note that if the second argument, referred to as arg2, is an organization, then the OrganizationAffiliation should be used when arg1 is a person, or the PartWhole relationship should be used when arg1 is an organization or GPE.",
            "The AgentArtifact Relation pertains when an individual, either a person or an organization, has ownership or control over an artifact, utilizes it, or is responsible for its creation. In the event that arg2 is an organization, the OrganizationAffiliation should be applied when arg1 is a person, while PartWhole should be used when arg1 is an organization or GPE.",
            "The AgentArtifact Relation is applicable when an individual, referred to as an agent, has ownership or possession of an artifact, utilizes the artifact, or is responsible for its creation. It is important to note that if the second argument (arg2) is an organization, then the OrganizationAffiliation should be used when the first argument (arg1) is a person, while the PartWhole should be used when the first argument is an organization or a GeneralPurposeEntity.",
            "The AgentArtifact Relation is applicable when an individual, referred to as an agent, has ownership of an object or product, referred to as an artifact. Additionally, the agent may have possession of the artifact, use it, or be responsible for its creation. It is important to note that if the second argument, referred to as `arg2`, is an organization, then the OrganizationAffiliation should be used when the first argument, referred to as `arg1`, is a person, and the PartWhole should be used when the first argument is an organization or a General Product Entity.",
        ]
    },
    "ace_appeal": {
        "en": [
            "An Appeal Event occurs whenever the decision of a court is taken to a higher court for review.",
            "A higher court reviews a lower court's decision in the event of an Appeal.",
            'A "notice of appeal" is triggered when a court\'s ruling is challenged by being sent to a higher court for further examination.',
            "A higher court is convened to review a court's decision whenever an Appeal Event occurs.",
            "A higher court reviews the decision of a lower court in an Appeal Event.",
        ]
    },
    "ace_arrestjail": {
        "en": [
            "A Jail Event occurs whenever the movement of a Person is constrained by a state actor (a GPE, its\nOrganization subparts, or its Person representatives).\n",
            "A Jail Event happens when the movement of a person is restricted by a state actor, which can be a Governmental Public Entity, its organizational subunits, or its representative persons.",
            '"A Jail Event takes place when the movement of a person is restricted by a state actor, which may be a GPE, its suborganizations, or its representative people."',
            "A Jail Event takes place when the movement of a person is restricted by a state actor, which can be a General Purpose Entity (GPE), its sub-organizations, or its representative individuals.",
            "A Jail Event takes place when the movement of an individual is restricted by a state actor, which can be a General Purpose Entity (GPE), its sub-organizations, or its representative persons.",
        ]
    },
    "ace_attack": {
        "en": [
            "An Attack Event is defined as a violent physical act causing harm or damage. Attack Events include any\nsuch Event not covered by the Injure or Die subtypes, including Events where there is no stated agent.\n",
            '"An Attack Event refers to a violent physical act that results in harm or damage. This category of events encompasses any incident that is not covered by the Injure or Die subtypes, including those where the perpetrator is not specified."',
            'An "Attack Event" refers to a violent physical act that results in harm or damage. This category of events encompasses any incidents that cannot be classified under the "Injure" or "Die" subtypes, including situations where no specific agent is identified.',
            'An attack event is characterized by a violent physical act that results in harm or damage. This type of event encompasses any attack that is not categorized under the "injure" or "die" subtypes, including instances where no specific agent is identified.',
            "An Attack Event is characterized by a violent physical act that results in harm or damage. This type of event encompasses any instance of an attack that is not classified under the Injure or Die subtypes, including those where the perpetrator is not specified.",
        ]
    },
    "ace_beborn": {
        "en": [
            "A BeBorn Event occurs whenever a Person Entity is given birth to.",
            "A BeBorn Event takes place when a Person Entity is born.",
            "A BeBorn Event takes place whenever a Person Entity is born.",
            '"The occurrence of a BeBorn Event is triggered when a Person Entity is born."',
            '"The occurrence of a BeBorn Event is triggered whenever a Person Entity is born."',
        ]
    },
    "ace_business": {
        "en": [
            "The Business Relation captures the connection between two entities in any professional relationship.\nBoth arguments must be entities of type Person.\n",
            'The "Business Relation" refers to the connection between two parties in a professional setting, where both parties must be represented by "Person" entities.',
            'The "Business Relation" refers to the connection that exists between two parties in a professional context. This connection is defined by the relationship between two entities, both of which must be classified as "Person" entities.',
            "The professional relationship between two entities is captured by the Business Relation, which connects two entities, both of which must be individuals or persons.",
            "The professional relationship is characterized by the connection between two parties, which are represented as entities of type Person.",
        ]
    },
    "ace_businessevent": {
        "en": [
            "A BusinessEvent refers to actions related to Organizations such as: creating, merging, declaring\nbankruptcy or ending organizations (including government agencies).\n",
            "A BusinessEvent encompasses actions pertaining to organizations, such as the creation, merger, bankruptcy filing, or discontinuation of entities, including government agencies.",
            "A BusinessEvent encompasses activities related to organizations, including the creation, merging, filing for bankruptcy, and dissolution of entities (both private and public).",
            "A BusinessEvent is defined as an action or set of actions related to organizations, such as the creation, merging, or dissolution of businesses, as well as the declaration of bankruptcy or the termination of government agencies.",
            "A BusinessEvent refers to actions that relate to organizations, such as the creation, merger, bankruptcy declaration, or discontinuation of organizations (including government agencies).",
        ]
    },
    "ace_chargeindict": {
        "en": [
            "A Charge Event occurs whenever a Person, Organization or GPE is accused of a crime by a state actor\n(GPE, an Organization subpart of a GPE or a Person representing a GPE).\n",
            "A Charge Event takes place when an individual, organization, or governmental public entity (GPE) is accused of committing a crime by a government actor (GPE, an organization subunit of a GPE, or a person representing a GPE).",
            "A Charge Event takes place when a person, organization, or governmental public entity (GPE) is accused of committing a crime by a state actor, which may include a GPE subpart, a person representing a GPE, or a state actor itself.",
            "A Charge Event takes place when a person, organization, or governmental public entity (GPE) is accused of committing a crime by a state actor, which may include a GPE subunit, a person representing a GPE, or a state official.",
            "A charge event takes place when an individual, organization, or governmental public entity (GPE) is accused of committing a crime by a state actor, which may include a GPE subunit, a person representing a GPE, or another organization.",
        ]
    },
    "ace_citizenresidentreligionethnicity": {
        "en": [
            "CitizenResidentReligionEthnicity describes the relation between a Person entity and (1) the GPE in\nwhich they have citizenship, (2) the GPE or Location in which they live, the religious Organization or\nPerson entity with which they have affiliation and (3) the GPE or PER entity that indicates their\nethnicity.\n",
            '"The CitizenResidentReligionEthnicity relates a Person entity to (1) the General Partnership Entity (GPE) in which they hold citizenship, (2) the GPE or Location where they reside, (3) the religious Organization or Person entity to which they are affiliated, and (4) the GPE or Specific Entity (PER) that identifies their ethnicity."',
            "The CitizenReligionEthnicity attribute connects a Person entity to (1) the General Partner Entity (GPE) in which they hold citizenship, (2) the GPE or Location where they reside, (3) the religious Organization or Person entity to which they belong, and (4) the GPE or Physical Entity Representation (PER) that defines their ethnicity.",
            'The "Citizen/Resident/Religion/Ethnicity" descriptor defines the connection between a "Person" entity and the following factors: (1) the "Government/Organization/Entity" (GPE) in which they hold citizenship, (2) the GPE or location where they reside, (3) the religious organization or person entity with which they have affiliation, and (4) the GPE or "Entity" (PER) that indicates their ethnicity.',
            "The Person entity has a relationship with several factors, including their citizenship status in a particular GPE, their place of residence in a GPE or Location, their religious affiliation with a religious Organization or Person entity, and their ethnicity as indicated by a GPE or PER entity.",
        ]
    },
    "ace_conflictevent": {
        "en": [
            "A ConflictEvent refers to either violent physical acts causing harm or damage, but are not covered by\nLife events (conflicts, clashes, fighting, gunfire, ...) or demonstrations (protests, sit-ins,\nstrikes, riots, ...).\n",
            "A ConflictEvent refers to incidents that involve physical violence, resulting in harm or damage, but are not considered part of Life events or demonstrations. These events may include conflicts, clashes, fighting, gunfire, among others, but are not covered under the aforementioned categories.",
            "A ConflictEvent refers to incidents that involve physical violence and result in harm or damage, but are not considered part of Life events, which include conflicts, clashes, fights, gunfire, and the like. Nor are they considered part of demonstrations, such as protests, sit-ins, strikes, or riots.",
            "A ConflictEvent is characterized by physical acts of violence that result in harm or damage, but are not included in the categories of Life events such as conflicts, clashes, fighting, gunfire, etc. or demonstrations like protests, sit-ins, strikes, riots, etc.",
            "A ConflictEvent is defined as any instance of physical harm or damage caused by violent acts, but it is not considered part of the Life events category, which includes conflicts, confrontations, fights, gunfire, and the like. It is also not encompassed by the category of demonstrations, which includes protests, sit-ins, strikes, and riots.",
        ]
    },
    "ace_contactevent": {
        "en": [
            "A ContactEvent occurs whenever two or more entities (persons or organization's representatives) come\ntogether at a single location and interact with one another face-to-face or directly enages in\ndiscussion via written or telephone communication.\n",
            "A ContactEvent takes place when multiple entities, whether individuals or representatives of organizations, gather at a single location and engage in direct communication with one another, either through face-to-face interactions or through written or telephone communication.",
            "A ContactEvent takes place when two or more individuals or representatives of organizations meet at a single location and interact with each other either in person or through direct communication, such as written or phone conversations.",
            "A ContactEvent takes place when two or more individuals or representatives of organizations meet each other in person or through direct communication, such as written or telephonic dialogue, at a specific location.",
            "A ContactEvent takes place when multiple entities, whether individuals or representatives of organizations, gather at a single location and engage in direct communication with one another, either through face-to-face interaction or through written or telephonic communication.",
        ]
    },
    "ace_contactinfo": {
        "en": [
            "A ContactInfo value refers to contact information values such as telephone numbers, emails, addresses.\nFor example: 'mich...@sumptionandwyland.com', ...\n",
            "\"ContactInfo refers to contact information, such as telephone numbers, email addresses, and street addresses. For example, '[michael.hayes@sumptionandwyland.com](mailto:michael.hayes@sumptionandwyland.com),' or '[sales@sumptionandwyland.com](mailto:sales@sumptionandwyland.com).'\"",
            'The ContactInfo value represents a range of contact information, including telephone numbers, email addresses, and physical addresses. For example, "michael\\_w@sumptionandwyland.com" or "9876543210" could be considered a ContactInfo value.',
            '"A ContactInfo value represents a variety of contact information, including telephone numbers, email addresses, and physical addresses. For example, a ContactInfo value may include a string in the format of "[michael.wyland@sumptionandwyland.com](mailto:michael.wyland@sumptionandwyland.com)," or another similar format."',
            "\"ContactInfo refers to information such as telephone numbers, email addresses, and physical addresses, like '[mich...@sumptionandwyland.com](mailto:mich...@sumptionandwyland.com)', etc.\"",
        ]
    },
    "ace_convict": {
        "en": [
            "A Convict Event occurs whenever a Try Event ends with a successful prosecution of the Defendant. In\nother words, a Person, Organization or GPE Entity is convicted whenever that Entity has been found\nguilty of a Crime.\n",
            '"A Convict Event takes place when a Trial Event concludes with a verdict of guilty against the Defendant. This means that a person, organization, or Government, Police, and Enforcement (GPE) entity has been convicted of committing a crime."',
            "A conviction event takes place when a trial event concludes with a successful prosecution of the defendant, meaning that a person, organization, or GPE entity has been found guilty of a crime.",
            "A conviction event takes place when a trial event comes to an end with a successful prosecution of the defendant. In simpler terms, it means that a person, organization, or GPE entity is convicted when it has been found guilty of a crime.",
            "A conviction event takes place when a trial event concludes with a successful prosecution of the accused defendant. In simpler terms, this means that a person, organization, or government-owned and -operated entity is convicted if they have been found guilty of a crime.",
        ]
    },
    "ace_crime": {
        "en": [
            "A Crime value refers to the specific reason (crime) that a Person entity can be judged or sentenced\nfor. For example: 'raping', 'murder', 'drug', ...\n",
            "\"A Crime value represents the specific offense or infraction (crime) for which a Person can be held accountable and face legal consequences, such as 'rape', 'murder', or 'drug-related offenses'.\"",
            'A Crime value refers to the specific offense (crime) for which a Person entity can be prosecuted or punished. This can include crimes such as "raping," "murder," or "drug-related offenses."',
            'A Crime value represents the specific offense (crime) for which a Person entity can be prosecuted or punished. Examples include: "raping," "murder," "drug trafficking," etc.',
            'A Crime value represents the specific offense for which a Person can be prosecuted or punished. This may include crimes such as "raping," "murder," or "drug-related offenses."',
        ]
    },
    "ace_declarebankruptcy": {
        "en": [
            "A DeclareBankruptcy Event will occur whenever an Entity officially requests legal protection from debt\ncollection due to an extremely negative balance sheet.\n",
            "A DeclareBankruptcy Event will take place when an Entity files for legal protection from creditors because of an extremely unfavorable financial situation.",
            "An entity will experience a DeclareBankruptcy Event when it officially seeks legal protection from debt collection due to a significantly negative balance sheet.",
            "A DeclareBankruptcy Event will take place when an Entity files for legal protection from creditors due to an insurmountable amount of debt.",
            "A DeclareBankruptcy Event will take place when an Entity legally seeks relief from debt accumulation due to a severely unfavorable financial position.",
        ]
    },
    "ace_demonstrate": {
        "en": [
            "A Demonstrate Event occurs whenever a large number of people come together in a public area to protest\nor demand some sort of official action. Demonstrate Events include, but are not limited to,\nprotests, sit-ins, strikes, and riots.\n",
            'A "Demonstrate Event" refers to a gathering of numerous individuals in a public space to express their dissent or call for official intervention. Such events encompass but are not limited to protests, sit-ins, strikes, and riots.',
            "A Demonstration Event takes place when a significant number of individuals congregate in a public area to express their dissent or demand for official intervention. Such events encompass but are not limited to protests, sit-ins, strikes, and riots.",
            "A demonstration event takes place when a significant number of individuals congregate in a public space to express their dissent or demand some sort of official response. Demonstration events encompass, but are not limited to, protests, sit-ins, strikes, and riots.",
            'A "Demonstrate Event" refers to a gathering of a large number of individuals in a public space for the purpose of expressing dissent or advocating for a specific action by authorities. Such events encompass a variety of forms, including but not limited to protests, sit-ins, strikes, and riots.',
        ]
    },
    "ace_die": {
        "en": [
            "A Die Event occurs whenever the life of a Person Entity ends. Die Events can be accidental, intentional\nor self-inflicted\n",
            "Whenever the life of a Person Entity comes to an end, a Die Event takes place. These events can be either accidental, intentional, or self-inflicted in nature.",
            "A Die Event takes place when the life of a Person Entity comes to an end. These events can be the result of accidental, intentional, or self-inflicted causes.",
            'A "Die Event" takes place whenever the life of a "Person Entity" comes to an end. These events can be either accidental, intentional, or self-inflicted.',
            '"A Die Event takes place when the life of a Person Entity comes to an end. These events can be caused by accident, intentional actions, or self-inflicted harm."',
        ]
    },
    "ace_divorce": {
        "en": [
            "A Divorce Event occurs whenever two people are officially divorced under the legal definition of\ndivorce. We do not include separations or church annulments.\n",
            "A Divorce Event refers to the legally recognized dissolution of a marriage between two individuals, which occurs when they are officially divorced. This term does not encompass separations or church annulments.",
            "A Divorce Event takes place when two individuals have their marriage legally dissolved, as defined by the legal system. This includes divorces, but not separations or annulments granted by a church.",
            "A Divorce Event is defined as the official legal dissolution of a marriage between two individuals, and does not include separations or church annulments.",
            "A Divorce Event is triggered when a couple's legal divorce is officially recognized. This includes all aspects of the divorce process, except for separations or church annulments.",
        ]
    },
    "ace_elect": {
        "en": [
            "An Elect Event occurs whenever a candidate wins an election designed to determine the Person argument\nof a StartPosition Event.\n",
            '"An Elect Event happens whenever a candidate is successful in an election that is intended to settle the Person argument of a StartPosition Event."',
            '"An Elect Event takes place when a candidate is successful in an election that is intended to decide the Person argument of a StartPosition Event."',
            '"An Elect Event takes place when a candidate emerges victorious in an election aimed at settling the Person argument of a StartPosition Event."',
            '"An Elect Event takes place when a contender emerges victorious in an election aimed at settling the Person argument of a StartPosition Event."',
        ]
    },
    "ace_employment": {
        "en": [
            "Employment captures the relationship between Persons and their employers. This Relation is only\ntaggable when it can be reasonably assumed that the Person is paid by the ORG or GPE.\n",
            "The employment relationship pertains to the association between individuals and their employers. This connection can only be categorized as such if it can be reasonably assumed that the individual is receiving remuneration from either the organization or the government.",
            "The employment relationship pertains to the association between individuals and their employers. This connection can only be categorized as such when it is plausible to assume that the individual is receiving payment from either the organization or the government.",
            "The employment relationship pertains to the association between individuals and their employers. This connection can only be labeled as such when it is reasonable to assume that the person is receiving remuneration from either the organization or the government entity.",
            '"Employment refers to the connection between individuals and their employers. This connection can only be classified as such when it is reasonable to assume that the individual is receiving payment from either the organization or government entity."',
        ]
    },
    "ace_endorg": {
        "en": [
            "An EndOrg Event occurs whenever an Organization ceases to exist (in other words 'goes out of\nbusiness').\n",
            "An EndOrg Event takes place when an organization terminates its operations and ceases to exist.",
            "An EndOrg Event takes place when an organization terminates its operations and ceases to exist.",
            "An EndOrg Event happens when an organization stops operating and ceases to exist.",
            "An EndOrg Event happens when an organization stops operating and ceases to exist.",
        ]
    },
    "ace_endposition": {
        "en": [
            "An EndPosition Event occurs whenever a Person Entity stops working for (or changes offices within) an\nOrganization or GPE.\n",
            "An EndPosition Event takes place when a Person Entity finishes working for (or transfers to a different department within) an Organization or GPE.",
            "An EndPosition Event takes place when a Person Entity terminates their employment with (or relocates to a different department within) a Company or General Partner Entity.",
            "A termination of employment or change of job position within an organization or GPE (Global Public Entity) is referred to as an EndPosition Event.",
            "An EndPosition Event takes place when a Person Entity finishes working for (or switches jobs within) a Business or Governmental Entity.",
        ]
    },
    "ace_execute": {
        "en": [
            "An Execute Event occurs whenever the life of a Person is taken by a state actor (a GPE, its\nOrganization subparts, or Person representatives).\n",
            '"The Execute Event happens whenever the life of a person is taken by a state actor, which can be a government, its agencies, or the person\'s representatives."',
            '"The Execute Event happens whenever the life of a person is terminated by a state actor, such as a government, its sub-organizations, or representatives of the person."',
            '"The Execute Event takes place when the life of a person is terminated by a state actor, such as a governmental organization, its subunits, or representatives of the person."',
            'A "Execute Event" takes place whenever a person\'s life is terminated by a state actor, which includes governmental public entities, their subdivisions, or representatives of the person.',
        ]
    },
    "ace_extradite": {
        "en": [
            "An Extradite Event occurs whenever a Person is sent by a state actor from one Place (normally the GPE\nassociated with the state actor, but sometimes a Facility under its control) to another place\n(Location, GPE or Facility) for the purposes of legal proceedings there.\n",
            '"The extradition event takes place when a person is transferred from one location to another, typically from one state actor\'s territory to another, for the purpose of legal proceedings."',
            "An Extradition Event takes place when a person is transferred from one location (usually the place associated with the sending state actor, but occasionally a facility under its control) to another location (either a location or a facility) for the purpose of legal proceedings at the second location.",
            '"The act of extradition involves the transfer of an individual from one location to another, typically from one country to another, for the purpose of legal proceedings."',
            "A rendition event occurs when an individual is transported by a state entity from one location (usually the place associated with the entity, but sometimes a facility under its control) to another location (place, global processing entity or facility) for the purpose of legal proceedings at the second location.",
        ]
    },
    "ace_facility": {
        "en": [
            "A facility is a functional, primarily man-made structure. These include buildings and similar\nfacilities designed for human habitation, such as houses, factories, stadiums, office buildings, ...\nRoughly speaking, facilities are artifacts falling under the domains of architecture and civil\nengineering.\n",
            "A facility refers to a functional structure that is primarily designed and constructed by humans. This category includes various types of buildings and structures such as houses, factories, stadiums, office buildings, and others. In general, facilities are considered to be artifacts that are associated with the fields of architecture and civil engineering.",
            "A facility refers to a functional structure that is primarily designed and built by humans. Examples of facilities include buildings such as houses, factories, stadiums, office buildings, and others that are intended for human use or occupation. In general, facilities can be considered as artifacts that fall within the domains of architecture and civil engineering.",
            "A facility refers to a purpose-built structure that is designed for a specific function or activity. These structures can range from residential buildings and factories to stadiums, office buildings, and other types of commercial or industrial properties. In general, facilities are man-made structures that are designed and constructed with the intention of serving a particular function or purpose. They are typically associated with the fields of architecture and civil engineering, which involve the design and construction of buildings and other structures.",
            "A facility refers to a purpose-built structure that is primarily designed for human use, such as buildings, houses, factories, stadiums, and office buildings. In essence, facilities are man-made structures that are associated with the fields of architecture and civil engineering.",
        ]
    },
    "ace_family": {
        "en": [
            "The Family Relation captures the connection between one entity and another with which it is in any\nfamilial relationship. Both arguments must be entities of type Person.\n",
            'The "Family Relation" relates the bond shared by two entities, regardless of the specific familial connection they have with each other. Both parties must be classified as "Person" entities.',
            "The concept of Family Relation pertains to the bond shared between two entities that have a familial connection. Both the entities in question must be classified as Persons.",
            '"The Family Relation refers to the bond that exists between two entities that are connected through a familial relationship. Both the entities in question must be classified as people."',
            "The concept of Family Relation pertains to the bond that exists between two entities that have a familial connection. This bond is established between two entities of the type Person.",
        ]
    },
    "ace_fine": {
        "en": [
            "A Fine Event takes place whenever a state actor issues a financial punishment to a GPE, Person or\nOrganization Entity, typically as a result of court proceedings.\n",
            '"When a government official imposes a financial penalty on a GPE, person, or organization as a consequence of legal proceedings, it is referred to as a Fine Event."',
            '"A Fine Event occurs when a government entity imposes a financial penalty on a GPE (governmental public entity), individual, or organization, often as a result of legal proceedings."',
            '"A Fine Event occurs when a government official imposes a financial penalty on a GPE (Global Public Entity), individual, or organization, typically as a result of legal proceedings."',
            '"A Fine Event occurs when a government actor imposes a financial penalty on a General Public, Person, or Organization, usually as a consequence of legal proceedings."',
        ]
    },
    "ace_founder": {
        "en": [
            "Founder captures the relationship between an agent (Person, Organization, or GPE) and an Organization\nor GPE established or set up by that agent.\n",
            'The term "Founder" refers to the connection between an individual or entity (such as a person, organization, or GPE) and an organization or GPE that has been established or created by that individual or entity.',
            'The term "Founder" refers to the connection between an individual or entity (such as a person, organization, or General Partnership Estate) and an organization or General Partnership Estate that has been established or created by that person or entity.',
            'The term "Founder" refers to the connection between an individual or entity (such as a person, organization, or General Partner Entity) and an organization or GPE that has been established or created by that individual or entity.',
            'The term "Founder" refers to the connection between an individual or entity (such as a person, organization, or General Purpose Entity) and an organization or GPE that was established or created by that individual or entity.',
        ]
    },
    "ace_genaffiliationrelation": {
        "en": [
            "The GenAffiliation Relation describes the citizen, resident, religion or ethnicity relation when the\n`arg1` is a Person. When the `arg1` is an Organization, the relation describes where it is located,\nbased or does business.\n",
            "The GenAffiliation Relation pertains to the connection between a person or organization and their status as a citizen, resident, member of a certain religion or ethnic group. When the individual in question is a person, the GenAffiliation Relation outlines their personal affiliation. However, when the individual is an organization, the GenAffiliation Relation highlights the location or context in which the organization operates.",
            "The GenAffiliation Relation pertains to the association between a person or organization and their citizenship, residency, religion, or ethnicity. When the arg1 is a person, the relation indicates their affiliation. When the arg1 is an organization, the relation provides information about its location, origin, or business activities.",
            "The GenAffiliation Relation pertains to the connection between a person or an organization and their citizenship, residency, religious or ethnic background. When the argument (arg1) is an individual, the relationship outlines their affiliation. On the other hand, when the argument is an organization, the relationship describes its location, origin, or the areas in which it operates.",
            "The GenAffiliation Relation pertains to the connection between a person or organization and their citizenship, residency, religion, or ethnicity. If the individual is a person, then the affiliation is based on their personal relationship. Conversely, if the individual is an organization, then the relationship describes the location where they are headquartered, operate, or conduct business.",
        ]
    },
    "ace_geographical": {
        "en": [
            "The Geographical relation captures the location of a Facility, Location, or GPE in or at or as a part\nof another Facility, Location, or GPE.\n",
            "The Geographical Relation describes the position of a Facility, Location, or GPE in relation to another Facility, Location, or GPE.",
            "The Geographical relation refers to the situation where a Facility, Location, or GPE is situated within or at another Facility, Location, or GPE.",
            "The Geographical relation refers to the situation where a Facility, Location, or GPE is situated within or at another Facility, Location, or GPE.",
            '"The Geographical relation refers to the situating of a Facility, Location, or GPE at or in another Facility, Location, or GPE."',
        ]
    },
    "ace_injure": {
        "en": [
            "An Injure Event occurs whenever a Person Entity experiences physical harm. Injure Events can be\naccidental, intentional or self-inflicted.\n",
            "A Injure Event takes place when a Person Entity suffers physical harm. This type of event can be either accidental, intentional, or self-inflicted.",
            'A "Person Entity" can become the victim of physical harm through an "Injure Event," which can either be accidental, intentional, or self-inflicted.',
            '"An Injure Event takes place when a Person Entity sustains physical harm. This can be either accidental, intentional, or self-inflicted."',
            'A "Injure Event" takes place when a "Person Entity" sustains physical harm. These events can be unintentional, deliberate, or self-inflicted.',
        ]
    },
    "ace_investorshareholder": {
        "en": [
            "InvestorShareholder captures the relationship between an agent (Person, Organization, or GPE) and an\nOrganization in which the agent has invested or in which the agent owns shares/stock. Please note that\nagents may invest in GPEs.\n",
            'The term "InvestorShareholder" refers to the connection between an individual or entity that has invested in or owns shares of a particular organization. This relationship is applicable to both natural persons and legal entities, such as corporations or partnerships. It is important to note that investors can also own shares in GPEs (Global Public Entreprises).',
            'The term "InvestorShareholder" refers to the connection between an individual or entity that has invested in or owns shares of an organization. This connection encompasses all agents, including people, companies, and other legal entities. It is important to note that agents may also invest in other legal entities, such as General Partnerships and Entities.',
            '"InvestorShareholder refers to the connection between an individual or entity that has invested in a particular organization or owns shares/stock in it, where the investment may be in the form of a GPE."',
            'The term "InvestorShareholder" refers to the connection between an individual or entity that has invested in or owns shares of a particular organization. This relationship encompasses both people and organizations as potential investors or shareholders. It is worth noting that agents, regardless of whether they are individuals or other organizations, may choose to invest in or acquire ownership of shares in a GPE (Group of People and/or Entities).',
        ]
    },
    "ace_jobtitle": {
        "en": [
            "A JobTitle value refers to the name of the job or position of a Person entity in a Organization. For\nexample: 'co-chief executive', 'move coordinator', 'interim ED', ...\n",
            "The JobTitle value signifies the designation or position held by an individual within an Organization. Examples include 'co-chief executive', 'move coordinator', 'interim ED', and so on.",
            'A JobTitle refers to the designation of the occupation or position held by an individual within an Organization. This may include titles such as "co-chief executive," "move coordinator," or "interim ED."',
            "A JobTitle refers to the designation of the occupation or post held by an individual in an Organization. This can include titles such as 'co-chief executive', 'move coordinator', 'interim ED', and so on.",
            "A JobTitle refers to the designation of the occupation or position held by an individual within an Organization. Examples of JobTitle include 'co-chief executive', 'move coordinator', 'interim ED', and so on.",
        ]
    },
    "ace_justiceevent": {
        "en": [
            "A JusticeEvent refers to any judicial action such as: arresting, jailing, releasing, granting parole,\ntrial starting, hearing, charging, indicting, suing, convicting, sentencing, fine, executing,\nextraditing, adquiting, appealing or pardoning a Person entity.\n",
            "A JusticeEvent refers to any legal proceeding involving a Person entity, such as arresting, detaining, releasing, granting parole, initiating a trial, holding a hearing, charging, indicting, suing, convicting, sentencing, imposing a fine, executing, extraditing, adjudicating, appealing, or granting a pardon.",
            "A JusticeEvent refers to any legal proceeding involving a Person entity, such as arrest, imprisonment, release, parole, trial, hearing, charging, indictment, lawsuit, conviction, sentencing, fine, execution, extradition, acquittal, appeal, or pardon.",
            "A JusticeEvent is any legal proceeding that involves taking action against a person, such as arresting, imprisoning, releasing, granting parole, initiating a trial, holding a hearing, bringing charges, indicting, suing, convicting, imposing a sentence, levying a fine, carrying out an execution, extraditing, acquitting, appealing, or granting a pardon to an individual.",
            "A JusticeEvent refers to any legal proceeding involving a Person entity, including actions such as arrest, imprisonment, release, parole, trial initiation, hearing, charging, indictment, lawsuit, conviction, sentencing, fine, execution, extradition, acquittal, appeal, or pardon.",
        ]
    },
    "ace_lastingpersonal": {
        "en": [
            "Lasting-Personal captures relationships that meet the following conditions: (1) The relationship must\ninvolve personal contact (or a reasonable assumption thereof). (2) There must be some indication or\nexpectation that the relationship exists outside of a particular cited interaction. Both arguments\nmust be entities of type Person.\n",
            '"Lasting-Personal is defined as a relationship that involves personal contact or a reasonable assumption of such contact, and where there is evidence or expectation that the relationship exists beyond a specific cited interaction. Both parties involved must be classified as type Person."',
            '"Lasting-Personal refers to relationships that meet certain criteria. Firstly, there must be personal contact or a reasonable assumption of it. Secondly, there must be evidence or expectation that the relationship exists beyond a specific cited interaction. Both the relationship and the indication or expectation of it must be classified as Person entities."',
            "Lasting-Personal is a concept that refers to relationships between individuals that meet certain criteria. These relationships must involve personal contact or a reasonable assumption of such contact, and there must be some indication or expectation that the relationship exists beyond a specific cited interaction. Both the individual and the relationship must be considered entities of type Person in order to qualify as a Lasting-Personal relationship.",
            "Lasting-Personal refers to relationships that meet certain criteria. These relationships must involve personal contact or a reasonable assumption of such contact. Additionally, there must be some indication or expectation that the relationship exists beyond a specific cited interaction. Both of these conditions must be applied to entities of type Person.",
        ]
    },
    "ace_lifeevent": {
        "en": [
            "A LifeEvent occurs whenever a Person Entity borns, dies, gets married, divorced or gets injured.",
            "A LifeEvent is triggered whenever a Person Entity experiences a significant milestone in their life, such as being born, dying, getting married, getting divorced, or getting injured.",
            "A LifeEvent occurs when a Person Entity experiences significant milestones in their life, such as birth, death, marriage, divorce, or injury.",
            "A LifeEvent is triggered when a Person Entity experiences significant milestones in their life, such as birth, death, marriage, divorce, or injury.",
            "A LifeEvent is triggered when a Person Entity experiences a significant milestone in their life, such as birth, death, marriage, divorce, or injury.",
        ]
    },
    "ace_located": {
        "en": [
            "The Located relation captures the physical location of an entity. This relation is restricted to\npeople. In other words, `arg1` in Located relations can only be occupied by mentions of Entities of\ntype Person.\n",
            'The "Located" relation pertains to the physical location of an entity, and this relation is specific to individuals, meaning that the argument position "arg1" in "Located" relations can only be occupied by references to entities that are classified as people.',
            "The Located relation pertains to the physical location of an individual. This relationship is limited to people and can only be occupied by mentions of entities that are classified as persons.",
            'The "Located" relation pertains to the physical location of an individual. This specific relation is limited to people, meaning that the argument position "arg1" in "Located" relations can only be filled by mentions of entities that are classified as persons.',
            "The Located relation pertains to the physical location of an entity, and this relation is limited to individuals, meaning that the arg1 position in Located relations can only be filled by references to entities of type Person.",
        ]
    },
    "ace_location": {
        "en": [
            "Places defined on a geographical or astronomical basis which are mentioned in a document and do not\nconstitute a political entity give rise to Location entities. These include, for example, the solar\nsystem, Mars, the Hudson River, Mt. Everest, and Death Valley.\n",
            "The document refers to geographical or celestial locations that are not political entities, such as the solar system, Mars, the Hudson River, Mount Everest, and Death Valley, which give rise to Location entities.",
            "The document mentions locations that are geographically or astronomically defined, but are not political entities, and these places are represented by Location entities. Examples of such places include the solar system, Mars, the Hudson River, Mount Everest, and Death Valley.",
            "The document mentions geographical or astronomical locations that are not political entities and they give rise to Location entities. Examples of such places include the solar system, Mars, the Hudson River, Mount Everest, and Death Valley.",
            "The document mentions locations that are not political entities and are geographically or astronomically defined. These places create Location entities, such as the solar system, Mars, the Hudson River, Mt. Everest, and Death Valley.",
        ]
    },
    "ace_marry": {
        "en": [
            "Marry Events are official Events, where two people are married under the legal definition.",
            '"Marriage events are formal gatherings where two individuals legally exchange wedding vows."',
            '"Marriage events are formal gatherings where two individuals legally exchange marriage vows."',
            '"Marriage events are formal gatherings in which two individuals legally exchange wedding vows."',
            '"Marriage events are official gatherings where two individuals are legally wedded."',
        ]
    },
    "ace_meet": {
        "en": [
            "A Meet Event occurs whenever two or more Entities come together at a single location and interact with\none another face-to-face. Meet Events include talks, summits, conferences, meetings, visits, and any\nother Event where two or more parties get together at some location.\n",
            "A meet event takes place when two or more entities gather at a single location and engage in direct interaction with one another. Such events include talks, conferences, summits, meetings, visits, and any other occasion where multiple parties come together at a specified place.",
            "A Meet Event takes place when multiple Entities gather at a single location and engage in direct face-to-face interaction. Such events may include gatherings for talks, conferences, meetings, visits, and any other occasion where two or more parties come together at a specific place.",
            "A Meet Event takes place when two or more Entities gather at a single location and engage in direct face-to-face interaction. Such events may include conferences, summits, talks, meetings, visits, and any other gathering where multiple parties come together at a specified place.",
            "A Meet Event takes place when two or more Entities gather at a single location to engage in face-to-face interactions with one another. This type of event encompasses a range of gatherings, such as conferences, summits, meetings, visits, and any other situation where multiple parties come together at a designated place.",
        ]
    },
    "ace_membership": {
        "en": [
            "Membership captures the relationship between an agent and an organization of which the agent is a\nmember. Organizations and GPEs can be members of other Organizations (such as NATO or the UN).\n",
            '"The concept of membership pertains to the bond between an individual and a group or organization, of which they are a part. This bond can extend to organizations being members of other organizations, such as NATO or the United Nations."',
            '"Membership refers to the connection between an individual and a group of which they are a part. This connection can extend to organizations being members of other organizations, such as NATO or the United Nations."',
            '"Membership refers to the connection between an individual and a group of which they are a part. Groups and organizations can also be members of other groups or organizations, such as NATO or the United Nations."',
            '"Membership refers to the connection between an individual and a group or entity of which they are a part. This connection can extend to organizations being members of other organizations, such as NATO or the United Nations."',
        ]
    },
    "ace_mergeorg": {
        "en": [
            "A MergeOrg Event occurs whenever two or more Organization Entities come together to form a new\nOrganization Entity. This Event applies to any kind of Organization, including government agencies. It\nalso includes joint venture.\n",
            "A MergeOrg Event happens when two or more organization entities combine to form a new organization entity. This event applies to all types of organizations, including government agencies, and also covers joint ventures.",
            '"A MergeOrg Event takes place when two or more Organization Entities unite to create a new Organization Entity. This event applies to all types of organizations, including government agencies and joint ventures."',
            "A MergeOrg Event takes place when two or more Organization Entities unite to form a new Organization Entity. This event applies to all types of organizations, including government agencies, and also encompasses joint ventures.",
            "A MergeOrg Event takes place when two or more Organization Entities unite to create a new Organization Entity. This Event applies to all types of organizations, including government agencies, and also covers joint ventures.",
        ]
    },
    "ace_movementevent": {
        "en": [
            "A TransportEvent occurs whenever an Artifact (Weapon or Vehicle) or a Person is moved from one Place\n(GPE, Facility, Location) to another. This event requires the explicit mention of the Artifact or\nPerson.\n",
            '"A TransportEvent takes place when an object, either an Artifact (such as a weapon or vehicle) or a person, is moved from one location (Place) to another. This event must specifically identify the object being transported."',
            "A TransportEvent takes place when an object, either an Artifact (such as a weapon or vehicle) or a Person, is moved from one location (Place) to another. This occurrence necessitates the explicit mention of the specific object being transported.",
            "A TransportEvent happens whenever an object (such as a weapon or vehicle), or a person is moved from one location to another. This movement requires the explicit mention of the object or person being moved.",
            "A TransportEvent takes place whenever an object, either a weapon or vehicle, or a person is moved from one specific location to another. This event necessitates the explicit identification of the object or person being moved.",
        ]
    },
    "ace_near": {
        "en": [
            "Near indicates that an entity is explicitly near another entity, but neither entity is a part of the\nother or located in/at the other.\n",
            '"Near signifies that an entity is in close proximity to another entity, but neither entity is a constituent of the other or situated inside/at the other."',
            'The term "near" suggests that one entity is in close proximity to another entity, but neither entity is a constituent part of the other or situated within the other.',
            '"Near suggests that one entity is in close proximity to another entity, but neither of them are a part of each other or positioned within the other."',
            '"Near signifies that an entity is in close proximity to another entity, but neither entity is an integral part of the other or situated within the other."',
        ]
    },
    "ace_nominate": {
        "en": [
            "A Nominate Event occurs whenever a Person is proposed for a StartPosition Event by the appropriate\nPerson, through official channels.\n",
            '"A Nominate Event takes place when a person is put forward as a candidate for a StartPosition Event by an appropriate person through official channels."',
            "A nomination event takes place when a person is suggested for a start position event by the appropriate person, through official channels.",
            '"The Nominate Event takes place when an individual is put forth as a candidate for a StartPosition Event by a suitable person, via official communication channels."',
            "A nomination event takes place when a person is proposed for a start position event by the appropriate person, through official channels.",
        ]
    },
    "ace_numeric": {
        "en": [
            "A Numeric value refers to relevant numbers, amounts, etc. For example: 'billions of dollars', '50\npercent', '100%', ...\n",
            'A numerical value pertains to specific digits, amounts, and the like. Some examples include "billions of dollars," "50 percent," and "100%."',
            'A numeric value is a reference to numerical amounts, such as "billions of dollars," "50 percent," or "100%."',
            'A numeric value is a reference to a specific quantity or amount, such as "billions of dollars," "50 percent," or "100%." These values are used to quantify and describe various phenomena.',
            'A numerical value pertains to specific numbers, amounts, and the like. Examples include "billions of dollars," "50 percent," and "100%."',
        ]
    },
    "ace_organization": {
        "en": [
            "Each organization or set of organizations mentioned in a document gives rise to an entity of type\nOrganization. Typical examples are businesses, government units, sports teams, and formally organized\nmusic groups.\n",
            "Every entity mentioned in a document is of type Organization and arises from an organization or group of organizations. Examples include businesses, government agencies, sports teams, and formally organized musical groups.",
            "Every entity mentioned in a document is of type Organization and arises from a particular organization or collection of organizations, such as businesses, government agencies, sports teams, and formally organized music groups.",
            "The mention of an organization or collection of organizations in a document results in the creation of an entity of type Organization. Examples of such entities include corporations, government agencies, sports teams, and groups that have been formally organized for music performance.",
            "The mention of an organization or group of organizations in a document results in the creation of an entity of type Organization. Examples of such entities include businesses, government agencies, sports teams, and formally organized musical groups.",
        ]
    },
    "ace_organizationaffiliationrelation": {
        "en": [
            "The OrganizationAffiliation Relation describes the relations between a Person (or other Organizations)\nand a related Organization. This relation includes: employment, ownership, founder, student or alumn,\nsport affiliation, inverstor or shareholder and membership relations.\n",
            "The OrganizationAffiliation Relation pertains to the connections between a person or other organizations and a related organization. This connection encompasses employment, ownership, being a founder, being a student or alumnus, having a sports affiliation, being an investor or shareholder, and having membership relations.",
            "The OrganizationAffiliation Relation pertains to the connections between a person or organization and another related organization. This association encompasses various types of relationships, including employment, ownership, founding, student or alumni status, sports affiliation, investor or shareholder ties, and membership.",
            "The OrganizationAffiliation Relation pertains to the connections between a person or other organizations and a related organization. This association encompasses employment, ownership, being a founder, being a student or alumnus, participating in sports, being an investor or shareholder, and having membership relations.",
            "The OrganizationAffiliation Relation pertains to the connections between a person or other organizations and a related organization. This connection encompasses employment, ownership, founding, being a student or alumnus, participating in sports, being an investor or shareholder, and having membership status.",
        ]
    },
    "ace_orglocationorigin": {
        "en": [
            "OrgLocationOrigin captures the relationship between an organization and the Location or GPE where it is\nlocated, based, or does business. Note: Subsidiary trumps this relation for government organizations.\n",
            '"OrgLocationOrigin defines the connection between an organization and the Location or GPE where it operates, resides, or conducts its activities. It is important to note that, for government entities, the relationship with the parent organization takes precedence over the relationship with the Location or GPE."',
            'The "OrgLocationOrigin" attribute signifies the connection between an organization and the "Location" or "GPE" (Global Policy Entity) where it is situated, based, or operates. It is worth noting that, for government organizations, a "Subsidiary" takes precedence over this relationship.',
            '"The OrgLocationOrigin attribute defines the connection between an organization and the Geographic Political Entity (GPE) or location where it is situated, headquartered, or operates." Note: In the case of government organizations, a subsidiary has higher priority in relation to this relationship.',
            '"The OrgLocationOrigin attribute represents the connection between an organization and the location or General Plot Entity (GPE) where it operates, is based, or conducts business. It is important to note that for government organizations, the subsidiary relationship takes precedence over this association."',
        ]
    },
    "ace_ownership": {
        "en": [
            "Ownership captures the relationship between a Person and an Organization owned by that Person. If the\n`arg2` is not an Organization, use the Agent-Artifact relation.\n",
            '"The concept of ownership refers to the connection between an individual and an organization that they own. If the argument passed in as `arg2` is not an organization, then the relationship between the individual and the Agent-Artifact should be considered."',
            '"The concept of ownership refers to the connection between an individual and an organization that they own. If the second argument (`arg2`) is not an organization, then the relationship should be represented as an agent-artifact association."',
            "The concept of ownership refers to the connection between an individual and an organization that they own. If the second argument (`arg2`) is not an organization, then the relationship between the individual and the artifact should be considered as an agent-artifact association.",
            "The concept of ownership pertains to the connection between an individual and an organization that they own. If the argument passed in (arg2) is not an organization, then the relationship between the individual and the artifact should be considered as the Agent-Artifact relation.",
        ]
    },
    "ace_pardon": {
        "en": [
            "A Pardon Event occurs whenever a head-of-state or their appointed representative lifts a sentence\nimposed by the judiciary.\n",
            "A pardon event takes place when the head of state or their designated representative overturns a sentence that was handed down by the judiciary.",
            "A pardon event takes place when the head of state or their designated representative annuls a sentence that was handed down by the judiciary.",
            "A pardon event takes place when a head of state or their designated representative nullifies a sentence imposed by the judiciary.",
            '"A Pardon Event takes place when the head of state or a designee of the head of state rescinds a sentence that was imposed by the judiciary."',
        ]
    },
    "ace_partwholerelation": {
        "en": [
            "The PartWhole Relation refers to the semantic relation between two entities that are parts of a larger\nwhole or vice versa. For example, the relation between a country and its states, or between a company\nand its subsidiaries, are instances of PartWhole relations.\n",
            "The PartWhole Relation pertains to the semantic connection between two entities that are either parts of a larger whole or the whole itself. This connection can be seen in relationships such as that between a nation and its provinces, or between a business and its subsidiaries. These are all instances of PartWhole relations.",
            "The PartWhole Relation pertains to the semantic connection between two entities that are constituents of a larger whole, or the reverse. Illustrations of this relation include the bond between a nation and its territories, or between a firm and its subsidiaries.",
            "The PartWhole Relation pertains to the semantic relationship that exists between two entities that are either parts of a larger whole or the whole is composed of them. This relationship can be observed in cases such as a country and its states, or a corporation and its subsidiaries.",
            "The PartWhole Relation is a semantic relation that exists between two entities that are either parts of a larger whole or the whole is composed of them. This relationship can be seen in examples such as the one between a country and its states, or a company and its subsidiaries.",
        ]
    },
    "ace_person": {
        "en": [
            'Each distinct person or set of people mentioned in a document refers to an entity of type Person. For\nexample, people may be specified by name ("John Smith"), occupation ("the butcher"), family relation\n("dad"), pronoun ("he"), etc., or by some combination of these.',
            "The individuals or groups mentioned in a document are classified as entities of type Person. This includes individuals identified by their name, occupation, familial relationship, pronoun, or a combination of these factors.",
            'Every individual or group of individuals mentioned in a document is classified as a Person entity. This category encompasses all references to people, including those identified by name ("John Smith"), profession ("the butcher"), familial relationship ("dad"), pronoun ("he"), or any combination of these characteristics.',
            "Every individual or group mentioned in a text is a Person entity, which can be identified by their name, job title, family relationship, pronoun, or a combination of these characteristics.",
            'Every person or group of people mentioned in a text is considered to be an entity of type Person. Examples of how people are referred to include by name ("John Smith"), occupation ("the butcher"), family relationship ("dad"), pronoun ("he"), or a combination of these.',
        ]
    },
    "ace_personalsocialrelation": {
        "en": [
            "The Personal-Social Relation describe the relationship between people. Both arguments must be entities\nof type Person. Please note: The arguments of these Relations are not ordered. The Relations are\nsymmetric.\n",
            "The Personal-Social Relation pertains to the connection between individuals. Both arguments must be of the type Person, and it should be noted that the arguments of these Relations are not arranged in a specific order. Additionally, these Relations are symmetric.",
            "The Personal-Social Relationship pertains to the connection between individuals. Both arguments must be representatives of the Person entity. Please be aware: The arguments of these Relations are not arranged in any specific order. The Relations are symmetrical.",
            "The Personal-Social Relation pertains to the connection between individuals. Both arguments must be entities of the type Person, and it should be noted that the arguments of these Relations are not arranged in any particular order. Additionally, these Relations are symmetric.",
            '"The Personal-Social Relation pertains to the connection between individuals. Both components are of the type Person. Please be aware: The components of these Relations are not arranged in a specific order. The Relations are symmetric."',
        ]
    },
    "ace_personellevent": {
        "en": [
            "A PersonellEvent occurs when a Person entity changes its job position (JobTitle entity) with respect an\nOrganization entity. It includes when a person starts working, ends working, changes offices within,\ngets nominated or is elected for a position in a Organization.\n",
            "A PersonEvent takes place when a Person entity undergoes a change in its job position, which is represented by a JobTitle entity in relation to an Organization entity. This includes instances such as when a person begins employment, concludes their employment, transfers to a different office within the organization, is appointed or elected to a position within the organization.",
            "A Personnel Event occurs when a person's job position within an organization changes. This can include when an individual begins working, ends their employment, changes offices within the organization, is nominated or elected for a position, or is appointed to a new job title.",
            "A Personnel Event takes place when a Person entity undergoes a change in its job position, as represented by a JobTitle entity, in relation to an Organization entity. This may involve the individual starting or ending their employment, transferring to a different office within the organization, being nominated or elected to a specific role within the organization.",
            "A PersonellEvent takes place when a Person entity undergoes a change in its job position, which is represented by a JobTitle entity in relation to an Organization entity. This can include instances such as when a person begins working, ends their employment, switches offices within the organization, is appointed or elected to a position within the organization.",
        ]
    },
    "ace_phonewrite": {
        "en": [
            "A PhoneWrite Event occurs when two or more people directly engage in discussion which does not take\nplace 'face-to-face'. To make this Event less open-ended, we limit it to written or telephone\ncommunication where at least two parties are specified.\n",
            "A PhoneWrite Event refers to a conversation that takes place through written or telephone communication between two or more people, who are not physically facing each other. In order to make this type of event more structured and focused, we have decided to specify that it involves at least two parties who are participating through written or telephone communication.",
            "A PhoneWrite Event refers to a conversation that takes place through written or telephone communication, involving at least two parties.",
            "A PhoneWrite Event refers to a conversation that takes place through written or telephone communication between two or more people who are not physically face-to-face. To make this type of event more structured and focused, we restrict it to instances where there are at least two parties involved in the communication.",
            "A PhoneWrite Event refers to a conversation that takes place through written or telephone communication, involving at least two participants who are not physically facing each other. To make this type of event more structured, we restrict it to instances where the communication is exclusively between two or more people.",
        ]
    },
    "ace_physicalrelation": {
        "en": [
            "The Physical Relation captures the physical location relation of entities such as: a Person entity\nlocated in a Facility, Location or GPE; or two entities that are near, but neither entity is a part of\nthe other or located in/at the other.\n",
            "The Physical Relation refers to the relationship between entities that are concerned with their physical location. This includes entities such as a Person entity that is situated in a Facility, Location, or General Practice (GPE), or two entities that are in close proximity to each other, but neither of them is a part of the other or located within the other.",
            "The Physical Relation refers to the relationship between entities that indicates their physical location. This includes instances where a Person entity is situated in a particular Facility, Location, or General Practice Entity (GPE), or when two entities are in close proximity to each other, but neither is a part of the other or located within the other.",
            "The Physical Relation refers to the physical location connections between various entities, such as a Person entity being situated within a Facility, Location, or GPE; or two entities that are in close proximity to each other, but neither entity is a part of the other or located within the other.",
            "The Physical Relation refers to the physical location relationship between different entities, including individuals who are situated in specific facilities, locations, or geographic points of interest (GPEs), or two entities that are in close proximity to each other, but neither of them is a part of the other or located within the other.",
        ]
    },
    "ace_releaseparole": {
        "en": [
            "A Release Event occurs whenever a state actor (GPE, Organization subpart, or Person representative)\nends its custody of a Person Entity.\n",
            "A Release Event takes place when a state actor (such as GPE, Organization subpart, or a Person representative) relinquishes their custody of a Person Entity.",
            "A release event takes place when a state actor (such as a governmental pension entity, an organization subpart, or a person representative) no longer has custody of a person entity.",
            "A release event takes place when a state actor, such as a governmental pension entity, an organization subpart, or a person representative, relinquishes their custody of a person entity.",
            "A release event takes place when a state actor, such as a General Partnership or an Organization subpart, relinquishes its control over a Person Entity.",
        ]
    },
    "ace_sentence": {
        "en": [
            "A Sentence value refers to sentences decided by a court or judge for a specific crime. For example:\n'124 years in prison', 'a sentence', 'death'...\n",
            "A sentence value refers to the sentences imposed by a court or judge for a specific offense. Some examples of sentence values include a prison term of 124 years, a sentence of imprisonment, or the death penalty.",
            'A sentence value refers to the penalties imposed by a court or judge for a particular offense. Examples of such sentences include "124 years in prison," "a sentence," and "death."',
            'A "Sentence value" refers to a determination made by a court or judge regarding a specific criminal offense. Examples of sentence values include sentences such as "124 years in prison," "a sentence," or "death."',
            'A sentence value is a term used to describe the verdict handed down by a judge or court for a specific offense. Examples of sentence values include prison terms such as "124 years," "a sentence," or "death."',
        ]
    },
    "ace_sentenceact": {
        "en": [
            "A SentenceAct Event takes place whenever the punishment (particularly incarceration) for the Defendant\nof a Try Event is issued by a state actor (a GPE, an Organization subpart or a Person representing\nthem)\n",
            "An SentenceAct Event occurs when the penalty, specifically imprisonment, for the defendant of a Trial Event is imposed by a state authority, such as a Governmental Participant Entity, an Organization subpart, or a representative of either of them.",
            "A SentenceAct Event occurs when a state actor, such as a GPE, organization subpart, or person representing them, issues the punishment, particularly incarceration, for the Defendant of a Try Event.",
            '"A SentenceAct Event occurs when the penalty, specifically imprisonment, for a Defendant in a Trial Event is imposed by a government agent, such as a General Purpose Entity, an Organization subunit, or a person representing them."',
            "A SentenceAct Event occurs when the penalty, specifically imprisonment, for a Defendant in a Try Event is imposed by a state actor, such as a GPE, an Organization subpart, or a person representing them.",
        ]
    },
    "ace_sportsaffiliation": {
        "en": [
            "Sports-Affiliation captures the relationship between a player, coach, manager, or assistant and his or\nher affiliation with a sports organization (including sports leagues or divisions as well as\nindividual sports teams).\n",
            '"Sports-Affiliation refers to the connection between a player, coach, manager, or assistant and their association with a sports club or league, as well as individual sports teams."',
            "The Sports-Affiliation object represents the connection between a player, coach, trainer, or assistant and their association with a sports organization, encompassing sports leagues, divisions, and individual teams.",
            "The Sports-Affiliation table records the connection between a player, coach, trainer, or assistant and their association with a sports club (encompassing sports associations or divisions as well as individual sports teams).",
            '"Sports-Affiliation refers to the bond that exists between a player, coach, manager, or assistant and their connection to a sports club or league."',
        ]
    },
    "ace_startorg": {
        "en": [
            "A StartOrg Event occurs whenever a new Organization is created.",
            "A new organization is established with the occurrence of a StartOrg Event.",
            '"The creation of a new Organization triggers a StartOrg Event."',
            '"The occurrence of a StartOrg Event is triggered whenever a new Organization is established."',
            'A "StartOrg Event" takes place whenever a fresh "Organization" is established.',
        ]
    },
    "ace_startposition": {
        "en": [
            "A StartPosition Event occurs whenever a Person Entity begins working for (or changes offices within) an\nOrganization or GPE. This includes government officials starting their terms, whether elected or\nappointed.\n",
            "A StartPosition Event takes place when a Person Entity starts working for, or transfers to a different office within, an Organization or Government Position Entity (GPE). This includes instances when government officials commence their tenures, whether they were elected or appointed.",
            '"The StartPosition Event takes place when a Person Entity commences employment with, or transitions to a new office within, an Organization or GPE. This includes government officials who are starting their tenure, whether they were elected or appointed."',
            "A StartPosition Event takes place when a Person Entity starts working for or changes offices within an Organization or GPE. This includes government officials who are starting their terms, whether they were elected or appointed.",
            "The StartPosition Event takes place when a Person Entity commences working for or transfers to a different department within an Organization or GPE. This includes government officials who are starting their tenure, whether they were elected or appointed.",
        ]
    },
    "ace_studentalum": {
        "en": [
            "StudentAlum captures the relationship between a Person and an educational institution the Person\nattends or attended.\n",
            '"StudentAlum is a term that describes the connection between an individual and a school or university they have attended or are currently attending."',
            '"StudentAlum defines the connection between a individual and a educational establishment that they or previously attended."',
            '"StudentAlum defines the connection between an individual and a school they have attended or are currently attending."',
            '"StudentAlum refers to the connection between an individual and a educational establishment that they are associated with, whether they are currently enrolled or have attended in the past."',
        ]
    },
    "ace_subsidiary": {
        "en": [
            "Subsidiary captures the ownership, administrative, and other hierarchical relationships between\norganizations and between organizations and GPEs.\n",
            '"A subsidiary refers to the ownership, administrative, and other relationships that exist between different organizations and between organizations and GPEs."',
            '"A subsidiary represents the ownership, administrative, and other structural relationships that exist between companies and between companies and their parent organizations."',
            '"A subsidiary represents the ownership, administrative, and other structural relationships that exist between organizations and between organizations and Global Public Entreprises."',
            "The subsidiary encompasses the ownership, operational, and regulatory relationships that exist among companies and between them and their parent organizations.",
        ]
    },
    "ace_sue": {
        "en": [
            "A Sue Event occurs whenever a court proceeding has been initiated for the purposes of determining the\nliability of a Person, Organization or GPE accused of committing a crime or neglecting a commitment.\n",
            "A Sue Event takes place when legal proceedings are initiated with the aim of establishing the liability of a person, organization, or GPE (government, public organization, or governmental agency) accused of committing a crime or neglecting a duty.",
            "A Sue Event takes place when legal proceedings are initiated with the aim of establishing the responsibility of a person, organization, or GPE (General Public Entity) accused of committing a crime or failing to fulfill a commitment.",
            "A Sue Event takes place when legal proceedings are initiated with the goal of establishing the responsibility of an individual, organization, or governmental public entity that is accused of committing a crime or failing to fulfill a commitment.",
            "A Sue Event takes place whenever legal proceedings are initiated with the objective of establishing the responsibility of an individual, organization, or GPE (Government, Public Authority or Entity) accused of committing a crime or neglecting a commitment.",
        ]
    },
    "ace_time": {
        "en": [
            "A Time value refers to a specific time frame. Usually known as time expressions. For example: '4\nyears', 'today', 'December', 'future', ...\n",
            'A time value is a designation that refers to a specific period of time, often denoted as time expressions. Some examples of time expressions include "4 years," "today," "December," and "future."',
            'A time value is a designation that refers to a specific period of time, often denoted as time expressions. Examples of time values include "4 years," "today," "December," and "future."',
            'A Time value is a designation that pertains to a particular time frame, often referred to as a time expression. Examples of time values include "4 years," "today," "December," and "future."',
            'A time value is a specific period of time, often referred to as a time expression, and may include designations such as "4 years," "today," "December," or "future."',
        ]
    },
    "ace_transactionevent": {
        "en": [
            "A TransactionEvent refers to buying, selling, loaning, borrowing, giving, or receving of Artifacts or\nOrganizations; or giving, receiving, borrowing, or lending Money.\n",
            "A TransactionEvent involves the exchange or transfer of Artifacts or Organizations, as well as the exchange or transfer of money. This can include buying, selling, loaning, borrowing, giving, or receiving these items or funds.",
            "A TransactionEvent involves the exchange of Artifacts or Organizations through buying, selling, loaning, borrowing, giving, or receiving; as well as the exchange of Money through giving, receiving, borrowing, or lending.",
            "A TransactionEvent involves the exchange of Artifacts or Organizations through buying, selling, loaning, borrowing, giving, or receiving, as well as the exchange of Money through giving, receiving, borrowing, or lending.",
            '"A TransactionEvent involves the exchange or transfer of Artifacts or Organizations, as well as the exchange or transfer of money, either through buying, selling, loaning, borrowing, or gifting."',
        ]
    },
    "ace_transfermoney": {
        "en": [
            "TransferMoney Events refer to the giving, receiving, borrowing, or lending money when it is not in the\ncontext of purchasing something. The canonical examples are: (1) people giving money to organizations\n(and getting nothing tangible in return); and (2) organizations lending money to people or other orgs.\n",
            "The TransferMoney Events refer to instances where money is exchanged without a direct transaction involving the purchase of a product or service. This includes situations where individuals or organizations donate money to charities or receive loans from financial institutions.",
            '"TransferMoney Events involve the exchange of money without the context of a purchase. This includes instances such as individuals donating money to organizations without receiving anything in return, and organizations lending money to individuals or other organizations."',
            'The term "TransferMoney Events" refers to instances where money is exchanged without a direct transaction involving the purchase of a product or service. Examples of such events include donations made to organizations, as well as loans provided to individuals or other organizations.',
            "The TransferMoney Events refer to instances where money is transferred without it being tied to a purchase. Examples of such events include individuals donating money to organizations without receiving any tangible goods in return, and organizations lending money to individuals or other organizations.",
        ]
    },
    "ace_transferownership": {
        "en": [
            "TransferOwnership Events refer to the buying, selling, loaning, borrowing, giving, or receiving of\nartifacts or organizations.\n",
            '"TransferOwnership Events encompass the acquisition and disposal of both physical objects and entities, such as through purchasing, selling, lending, borrowing, donating, or accepting ownership."',
            '"TransferOwnership Events encompass the acquisition and disposal of both physical objects and entities, including but not limited to purchasing, selling, lending, borrowing, donating, and accepting ownership of these items or entities."',
            'The "TransferOwnership Events" pertain to the acquisition or disposition of artifacts or entities through processes such as purchasing, selling, lending, borrowing, donating, or accepting ownership.',
            '"TransferOwnership Events encompass the acquisition and disposition of both physical objects and entities, such as the process of purchasing, selling, lending, borrowing, granting, or accepting ownership of various assets or establishments."',
        ]
    },
    "ace_transport": {
        "en": [
            "A Transport Event occurs whenever an Artifact (Weapon or Vehicle) or a Person is moved from one Place\n(GPE, Facility, Location) to another.\n",
            "A transport event takes place when an object, either an artifact such as a weapon or vehicle, or a person, is relocated from one location to another.",
            "A transport event takes place when an artifact, such as a weapon or vehicle, or a person is relocated from one place to another.",
            "A transport event happens whenever an artifact (such as a weapon or vehicle) or a person is relocated from one location (place) to another.",
            "A transport event takes place whenever an artifact, such as a weapon or vehicle, or a person is relocated from one place to another.",
        ]
    },
    "ace_trialhearing": {
        "en": [
            "A Trial Event occurs whenever a court proceeding has been initiated for the purposes of determining the\nguilt or innocence of a Person, Organization or GPE accused of committing a crime.\n",
            "A trial event takes place whenever legal proceedings are initiated with the objective of determining whether a person, organization, or GPE is guilty or innocent of a crime they are accused of committing.",
            "A trial event takes place when a legal proceeding has been initiated to determine whether a person, organization, or governmental public entity is guilty or not of committing a crime.",
            "A trial event takes place when legal proceedings are initiated to determine the guilt or innocence of a person, organization, or governmental public entity that is accused of committing a crime.",
            "A trial event takes place when a legal proceeding has been initiated with the aim of determining whether a person, organization, or governmental entity is guilty or not of committing a crime.",
        ]
    },
    "ace_userownerinventormanufacturer": {
        "en": [
            "This Relation applies when an agent owns an artifact, has possession of an artifact, uses an artifact,\nor caused an artifact to come into being. Note: if `arg2` is an Organization, use Ownership relation\n(arg1=PER) or Subsidiary relation (arg1=ORG or GPE).\n",
            "The ownership, possession, use, and creation of an artifact are all covered by this relation, and if the arg2 is an organization, then either the ownership relation (arg1=PER) or the subsidiary relation (arg1=ORG or GPE) should be used.",
            "The following relation applies when an individual possesses a commodity, exercises control over it, utilizes it, or brought it into existence. It is important to note that if the second element (arg2) is an organization, then either the ownership relation (arg1=PER) or the subsidiary relation (arg1=ORG or GPE) should be used instead.",
            "This Relation applies when an individual possesses an item, utilizes an item, or created an item. Note: if the second entity is an organization, then a ownership or subsidiary relationship should be applied, where the first entity is either a person or an organization.",
            "\"When an agent possesses, utilizes, or has created an artifact, they are associated with it through this particular relationship. It is important to note that if 'arg2' is an organization, then either the ownership relation (where 'arg1' is an individual) or the subsidiary relation (where 'arg1' is an organization or group of people) should be used instead.\"",
        ]
    },
    "ace_vehicle": {
        "en": [
            "A Vehicle entity refers to vehicles that are used for transportation. The vehicles can transport either\npersons or artifacts. For example: 'car', 'plane', 'cabin', ...\n",
            'The term "Vehicle entity" refers to vehicles that are used for transportation purposes. These vehicles can either transport people or goods, such as cars, planes, and cabins.',
            '"The Vehicle entity is utilized to represent vehicles that are used for transportation. These vehicles can convey either humans or objects, such as automobiles, airplanes, and cabins, among others."',
            "\"The term 'Vehicle entity' refers to vehicles that are utilized for transportation. These vehicles are capable of transporting both humans and objects, such as cars, planes, and cabins.\"",
            "A Vehicle entity represents vehicles utilized for transportation, which can transport either humans or goods. Examples of such vehicles include cars, planes, and cabins.",
        ]
    },
    "ace_weapon": {
        "en": [
            "A Weapon entity refers to instruments that can be used to deal physical damage, destroy something or\nkill someone. For example: 'bomb', 'm-16s', 'missile', ...\n",
            'A Weapon entity denotes objects that are utilized to inflict physical harm, demolish something, or cause fatality. Examples include, but are not limited to: "bomb," "M-16s," "missile," etc.',
            "\"A Weapon entity encompasses instruments that can inflict physical harm, cause destruction, or result in fatalities. Examples of such weapons include 'bomb', 'M-16s', 'missiles', and the like.\"",
            '"A Weapon entity is defined as an object that can inflict physical harm, cause destruction, or result in fatality. Examples of such entities include bombs, M-16s, and missiles."',
            "A Weapon entity refers to objects that can inflict physical harm, cause destruction, or result in fatalities, such as explosives, firearms, and projectiles.",
        ]
    },
}

