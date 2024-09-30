import random
import re
from typing import Dict, Any

def apply_entity_type_masking(entry: Dict[str, Any], probability: float) -> Dict[str, Any]:
    """
    Masks class names in the 'text' and 'labels' fields of the entry
    with a placeholder 'MaskedClass' with probability p. Class names are masked consistently
    throughout the fields (if classname A is masked in text, it'd be masked in labels as well)

    Args:
        entry (Dict[str, Any]): The JSON object containing the data fields. (entry of the dataset)
        probability (float): The probability that any given class name is masked.

    Returns:
        Dict[str, Any]: The modified entry with class names masked.
    """
    # Make a copy of the entry to avoid modifying the original
    entry = entry.copy()
    
    # Extract the 'text' field
    text = entry.get('text', '')
    
    # Find all class definitions in 'text'
    class_def_pattern = re.compile(r'^(\s*class\s+)(\w+)(\s*(?:\(|:))', re.MULTILINE)
    class_names = class_def_pattern.findall(text)
    class_names = [name[1] for name in class_names]  # Extract class names

    # Decide which class names to mask
    masked_class_names = set()
    for name in class_names:
        if random.random() < probability:
            masked_class_names.add(name)

    # Function to replace class names in 'text'
    def mask_class_names_in_text(match):
        prefix, name, suffix = match.groups()
        if name in masked_class_names:
            return f"{prefix}MaskedClass{suffix}"
        else:
            return match.group(0)
    
    # Mask class names in class definitions in 'text'
    text = class_def_pattern.sub(mask_class_names_in_text, text)

    # Mask class names throughout 'text'
    for name in masked_class_names:
        # Use word boundaries to replace the class names
        text = re.sub(rf'\b{name}\b', 'MaskedClass', text)
    
    # Update the 'text' field
    entry['text'] = text

    # Now, mask class names in the 'labels' field
    labels = entry.get('labels', '')
    for name in masked_class_names:
        # Replace class names in 'labels'
        labels = re.sub(rf'\b{name}\b', 'MaskedClass', labels)
    # Update the 'labels' field
    entry['labels'] = labels

    return entry

def apply_negatives(entry: Dict[str, Any], probability: float) -> Dict[str, Any]:
    """
    Placeholder function for applying negative examples to the entry.
    Implement your negative sampling logic here.
    """
    # TODO: Implement the logic for applying negatives
    return entry


if __name__ == "__main__":
    import json

    # Set random seed for reproducibility
    random.seed(42)

    # Define the example JSON object
    entry = {
        "ids": ["<urn:uuid:10a10a8a-c433-497e-b939-429fea3e7e01>"],
        "task_id": "fineweb-edu_pretrain_gollie2",
        "scorer_cls": "src.tasks.fineweb-edu_pretrain.scorer.fineweb-edu_pretrainScorer",
        "labels": "[\n    NapaRiverEcologicalReserveGuide(\n        purpose=\"encourage use of the Napa River Ecological Reserve as a learning laboratory\",\n        description=ReserveDescription(\n            area=\"73-acre\",\n            significance=\"last sizable section of riparian vegetation in Napa Valley\",\n            habitat=\"diverse community of birds, butterflies, mammals and plants\",\n            historical=\"Valley oaks significant to Wappo tribe and early European settlers\"\n        ),\n        educational_opportunities=EducationalOpportunities(\n            topics=[\"watershed function\", \"ecology\", \"biodiversity\", \"ecological restoration\", \"local history\", \"appreciation for conservation\"]\n        ),\n        activities=Activities(\n            categories=[\"art\", \"ecology\", \"history\"],\n            hands_on_learning=\"see, hear, feel, and appreciate Napa River Watershed\"\n        ),\n        curriculum=Curriculum(\n            alignment=\"established classroom standards\",\n            adaptability=\"alter lessons for multiple grade levels\"\n        ),\n        extensions=\"lesson extensions for classroom follow-up\",\n        resources=Resources(\n            volunteer_opportunities=\"list available\",\n            stewardship_projects=\"project ideas included\",\n            local_resources=\"for natural resource appreciation and conservation\"\n        )\n    )\n]",
        "text": "# The following lines describe the task definition\nfrom dataclasses import dataclass\nfrom typing import List, Optional\n\n@dataclass\nclass ReserveDescription:\n    \"\"\"\n    Contains detailed information about the Napa River Ecological Reserve,\n    its significance, habitat diversity, and historical context.\n    \"\"\"\n    area: str\n    \"\"\"The total area of the Reserve, indicating its size in acres.\"\"\"\n    significance: str\n    \"\"\"Description of the ecological importance of the Reserve within Napa Valley.\"\"\"\n    habitat: str\n    \"\"\"Information on the variety of living organisms that inhabit the Reserve.\"\"\"\n    historical: str\n    \"\"\"Summary of the historical relevance of the vegetation in connection with the native tribe and early settlers.\"\"\"\n\n@dataclass\nclass EducationalOpportunities:\n    \"\"\"\n    Holds various educational topics that can be explored through activities in the Reserve.\n    \"\"\"\n    topics: List[str]\n    \"\"\"A list of key educational topics related to ecology, history, and conservation.\"\"\"\n\n@dataclass\nclass Activities:\n    \"\"\"\n    Represents the types of activities designed for engagement in the Reserve,\n    focused on holistic learning experiences.\n    \"\"\"\n    categories: List[str]\n    \"\"\"List of categories for the activities, such as art, ecology, and history.\"\"\"\n    hands_on_learning: str\n    \"\"\"Description of the experiential learning component provided by the activities.\"\"\"\n\n@dataclass\nclass Curriculum:\n    \"\"\"\n    Provides information on how the activities align with educational standards\n    and their adaptability for different educational levels.\n    \"\"\"\n    alignment: str\n    \"\"\"Indicates how the activities fit with established classroom standards.\"\"\"\n    adaptability: str\n    \"\"\"Describes how lessons can be tailored for various grade levels.\"\"\"\n\n@dataclass\nclass Resources:\n    \"\"\"\n    Contains additional resources available for students and educators\n    that promote involvement in conservation and appreciation of natural areas.\n    \"\"\"\n    volunteer_opportunities: str\n    \"\"\"A description of available volunteer options for students.\"\"\"\n    stewardship_projects: str\n    \"\"\"Ideas for stewardship projects that contribute to local conservation efforts.\"\"\"\n    local_resources: str\n    \"\"\"Additional resources that support natural resource appreciation and conservation.\"\"\"\n\n@dataclass\nclass NapaRiverEcologicalReserveGuide:\n    \"\"\"\n    Encapsulates all relevant information pertaining to the Napa River Ecological Reserve\n    Curriculum Guide, including educational purposes, activities, and resources for students.\n    \"\"\"\n    purpose: str\n    \"\"\"Explanation of why the guide was created and its intended use for education.\"\"\"\n    description: ReserveDescription\n    \"\"\"Detailed description of the Reserve itself, including size and ecological significance.\"\"\"\n    educational_opportunities: EducationalOpportunities\n    \"\"\"List of educational opportunities associated with the Reserve activities.\"\"\"\n    activities: Activities\n    \"\"\"Information on activities available for hands-on learning experiences.\"\"\"\n    curriculum: Curriculum\n    \"\"\"Details on how the activities align with educational standards and their adaptability.\"\"\"\n    extensions: str\n    \"\"\"Information on lesson extensions that can be implemented in the classroom.\"\"\"\n    resources: Resources\n    \"\"\"Collection of additional resources for volunteer work and conservation initiatives.\"\"\"\n\n# This is the text to analyze\ntext = \"The Napa River Ecological Reserve Curriculum Guide was created to encourage the use of the Napa River Ecological Reserve as a learning laboratory for students of all ages. The 73-acre Reserve is the last sizable section of riparian vegetation in the Napa Valley and provides habitat for a diverse community of birds, butterflies, mammals and plants. Valley oaks that surrounded the native Wappo tribe and early European settlers of the Valley can still be found in the diverse habitats within the Reserve. The Reserve\\u2019s ecological and historical significance make it an ideal location for students to learn about watershed function and ecology, biodiversity, ecological restoration, the history of the people and industries of Napa Valley, and appreciation for the need to conserve natural areas.\\nThe activities in the guide allow students to develop an understanding and appreciation for the natural environment through activities in three main categories: art, ecology, and history. The activities will give participating classes the opportunity to see, hear, feel, and appreciate the Napa River Watershed in a hands-on way that classroom lessons alone cannot provide. The activities in the guide align with established classroom curriculum standards and contain notes on how to alter the lessons for multiple grade levels. Many of the activities in this guide also contain lesson extensions that can be brought back into the classroom so that the knowledge gained while at the Reserve can continue to grow. The guide concludes with a list of volunteer opportunities, stewardship project ideas, and other local resources that can help your students become involved with natural resource appreciation and conservation.\\nNapa River Ecological Reserve Guide 2014 (pdf=33.2mb)\"\n",
        "unlabelled_sentence": "The Napa River Ecological Reserve Curriculum Guide was created to encourage the use of the Napa River Ecological Reserve as a learning laboratory for students of all ages. The 73-acre Reserve is the last sizable section of riparian vegetation in the Napa Valley and provides habitat for a diverse community of birds, butterflies, mammals and plants. Valley oaks that surrounded the native Wappo tribe and early European settlers of the Valley can still be found in the diverse habitats within the Reserve. The Reserve’s ecological and historical significance make it an ideal location for students to learn about watershed function and ecology, biodiversity, ecological restoration, the history of the people and industries of Napa Valley, and appreciation for the need to conserve natural areas.\nThe activities in the guide allow students to develop an understanding and appreciation for the natural environment through activities in three main categories: art, ecology, and history. The activities will give participating classes the opportunity to see, hear, feel, and appreciate the Napa River Watershed in a hands-on way that classroom lessons alone cannot provide. The activities in the guide align with established classroom curriculum standards and contain notes on how to alter the lessons for multiple grade levels. Many of the activities in this guide also contain lesson extensions that can be brought back into the classroom so that the knowledge gained while at the Reserve can continue to grow. The guide concludes with a list of volunteer opportunities, stewardship project ideas, and other local resources that can help your students become involved with natural resource appreciation and conservation.\nNapa River Ecological Reserve Guide 2014 (pdf=33.2mb)"
    }

    # Apply the masking function with probability p
    p = 0.5  # Adjust the probability as needed
    modified_entry = apply_entity_type_masking(entry, p)
    
    #print the original entry
    print("Original Entry:")
    print("-----------------")
    print(json.dumps(entry, indent=4))
    
    print("\n")

    # Print the modified entry
    print("Modified Entry:")
    print("-----------------")
    print(json.dumps(modified_entry, indent=4))
