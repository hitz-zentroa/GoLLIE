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

    config_template: str = field(
        default="vicuna_v1.1",
        metadata={
            "help": (
                "The config template to use. Available templates: 'one_shot', 'vicuna_v1.1', 'koala_v1', 'dolly_v2',"
                " 'oasst_pythia', 'stablelm', 'baize', 'rwkv', 'openbuddy', 'phoenix', 'chatgpt', 'claude', 'mpt'"
            )
        },
    )

    language: str = field(
        default="en",
        metadata={"help": "The language to do phrase paraphrasing."},
    )

    generation_args_json: str = field(
        default=None,
        metadata={"help": "The generation args json file."},
    )
