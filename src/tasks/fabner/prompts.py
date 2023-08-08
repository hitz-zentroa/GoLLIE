from typing import List

from ..utils_typing import Entity, dataclass


"""Entity definitions

The entity definitions are derived from the official fabner guidelines:
https://par.nsf.gov/servlets/purl/10290810

"""


@dataclass
class Material(Entity):
    """{fabner_material}"""

    span: str  # {fabner_material_examples}


@dataclass
class ManufacturingProcess(Entity):
    """{fabner_manufacturingprocess}"""

    span: str  # {fabner_manufacturingprocess_examples}


@dataclass
class MachineEquipment(Entity):
    """{fabner_machineequipment}"""

    span: str  # {fabner_machineequipment_examples}


@dataclass
class Application(Entity):
    """{fabner_application}"""

    span: str  # {fabner_application_examples}


@dataclass
class EngineeringFeatures(Entity):
    """{fabner_engineeringfeatures}"""

    span: str  # {fabner_engineeringfeatures_examples}


@dataclass
class MechanicalProperties(Entity):
    """{fabner_mechanicalproperties}"""

    span: str  # {fabner_mechanicalproperties_examples}


@dataclass
class ProcessCharacterization(Entity):
    """{fabner_processcharacterization}"""

    span: str  # {fabner_processcharacterization_examples}


@dataclass
class ProcessParameters(Entity):
    """{fabner_processparameters}"""

    span: str  # {fabner_processparameters_examples}


@dataclass
class EnablingTechnology(Entity):
    """{fabner_enablingtechnology}"""

    span: str  # {fabner_enablingtechnology_examples}


@dataclass
class ConceptPrinciples(Entity):
    """{fabner_conceptprinciples}"""

    span: str  # {fabner_conceptprinciples_examples}


@dataclass
class ManufacturingStandards(Entity):
    """{fabner_manufacturingstandards}"""

    span: str  # {fabner_manufacturingstandards_examples}


@dataclass
class Biomedical(Entity):
    """{fabner_biomedical}"""

    span: str  # {fabner_biomedical_examples}


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
