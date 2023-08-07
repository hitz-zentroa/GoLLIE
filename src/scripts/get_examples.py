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
    if config["tasks"] != ["NER"]:
        raise ValueError("This function only supports NER task")
    dataloader_cls = get_class(config["dataloader_cls"])
    if "train_file" not in config:
        raise ValueError("train_file is not specified in config")
    dataloader = dataloader_cls(config["train_file"], **config)
    ENTITY_TO_CLASS_MAPPING = dataloader.ENTITY_TO_CLASS_MAPPING
    CLASS_TO_ENTITY_MAPPING = {v: k for k, v in ENTITY_TO_CLASS_MAPPING.items()}

    ENTITY_COUNT = {k: {} for k in ENTITY_TO_CLASS_MAPPING.keys()}

    for example in dataloader:
        entities = example["entities"]
        for entity in entities:
            ENTITY_COUNT[CLASS_TO_ENTITY_MAPPING[entity.__class__]][entity.span] = (
                ENTITY_COUNT[CLASS_TO_ENTITY_MAPPING[entity.__class__]].get(entity.span, 0) + 1
            )

    top_k_labels = {}

    for entity_type, entity_count in ENTITY_COUNT.items():
        top_k_labels[entity_type] = sorted(entity_count.items(), key=lambda x: x[1], reverse=True)[:top_k]

    print("Top k labels per class")
    print(top_k_labels)

    print("\n\nTop k labels per class (formatted)\n")
    for entity_type, entity_count in top_k_labels.items():
        print(f"{entity_type}. Examples: {', '.join([f'{k}' for k, v in entity_count])}.\n")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", type=str, required=True, help="The config file")
    parser.add_argument("--top_k", type=int, default=10, help="The number of top labels to return")
    args = parser.parse_args()
    config = json.load(open(args.config, "r"))
    get_top_label_per_class(config, args.top_k)
