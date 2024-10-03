import random
import re
from typing import Dict, Any
import ast
import random
import sys
import nltk
import spacy
from collections import defaultdict


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
    Removes class instances from 'labels' and 'result' list in 'text' with a certain probability.
    Additionally, removes phrases mentioning these classes from 'unlabelled_sentence' and
    the unlabelled text within 'text'.
    
    Args:
        entry (Dict[str, Any]): The JSON object containing the data fields.
        probability (float): The probability of each class being removed.
    
    Returns:
        Dict[str, Any]: The modified entry with negatives applied.
    """
    # Make a deep copy to avoid modifying the original entry
    modified_entry = entry.copy()
    
    # Extract relevant fields
    text = modified_entry.get('text', '')
    labels = modified_entry.get('labels', '')
    unlabelled_sentence = modified_entry.get('unlabelled_sentence', '')
    
    # Step 1: Extract class names from class definitions in 'text'
    # Pattern matches lines starting with '@dataclass' followed by 'class ClassName'
    class_def_pattern = re.compile(r'^@dataclass\s*\nclass\s+(\w+)', re.MULTILINE)
    class_names = class_def_pattern.findall(text)
    
    if not class_names:
        # No class definitions found; return the original entry
        return modified_entry
    
    # Step 2: Extract class instances from 'labels'
    # Assuming labels are in the format: [ClassName(field1="value1", field2="value2"), ...]
    class_instance_pattern = re.compile(r'(\w+)\s*\(([^)]*)\)')
    class_instances = class_instance_pattern.findall(labels)
    
    if not class_instances:
        # No class instances found; return the original entry
        return modified_entry
    
    # Step 3: Organize class instances by class name
    class_to_instances = defaultdict(list)
    for cls, fields in class_instances:
        class_to_instances[cls].append(fields)
    
    # Step 4: Determine which classes to remove based on probability
    classes_to_remove = []
    for cls in class_names:
        if random.random() < probability:
            if cls in class_to_instances:
                classes_to_remove.append(cls)
    
    if not classes_to_remove:
        # No classes selected for removal; return the original entry
        return modified_entry
    
    # Debugging: Log which classes are selected for removal
    print(f"Classes selected for removal: {classes_to_remove}")
    
    # Step 5: Remove selected class instances from 'labels'
    # Reconstruct 'labels' as a list string excluding the classes to remove
    remaining_instances = [
        f"{cls}({fields})" for cls, fields in class_instances if cls not in classes_to_remove
    ]
    labels_modified = "[\n" + ",\n".join(remaining_instances) + "]"
    modified_entry['labels'] = labels_modified
    
    # Step 6: Remove selected class instances from 'result' list in 'text'
    # Assuming 'result = [ClassName(...), ...]'
    result_pattern = re.compile(r'(result\s*=\s*\[)([\s\S]*?)(\])', re.MULTILINE)
    result_match = result_pattern.search(text)
    
    if result_match:
        result_prefix, result_content, result_suffix = result_match.groups()
        
        # Extract individual class instances within 'result'
        result_class_instances = class_instance_pattern.findall(result_content)
        
        # Reconstruct 'result' list excluding the classes to remove
        remaining_result_instances = [
            f"{cls}({fields})" for cls, fields in result_class_instances if cls not in classes_to_remove
        ]
        if remaining_result_instances:
            result_content_modified = ",\n    ".join(remaining_result_instances)
            result_modified = f"{result_prefix}\n    {result_content_modified}\n{result_suffix}"
        else:
            result_modified = f"{result_prefix}\n]\n{result_suffix}"
        
        # Replace the old 'result' list with the modified one
        text = text[:result_match.start()] + result_modified + text[result_match.end():]
        modified_entry['text'] = text
    else:
        # 'result' list not found; proceed without modification
        pass
    
    # Step 7: Remove related phrases from 'unlabelled_sentence'
    # and the unlabelled text within 'text'
    
    # Function to remove phrases mentioning any of the classes to remove
    def remove_class_phrases(text_to_modify: str, classes: list) -> str:
        """
        Removes phrases mentioning any of the specified classes.
        
        Args:
            text_to_modify (str): The text containing sentences.
            classes (list): The list of class names to remove.
        
        Returns:
            str: The text with relevant phrases removed.
        """
        for cls in classes:
            # Define patterns to identify phrases mentioning the class
            # Example pattern: "and the Cat he has is 12 and is called Miau"
            pattern = re.compile(rf'\b(?:and\s+)?the\s+{re.escape(cls)}\b[^.]*', re.IGNORECASE)
            text_to_modify = pattern.sub('', text_to_modify)
        # Clean up any redundant spaces or punctuation
        text_to_modify = re.sub(r'\s+,', ',', text_to_modify)
        text_to_modify = re.sub(r'\s+', ' ', text_to_modify).strip()
        return text_to_modify
    
    # Remove from 'unlabelled_sentence'
    unlabelled_sentence_modified = remove_class_phrases(unlabelled_sentence, classes_to_remove)
    modified_entry['unlabelled_sentence'] = unlabelled_sentence_modified
    
    # Remove from unlabelled text in 'text' field
    # Assuming unlabelled text is after the line '# This is the text to analyze\ntext = "..."'
    # Adjust the regex based on the actual structure of 'text'
    unlabelled_text_pattern = re.compile(
        r'(# This is the text to analyze\s*text\s*=\s*["\'])([\s\S]*?)(["\']\n# The list called result contains)',
        re.MULTILINE
    )
    unlabelled_text_match = unlabelled_text_pattern.search(text)
    
    if unlabelled_text_match:
        prefix, unlabelled_text, suffix = unlabelled_text_match.groups()
        # Remove phrases mentioning the classes to remove
        unlabelled_text_filtered = remove_class_phrases(unlabelled_text, classes_to_remove)
        # Reconstruct the 'text' field with the modified unlabelled text
        text_modified = prefix + unlabelled_text_filtered + suffix
        modified_entry['text'] = text_modified
    else:
        # Unlabelled text pattern not found; proceed without modification
        pass
    
    # Final Check: Ensure that 'labels' and 'result' list have the same classes
    # Extract remaining class names from 'labels'
    remaining_labels_classes = class_instance_pattern.findall(labels_modified)
    remaining_labels_class_names = set(cls for cls, _ in remaining_labels_classes)
    
    # Extract remaining class names from 'result' list
    if result_match:
        remaining_result_class_instances = class_instance_pattern.findall(result_content_modified)
        remaining_result_class_names = set(cls for cls, _ in remaining_result_class_instances)
    else:
        remaining_result_class_names = set()
    
    # Compare both sets; they should be identical
    if remaining_labels_class_names != remaining_result_class_names:
        raise ValueError("Mismatch between 'labels' and 'result' list after applying negatives.")
    
    return modified_entry

if __name__ == "__main__":
    import json

    # Set random seed for reproducibility
    random.seed(42)

    # Define the example JSON object
    '''entry = {"ids": ["<urn:uuid:ce2e2d4d-f5f6-4796-a159-7624c53c7390>"],
            "task_id": "fineweb-edu_pretrain_gollie2",
            "scorer_cls": "src.tasks.fineweb-edu_pretrain.scorer.fineweb-edu_pretrainScorer",
            "labels": "[\nDog(name=\"Woof\", age=5),\n Cat(name=\"Miau\", age=12)]", 
            "text": "# The following lines describe the task definition\nfrom dataclasses import dataclass\nfrom typing import Dict, Any\n\n@dataclass\nclass Dog:\n    \"\"\"\n    a 4 legged animal that is said to be men's best friend\n    \"\"\"\n    name: str\n    # The name of the dog.\n\n    age: int\n    # The age of the dog.\n\n\n@dataclass\nclass Cat:\n    \"\"\"\n    a 4 legged animal that is relaxed and loves being home, they eat fish\n    \"\"\"\n    name: str\n    # The name of the cat.\n\n    age: int\n    # The age of the cat.\n\n\n# This is the text to analyze \ntext = \"the dog of my friend Luis is 5 years old and is called Woof, and the cat he has is 12 and is called Miau\"\n\n# The list called result contains the instances for the following events according to the guidelines above:\nresult = [\n    Dog(name=\"Woof\", age=5),\n    Cat(name=\"Miau\", age=12)]\n",
            "unlabelled_sentence": "the dog of my friend Luis is 5 years old and is called Woof, and the cat he has is 12 and is called Miau"
                
            }
    '''
    entry ={
        "ids": [
            "<urn:uuid:ce2e2d4d-f5f6-4796-a159-7624c53c7390>"
        ],
        "task_id": "fineweb-edu_pretrain_gollie2",
        "scorer_cls": "src.tasks.fineweb-edu_pretrain.scorer.fineweb-edu_pretrainScorer",
        "labels": "[\nDog(name=\"Woof\", age=5),\nTurtle(name=\"Shelly\", age=2),\nCat(name=\"Miau\", age=12),\nBird(name=\"Tweety\", age=3),\nDog(name=\"Rex\", age=7),\nBird(name=\"Polly\", age=4)]",
        "text": "# The following lines describe the task definition\nfrom dataclasses import dataclass\nfrom typing import Dict, Any\n\n@dataclass\nclass Dog:\n    \"\"\"\n    A 4-legged animal that is said to be men's best friend.\n    \"\"\"\n    name: str\n    # The name of the dog.\n\n    age: int\n    # The age of the dog.\n\n\n@dataclass\nclass Cat:\n    \"\"\"\n    A 4-legged animal that is relaxed and loves being home; they eat fish.\n    \"\"\"\n    name: str\n    # The name of the cat.\n\n    age: int\n    # The age of the cat.\n\n\n@dataclass\nclass Turtle:\n    \"\"\"\n    A slow-moving reptile often kept as a pet in aquariums or terrariums.\n    \"\"\"\n    name: str\n    # The name of the turtle.\n\n    age: int\n    # The age of the turtle.\n\n\n@dataclass\nclass Bird:\n    \"\"\"\n    A feathered animal capable of flight, often kept as pets for their singing or colorful appearance.\n    \"\"\"\n    name: str\n    # The name of the bird.\n\n    age: int\n    # The age of the bird.\n\n\n# This is the text to analyze \ntext = \"The dog of my friend Luis is 5 years old and is called Woof, the turtle he has is 2 and is called Shelly, the cat he has is 12 and is called Miau, and the bird he has is 3 and is called Tweety. Another dog named Rex is 7, and another bird named Polly is 4.\"\n\n# The list called result contains the instances for the following events according to the guidelines above:\nresult = [\n    Dog(name=\"Woof\", age=5),\n    Turtle(name=\"Shelly\", age=2),\n    Cat(name=\"Miau\", age=12),\n    Bird(name=\"Tweety\", age=3),\n    Dog(name=\"Rex\", age=7),\n    Bird(name=\"Polly\", age=4)]\n",
        "unlabelled_sentence": "The dog of my friend Luis is 5 years old and is called Woof, the turtle he has is 2 and is called Shelly, the cat he has is 12 and is called Miau, and the bird he has is 3 and is called Tweety. Another dog named Rex is 7, and another bird named Polly is 4."
    }



    # Apply the negatives function with probability p
    p = 0.7 #for testing  # Adjust the probability as needed
    
    

    # Print the original entry
    print("Original Entry:")
    print("-----------------")
    print(json.dumps(entry, indent=4))

    print("\n")

    # Print the modified entry
    modified_entry_masking = apply_entity_type_masking(entry, p)
    print("\n\nModified Entry with Masking:")
    print("-----------------")
    print(json.dumps(modified_entry_masking, indent=4))
    
    modified_entry_negatives = apply_negatives(entry, p)
    print("\n\nModified Entry with Negatives:")
    print("-----------------")
    print(json.dumps(modified_entry_negatives, indent=4))
    
    print("Expected output from modified entry with negatives:")
    print("----------------------------------------------------")
    
    '''expected_output_with_negatives_applied = {
    "ids": ["<urn:uuid:ce2e2d4d-f5f6-4796-a159-7624c53c7390>"],
    "task_id": "fineweb-edu_pretrain_gollie2",
    "scorer_cls": "src.tasks.fineweb-edu_pretrain.scorer.fineweb-edu_pretrainScorer",
    "labels": "[\nDog(name=\"Woof\", age=5)]",
    "text": "# The following lines describe the task definition\nfrom dataclasses import dataclass\nfrom typing import Dict, Any\n\n@dataclass\nclass Dog:\n    \"\"\"\n    a 4 legged animal that is said to be men's best friend\n    \"\"\"\n    name: str\n    # The name of the dog.\n\n    age: int\n    # The age of the dog.\n\n\n@dataclass\nclass Cat:\n    \"\"\"\n    a 4 legged animal that is relaxed and loves being home, they eat fish\n    \"\"\"\n    name: str\n    # The name of the cat.\n\n    age: int\n    # The age of the cat.\n\n\n# This is the text to analyze \ntext = \"the dog of my friend Luis is 5 years old and is called Woof\"\n\n# The list called result contains the instances for the following events according to the guidelines above:\nresult = [\n    Dog(name=\"Woof\", age=5)]\n",
    "unlabelled_sentence": "the dog of my friend Luis is 5 years old and is called Woof"
    }'''
    
    expected_output_with_negatives_applied = {
        "ids": [
            "<urn:uuid:ce2e2d4d-f5f6-4796-a159-7624c53c7390>"
        ],
        "task_id": "fineweb-edu_pretrain_gollie2",
        "scorer_cls": "src.tasks.fineweb-edu_pretrain.scorer.fineweb-edu_pretrainScorer",
        "labels": "[\nDog(name=\"Woof\", age=5),\nTurtle(name=\"Shelly\", age=2),\nDog(name=\"Rex\", age=7)]",
        "text": "# The following lines describe the task definition\nfrom dataclasses import dataclass\nfrom typing import Dict, Any\n\n@dataclass\nclass Dog:\n    \"\"\"\n    A 4-legged animal that is said to be men's best friend.\n    \"\"\"\n    name: str\n    # The name of the dog.\n\n    age: int\n    # The age of the dog.\n\n\n@dataclass\nclass Cat:\n    \"\"\"\n    A 4-legged animal that is relaxed and loves being home; they eat fish.\n    \"\"\"\n    name: str\n    # The name of the cat.\n\n    age: int\n    # The age of the cat.\n\n\n@dataclass\nclass Turtle:\n    \"\"\"\n    A slow-moving reptile often kept as a pet in aquariums or terrariums.\n    \"\"\"\n    name: str\n    # The name of the turtle.\n\n    age: int\n    # The age of the turtle.\n\n\n@dataclass\nclass Bird:\n    \"\"\"\n    A feathered animal capable of flight, often kept as pets for their singing or colorful appearance.\n    \"\"\"\n    name: str\n    # The name of the bird.\n\n    age: int\n    # The age of the bird.\n\n\n# This is the text to analyze \ntext = \"The dog of my friend Luis is 5 years old and is called Woof, the turtle he has is 2 and is called Shelly. Another dog named Rex is 7.\"\n\n# The list called result contains the instances for the following events according to the guidelines above:\nresult = [\n    Dog(name=\"Woof\", age=5),\n    Turtle(name=\"Shelly\", age=2),\n    Dog(name=\"Rex\", age=7)\n]\n",
        "unlabelled_sentence": "The dog of my friend Luis is 5 years old and is called Woof, the turtle he has is 2 and is called Shelly. Another dog named Rex is 7."
    }


    
    print(json.dumps(expected_output_with_negatives_applied, indent=4))