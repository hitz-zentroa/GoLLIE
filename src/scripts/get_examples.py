import argparse
import json

from src.generate_data import get_class


def get_top_label_per_class(config, top_k: int = 10):
    """
    Get the top k labels per class of the train set
    Args:
        config (dict): The config dictionary
        top_k (int): The number of top labels to return
    Returns:
        (dict): A dictionary with the top k labels per class
    """
    if config["tasks"] != ["NER"] and "ner" not in config["tasks"][0].lower():
        raise ValueError(f"This function only supports NER task. Got {config['tasks']}")
    dataloader_cls = get_class(config["dataloader_cls"])
    if "train_file" not in config:
        raise ValueError("train_file is not specified in config")
    dataloader = dataloader_cls(config["train_file"], **config)
    ENTITY_TO_CLASS_MAPPING = dataloader.ENTITY_TO_CLASS_MAPPING
    {v: k for k, v in ENTITY_TO_CLASS_MAPPING.items()}

    ENTITY_COUNT = {str(k).split(".")[-1][:-2]: {} for k in ENTITY_TO_CLASS_MAPPING.values()}
    print(ENTITY_COUNT)
    for example in dataloader:
        entities = example["entities"]
        for entity in entities:
            ENTITY_COUNT[str(entity).split("(")[0]][entity.span] = (
                ENTITY_COUNT[str(entity).split("(")[0]].get(entity.span, 0) + 1
            )

    top_k_labels = {}

    for entity_type, entity_count in ENTITY_COUNT.items():
        top_k_labels[entity_type] = sorted(entity_count.items(), key=lambda x: x[1], reverse=True)[:top_k]

    print("Top k labels per class")
    print(top_k_labels)

    print("\n\nTop k labels per class (formatted)\n")
    for entity_type, entity_count in top_k_labels.items():
        print(f"{entity_type}. Examples: {', '.join([f'{k}' for k, v in entity_count])}.\n")

    print("\n\nTop k labels per class (Python List)\n")

    for entity_type, entity_count in top_k_labels.items():
        print(entity_type)
        print([f"{k}" for k, v in entity_count])

    return top_k_labels


def add_examples(config, top_k, lang="en"):
    # Get entity to example_name mapping
    entity_to_example_name = {}
    prompt_template = config["dataloader_cls"]
    prompt_template = prompt_template.split(".")[:3]
    guilines_gold = prompt_template + ["guidelines_gold.py"]
    prompt_template += ["prompts.py"]

    prompt_template = "/".join(prompt_template)

    if config["tasks"] == ["CrossNER_POLITICS"]:
        prompt_template = prompt_template.replace("prompts.py", "prompts_politics.py")
    elif config["tasks"] == ["CrossNER_MUSIC"]:
        prompt_template = prompt_template.replace("prompts.py", "prompts_music.py")
    elif config["tasks"] == ["CrossNER_AI"]:
        prompt_template = prompt_template.replace("prompts.py", "prompts_ai.py")
    elif config["tasks"] == ["CrossNER_NATURAL_SCIENCE"]:
        prompt_template = prompt_template.replace("prompts.py", "prompts_natural_science.py")
    elif config["tasks"] == ["CrossNER_LITERATURE"]:
        prompt_template = prompt_template.replace("prompts.py", "prompts_literature.py")

    guilines_gold = "/".join(guilines_gold)

    with open(prompt_template, "r", encoding="utf8") as f:
        lines = f.readlines()
    i = 0
    while i < len(lines):
        if lines[i].startswith("class"):
            entity = lines[i].split("(")[0].split(" ")[1]
            i += 1
            while not lines[i].strip().startswith("span"):
                i += 1

            name = lines[i].split("{")[1].split("}")[0]
            entity_to_example_name[entity] = name
        i += 1

    print(f"entity_to_example_name:\n{json.dumps(entity_to_example_name, indent=4)}")

    # Get top k labels per class
    top_k_labels = get_top_label_per_class(config, top_k)

    # Add examples to guilines
    examples = {}
    for entity_type, entity_count in top_k_labels.items():
        examples[entity_to_example_name[entity_type]] = {lang: [f"{k}" for k, v in entity_count]}

    print(f"\nEXAMPLES={json.dumps(examples, indent=4)}", file=open(guilines_gold, "a", encoding="utf8"))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", type=str, required=True, help="The config file")
    parser.add_argument("--top_k", type=int, default=10, help="The number of top labels to return")
    parser.add_argument("--add_to_guidelines", action="store_true", help="Add examples to guidelines_gold.py")
    args = parser.parse_args()
    config = json.load(open(args.config, "r"))
    if args.add_to_guidelines:
        add_examples(config, args.top_k)
    else:
        get_top_label_per_class(config, args.top_k)
