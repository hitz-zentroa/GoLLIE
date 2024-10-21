from dataclasses import dataclass, field
from typing import List


@dataclass
class DataInferenceArguments:
    """
    Arguments pertaining to what data we are going to input our model for paraphrasing.
    """

    datasets: List[str] = field(
        default=None,
        metadata={"help": "The tasks to train on. Can be a list of tasks or a single task."},
    )

    language: str = field(
        default="en",
        metadata={"help": "The language to do phrase paraphrasing."},
    )

    generation_args_json: str = field(
        default=None,
        metadata={"help": "The generation args json file."},
    )
