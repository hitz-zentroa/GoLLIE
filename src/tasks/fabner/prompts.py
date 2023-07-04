from typing import List

from ..utils_typing import Entity, dataclass


"""Entity definitions

The entity definitions are derived from the official fabner guidelines:
https://par.nsf.gov/servlets/purl/10290810

"""


@dataclass
class Material(Entity):
    """{fabner_material}"""

    span: str


@dataclass
class ManufacturingProcess(Entity):
    """{fabner_manufacturingprocess}"""

    span: str


@dataclass
class MachineEquipment(Entity):
    """{fabner_machineequipment}"""

    span: str


@dataclass
class Application(Entity):
    """{fabner_application}"""

    span: str


@dataclass
class EngineeringFeatures(Entity):
    """{fabner_engineeringfeatures}"""

    span: str


@dataclass
class MechanicalProperties(Entity):
    """{fabner_mechanicalproperties}"""

    span: str


@dataclass
class ProcessCharacterization(Entity):
    """{fabner_processcharacterization}"""

    span: str


@dataclass
class ProcessParameters(Entity):
    """{fabner_processparameters}"""

    span: str


@dataclass
class EnablingTechnology(Entity):
    """{fabner_enablingtechnology}"""

    span: str


@dataclass
class ConceptPrinciples(Entity):
    """{fabner_conceptprinciples}"""

    span: str


@dataclass
class ManufacturingStandards(Entity):
    """{fabner_manufacturingstandards}"""

    span: str


@dataclass
class Biomedical(Entity):
    """{fabner_biomedical}"""

    span: str


ENTITY_DEFINITIONS: List[Entity] = [
    Material,
    ManufacturingProcess,
    MachineEquipment,
    Application,
    EngineeringFeatures,
    MechanicalProperties,
    ProcessCharacterization,
    ProcessParameters,
    EnablingTechnology,
    ConceptPrinciples,
    ManufacturingStandards,
    Biomedical,
]

# __all__ = list(map(str, [*ENTITY_DEFINITIONS]))
