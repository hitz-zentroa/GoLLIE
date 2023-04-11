import logging
from argparse import ArgumentParser
import json
from typing import Type
import os
from rich.progress import Progress, TimeElapsedColumn, SpinnerColumn


parser = ArgumentParser("generate_data", description="Generate Code formatted data.")

parser.add_argument(
    "-c",
    "--configs",
    nargs="+",
    dest="configs",
    type=str,
    help="The list of configuration files.",
)
parser.add_argument(
    "-o",
    "--output",
    type=str,
    dest="output_dir",
    default="data/processed",
    help="Output directory where files will be saved.",
)
parser.add_argument(
    "--overwrite_output_dir",
    action="store_true",
    help="Whether to overwrite the output dir.",
)


def get_class(class_path: str) -> Type:
    components = class_path.split(".")
    mod = __import__(components[0])
    for comp in components[1:]:
        mod = getattr(mod, comp)

    return mod


def main(args):
    os.makedirs(args.output_dir, exist_ok=True)

    for config_file in args.configs:
        with open(config_file, "rt") as f:
            config = json.load(f)

        dataloader_cls = get_class(config["dataloader_cls"])
        sampler_cls = get_class(config["sampler_cls"])

        if "train_file" in config:
            dataloader = dataloader_cls(config["train_file"], **config)
            for task in config["tasks"]:
                sampler = sampler_cls(
                    dataloader,
                    task=task,
                    split="train",
                    **config,
                    **config["task_configuration"][task],
                )

                output_name = (
                    f"{config['dataset_name'].lower()}.{task.lower()}.train.jsonl"
                )

                if (
                    os.path.exists(os.path.join(args.output_dir, output_name))
                    and not args.overwrite_output_dir
                ):
                    logging.warning(f"Skipping {output_name} because it already exists.")
                    continue

                with open(
                    os.path.join(args.output_dir, output_name), "w"
                ) as _file, Progress(
                    SpinnerColumn(),
                    *Progress.get_default_columns(),
                    TimeElapsedColumn(),
                ) as progress:
                    task = progress.add_task(
                        f"[cyan]{config['dataset_name']}-{task}-train",
                        total=len(dataloader),
                    )
                    ids = []
                    for elem in sampler:
                        _file.write(f"{json.dumps(elem, ensure_ascii=False)}\n")
                        if ids != elem["ids"]:
                            ids = elem["ids"]
                            progress.update(task, advance=len(ids))

        if "dev_file" in config:
            dataloader = dataloader_cls(config["dev_file"], **config)
            for task in config["tasks"]:
                sampler = sampler_cls(
                    dataloader,
                    task=task,
                    split="dev",
                    **config,
                    **config["task_configuration"][task],
                )

                output_name = f"{config['dataset_name'].lower()}.{task.lower()}.dev.jsonl"

                if (
                    os.path.exists(os.path.join(args.output_dir, output_name))
                    and not args.overwrite_output_dir
                ):
                    logging.warning(f"Skipping {output_name} because it already exists.")
                    continue

                with open(
                    os.path.join(args.output_dir, output_name), "w"
                ) as _file, Progress(
                    SpinnerColumn(),
                    *Progress.get_default_columns(),
                    TimeElapsedColumn(),
                ) as progress:
                    task = progress.add_task(
                        f"[cyan]{config['dataset_name']}-{task}-dev",
                        total=len(dataloader),
                    )
                    ids = []
                    for elem in sampler:
                        _file.write(f"{json.dumps(elem, ensure_ascii=False)}\n")
                        if ids != elem["ids"]:
                            ids = elem["ids"]
                            progress.update(task, advance=len(ids))

        if "test_file" in config:
            dataloader = dataloader_cls(config["test_file"], **config)
            for task in config["tasks"]:
                sampler = sampler_cls(
                    dataloader,
                    task=task,
                    split="test",
                    **config,
                    **config["task_configuration"][task],
                )

                output_name = (
                    f"{config['dataset_name'].lower()}.{task.lower()}.test.jsonl"
                )

                if (
                    os.path.exists(os.path.join(args.output_dir, output_name))
                    and not args.overwrite_output_dir
                ):
                    logging.warning(f"Skipping {output_name} because it already exists.")
                    continue

                with open(
                    os.path.join(args.output_dir, output_name), "w"
                ) as _file, Progress(
                    SpinnerColumn(),
                    *Progress.get_default_columns(),
                    TimeElapsedColumn(),
                ) as progress:
                    task = progress.add_task(
                        f"[cyan]{config['dataset_name']}-{task}-test",
                        total=len(dataloader),
                    )
                    ids = []
                    for elem in sampler:
                        _file.write(f"{json.dumps(elem, ensure_ascii=False)}\n")
                        if ids != elem["ids"]:
                            ids = elem["ids"]
                            progress.update(task, advance=len(ids))


if __name__ == "__main__":
    args = parser.parse_args()
    main(args)
