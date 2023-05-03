from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class ModelArguments:
    """
    Arguments pertaining to which model/config/tokenizer we are going to fine-tune, or train from scratch.
    """

    model_name_or_path: Optional[str] = field(
        default=None,
        metadata={"help": "The local path or huggingface hub name of the model and tokenizer to use."},
    )

    torch_dtype: Optional[str] = field(
        default=None,
        metadata={
            "help": (
                "Override the default `torch.dtype` and load the model under this"
                " dtype. If `auto` is passed, the dtype will be automatically derived"
                " from the model's weights."
            ),
            "choices": ["auto", "bfloat16", "float16", "float32"],
        },
    )

    use_lora: bool = field(
        default=False,
        metadata={
            "help": (
                "Whether to use LoRA. If True, the model will be trained with LoRA: https://arxiv.org/abs/2106.09685"
            )
        },
    )

    int8_quantization: bool = field(
        default=False,
        metadata={
            "help": (
                "Whether to use int8 quantization. Requires bitsandbytes library:"
                " https://github.com/TimDettmers/bitsandbytes"
            )
        },
    )
    lora_weights_name_or_path: Optional[str] = field(
        default=None,
        metadata={
            "help": (
                "If the model has been trained with LoRA, "
                "path or huggingface hub name or local path to the pretrained weights."
            )
        },
    )

    lora_r: Optional[int] = field(
        default=8,
        metadata={"help": "Lora attention dimension."},
    )

    lora_alpha: Optional[float] = field(
        default=16,
        metadata={"help": "The alpha parameter for Lora scaling."},
    )
    lora_dropout: Optional[float] = field(
        default=0.05,
        metadata={"help": "The dropout probability for Lora layers."},
    )

    lora_target_modules: Optional[List[str]] = field(
        default_factory=list,
        metadata={
            "help": (
                "The target modules to which LoRA will be applied. If not specified, We"
                " will use the default modules for the model in huggingface PEFT library."
            )
        },
    )


@dataclass
class DataTrainingArguments:
    """
    Arguments pertaining to what data we are going to input our model for training and eval.
    """

    dataset_dir: str = field(
        default="~/CoLLIE/data/processed",
        metadata={"help": "The tasks to train on. Can be a list of tasks or a single task."},
    )

    train_tasks: List[str] = field(
        default=None,
        metadata={"help": "The tasks to train on. Can be a list of tasks or a single task."},
    )

    validation_tasks: List[str] = field(
        default=None,
        metadata={"help": "The tasks to train on. Can be a list of tasks or a single task."},
    )

    test_tasks: List[str] = field(
        default=None,
        metadata={"help": "The tasks to test on. Can be a list of tasks or a single task."},
    )

    max_seq_length: int = field(
        default=512,
        metadata={
            "help": (
                "The maximum total input sequence length after tokenization. Sequences"
                " longer than this will be truncated, sequences shorter will be padded."
            )
        },
    )

    ignore_pad_token_for_loss: bool = field(
        default=True,
        metadata={
            "help": "Whether to ignore the tokens corresponding to padded labels in the loss computation or not."
        },
    )

    use_dev_inference: bool = field(
        default=False,
        metadata={"help": "Use the development set for inference instead of the test set."},
    )

    evaluate_all_checkpoints: bool = field(
        default=False,
        metadata={"help": "Evaluate all checkpoints in the model directory."},
    )

    prompt_loss_weight: float = field(
        default=0.05,
        metadata={
            "help": (
                "The weight of the prompt tokens in the loss. If set to '0.05' the prompt tokens will have a total"
                " weight of 5% in the loss while the result tokens will have a total weight of 95%. Only used for"
                " computing the loss in the training data. Defaults to `0.05`."
            )
        },
    )
