from typing import List

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
"""


@dataclass
class DatabreachAttack(Event):
    """An DatabreachAttack Event happens when an attacker compromises a system
    to later remove or expose the data, e.g., to sell, publish or make it accessible.
    """

    mention: str
    """The text span that triggers the event, such as:
        - 'attack', 'expose', 'publish', 'steal', ...
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
    """A PhisingAttack Event happens when an attacker imitates another entity, in
    an attempt to get a victim to access malicious materials, such as a website or
    attachments.
    """

    mention: str
    """The text span that triggers the event, such as:
        - 'attack', 'purports to be', 'dupe', ...
        - 'masquerading as', 'pretending to be', 'scam', ...
    """
    pattern: List[str]  # How was the attack triggered, such as 'opening something' or 'clicking somewhere'
    attacker: str  # The person or organization behind the attack
    victim: List[str]  # The victim of the attack
    damage_amount: List[str]  # The amount of damage done to the victim
    tool: List[str]  # The tool used to send the attack, such as 'email', 'website', 'file'
    trusted_entity: List[str]  # The bait, i.e., what the tool pretended (purported) to be
    purpose: List[str]  # What wants to steal the attacker, such as 'information'
    place: List[str]  # Where the attack occurred
    time: List[str]  # When did the attack occurred, such as 'today', 'tomorrow', ...


@dataclass
class RansomAttack(Event):
    """A RansomAttack Event happens when n attacker breaks into a system and
    encrypts data, and will only decrypt the data for a ransom payment.
    """

    mention: str
    """The text span that triggers the event, such as:
        - 'attack', ransomware', 'selling', 'ransom', ...
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
