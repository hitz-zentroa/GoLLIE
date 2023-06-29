from typing import Dict, List, Type

from ..utils_typing import Span


class Person(Span):
    """{multiconer_person}"""

    span: str


class Group(Span):
    """{multiconer_group}"""

    span: str


class Location(Span):
    """{multiconer_location}"""

    span: str


class CreativeWork(Span):
    """{multiconer_creative_work}"""

    span: str


class Product(Span):
    """{multiconer_product}"""

    span: str


class Medical(Span):
    """{multiconer_medical}"""

    span: str


COARSE_ENTITY_DEFINITIONS: List[Type] = [Person, Group, Location, CreativeWork, Product, Medical]


class Scientist(Person):
    """{multiconer_scientist}"""

    span: str


class Artist(Person):
    """{multiconer_artist}"""

    span: str


class Athlete(Person):
    """{multiconer_athlete}"""

    span: str


class Politician(Person):
    """{multiconer_politician}"""

    span: str


class Cleric(Person):
    """{multiconer_cleric}"""

    span: str


class SportsManager(Person):
    """{multiconer_sports_manager}"""

    span: str


class OtherPerson(Person):
    """{multiconer_other_person}"""

    span: str


class MusicalGroup(Group):
    """{multiconer_musical_group}"""

    span: str


class PublicCorp(Group):
    """{multiconer_public_corp}"""

    span: str


class PrivateCorp(Group):
    """{multiconer_private_corp}"""

    span: str


class AerospaceManufacturer(Group):
    """{multiconer_aerospace_manufacturer}"""

    span: str


class SportsGroup(Group):
    """{multiconer_sports_group}"""

    span: str


class OtherGroup(Group):
    """{multiconer_other_group}"""

    span: str


class VisualWork(CreativeWork):
    """{multiconer_visual_work}"""

    span: str


class MusicalWork(CreativeWork):
    """{multiconer_musical_work}"""

    span: str


class WrittenWork(CreativeWork):
    """{multiconer_written_work}"""

    span: str


class ArtWork(CreativeWork):
    """{multiconer_art_work}"""

    span: str


class Software(CreativeWork):
    """{multiconer_software}"""

    span: str


class Facility(Location):
    """{multiconer_facility}"""

    span: str


class HumanSettlement(Location):
    """{multiconer_human_settlement}"""

    span: str


class Station(Location):
    """{multiconer_station}"""

    span: str


class OtherLocation(Location):
    """{multiconer_other_location}"""

    span: str


class Clothing(Product):
    """{multiconer_clothing}"""

    span: str


class Vehicle(Product):
    """{multiconer_vehicle}"""

    span: str


class Food(Product):
    """{multiconer_food}"""

    span: str


class Drink(Product):
    """{multiconer_drink}"""

    span: str


class OtherProduct(Product):
    """{multiconer_other_product}"""

    span: str


class MedicationOrVaccine(Medical):
    """{multiconer_medication_or_vaccine}"""

    span: str


class MedicalProcedure(Medical):
    """{multiconer_medical_procedure}"""

    span: str


class AnatomicalStructure(Medical):
    """{multiconer_anatomical_structure}"""

    span: str


class Symptom(Medical):
    """{multiconer_symtpom}"""

    span: str


class Disease(Medical):
    """{multiconer_disease}"""

    span: str


ENTITY_DEFINITIONS: List[Type] = [
    Scientist,
    Artist,
    Athlete,
    Politician,
    Cleric,
    SportsManager,
    OtherPerson,
    MusicalGroup,
    PublicCorp,
    PrivateCorp,
    AerospaceManufacturer,
    SportsGroup,
    OtherGroup,
    VisualWork,
    MusicalWork,
    WrittenWork,
    ArtWork,
    Software,
    Facility,
    HumanSettlement,
    Station,
    OtherLocation,
    Clothing,
    Vehicle,
    Food,
    Drink,
    OtherProduct,
    MedicationOrVaccine,
    MedicalProcedure,
    AnatomicalStructure,
    Symptom,
    Disease,
]

FINE_TO_COARSE_ENTITIES: Dict[Type, Type] = {_def: _def.__base__ for _def in ENTITY_DEFINITIONS}
COARSE_TO_FINE_ENTITIES: Dict[Type, List[Type]] = {}
for fine, coarse in FINE_TO_COARSE_ENTITIES.items():
    if coarse not in COARSE_TO_FINE_ENTITIES:
        COARSE_TO_FINE_ENTITIES[coarse] = []
    COARSE_TO_FINE_ENTITIES[coarse].append(fine)
