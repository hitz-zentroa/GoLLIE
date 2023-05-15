import json
import logging
import os
from argparse import ArgumentParser
from itertools import cycle
from typing import Type

from rich.progress import Progress, SpinnerColumn, TimeElapsedColumn


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
        seeds = config.get("seed", 0)
        if isinstance(seeds, int):
            seeds = [seeds]
        label_noise = config.get("label_noise_prob", 0.0)
        if isinstance(label_noise, float):
            label_noise = cycle([label_noise])

        if "train_file" in config:
            dataloader = dataloader_cls(config["train_file"], **config)
            for ie_task in config["tasks"]:
                for seed, noise_prob in zip(seeds, label_noise):
                    config["seed"] = seed
                    config["label_noise_prob"] = noise_prob
                    sampler = sampler_cls(
                        dataloader,
                        task=ie_task,
                        split="train",
                        **config,
                        **config["task_configuration"][ie_task],
                    )

                    output_name = f"{config['dataset_name'].lower()}.{ie_task.lower()}.train.{seed}.jsonl"

                    if os.path.exists(os.path.join(args.output_dir, output_name)) and not args.overwrite_output_dir:
                        logging.warning(f"Skipping {output_name} because it already exists.")
                        continue

                    with open(os.path.join(args.output_dir, output_name), "w") as _file, Progress(
                        SpinnerColumn(),
                        *Progress.get_default_columns(),
                        TimeElapsedColumn(),
                    ) as progress:
                        task = progress.add_task(
                            f"[cyan]{config['dataset_name']}-{ie_task}-train-{seed}",
                            total=len(dataloader),
                        )
                        ids = []
                        for elem in sampler:
                            _file.write(f"{json.dumps(elem, ensure_ascii=False)}\n")
                            if ids != elem["ids"]:
                                ids = elem["ids"]
                                progress.update(task, advance=len(ids))

                    logging.info(f"Data saved to {os.path.abspath(os.path.join(args.output_dir, output_name))}")

        if "dev_file" in config:
            config["seed"] = 0
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

                if os.path.exists(os.path.join(args.output_dir, output_name)) and not args.overwrite_output_dir:
                    logging.warning(f"Skipping {output_name} because it already exists.")
                    continue

                with open(os.path.join(args.output_dir, output_name), "w") as _file, Progress(
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

                logging.info(f"Data saved to {os.path.abspath(os.path.join(args.output_dir, output_name))}")

        if "test_file" in config:
            config["seed"] = 0
            dataloader = dataloader_cls(config["test_file"], **config)
            for task in config["tasks"]:
                sampler = sampler_cls(
                    dataloader,
                    task=task,
                    split="test",
                    **config,
                    **config["task_configuration"][task],
                )

                output_name = f"{config['dataset_name'].lower()}.{task.lower()}.test.jsonl"

                if os.path.exists(os.path.join(args.output_dir, output_name)) and not args.overwrite_output_dir:
                    logging.warning(f"Skipping {output_name} because it already exists.")
                    continue

                with open(os.path.join(args.output_dir, output_name), "w") as _file, Progress(
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

                logging.info(f"Data saved to {os.path.abspath(os.path.join(args.output_dir, output_name))}")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
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

    args = parser.parse_args()
    main(args)
