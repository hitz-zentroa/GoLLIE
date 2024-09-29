import argparse
import json
import glob
import os
import random
import spacy
import re
from typing import List, Dict, Any
import spacy

def parse_labels_recursive(labels_str: str) -> List[Dict]:
    """
    Recursively parses the serialized dataclass string in the 'labels' field
    and converts it into a list of dictionaries.
    """
    labels_str = labels_str.replace('\n', '').replace('    ', '').strip()
    
    # Regular expression to match dataclass instances
    pattern = re.compile(r'(\w+)\((.*?)\)')
    
    def parse_arguments(arg_str):
        args = {}
        # Split by comma not within parentheses or brackets
        parts = re.split(r',\s*(?![^()]*\))', arg_str)
        for part in parts:
            if not part:
                continue
            if '=' not in part:
                continue
            key, value = part.split('=', 1)
            key = key.strip()
            value = value.strip()
            
            # Check for nested dataclass
            if '(' in value and ')' in value:
                nested_match = pattern.match(value)
                if nested_match:
                    nested_class, nested_args = nested_match.groups()
                    args[key] = parse_arguments(nested_args)
                else:
                    args[key] = value.strip('"').strip("'")
            elif value.startswith('[') and value.endswith(']'):
                # Handle lists
                list_content = value[1:-1].strip()
                if list_content:
                    # Check if list items are dataclass instances
                    list_items = []
                    for item in re.findall(r'\w+\(.*?\)', list_content):
                        nested_match = pattern.match(item)
                        if nested_match:
                            nested_class, nested_args = nested_match.groups()
                            list_items.append({
                                'class': nested_class,
                                'attributes': parse_arguments(nested_args)
                            })
                        else:
                            # Handle simple list items
                            list_items.append(item.strip('"').strip("'"))
                    args[key] = list_items
                else:
                    args[key] = []
            else:
                # Handle simple types and integers
                if value.isdigit():
                    args[key] = int(value)
                else:
                    args[key] = value.strip('"').strip("'")
        return args
    
    # Find all top-level dataclass instances
    matches = pattern.findall(labels_str)
    parsed_labels = []
    for match in matches:
        class_name, arg_str = match
        args = parse_arguments(arg_str)
        parsed_label = {'class': class_name, 'attributes': args}
        parsed_labels.append(parsed_label)
    
    return parsed_labels

def classify_difficulty(parsed_labels: List[Dict]) -> float:
    """
    Assigns a difficulty score to a document based on predefined heuristics.
    Example Heuristics:
    - Number of annotations
    - Length of the text
    """
    # heuristic 1: Number of annotations
    num_annotations = len(parsed_labels)
    
    # heuristic 2: Length of the text
    text_length = sum(len(label['attributes']['text']) for label in parsed_labels)
    
    # Example difficulty score
    difficulty_score = num_annotations + text_length
    
    return difficulty_score


def add_negatives(parsed_labels: List[Dict], all_possible_classes: List[str], negative_proportion: float = 0.15) -> List[Dict]:
    """
    Introduces negative classes by adding annotations for classes not present in the text.
    
    Args:
    - parsed_labels: List of current annotations.
    - all_possible_classes: List of all possible classes.
    - negative_proportion: Proportion of negative classes to add.
    
    Returns:
    - Updated list of annotations with negatives.
    """
    present_classes = {label['class'] for label in parsed_labels}
    negative_classes = [cls for cls in all_possible_classes if cls not in present_classes]
    
    num_negatives = max(1, int(len(negative_classes) * negative_proportion))
    selected_negatives = random.sample(negative_classes, min(num_negatives, len(negative_classes)))
    
    for neg in selected_negatives:
        parsed_labels.append({'class': neg, 'attributes': {'value': None}})
    
    return parsed_labels




def mask_entities(text: str, parsed_labels: List[Dict], mask_percentage: float = 0.15) -> (str, List[Dict]):
    """
    Masks a percentage of entities in the text and updates annotations.
    
    Args:
    - text: Original text.
    - parsed_labels: Current list of annotations.
    - mask_percentage: Fraction of entities to mask.
    
    Returns:
    - Masked text.
    - Updated list of annotations with masked entities.
    """
    doc = nlp(text)
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    
    num_to_mask = max(1, int(len(entities) * mask_percentage))
    entities_to_mask = random.sample(entities, min(num_to_mask, len(entities)))
    
    masked_text = text
    for ent_text, ent_label in entities_to_mask:
        masked_text = masked_text.replace(ent_text, "[MASK]")
    
    # Optionally, adjust annotations to reflect masked entities
    # This depends on how your model should interpret masked entities
    # For example, you might want to remove or mark certain annotations
    # Here, we keep annotations as is
    
    return masked_text, entities_to_mask


# Load SpaCy model globally to avoid reloading in each function call
nlp = spacy.load("en_core_web_sm")

def parse_labels_recursive(labels_str: str) -> List[Dict]:
    """
    Recursively parses the serialized dataclass string in the 'labels' field
    and converts it into a list of dictionaries.
    """
    labels_str = labels_str.replace('\n', '').replace('    ', '').strip()
    
    # Regular expression to match dataclass instances
    pattern = re.compile(r'(\w+)\((.*?)\)')
    
    def parse_arguments(arg_str):
        args = {}
        # Split by comma not within parentheses or brackets
        parts = re.split(r',\s*(?![^()]*\))', arg_str)
        for part in parts:
            if not part:
                continue
            if '=' not in part:
                continue
            key, value = part.split('=', 1)
            key = key.strip()
            value = value.strip()
            
            # Check for nested dataclass
            if '(' in value and ')' in value:
                nested_match = pattern.match(value)
                if nested_match:
                    nested_class, nested_args = nested_match.groups()
                    args[key] = parse_arguments(nested_args)
                else:
                    args[key] = value.strip('"').strip("'")
            elif value.startswith('[') and value.endswith(']'):
                # Handle lists
                list_content = value[1:-1].strip()
                if list_content:
                    # Check if list items are dataclass instances
                    list_items = []
                    for item in re.findall(r'\w+\(.*?\)', list_content):
                        nested_match = pattern.match(item)
                        if nested_match:
                            nested_class, nested_args = nested_match.groups()
                            list_items.append({
                                'class': nested_class,
                                'attributes': parse_arguments(nested_args)
                            })
                        else:
                            # Handle simple list items
                            list_items.append(item.strip('"').strip("'"))
                    args[key] = list_items
                else:
                    args[key] = []
            else:
                # Handle simple types and integers
                if value.isdigit():
                    args[key] = int(value)
                else:
                    args[key] = value.strip('"').strip("'")
        return args
    
    # Find all top-level dataclass instances
    matches = pattern.findall(labels_str)
    parsed_labels = []
    for match in matches:
        class_name, arg_str = match
        args = parse_arguments(arg_str)
        parsed_label = {'class': class_name, 'attributes': args}
        parsed_labels.append(parsed_label)
    
    return parsed_labels

def classify_difficulty(parsed_labels: List[Dict]) -> float:
    """
    Assigns a difficulty score to a document based on predefined heuristics.
    """
    # Example heuristic: Number of annotations
    num_annotations = len(parsed_labels)
    
    # Additional heuristics can be added here
    # For example, counting specific classes that are considered more difficult
    complex_classes = {'InnovationLedTransformation', 'CollagenInformation'}
    num_complex_annotations = sum(1 for label in parsed_labels if label['class'] in complex_classes)
    
    # Example difficulty score
    difficulty_score = num_annotations + (num_complex_annotations * 2)
    
    return difficulty_score

def add_negatives(parsed_labels: List[Dict], all_possible_classes: List[str], negative_proportion: float = 0.15) -> List[Dict]:
    """
    Introduces negative classes by adding annotations for classes not present in the text.
    
    Args:
    - parsed_labels: List of current annotations.
    - all_possible_classes: List of all possible classes.
    - negative_proportion: Proportion of negative classes to add.
    
    Returns:
    - Updated list of annotations with negatives.
    """
    present_classes = {label['class'] for label in parsed_labels}
    negative_classes = [cls for cls in all_possible_classes if cls not in present_classes]
    
    num_negatives = max(1, int(len(negative_classes) * negative_proportion))
    selected_negatives = random.sample(negative_classes, min(num_negatives, len(negative_classes)))
    
    for neg in selected_negatives:
        parsed_labels.append({'class': neg, 'attributes': {'value': None}})
    
    return parsed_labels

def mask_entities(text: str, parsed_labels: List[Dict], mask_percentage: float = 0.15) -> (str, List[Dict]):
    """
    Masks a percentage of entities in the text and updates annotations.
    
    Args:
    - text: Original text.
    - parsed_labels: Current list of annotations.
    - mask_percentage: Fraction of entities to mask.
    
    Returns:
    - Masked text.
    - Updated list of annotations with masked entities.
    """
    doc = nlp(text)
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    
    num_to_mask = max(1, int(len(entities) * mask_percentage))
    entities_to_mask = random.sample(entities, min(num_to_mask, len(entities)))
    
    masked_text = text
    for ent_text, ent_label in entities_to_mask:
        masked_text = masked_text.replace(ent_text, "[MASK]")
    
    # Optionally, adjust annotations to reflect masked entities
    # This depends on how your model should interpret masked entities
    # For example, you might want to remove or mark certain annotations
    # Here, we keep annotations as is
    
    return masked_text, entities_to_mask

def prepare_data(strategy_flags: List[str], input_dir: str, output_dir: str, all_possible_classes: List[str]):
    """
    Prepares the pretraining data by applying the specified strategies.
    
    Args:
    - strategy_flags: List of strategies to apply.
    - input_dir: Directory containing raw JSONL files.
    - output_dir: Directory to save processed JSONL files.
    - all_possible_classes: List of all possible classes for negatives.
    """
    raw_files = glob.glob(os.path.join(input_dir, '*.jsonl'))
    processed_data = []
    difficulty_scores = {}
    
    for file in raw_files:
        with open(file, 'r') as f:
            for line in f:
                doc = json.loads(line)
                doc_id = doc['ids'][0]  # Assuming single ID per entry
                text_script = doc['text']
                labels_str = doc['labels']
                unlabelled_sentence = doc['unlabelled_sentence']
                
                # Parse labels
                parsed_labels = parse_labels_recursive(labels_str)
                
                # Apply Entity Masking
                if 'entity_masking' in strategy_flags:
                    # Extract the raw text from the script
                    # Assuming 'text = "..."' is present in the script
                    match = re.search(r'text\s*=\s*"(.+?)"', text_script, re.DOTALL)
                    if match:
                        raw_text = match.group(1)
                        masked_text, masked_entities = mask_entities(raw_text, parsed_labels, mask_percentage=0.15)
                        
                        # Replace the original text in the script with masked_text
                        text_script = re.sub(r'text\s*=\s*".+?"', f'text = "{masked_text}"', text_script, flags=re.DOTALL)
                    
                # Apply Negatives
                if 'negatives' in strategy_flags:
                    parsed_labels = add_negatives(parsed_labels, all_possible_classes, negative_proportion=0.15)
                
                # Assign difficulty scores for Curriculum Learning
                if 'curriculum_learning' in strategy_flags:
                    score = classify_difficulty(parsed_labels)
                    difficulty_scores[doc_id] = score
                
                # Update the labels in the script
                # Reconstruct the 'result' variable with updated parsed_labels
                result_str = "result = [\n"
                for label in parsed_labels:
                    class_name = label['class']
                    attributes = label['attributes']
                    
                    # Convert attributes back to dataclass instantiation string
                    attr_str = ", ".join([f'{k}="{v}"' if isinstance(v, str) else f'{k}={v}' for k, v in attributes.items()])
                    result_str += f'    {class_name}({attr_str}),\n'
                result_str += "]\n"
                
                # Replace the old result in the script with the new result_str
                text_script = re.sub(r'result\s*=\s*\[.*?\]', result_str, text_script, flags=re.DOTALL)
                
                # Prepare the processed entry
                processed_entry = {
                    "ids": [doc_id],
                    "task_id": doc['task_id'],
                    "scorer_cls": doc['scorer_cls'],
                    "labels": json.dumps(parsed_labels, ensure_ascii=False),
                    "text": text_script,
                    "unlabelled_sentence": unlabelled_sentence
                }
                
                processed_data.append(processed_entry)
    
    # Sort data if Curriculum Learning is enabled
    if 'curriculum_learning' in strategy_flags:
        processed_data = sorted(processed_data, key=lambda x: difficulty_scores.get(x['ids'][0], 0))
    
    # Ensure output directory exists
    os.makedirs(output_dir, exist_ok=True)
    
    # Save processed data
    output_file = os.path.join(output_dir, 'pretraining_data.jsonl')
    with open(output_file, 'w') as f:
        for entry in processed_data:
            json.dump(entry, f, ensure_ascii=False)
            f.write('\n')
    
    print(f"Data preparation with strategies {strategy_flags} completed. Saved to {output_dir}")
