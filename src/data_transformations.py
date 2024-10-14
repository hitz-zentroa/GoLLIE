import random
import re
from typing import Dict, Any
import ast
import random
import sys
import nltk
import spacy
from collections import defaultdict

# Load spaCy model for sentence segmentation used in negatives
nlp = spacy.load("en_core_web_sm")


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



def apply_negatives(entry, ratio=0.2):
    """
    Modify a dataset entry by introducing negative examples.
    
    This function removes a percentage of entities from the entry's text fields,
    effectively creating a "negative" version of the original data. The function
    ensures consistency across multiple fields, removing references from all
    relevant parts of the entry.
    
    Args:
        entry (dict): The dataset entry to modify, containing multiple fields such as
                      'unlabelled_sentence', 'labels', 'text'.
        ratio (float): The ratio of spans to remove from the text (default is 0.2).
    
    Returns:
        dict: A new dictionary representing the modified dataset entry with negative examples.
    """
    # Extract entry components
    unlabelled_sentence = entry["unlabelled_sentence"]
    labels = entry["labels"]
    text = entry["text"]


    # Split text into different parts
    guidelines = text.split("# This is the text to analyze")[0]
    unlabelled_text = text.split("# This is the text to analyze")[1].split("# The list ")[0]
    result = "# The list " + text.split("# The list ")[1]


    # Make a copy of the entry for modification
    modified_entry = entry.copy()

    # Segment text into sentences using spaCy
    doc = nlp(unlabelled_sentence)
    sentences = [sent for sent in doc.sents for sent in sent.text.split('\n') if sent]


    # Get the spans of the annotations in the text
    spans_re = re.compile(r'"(.*?)"')
    spans = spans_re.findall(labels)


    # Get the existing spans in the text
    existing_spans = [span for span in spans if span in unlabelled_sentence]


    # Remove a percentage of spans from the text given the ratio
    n_spans = len(existing_spans)
    n_remove = int(n_spans * ratio)
    spans_to_remove = random.sample(existing_spans, n_remove)


    # Remove spans from the unlabelled_sentence
    filtered_sentence = [line for line in sentences if not any(span in line for span in spans_to_remove)]


    # Update the unlabelled_sentence and unlabelled_text
    modified_entry["unlabelled_sentence"] = " ".join(filtered_sentence)
    unlabelled_text = "# This is the text to analyze\n" + " ".join(filtered_sentence)


    # Remove spans from the labels field
    modified_labels = labels
    for span in spans_to_remove:
        # Remove lines in the labels that contain the span
        modified_labels = re.sub(r'.*' + re.escape(span) + r'.*\n?', '', modified_labels)
    modified_entry["labels"] = modified_labels

    # Update the result field
    result = "# The list called result contains the instances for the following events according to the guidelines above:\nresult=" + modified_labels

    # Concatenate the guidelines, unlabelled_text, and result to get the modified text
    modified_text = guidelines + unlabelled_text + result
    modified_entry["text"] = modified_text


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
    p = 0.3 #for testing  # Adjust the probability as needed
    
    
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