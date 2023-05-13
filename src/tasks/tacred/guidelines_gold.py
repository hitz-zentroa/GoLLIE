GUIDELINES = {
    "tacred_organizationalternatename": {
        "en": [
            "The OrganizationAlternateName relation encodes any name used to refer to the assigned organization that\n"
            'is distinct from the "official"name. Alternate names may include former names, aliases, alternate\n'
            "spellings, acronyms, abbreviations, translations or transliterations of names, and any official\n"
            "designators such as stock ticker code or airline call sign.\n\n"
            "Verbalization: {arg1} is also known as {arg2}.\n"
        ]
    },
    "tacred_organizationcityofheadquarters": {
        "en": [
            "The OrganizationCityOfHeadquarters relation encodes the location of the headquarters of the assigned\n"
            "organization ath the city, town, or village level. The `arg2` slot must be filled with a city, town,\n"
            "or village name.\n\n"
            "Verbalization: {arg1} is located in {arg2}.\n"
        ]
    },
    "tacred_organizationcountryofheadquarters": {
        "en": [
            "The OrganizationCountryOfHeadquarters relation encodes the country in which the headquarters of\n"
            "the assigned organization are located. The `arg2` slot must be filled with a country name.\n\n"
            "Verbalization: {arg1} is located in {arg2}.\n"
        ]
    },
    "tacred_organizationdatedissolved": {
        "en": [
            "The OrganizationDateDissolved relation encodes the date on which the assigned organization was\n"
            "dissolved. When Companies merge to form a new entity, the original companies should be considered as\n"
            "dissolved.\n\n"
            "Verbalization: {arg1} dissolved in {arg2}.\n"
        ]
    },
    "tacred_organizationdatefounded": {
        "en": [
            "The OrganizationDateFounded relations encodes the date on which the assigned organization was founded.\n"
            "\nVerbalization: {arg1} was founded in {arg2}.\n"
        ]
    },
    "tacred_organizationfoundedby": {
        "en": [
            "The OrganizationFoundedBy relation encodes the person, organization or geopolitical (GPE) entity that\n"
            "founded the assigned organization.\n\n"
            "Verbalization: {arg1} was founded by {arg2}.\n"
        ]
    },
    "tacred_organizationmember": {
        "en": [
            "The OrganizationMember relation encodes the organizations or geopolitical (GPE) entities that are\n"
            "members of the assigned organization (the inverse of OrganizationMemberOf). While similar to\n"
            "OrganizationSubsidiary, OrganizationMember is different because correct `arg2` fillers are distinct\n"
            "entities that are generally capable of autonomously ending their membership with the assigned\n"
            "organization.\n\n"
            "Verbalization: {arg2} is member of {arg1}.\n"
        ]
    },
    "tacred_organizationmemberof": {
        "en": [
            "The OrganizationMemberOf relation encodes the organizations or geopolitical (GPE) entities of which the\n"
            "assigned organization is a member itself (the inverse of OrganizationMember). For the `arg2` slot, the\n"
            "assigned organization is a distinct entity from the parent organization and is generally capable of\n"
            "autonomously ending the membership relation.\n\n"
            "Verbalization: {arg1} is member of {arg2}.\n"
        ]
    },
    "tacred_organizationnumberofemployeesmembers": {
        "en": [
            "The OrganizationNumberOfEmployeesMembers relation encodes the total number of people who are employed\n"
            "by or have membership in the associated organization.\n\n"
            "Verbalization: {arg1} employs nearly {arg2} people.\n"
        ]
    },
    "tacred_organizationparent": {
        "en": [
            "The OrganizationParent relation encodes the organizations or geopolitical (GPE) entities of which the\n"
            "assigned organization is a subsidiary (the inverse of OrganizationSubsidiary). While similar to\n"
            "OrganizationMemberOf, OrganizationParent is different because the assigned organization is subsumed\n"
            "under the parent organization(s), rather than being a distinct entity.\n\n"
            "Verbalization: {arg1} is a subsidiary or branch of {arg2}.\n"
        ]
    },
    "tacred_organizationpoliticalreligiousaffiliation": {
        "en": [
            "The OrganizationPoliticalReligiousAffiliation relation encodes the ideological groups with which\n"
            "the organization is associated.\n\n"
            "Verbalization: {arg1} has political or religious affiliation with {arg2}.\n"
        ]
    },
    "tacred_organizationshareholders": {
        "en": [
            "The OrganizationShareholders relation encodes any organization, person, or geopolitical (GPE) entity\n"
            "that holds shares (majority or not) of the organization. Former shareholders are acceptable\n"
            "responses.\n\n"
            "Verbalization: {arg2} holds shares in {arg1}.\n"
        ]
    },
    "tacred_organizationstateorprovinceofheadquarters": {
        "en": [
            "The OrganizationStateOrProvinceOfHeadquarters relation encodes the location of the headquarters of the\n"
            "assigned organization at the state or province level. The `arg2` slot must be filled with a state or\n"
            "province name.\n\n"
            "Verbalization: {arg1} is located in {arg2}.\n"
        ]
    },
    "tacred_organizationsubsidiary": {
        "en": [
            "The OrganizationSubsidiary relation encodes the organizations that are subsidiaries of the\n"
            "assigned organization (the inverse of OrganizationParent). Subsidiaries are subsumed under the\n"
            "assigned organization, rather than being distinct entities.\n\n"
            "Verbalization: {arg2} is a subsidiary or branch of\n{arg1}.\n"
        ]
    },
    "tacred_organizationtopmembersemployees": {
        "en": [
            "The OrganizationTopMembersEmployees relation encodes the persons in high-level, leading positions at\n"
            "the assigned organization. Although the definition of 'leading position'is relatively broad, all\n"
            "Top Member/Employee positions should imply a level of decidion-making authority over the entire\n"
            "assigned organization.\n\n"
            "Verbalization: {arg1} is a high level member of {arg2}.\n"
        ]
    },
    "tacred_organizationwebsite": {
        "en": [
            "The OrganizationWebsite relation encodes an official top level URL for the assigned organization's\n"
            "website.\n\n"
            "Verbalization: {arg2} is the website of {arg1}.\n"
        ]
    },
    "tacred_personage": {
        "en": [
            "The PersonAge relation encondes the age of the assigned person.\n\n"
            "Verbalization: {arg1} is {arg2} years old.\n"
        ]
    },
    "tacred_personalternatenames": {
        "en": [
            "The PersonAlaternateNames relation encodes names used to refer to the assigned person that are\n"
            'distinct from the "official"name. Alternate names may include aliases, stage names,\n'
            "alternate transliterations, abbreviations, alternate spellings, nicknames, or birth names.\n\n"
            "Verbalization: {arg1} is also known as {arg2}.\n"
        ]
    },
    "tacred_personcauseofdeath": {
        "en": [
            "The PersonCauseOfDeath relation encodes the explicit cause of death for the assigned person.\n\n"
            "Verbalization: {arg2} is the cause of {arg1}'s death.\n"
        ]
    },
    "tacred_personcharges": {
        "en": [
            "The PersonCharges relation encodes the charges or crimes (alleged or convicted) of the assigned person.\n"
            "\nVerbalization: {arg1} was convicted for {arg2}.\n"
        ]
    },
    "tacred_personchildren": {
        "en": [
            "The PersonChildren relation encodes the children of the assigned person, including adopted and\n"
            "step-children.\n\n"
            "Verbalization: {arg2} is the child of {arg1}.\n"
        ]
    },
    "tacred_personcityofbirth": {
        "en": [
            "The PersonCityOfBirth relation encodes the geopolitical (GPE) entity at the municipality level (city,\n"
            "town, or village) in which the assigned person was born. The `arg2` slot must be filled with the name\n"
            "of a city, town, or village.\n\n"
            "Verbalization: {arg1} was born in {arg2}.\n"
        ]
    },
    "tacred_personcityofdeath": {
        "en": [
            "The PersonCityOfDeath relation encodes the geopolitical (GPE) entity at the level of city, town,\n"
            "village in which the assigned person died. The `arg2` slot must be filled with a city, town, or\n"
            "village name.\n\n"
            "Verbalization: {arg1} died in {arg2}.\n"
        ]
    },
    "tacred_personcityofresidence": {
        "en": [
            "The PersonCityOfResidence relations encodes the geopolitical (GPE) entities at the level of city, town,\n"
            "or village in which the assigned person has lived. The `arg2` slot must be filled with the name of a\n"
            "city, town, or village.\n\n"
            "Verbalization: {arg1} lives or has lived in {arg2}.\n"
        ]
    },
    "tacred_personcountryofbirth": {
        "en": [
            "The PersonCountryOfBirth relation encodes the country in which the assigned person was born.\n\n"
            "Verbalization: {arg1} was born in {arg2}.\n"
        ]
    },
    "tacred_personcountryofdeath": {
        "en": [
            "The PersonCountryOfDeath relation encodes the country in which the assigned person died. The `arg2`\n"
            "slot must be filled with the name of a country.\n\n"
            "Verbalization: {arg1} died in {arg2}.\n"
        ]
    },
    "tacred_personcountryofresidence": {
        "en": [
            "The PersonCountryOfResidence relation encodes the country in which the assigned person has lived.\n\n"
            "Verbalization: {arg1} lives or has lived in {arg2}.\n"
        ]
    },
    "tacred_persondateofbirth": {
        "en": [
            "The PersonDateOfBirth relation encodes the date on which the assigned person was born.\n\n"
            "Verbalization: {arg1} was born on {arg2}.\n"
        ]
    },
    "tacred_persondateofdeath": {
        "en": [
            "The PersonDateOfDeath relation encodes the date of the assigned person's death.\n\n"
            "Verbalization: {arg1} died in {arg2}.\n"
        ]
    },
    "tacred_personemployeeormemberof": {
        "en": [
            "The PersonEmployeeOrMemberOf relation encodes the organization or geopolitical (GPE)\n"
            "entities (governments) of which the assigned person has been an employee or member.\n\n"
            "Verbalization: {arg1} is a member of {arg2}.\n"
        ]
    },
    "tacred_personorigin": {
        "en": [
            "The PersonOrigin relation encodes the nationality and/or ethnicity of the assigned person.\n\n"
            "Verbalization: {arg2} is the nationality of {arg1}.\n"
        ]
    },
    "tacred_personotherfamily": {
        "en": [
            "The PersonOtherFamily relation encodes the family other than siblings, children, and spouse (or former\n"
            "spouse). Correct fillers for the `arg2` slot include brothers-in-law, sisters-in-law, grandparents,\n"
            "grandchildren, cousins, aunts, uncles, etc.\n\n"
            "Verbalization: {arg1} and {arg2} are family.\n"
        ]
    },
    "tacred_personparents": {
        "en": [
            "The PersonParents relation encodes the parents of the assigned person. In addition to\n"
            "biological parents, step-parents and adoptive parents are also acceptable answers.\n\n"
            "Verbalization: {arg2} is the parent of {arg1}.\n"
        ]
    },
    "tacred_personreligion": {
        "en": [
            "The PersonReligion relation encodes the religion to which the assigned person has belonged. Former\n"
            "religions are also acceptable answers.\n\n"
            "Verbalization: {arg2} is the religion of {arg1}.\n"
        ]
    },
    "tacred_personschoolattended": {
        "en": [
            "The PersonSchoolAttended relations encodes any school (college, high school, university, etc.) that the\n"
            "assigned person has attended.\n\n"
            "Verbalization: {arg1} studied in {arg2}.\n"
        ]
    },
    "tacred_personsiblings": {
        "en": [
            "The PersonSiblings relation encodes the brothers and sisters of the assigned person. In addition to\n"
            " full siblings, step-siblings and half-siblings are acceptable answers. Brothers- or sisters-in-law are\n"
            " not acceptable responses for PersonSiblings relation.\n\n"
            "Verbalization: {arg1} and {arg2} are siblings.\n"
        ]
    },
    "tacred_personspouse": {
        "en": [
            "The PersonSpouse relation encodes the spouse(s) of the assigned person. Former spouses are acceptable\n"
            "answers. This relation is bidirectional.\n\n"
            "Verbalization: {arg2} is the spouse of {arg1}.\n"
        ]
    },
    "tacred_personstateorprovinceofbirth": {
        "en": [
            "The PersonStateOrProvinceOfBirth relation encodes the geopolitical (GPE) entity at state or province\n"
            "level in which the assigned person was born. The `arg2` slot must be filled with the name of a state\n"
            "or province.\n\n"
            "Verbalization: {arg1} was born in {arg2}.\n"
        ]
    },
    "tacred_personstateorprovinceofdeath": {
        "en": [
            "The PersonStateOrProvinceOfDeath relation encodes the geopolitical (GPE) entity at state or province\n"
            "level in which the assigned person died. The `arg2` slot must be filled with a state or province name.\n"
            "\nVerbalization: {arg1} died in {arg2}.\n"
        ]
    },
    "tacred_personstateorprovinceofresidence": {
        "en": [
            "The PersonStateOrProvinceOfResidence relation encodes the geopolotical (GPE) entities at the state or\n"
            "province level in which the assigned person has lived. The `arg2` slot must be filled with state or\n"
            "province names.\n\n"
            "Verbalization: {arg1} lives or has lived in {arg2}.\n"
        ]
    },
    "tacred_persontitle": {
        "en": [
            "The PersonTitle relation encodes the official or unofficial name(s) of the employment or membership\n"
            "position that have been held by the assigned person. The `arg2` slot must be filled with the name of\n"
            "the position or title.\n\n"
            "Verbalization: {arg1} is a {arg2}.\n"
        ]
    },
}
