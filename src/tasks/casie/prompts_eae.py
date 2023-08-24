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
    attacker: List[str]  # The agent (person or organization) of the attack
    attack_pattern: List[str]  # How the attack is done
    victim: List[str]  # The device, organization, person, product or website victim of the attack
    number_of_victim: List[str]  # The number of victims affected by the attack
    compromised_data: List[str]  # The data being compromised: 'information', 'data', ...
    number_of_data: List[str]  # The amount of compromised data
    damage_amount: List[str]  # The amount of damage done to the victim
    tool: List[str]  # The file, malware or website used to attack
    purpose: List[str]  # The reason or purpose behind the attack
    place: List[str]  # Where the attack occurred
    time: List[str]  # When the attack occurred


@dataclass
class PhisingAttack(Event):
    """{phising_attack_main}"""

    mention: str
    """The text span that triggers the event.
    {phising_attack_examples}
    """
    pattern: List[str]  # How was the attack triggered, such as 'opening something' or 'clicking somewhere'
    attacker: List[str]  # The person or organization behind the attack
    victim: List[str]  # The victim of the attack
    damage_amount: List[str]  # The amount of damage done to the victim
    tool: List[str]  # The tool used to send the attack, such as 'email', 'website', 'file'
    trusted_entity: List[str]  # The bait, i.e., what the tool pretended (purported) to be
    purpose: List[str]  # What wants to steal the attacker, such as 'information'
    place: List[str]  # Where the attack occurred
    time: List[str]  # When did the attack occurred, such as 'today', 'tomorrow', ...


@dataclass
class RansomAttack(Event):
    """{ransom_attack_main}"""

    mention: str
    """The text span that triggers the event.
    {ransom_attack_examples}
    """
    pattern: List[str]  # What does the attack do until demands are met.
    attacker: List[str]  # Who performed the attack
    victim: List[str]  # The victim of the attack
    damage_amount: List[str]  # The amount of damage the attack produced
    tool: List[str]  # The tool used
    price: List[str]  # The price of the payment
    payment_method: List[str]  # How the payment have to be done, such as 'a webpage'
    time: List[str]  # When the attack took place
    place: List[str]  # Where the attack took place


@dataclass
class VulnerabilityDiscover(Event):
    """{vulnerability_discover_main}"""

    mention: str
    """The text span that triggers the event.
    {vulnerability_discover_examples}
    """
    cve: List[str]  # The vulnerability identifier: such 'CVE-2018-5003'
    used_for: List[str]  # What is the vulnerability used for such as 'allow to take control'
    discoverer: List[str]  # The entity that reported the vulnerability
    supported_platform: List[str]  # The platforms that support the vulnerability
    vulnerability: List[str]  # The vulnerabilities, such as 'vulnerability'
    vulnerable_system: List[str]  # The systems vulnerable to the vulnerability
    system_owner: List[str]  # The owners of the vulnerable system
    system_version: List[str]  # The version of the vulnerable system
    time: List[str]  # When was the vulnerability discovered


@dataclass
class VulnerabilityPatch(Event):
    """{vulnerability_patch_main}"""

    mention: str
    """The text span that triggers the event.
    {vulnerability_patch_examples}
    """
    cve: List[str]  # The vulnerability identifier: such 'CVE-2018-5003'
    issues_addressed: List[str]  # What did the patch fixed
    supported_platform: List[str]  # The platforms that support the vulnerability
    vulnerability: List[str]  # The vulnerability, such as 'vulnerability'
    vulnerable_system: List[str]  # The affected systems, such as 'infraestructures'
    releaser: List[str]  # The entity releasing the patch
    patch: List[str]  # What was the patch about
    patch_number: List[str]  # Nunber or name of the patch
    system_version: List[str]  # The version of the vulnerable system
    time: List[str]  # When was the patch implemented, the date


EAE_EVENT_DEFINITIONS: List[Type] = [
    DatabreachAttack,
    PhisingAttack,
    RansomAttack,
    VulnerabilityDiscover,
    VulnerabilityPatch,
]
