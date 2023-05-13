GUIDELINES = {
    "tacred_organizationalternatename": {
        "en": [
            'The OrganizationAlternateName relation encodes any name used to refer to the assigned organization that\nis distinct from the "official"name. Alternate names may include former names, aliases, alternate\nspellings, acronyms, abbreviations, translations or transliterations of names, and any official\ndesignators such as stock ticker code or airline call sign.\n\nVerbalization: {arg1} is also known as {arg2}.\n',
            "The OrganizationAlternateName relation represents any alternate names that are used to refer to the assigned organization, which are different from the official name. These alternate names may include former names, aliases, alternate spellings, acronyms, abbreviations, translations or transliterations of names, and any official designators such as stock ticker code or airline call sign.",
        ]
    },
    "tacred_organizationcityofheadquarters": {
        "en": [
            "The OrganizationCityOfHeadquarters relation encodes the location of the headquarters of the assigned\norganization ath the city, town, or village level. The `arg2` slot must be filled with a city, town,\nor village name.\n\nVerbalization: {arg1} is located in {arg2}.\n",
            "The OrganizationCityOfHeadquarters connection represents the location of the headquarters of the designated organization at the city, town, or village level. The 'arg2' slot must be occupied by a city, town, or village name. Description: {arg1} is stationed in {arg2}.",
        ]
    },
    "tacred_organizationcountryofheadquarters": {
        "en": [
            "The OrganizationCountryOfHeadquarters relation encodes the country in which the headquarters of\nthe assigned organization are located. The `arg2` slot must be filled with a country name.\n\nVerbalization: {arg1} is located in {arg2}.\n",
            "The OrganizationCountryOfHeadquarters relation links the country where the headquarters of the specified organization are situated. The 'arg2' position must be occupied by a country name. Description: {arg1} is situated in {arg2}.",
        ]
    },
    "tacred_organizationdatedissolved": {
        "en": [
            "The OrganizationDateDissolved relation encodes the date on which the assigned organization was\ndissolved. When Companies merge to form a new entity, the original companies should be considered as\ndissolved.\n\nVerbalization: {arg1} dissolved in {arg2}.\n",
            "The OrganizationDateDissolved relation pertains to the date on which the assigned organization was disbanded. When companies merge to form a new entity, it is necessary to regard the original companies as discontinued.",
        ]
    },
    "tacred_organizationdatefounded": {
        "en": [
            "The OrganizationDateFounded relations encodes the date on which the assigned organization was founded.\n\nVerbalization: {arg1} was founded in {arg2}.\n",
            '"The OrganizationDateFounded relation represents the date on which the assigned organization was established."',
        ]
    },
    "tacred_organizationfoundedby": {
        "en": [
            "The OrganizationFoundedBy relation encodes the person, organization or geopolitical (GPE) entity that\nfounded the assigned organization.\n\nVerbalization: {arg1} was founded by {arg2}.\n",
            "The OrganizationFoundedBy relation identifies the individual, entity, or geopolitical organization (GPE) that established the company. Verbalization: {arg1} was established by {arg2}.",
        ]
    },
    "tacred_organizationmember": {
        "en": [
            "The OrganizationMember relation encodes the organizations or geopolitical (GPE) entities that are\nmembers of the assigned organization (the inverse of OrganizationMemberOf). While similar to\nOrganizationSubsidiary, OrganizationMember is different because correct `arg2` fillers are distinct\nentities that are generally capable of autonomously ending their membership with the assigned\norganization.\n\nVerbalization: {arg2} is member of {arg1}.\n",
            "The OrganizationMember relation indicates the membership of organizations or geopolitical entities (GPEs) in a particular organization. Unlike OrganizationSubsidiary, OrganizationMember refers to distinct entities that have the ability to withdraw their membership from the organization they are associated with. In simpler terms, this means that the member organizations or GPEs are capable of leaving the organization they are a part of on their own.",
        ]
    },
    "tacred_organizationmemberof": {
        "en": [
            "The OrganizationMemberOf relation encodes the organizations or geopolitical (GPE) entities of which the\nassigned organization is a member itself (the inverse of OrganizationMember). For the `arg2` slot, the\nassigned organization is a distinct entity from the parent organization and is generally capable of\nautonomously ending the membership relation.\n\nVerbalization: {arg1} is member of {arg2}.\n",
            "The OrganizationMemberOf relation represents the affiliation of an organization with other organizations or geopolitical entities. Unlike the OrganizationMember relation, which indicates that an organization is a member of another organization, the OrganizationMemberOf relation indicates that an organization is a member of another entity. The assigned organization is usually a separate entity from the parent organization and has the capability to end the membership relation independently.",
        ]
    },
    "tacred_organizationnumberofemployeesmembers": {
        "en": [
            "The OrganizationNumberOfEmployeesMembers relation encodes the total number of people who are employed\nby or have membership in the associated organization.\n\nVerbalization: {arg1} employs nearly {arg2} people.\n",
            "The OrganizationNumberOfEmployeesMembers relation represents the total number of individuals who are employed by or hold membership in the relevant organization. Specifically, {arg1} has approximately {arg2} employees.",
        ]
    },
    "tacred_organizationparent": {
        "en": [
            "The OrganizationParent relation encodes the organizations or geopolitical (GPE) entities of which the\nassigned organization is a subsidiary (the inverse of OrganizationSubsidiary). While similar to\nOrganizationMemberOf, OrganizationParent is different because the assigned organization is subsumed\nunder the parent organization(s), rather than being a distinct entity.\n\nVerbalization: {arg1} is a subsidiary or branch of {arg2}.\n",
            "The OrganizationParent relation represents the higher-level organization or geopolitical entity of which the assigned organization is a part. This is distinct from OrganizationMemberOf, as the assigned organization is integrated into the parent organization rather than being a separate entity. In other words, {arg1} is a subsidiary or branch of {arg2}.",
        ]
    },
    "tacred_organizationpoliticalreligiousaffiliation": {
        "en": [
            "The OrganizationPoliticalReligiousAffiliation relation encodes the ideological groups with which\nthe organization is associated.\n\nVerbalization: {arg1} has political or religious affiliation with {arg2}.\n",
            "The OrganizationPoliticalReligiousAffiliation relation is used to indicate the political or religious groups that an organization is associated with.",
        ]
    },
    "tacred_organizationshareholders": {
        "en": [
            "The OrganizationShareholders relation encodes any organization, person, or geopolitical (GPE) entity\nthat holds shares (majority or not) of the organization. Former shareholders are acceptable\nresponses.\n\nVerbalization: {arg2} holds shares in {arg1}.\n",
            '"The OrganizationShareholders relation represents any organization, person, or geopolitical entity that possesses shares (whether it be a majority or minority stake) in the organization. Former shareholders are also considered valid responses."',
        ]
    },
    "tacred_organizationstateorprovinceofheadquarters": {
        "en": [
            "The OrganizationStateOrProvinceOfHeadquarters relation encodes the location of the headquarters of the\nassigned organization at the state or province level. The `arg2` slot must be filled with a state or\nprovince name.\n\nVerbalization: {arg1} is located in {arg2}.\n",
            "In summary, the OrganizationStateOrProvinceOfHeadquarters connection defines the location of the head office of the assigned organization at the state or province level by specifying the state or province name in the 'arg2' slot.",
        ]
    },
    "tacred_organizationsubsidiary": {
        "en": [
            "The OrganizationSubsidiary relation encodes the organizations that are subsidiaries of the\nassigned organization (the inverse of OrganizationParent). Subsidiaries are subsumed under the\nassigned organization, rather than being distinct entities.\n\nVerbalization: {arg2} is a subsidiary or branch of\n{arg1}.\n",
            "The OrganizationSubsidiary relation represents the organizations that are under the ownership or control of the specified organization, which is the inverse of OrganizationParent. These subsidiaries are considered as a part of the assigned organization, rather than being separate entities.",
        ]
    },
    "tacred_organizationtopmembersemployees": {
        "en": [
            "The OrganizationTopMembersEmployees relation encodes the persons in high-level, leading positions at\nthe assigned organization. Although the definition of 'leading position'is relatively broad, all\nTop Member/Employee positions should imply a level of decidion-making authority over the entire\nassigned organization.\n\nVerbalization: {arg1} is a high level member of {arg2}.\n",
            "The OrganizationTopMembersEmployees relation refers to individuals who hold prominent positions within a specified organization. These positions are characterized by decision-making authority over the entire organization. Specifically, all Top Member/Employee positions should imply a high level of decision-making power within the organization.",
        ]
    },
    "tacred_organizationwebsite": {
        "en": [
            "The OrganizationWebsite relation encodes an official top level URL for the assigned organization's\nwebsite.\n\nVerbalization: {arg2} is the website of {arg1}.\n",
            "The OrganizationWebsite relation represents the official website of a particular organization, specified by {arg1}, through its top-level URL, which is denoted by {arg2}.",
        ]
    },
    "tacred_personage": {
        "en": [
            "The PersonAge relation encondes the age of the assigned person.\n\nVerbalization: {arg1} is {arg2} years old.\n",
            "The PersonAge relation represents the age of the assigned individual.",
        ]
    },
    "tacred_personalternatenames": {
        "en": [
            'The PersonAlaternateNames relation encodes names used to refer to the assigned person that are\ndistinct from the "official"name. Alternate names may include aliases, stage names,\nalternate transliterations, abbreviations, alternate spellings, nicknames, or birth names.\n\nVerbalization: {arg1} is also known as {arg2}.\n',
            "The PersonAlternateNames relation includes information about the alternate names that are used to refer to the individual, which may differ from their official or legal name. These alternate names can include various forms of aliases, stage names, alternate transliterations, abbreviations, alternate spellings, nicknames, or birth names.",
        ]
    },
    "tacred_personcauseofdeath": {
        "en": [
            "The PersonCauseOfDeath relation encodes the explicit cause of death for the assigned person.\n\nVerbalization: {arg2} is the cause of {arg1}'s death.\n",
            "The PersonCauseOfDeath relation represents the explicit reason for the demise of the designated individual. Verbalization: {arg2} was the cause of {arg1}'s death.",
        ]
    },
    "tacred_personcharges": {
        "en": [
            "The PersonCharges relation encodes the charges or crimes (alleged or convicted) of the assigned person.\n\nVerbalization: {arg1} was convicted for {arg2}.\n",
            '"The PersonCharges relation refers to the criminal charges or offenses that have been leveled against the individual in question. Specifically, it indicates whether the person has been convicted of a crime or not, with the verbalization stating that {arg1} was found guilty of {arg2}."',
        ]
    },
    "tacred_personchildren": {
        "en": [
            "The PersonChildren relation encodes the children of the assigned person, including adopted and\nstep-children.\n\nVerbalization: {arg2} is the child of {arg1}.\n",
            '"The PersonChildren relation represents the offspring of the designated individual, including biological, adopted, and step-children. Explanation: {arg2} is a child of {arg1}."',
        ]
    },
    "tacred_personcityofbirth": {
        "en": [
            "The PersonCityOfBirth relation encodes the geopolitical (GPE) entity at the municipality level (city,\ntown, or village) in which the assigned person was born. The `arg2` slot must be filled with the name\nof a city, town, or village.\n\nVerbalization: {arg1} was born in {arg2}.\n",
            "The PersonCityOfBirth connection represents the geopolitical entity at the municipal level, such as a city, town, or village, where the assigned individual was born. The 'arg2' slot must be filled with the name of a city, town, or village. To express this idea in words, one might say: \"The PersonCityOfBirth relation identifies the location where the individual was born, at the municipal level, and the value in the 'arg2' position must be a name of a city, town, or village.\"",
        ]
    },
    "tacred_personcityofdeath": {
        "en": [
            "The PersonCityOfDeath relation encodes the geopolitical (GPE) entity at the level of city, town,\nvillage in which the assigned person died. The `arg2` slot must be filled with a city, town, or\nvillage name.\n\nVerbalization: {arg1} died in {arg2}.\n",
            'The PersonCityOfDeath relation pertains to the geopolitical (GPE) entity situated at the level of a city, town, or village, which is assigned to a person who passed away. The value occupying the `arg2` position must be a city, town, or village name. The verbalization of this relation can be expressed as follows: "The individual passed away in [city, town, or village name]."',
        ]
    },
    "tacred_personcityofresidence": {
        "en": [
            "The PersonCityOfResidence relations encodes the geopolitical (GPE) entities at the level of city, town,\nor village in which the assigned person has lived. The `arg2` slot must be filled with the name of a\ncity, town, or village.\n\nVerbalization: {arg1} lives or has lived in {arg2}.\n",
            "\"The PersonCityOfResidence relations refers to the geopolitical entities located at a city, town, or village level, which are assigned to a person. The 'arg2' slot must contain the name of a city, town, or village. The verbalization for this relationship is that the person lives or has lived in the specified location.\"",
        ]
    },
    "tacred_personcountryofbirth": {
        "en": [
            "The PersonCountryOfBirth relation encodes the country in which the assigned person was born.\n\nVerbalization: {arg1} was born in {arg2}.\n",
            '"The PersonCountryOfBirth relation indicates the nation where the assigned individual was born. Description: {arg1} was born in {arg2}."',
        ]
    },
    "tacred_personcountryofdeath": {
        "en": [
            "The PersonCountryOfDeath relation encodes the country in which the assigned person died. The `arg2`\nslot must be filled with the name of a country.\n\nVerbalization: {arg1} died in {arg2}.\n",
            'The "PersonCountryOfDeath" relation indicates the country where a particular person passed away. The "arg2" slot must be filled with the name of the country. To be more specific, the statement "The PersonCountryOfDeath relation encodes the country in which the assigned person died. The `arg2` slot must be filled with the name of a country. Verbalization: {arg1} died in {arg2}" means that the "arg1" slot represents the name of the person who passed away, and the "arg2" slot represents the country where they died.',
        ]
    },
    "tacred_personcountryofresidence": {
        "en": [
            "The PersonCountryOfResidence relation encodes the country in which the assigned person has lived.\n\nVerbalization: {arg1} lives or has lived in {arg2}.\n",
            'The "PersonCountryOfResidence" connection represents the country where the specified individual has resided. Rephrasing: {arg1} has lived in {arg2}.',
        ]
    },
    "tacred_persondateofbirth": {
        "en": [
            "The PersonDateOfBirth relation encodes the date on which the assigned person was born.\n\nVerbalization: {arg1} was born on {arg2}.\n",
            'The "PersonDateOfBirth" relation represents the date on which the assigned individual was born. Specifically, it signifies the day on which the person was born, as well as the year and month. For example, "John was born on January 12th, 1990."',
        ]
    },
    "tacred_persondateofdeath": {
        "en": [
            "The PersonDateOfDeath relation encodes the date of the assigned person's death.\n\nVerbalization: {arg1} died in {arg2}.\n",
            '"The PersonDateOfDeath relation conveys the date on which the designated individual passed away. Articulation: {arg1} expired in {arg2}."',
        ]
    },
    "tacred_personemployeeormemberof": {
        "en": [
            "The PersonEmployeeOrMemberOf relation encodes the organization or geopolitical (GPE)\nentities (governments) of which the assigned person has been an employee or member.\n\nVerbalization: {arg1} is a member of {arg2}.\n",
            'The "PersonEmployeeOrMemberOf" relation connects the assigned person to the organization or geopolitical entities (governments) of which they have been an employee or member.',
        ]
    },
    "tacred_personorigin": {
        "en": [
            "The PersonOrigin relation encodes the nationality and/or ethnicity of the assigned person.\n\nVerbalization: {arg2} is the nationality of {arg1}.\n",
            "The PersonOrigin relation indicates the country of origin and/or ethnicity of the individual assigned.",
        ]
    },
    "tacred_personotherfamily": {
        "en": [
            "The PersonOtherFamily relation encodes the family other than siblings, children, and spouse (or former\nspouse). Correct fillers for the `arg2` slot include brothers-in-law, sisters-in-law, grandparents,\ngrandchildren, cousins, aunts, uncles, etc.\n\nVerbalization: {arg1} and {arg2} are family.\n",
            'The PersonOtherFamily relation represents a familial relationship that is not accounted for by the sibling, child, or spouse (or former spouse) categories. The appropriate fillers for the \'arg2\' slot include individuals such as brothers-in-law, sisters-in-law, grandparents, grandchildren, cousins, aunts, uncles, and the like. To verbally convey this relationship, one may say that "{arg1}" and "{arg2}" are family.',
        ]
    },
    "tacred_personparents": {
        "en": [
            "The PersonParents relation encodes the parents of the assigned person. In addition to\nbiological parents, step-parents and adoptive parents are also acceptable answers.\n\nVerbalization: {arg2} is the parent of {arg1}.\n",
            "The PersonParents relation represents the parents of a particular individual. This includes biological parents, as well as step-parents and adoptive parents.",
        ]
    },
    "tacred_personreligion": {
        "en": [
            "The PersonReligion relation encodes the religion to which the assigned person has belonged. Former\nreligions are also acceptable answers.\n\nVerbalization: {arg2} is the religion of {arg1}.\n",
            'The PersonReligion relation represents the religious affiliation of the individual in question. It can also include information about previous religious affiliations. The verbalization of this relation can be expressed as " {arg2} is the religion of {arg1}."',
        ]
    },
    "tacred_personschoolattended": {
        "en": [
            "The PersonSchoolAttended relations encodes any school (college, high school, university, etc.) that the\nassigned person has attended.\n\nVerbalization: {arg1} studied in {arg2}.\n",
            'The "PersonSchoolAttended" relation refers to the educational institutions that a specific individual has attended. This includes universities, colleges, high schools, and any other academic institutions. The given verbalization highlights the specific school where the individual studied.',
        ]
    },
    "tacred_personsiblings": {
        "en": [
            "The PersonSiblings relation encodes the brothers and sisters of the assigned person. In addition to\n full siblings, step-siblings and half-siblings are acceptable answers. Brothers- or sisters-in-law are\n not acceptable responses for PersonSiblings relation.\n\nVerbalization: {arg1} and {arg2} are siblings.\n",
            "The PersonSiblings relation pertains to the brothers and sisters of a particular person. This includes both full siblings and step-siblings, but not brothers- or sisters-in-law. To clarify, {arg1} and {arg2} are siblings.",
        ]
    },
    "tacred_personspouse": {
        "en": [
            "The PersonSpouse relation encodes the spouse(s) of the assigned person. Former spouses are acceptable\nanswers. This relation is bidirectional.\n\nVerbalization: {arg2} is the spouse of {arg1}.\n",
            'The "PersonSpouse" relation represents the spouse(s) of the individual in question. Current or former spouses are valid answers. This relationship is reciprocal. Verbalization: {arg2} is married to {arg1}.',
        ]
    },
    "tacred_personstateorprovinceofbirth": {
        "en": [
            "The PersonStateOrProvinceOfBirth relation encodes the geopolitical (GPE) entity at state or province\nlevel in which the assigned person was born. The `arg2` slot must be filled with the name of a state\nor province.\n\nVerbalization: {arg1} was born in {arg2}.\n",
            'The PersonStateOrProvinceOfBirth relation represents the geopolitical entity at the state or province level where the assigned individual was born. The `arg2` slot must be populated with the name of a state or province. To verbalize this relation, one can say "The person was born in [state/province name]," where [state/province name] is specified in the `arg2` slot.',
        ]
    },
    "tacred_personstateorprovinceofdeath": {
        "en": [
            "The PersonStateOrProvinceOfDeath relation encodes the geopolitical (GPE) entity at state or province\nlevel in which the assigned person died. The `arg2` slot must be filled with a state or province name.\n\nVerbalization: {arg1} died in {arg2}.\n",
            "The PersonStateOrProvinceOfDeath connection represents the geopolitical entity at the state or province level where the assigned individual passed away. The 'arg2' slot must be filled with a state or province name.",
        ]
    },
    "tacred_personstateorprovinceofresidence": {
        "en": [
            "The PersonStateOrProvinceOfResidence relation encodes the geopolotical (GPE) entities at the state or\nprovince level in which the assigned person has lived. The `arg2` slot must be filled with state or\nprovince names.\n\nVerbalization: {arg1} lives or has lived in {arg2}.\n",
            'The "PersonStateOrProvinceOfResidence" relates to the geopolitical entities at a state or province level, where an assigned person has resided. The "arg2" position must be filled with specific state or province names. In summary, the given statement expresses that a certain person has lived or is currently living in a particular state or province.',
        ]
    },
    "tacred_persontitle": {
        "en": [
            "The PersonTitle relation encodes the official or unofficial name(s) of the employment or membership\nposition that have been held by the assigned person. The `arg2` slot must be filled with the name of\nthe position or title.\n\nVerbalization: {arg1} is a {arg2}.\n",
            "The PersonTitle relation pertains to the official or unofficial designation(s) of the job or membership position that a particular individual has held. The 'arg2' slot must be filled with the name of the position or title. The statement can be rephrased as \"The PersonTitle relation refers to the {arg1} who has held the {arg2} job or membership position.\"",
        ]
    },
}

