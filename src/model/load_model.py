import logging
import os
from typing import List, Optional, Tuple

import torch

from transformers import (
    AutoConfig,
    AutoModelForCausalLM,
    AutoModelForSeq2SeqLM,
    AutoTokenizer,
    PreTrainedModel,
    PreTrainedTokenizerBase,
)
from transformers.models.auto.modeling_auto import (
    MODEL_FOR_CAUSAL_LM_MAPPING_NAMES,
    MODEL_FOR_SEQ_TO_SEQ_CAUSAL_LM_MAPPING_NAMES,
)

from .model_utils import get_trainable_parameters


def load_model_for_training(
    model_weights_name_or_path: str,
    int8_quantization: bool = False,
    use_lora: bool = False,
    lora_weights_name_or_path: Optional[str] = None,
    lora_target_modules: Optional[List[str]] = None,
    lora_r: Optional[int] = 8,
    lora_alpha: Optional[int] = 16,
    lora_dropout: Optional[float] = 0.05,
    torch_dtype: Optional[str] = None,
) -> Tuple[PreTrainedModel, PreTrainedTokenizerBase]:
    """
    Load any Decoder model for training.

    Args:
        model_weights_name_or_path (`str`):
            The path to your local model weights and tokenizer or huggingface model name.
        int8_quantization (`bool`, optional):
            Whether to use int8 quantization. Defaults to `False`.

            Requires bitsandbytes library: https://github.com/TimDettmers/bitsandbytes
        use_lora (`bool`, optional):
            Whether to use LORA. Defaults to False.

            See https://arxiv.org/pdf/2106.09685.pdf for more details.

            Requires huggingface PEFT library: https://github.com/huggingface/peft
        lora_weights_name_or_path (`Optional[str]`, optional):
            The name or path to the pre-trained LORA model weights. You can also provide
            a huggingface hub model name to load the weights from there. If not provided,
            the weights will be initialized randomly, this requires training the model.
            Defaults to `None`.
        lora_target_modules (`Optional[List[str]]`, optional):
            The list of modules to apply LORA to. If not provided, we will use PEFT
            default modules. Defaults to `None`.
        lora_r (`Optional[int]`, optional):
            Lora attention dimension. Defaults to `8`.
        lora_alpha (`Optional[int]`, optional):
            The alpha parameter for Lora scaling. Defaults to `16`.
        lora_dropout (`Optional[float]`, optional):
            The dropout probability for Lora layers. Defaults to 0.05.
        torch_dtype (`Optional[str]`, optional):
            Override the default `torch.dtype` and load the model under this dtype. If
            `auto` is passed, the dtype will be automatically derived from the model's
            weights. Defaults to `None`.

    Raises:
        `ValueError`:
            is raised when `int8_quantization=True` but `use_lora=False`.

    Returns:
        `Tuple[PreTrainedModel, PreTrainedTokenizerBase]`:
            The loaded model and tokenizer.
    """

    if int8_quantization and not use_lora:
        raise ValueError(
            "Training with Int8 quantization is only supported with LoRA. If you want"
            " to train in Int8, please add the flag --use_lora. You can only evaluate"
            " in Int8 without LoRA."
        )

    device_map = "auto"
    world_size = int(os.environ.get("WORLD_SIZE", 1))
    ddp = world_size != 1
    if ddp:
        device_map = {"": int(os.environ.get("LOCAL_RANK") or 0)}

    if int8_quantization:
        logging.info(f"Device map: {device_map}")

    logging.info(f"Loading model model from {model_weights_name_or_path}")

    config = AutoConfig.from_pretrained(model_weights_name_or_path)

    torch_dtype = torch_dtype if torch_dtype in ["auto", None] else getattr(torch, torch_dtype)
    logging.info(f"Loading model with dtype: {torch_dtype}")
    tokenizer: PreTrainedTokenizerBase = AutoTokenizer.from_pretrained(
        model_weights_name_or_path,
        add_eos_token=True,
    )

    if config.model_type in MODEL_FOR_SEQ_TO_SEQ_CAUSAL_LM_MAPPING_NAMES:
        logging.warning(
            f"Model {model_weights_name_or_path} is a encoder-decoder model. We will load it as a Seq2SeqLM model."
        )

        if config.model_type == "t5" or config.model_type == "mt5":
            logging.warning(
                f"PLEASE READ!!! Model {model_weights_name_or_path} is a T5 model."
                " T5/mT5/Flan-T5/UL2/Flan-UL2 released by google lack the token"
                " representation for new line tokens and multiple spaces, they are"
                " currently NOT supported in CoLLIE. We will attempt to load the model"
                " anyway but you might encounter unexpected behavior or errors."
            )

        model: PreTrainedModel = AutoModelForSeq2SeqLM.from_pretrained(
            pretrained_model_name_or_path=model_weights_name_or_path,
            load_in_8bit=int8_quantization and use_lora,
            device_map=device_map if int8_quantization else None,
            torch_dtype=torch_dtype,
        )

    elif config.model_type in MODEL_FOR_CAUSAL_LM_MAPPING_NAMES:
        logging.warning(
            f"Model {model_weights_name_or_path} is an decoder-only model. We will load it as a CausalLM model."
        )
        model: PreTrainedModel = AutoModelForCausalLM.from_pretrained(
            pretrained_model_name_or_path=model_weights_name_or_path,
            load_in_8bit=int8_quantization and use_lora,
            device_map=device_map if int8_quantization else None,
        )

        # Ensure that the padding token is added to the left of the input sequence.
        tokenizer.padding_side = "left"

    else:
        raise ValueError(
            f"Model {model_weights_name_or_path} of type {config.model_type} is not supported by CoLLIE."
            "Supported models are:\n"
            f"Seq2SeqLM: {MODEL_FOR_SEQ_TO_SEQ_CAUSAL_LM_MAPPING_NAMES}\n"
            f"CausalLM: {MODEL_FOR_CAUSAL_LM_MAPPING_NAMES}\n"
        )

    if tokenizer.pad_token_id is None:
        if "<|padding|>" in tokenizer.get_vocab():
            # StabilityLM specific fix
            tokenizer.add_special_tokens({"pad_token": "<|padding|>"})
        elif tokenizer.unk_token is not None:
            logging.warning("Model does not have a pad token, we will use the unk token as pad token.")
            tokenizer.pad_token_id = tokenizer.unk_token_id
        else:
            logging.warning("Model does not have a pad token. We will use the eos token as pad token.")
            tokenizer.pad_token_id = tokenizer.eos_token_id

    if int8_quantization:
        from peft import prepare_model_for_int8_training

        model = prepare_model_for_int8_training(model)

    if use_lora:
        from peft import LoraConfig, PeftModel, TaskType, get_peft_model

        if lora_weights_name_or_path is None:
            logging.info("No pretrained LORA weights provided, we will initialize the weights randomly.")

            if lora_target_modules is None or (lora_target_modules is not None and len(lora_target_modules) == 0):
                logging.warning(
                    "No target modules provided,  will use the default modules for the"
                    " model in huggingface PEFT library. "
                )
                lora_target_modules = None

            config = LoraConfig(
                r=lora_r,
                lora_alpha=lora_alpha,
                lora_dropout=lora_dropout,
                bias="none",
                task_type=TaskType.CAUSAL_LM,
                target_modules=lora_target_modules,
            )

            model = get_peft_model(model, config)

        else:
            logging.info(f"Loading pretrained LORA weights from {lora_weights_name_or_path}")

            model = PeftModel.from_pretrained(model, lora_weights_name_or_path)

        logging.info(f"\nLoRA config:\n{model.peft_config}\n")

    trainable_params, total_params, trainable_percentage = get_trainable_parameters(model)
    logging.info(
        f"---> Trainable params: {trainable_params} || all params: {total_params} ||"
        f" trainable%: {round(trainable_percentage,6)}\n"
    )

    return model, tokenizer


def load_model_for_inference(
    weights_path: str,
    int8_quantization: bool = False,
    lora_weights_name_or_path: Optional[str] = None,
    torch_dtype: Optional[str] = None,
) -> Tuple[PreTrainedModel, PreTrainedTokenizerBase]:
    """
    Load any Decoder model for inference.

    Args:
        weights_path (`str`):
            The path to your local model weights and tokenizer. You can also provide a
            huggingface hub model name.
        int8_quantization (`bool`, optional):
            Whether to use int8 quantization. Defaults to `False`.

            Requires bitsandbytes library: https://github.com/TimDettmers/bitsandbytes
        lora_weights_name_or_path (`Optional[str]`, optional):
            If the model has been trained with LoRA, path or huggingface hub name to the
            pretrained weights. Defaults to `None`.
        torch_dtype (`Optional[str]`, optional):
            The torch dtype to use for the model. If set to `"auto"`, the dtype will be
            automatically derived. Defaults to `None`.

    Returns:
        `Tuple[PreTrainedModel, PreTrainedTokenizerBase]`:
            The loaded model and tokenizer.
    """

    device_map = "auto"
    world_size = int(os.environ.get("WORLD_SIZE", 1))
    ddp = world_size != 1
    if ddp:
        device_map = {"": int(os.environ.get("LOCAL_RANK") or 0)}

    if int8_quantization:
        logging.info(f"Device map: {device_map}")

    logging.info(f"Loading model from {weights_path}")

    config = AutoConfig.from_pretrained(weights_path)

    torch_dtype = torch_dtype if torch_dtype in ["auto", None] else getattr(torch, torch_dtype)

    tokenizer: PreTrainedTokenizerBase = AutoTokenizer.from_pretrained(
        weights_path,
        add_eos_token=True,
    )

    if config.model_type in MODEL_FOR_SEQ_TO_SEQ_CAUSAL_LM_MAPPING_NAMES:
        logging.warning(f"Model {weights_path} is a encoder-decoder model. We will load it as a Seq2SeqLM model.")
        model: PreTrainedModel = AutoModelForSeq2SeqLM.from_pretrained(
            pretrained_model_name_or_path=weights_path,
            load_in_8bit=int8_quantization,
            device_map=device_map if int8_quantization else None,
            torch_dtype=torch_dtype,
        )

    elif config.model_type in MODEL_FOR_CAUSAL_LM_MAPPING_NAMES:
        logging.warning(f"Model {weights_path} is an encoder-only model. We will load it as a CausalLM model.")
        model: PreTrainedModel = AutoModelForCausalLM.from_pretrained(
            pretrained_model_name_or_path=weights_path,
            load_in_8bit=int8_quantization,
            device_map=device_map if int8_quantization else None,
            torch_dtype=torch_dtype,
        )

        # Ensure that the padding token is added to the left of the input sequence.
        tokenizer.padding_side = "left"
    else:
        raise ValueError(
            f"Model {weights_path} of type {config.model_type} is not supported by CoLLIE."
            "Supported models are:\n"
            f"Seq2SeqLM: {MODEL_FOR_SEQ_TO_SEQ_CAUSAL_LM_MAPPING_NAMES}\n"
            f"CausalLM: {MODEL_FOR_CAUSAL_LM_MAPPING_NAMES}\n"
        )

    if tokenizer.pad_token_id is None:
        if "<|padding|>" in tokenizer.get_vocab():
            # StableLM specific fix
            tokenizer.add_special_tokens({"pad_token": "<|padding|>"})
        elif tokenizer.unk_token is not None:
            logging.warning("Model does not have a pad token, we will use the unk token as pad token.")
            tokenizer.pad_token_id = tokenizer.unk_token_id
        else:
            logging.warning("Model does not have a pad token. We will use the eos token as pad token.")
            tokenizer.pad_token_id = tokenizer.eos_token_id

    if lora_weights_name_or_path:
        from peft import PeftModel

        logging.info(f"Loading pretrained LORA weights from {lora_weights_name_or_path}")
        model = PeftModel.from_pretrained(model, lora_weights_name_or_path)

        if not int8_quantization:
            # If we are not using int8 quantization, we need to merge the LoRA layers into the model
            # This is not possible if we are using int8 quantization.
            model = model.merge_and_unload()

    return model, tokenizer
