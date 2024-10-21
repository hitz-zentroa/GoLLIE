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
    result = "\n# The list " + text.split("# The list ")[1]


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
    if n_remove >= n_spans: #Added conditional to avoid removing all spans.
        n_remove = n_spans -1 #Change to avoid removing all spans if p is to high.
        
    if n_spans == 0: # Check for empty existing spans to avoid empty prompts.
        print("No existing spans found. Skipping apply_negatives.")
        return entry
    
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
        modified_labels = re.sub(rf"\n?\s*[a-zA-Z]+\({re.escape(span)}.*?\),?", "", modified_labels)  # Use re.escape to handle special characters
    modified_labels = modified_labels.strip()
    
    if not modified_labels or modified_labels == "[]":  # Handle empty labels
        modified_labels = ""  # Or some other default value if needed
        result = "# The list called result contains the instances for the following events according to the guidelines above:\nresult ="  # Correct format and no list if empty modified_labels
    else: #added else statement
        result = "# The list called result contains the instances for the following events according to the guidelines above:\nresult =" + modified_labels.lstrip("[")  # Correctly adds `modified_labels`
    
    modified_entry["labels"] = modified_labels

    # Concatenate the guidelines, unlabelled_text, and result to get the modified text
    modified_text = guidelines + unlabelled_text + result
    modified_entry["text"] = modified_text


    return modified_entry



if __name__ == "__main__":
    import json

    # Set random seed for reproducibility
    random.seed(42)
    
    entries = []
    with open("/sorgin1/users/neildlf/GoLLIE-dev/data/pretraining_data_processed_w_examples/miniset.jsonl") as f:
        for line in f:
            entries.append(json.loads(line))

    outputs = []
    for entry in entries:

        # Apply the negatives function with probability p
        p = 0.2 #for testing  # Adjust the probability as needed
        
        
        # Print the original entry
        print("Original Entry:")
        print("-----------------")
        print(json.dumps(entry, indent=4))
        #save original entry
        outputs.append(f"Original Entry:{entry}\n")
        
        print("\n")

        # Print the modified entry
        #modified_entry_masking = apply_entity_type_masking(entry, p)
        #print("\n\nModified Entry with Masking:")
        #print("-----------------")
        #print(json.dumps(modified_entry_masking, indent=4))
        
        modified_entry_negatives = apply_negatives(entry, p)
        print("\n\nModified Entry with Negatives:")
        print("-----------------")
        print(json.dumps(modified_entry_negatives, indent=4))
        outputs.append(f"Modified Entry with Negatives:{modified_entry_negatives}\n")
        
    #store the outputs
    with open("outputs.txt", "w") as f:
        f.writelines(outputs)        
    