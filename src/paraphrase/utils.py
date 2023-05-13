import json
import math
from typing import Dict, Iterator, List, Sized

import black


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


def clean_guidelines(guidelines: Dict[str, Dict[str, List[str]]]):
    """
    Clean the guidelines.

    Args:
        guidelines (Dict[str, Dict[str, List[str]]]): The guidelines.

    Returns:
        The cleaned guidelines.
    """

    for guideline in guidelines.values():
        for language in guideline.keys():
            for i in range(len(guideline[language])):
                text = guideline[language][i]
                text = text.replace("\n", " ")
                text = text.replace("\t", " ")
                text = " ".join(text.split())
                guideline[language][i] = text

    return guidelines


def update_guidelines(paraphrases: List[str], guidelines: Dict[str, Dict[str, List[str]]], language: str):
    """
    Update the guidelines for a given task.

    Args:
        paraphrases (List[str]): The paraphrases.
        guidelines (Dict[str, Dict[str, List[str]]]): The guidelines.
        language (str): The language for which the paraphrases were generated.

    Returns:
        The updated guidelines.
    """

    i = 0
    for guideline in guidelines.values():
        guideline[language].append(paraphrases[i])
        i += 1
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
    # Add a \n every 98 characters. Do not split words.
    for guideline in guidelines.values():
        for language in guideline.keys():
            for i in range(len(guideline[language])):
                text = guideline[language][i]

                # Remove \" and \' at the beginning and end of the string
                text = text.strip()
                text = text.strip('"').strip()
                text = text.strip("'").strip()

                words = text.split()
                c: int = 0
                for j in range(len(words)):
                    c += len(words[j])
                    if c > 98:
                        words[j] = "\n" + words[j]
                        c = 0
                text = " ".join(words)
                guideline[language][i] = text

    guidelines_py = json.dumps(guidelines, indent=4)
    guidelines_py = f"GUIDELINES = {guidelines_py}"
    guidelines_py = black.format_str(guidelines_py, mode=black.Mode())
    return guidelines_py
