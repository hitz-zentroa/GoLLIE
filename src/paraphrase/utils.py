import json
import math
from typing import Dict, Iterator, List, Sized

import black

from src.tasks import task_id_to_guidelines


def batch(iterable: Sized, n=1) -> Iterator:
    """
    Yield successive n-sized chunks from iterable.

    Args:
        iterable (`Sized`):
            The iterable to split.
        n (`int`, optional):
            The size of the chunks. Defaults to `1`.

    Yields:
        `Iterator`:
            An iterator with the chunks.
    """
    l: int = len(iterable)
    p: int = math.ceil(l / n)
    for ndx in range(0, l, p):
        yield iterable[ndx : min(ndx + p, l)]


def update_guidelines(paraphrases: List[str], task_name: str, language: str, num_paraphrases_per_guideline: int):
    """
    Update the guidelines for a given task.

    Args:
        paraphrases (List[str]): The paraphrases.
        task_name (str): The task name.
        language (str): The language for which the paraphrases were generated.
        num_paraphrases_per_guideline (int): The number of paraphrases generated per guideline.

    Returns:
        The updated guidelines.
    """

    guidelines = task_id_to_guidelines(task_name)
    paraphrases = batch(paraphrases, n=num_paraphrases_per_guideline)
    for guideline in guidelines.values():
        guideline[language].extend(next(paraphrases))
    return guidelines


def get_num_return_sentences(config_path: str):
    """
    Get the number of sentences to return.

    Args:
        config_path (str): The path to the config json file.

    Returns:
        The number of sentences to return.
    """

    with open(config_path, "r") as f:
        config = json.load(f)
    return config["num_return_sequences"]


def format_guidelines_as_py(guidelines: Dict[str, Dict[str, List[str]]]):
    guidelines_py = json.dumps(guidelines, indent=4)
    guidelines_py = f"GUIDELINES = {{{guidelines_py}}}"
    guidelines_py = black.format_str(guidelines_py, mode=black.Mode())
    return guidelines_py
