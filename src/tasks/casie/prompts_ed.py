from typing import List, Type

from ..utils_typing import Event, dataclass


"""Event definitions

The events definitions are derived from the original paper:
https://ojs.aaai.org/index.php/AAAI/article/view/6401


Attack:Databreach:Attack-Pattern -> 'attack_pattern'
Attack:Databreach:Attacker -> 'attacker'
Attack:Databreach:Compromised-Data -> 'compromised_data'
Attack:Databreach:Damage-Amount -> 'damage_amount'
Attack:Databreach:Number-of-Data -> 'number_of_data'
Attack:Databreach:Number-of-Victim -> 'number_of_victim'
Attack:Databreach:Place -> 'place'
Attack:Databreach:Purpose -> 'purpose'
Attack:Databreach:Time -> 'time'
Attack:Databreach:Tool -> 'tool'
Attack:Databreach:Victim -> 'victim'

Attack:Phising:Attack-Pattern -> 'pattern'
Attack:Phising:Attacker -> 'attacker'
Attack:Phising:Damage-Amount -> 'damage_amount'
Attack:Phising:Place -> 'place'
Attack:Phising:Purpose -> 'purpose'
Attack:Phising:Time -> 'time'
Attack:Phising:Tool -> 'tool'
Attack:Phising:Trusted-Entity -> 'trusted_entity'
Attack:Phising:Victim -> 'victim'

Attack:Ransom:Attack-Pattern -> 'pattern'
Attack:Ransom:Attacker -> 'attacker'
Attack:Ransom:Damage-Amount ->  'damage_amount'
Attack:Ransom:Payment-Method ->  'payment_method'
Attack:Ransom:Place ->  'place'
Attack:Ransom:Price ->  'price'
Attack:Ransom:Time ->  'time'
Attack:Ransom:Tool ->  'tool'
Attack:Ransom:Victim ->  'victim'

Vulnerability:Discover:CVE -> 'cve'
Vulnerability:Discover:Capabilities -> 'used_for'
Vulnerability:Discover:Discoverer -> 'discoverer
Vulnerability:Discover:Supported_Platform -> 'supported_platform
Vulnerability:Discover:Time -> 'time'
Vulnerability:Discover:Vulnerability -> 'vulnerability'
Vulnerability:Discover:Vulnerable_System -> 'vulnerable_system'
Vulnerability:Discover:Vulnerable_System_Owner -> 'system_owner'
Vulnerability:Discover:Vulnerable_System_Version -> 'system_version'

Vulnerability:Patch:CVE -> 'cve'
Vulnerability:Patch:Issues-Addressed -> 'issues_addressed'
Vulnerability:Patch:Patch -> 'patch'
Vulnerability:Patch:Patch-Number -> 'patch_number'
Vulnerability:Patch:Releaser -> 'releaser'
Vulnerability:Patch:Supported_Platform -> 'supported_platform'
Vulnerability:Patch:Time -> 'time'
Vulnerability:Patch:Vulnerability -> 'vulnerability'
Vulnerability:Patch:Vulnerable_System -> 'vulnerable_system'
Vulnerability:Patch:Vulnerable_System_Version -> 'system_version'
"""


@dataclass
class DatabreachAttack(Event):
    """{databreach_attack_main}"""

    mention: str
    """The text span that triggers the event.
    {databreach_attack_examples}
    """


@dataclass
class PhisingAttack(Event):
    """{phising_attack_main}"""

    mention: str
    """The text span that triggers the event.
    {phising_attack_examples}
    """


@dataclass
class RansomAttack(Event):
    """{ransom_attack_main}"""

    mention: str
    """The text span that triggers the event.
    {ransom_attack_examples}
    """


@dataclass
class VulnerabilityDiscover(Event):
    """{vulnerability_discover_main}"""

    mention: str
    """The text span that triggers the event.
    {vulnerability_discover_examples}
    """


@dataclass
class VulnerabilityPatch(Event):
    """{vulnerability_patch_main}"""

    mention: str
    """The text span that triggers the event.
    {vulnerability_patch_examples}
    """


ED_EVENT_DEFINITIONS: List[Type] = [
    DatabreachAttack,
    PhisingAttack,
    RansomAttack,
    VulnerabilityDiscover,
    VulnerabilityPatch,
]
