import json
import os
from argparse import ArgumentParser

from src.tasks import TASK_ID_TO_TASKS


def main(args):
    # Create the directory if not exists
    os.makedirs(args.output_dir, exist_ok=True)

    with open(args.input_file) as f:
        lines = [json.loads(line) for line in f]

    basename = os.path.basename(args.input_file).rstrip(".jsonl")
    output_path = os.path.join(args.output_dir, f"{basename}.{args.row}.py")
    with open(output_path, "wt", encoding="utf-8") as f:
        line = lines[args.row]
        imports = TASK_ID_TO_TASKS[line["task_id"]]

        print(f"from {imports} import *", file=f)
        print("from src.tasks.utils_typing import Entity, Value, Relation, Event", file=f)
        print("from dataclasses import dataclass", file=f)
        print(line["text"], file=f)
        print(f"labels = {line['labels']}", file=f)

    os.system(f"black {output_path}")
    os.system(f"ruff check {output_path} --fix")


if __name__ == "__main__":
    parser = ArgumentParser("Visualize examples")

    parser.add_argument("-i", "--input_file", dest="input_file", type=str)
    parser.add_argument("-r", "--row", dest="row", type=int, default=0)
    parser.add_argument("-o", "--output_dir", dest="output_dir", default=".ignore/examples")

    args = parser.parse_args()
    main(args)
