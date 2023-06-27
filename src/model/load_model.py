import json
import logging
import os
from typing import List, Optional, Tuple

import torch

from transformers import (
    AutoConfig,
    AutoModelForCausalLM,
    AutoModelForSeq2SeqLM,
    AutoTokenizer,
    BitsAndBytesConfig,
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
    quantization: Optional[int] = None,
    use_lora: bool = False,
    lora_weights_name_or_path: Optional[str] = None,
    lora_target_modules: Optional[List[str]] = None,
    lora_r: Optional[int] = 8,
    lora_alpha: Optional[int] = 16,
    lora_dropout: Optional[float] = 0.05,
    torch_dtype: Optional[str] = None,
    force_auto_device_map: bool = False,
    use_gradient_checkpointing: bool = False,
) -> Tuple[PreTrainedModel, PreTrainedTokenizerBase]:
    """
    Load any Decoder model for training.

    Args:
        model_weights_name_or_path (`str`):
            The path to your local model weights and tokenizer or huggingface model name.
        quantization (`int`, optional):
            '4' or '8' for 4 bits or 8 bits quantization or None for 16/32bits training. Defaults to `None`.

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
        force_auto_device_map (`bool`, optional):
            Whether to force the use of the auto device map. If set to True, the model will be split across
            GPUs and CPU to fit the model in memory. If set to False, a full copy of the model will be loaded
            into each GPU. Defaults to False.
        use_gradient_checkpointing (`bool`, optiona):
            Whether to use gradient checkpointing for training

    Raises:
        `ValueError`:
            is raised when `int8_quantization=True` but `use_lora=False`.

    Returns:
        `Tuple[PreTrainedModel, PreTrainedTokenizerBase]`:
            The loaded model and tokenizer.
    """

    if type(quantization) == str:
        quantization = int(quantization)
    assert (quantization is None) or (
        quantization in [4, 8]
    ), f"Quantization must be 4 or 8, or None for FP32/FP16 training. You passed: {quantization}"

    if quantization is not None and not use_lora:
        raise ValueError(
            "'Quantization' == 4/8 is only supported with LoRA. If you want "
            "to train a 4/8bits quantified model, you must set `use_lora=True`. If you want to "
            "use a 4/8 bits optimizer, set `quantization=None` and choose a 4/8 bit optimizer using 'optim' "
            "argument (e.g 'adamw_bnb_8bit', 'lion_8bit', 'paged_adamw_8bit', ...)."
        )

    if force_auto_device_map:
        logging.info("Device map: auto")

    logging.info(f"Loading model model from {model_weights_name_or_path}")

    MODEL_FOR_CAUSAL_LM_MAPPING_NAMES.update(
        {
            "mpt": "MPTForCausalLM",
            "RefinedWebModel": "RWForCausalLM",
            "RefinedWeb": "RWForCausalLM",
        }
    )  # MPT and Falcon are not in transformers yet

    config = AutoConfig.from_pretrained(
        model_weights_name_or_path,
        trust_remote_code=(
            True if ("mpt" in model_weights_name_or_path or "falcon" in model_weights_name_or_path) else False
        ),
    )

    tokenizer: PreTrainedTokenizerBase = AutoTokenizer.from_pretrained(
        model_weights_name_or_path,
        add_eos_token=True,
        trust_remote_code=(
            True if ("mpt" in model_weights_name_or_path or "falcon" in model_weights_name_or_path) else False
        ),
    )

    quant_args = {}
    if quantization is not None:
        quant_args = {"load_in_4bit": True} if quantization == 4 else {"load_in_8bit": True}
        if quantization == 4:
            bnb_config = BitsAndBytesConfig(
                load_in_4bit=True,
                bnb_4bit_use_double_quant=True,
                bnb_4bit_quant_type="nf4",
                bnb_4bit_compute_dtype=torch.bfloat16,
            )
            # torch_dtype = torch.bfloat16

        else:
            bnb_config = BitsAndBytesConfig(
                load_in_8bit=True,
            )
        logging.info(f"Bits and Bytes config: {json.dumps(bnb_config.to_dict(),indent=4,ensure_ascii=False)}")
    else:
        torch_dtype = torch_dtype if torch_dtype in ["auto", None] else getattr(torch, torch_dtype)
        logging.info(f"Loading model with dtype: {torch_dtype}")
        bnb_config = None

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
            device_map="auto" if force_auto_device_map else None,
            quantization_config=bnb_config,
            torch_dtype=torch_dtype,
            **quant_args,
        )

    elif config.model_type in MODEL_FOR_CAUSAL_LM_MAPPING_NAMES:
        logging.warning(
            f"Model {model_weights_name_or_path} is an decoder-only model. We will load it as a CausalLM model."
        )
        model: PreTrainedModel = AutoModelForCausalLM.from_pretrained(
            pretrained_model_name_or_path=model_weights_name_or_path,
            device_map="auto" if force_auto_device_map else None,
            quantization_config=bnb_config,
            torch_dtype=torch_dtype,
            trust_remote_code=(
                True if ("mpt" in model_weights_name_or_path or "falcon" in model_weights_name_or_path) else False
            ),
            **quant_args,
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

    logging.info("Total model memory footprint: " + str(model.get_memory_footprint() / 1e6) + " MB")

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

    if quantization is not None:
        from .model_utils import prepare_model_for_kbit_training

        # from peft import prepare_model_for_kbit_training

        # model.gradient_checkpointing_enable()
        model = prepare_model_for_kbit_training(model, use_gradient_checkpointing=use_gradient_checkpointing)

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
    quantization: Optional[int] = None,
    lora_weights_name_or_path: Optional[str] = None,
    torch_dtype: Optional[str] = None,
    force_auto_device_map: bool = False,
) -> Tuple[PreTrainedModel, PreTrainedTokenizerBase]:
    """
    Load any Decoder model for inference.

    Args:
        weights_path (`str`):
            The path to your local model weights and tokenizer. You can also provide a
            huggingface hub model name.
        quantization (`int`, optional):
            '4' or '8' for 4 bits or 8 bits quantization or None for 16/32bits training. Defaults to `None`.

            Requires bitsandbytes library: https://github.com/TimDettmers/bitsandbytes
        lora_weights_name_or_path (`Optional[str]`, optional):
            If the model has been trained with LoRA, path or huggingface hub name to the
            pretrained weights. Defaults to `None`.
        torch_dtype (`Optional[str]`, optional):
            The torch dtype to use for the model. If set to `"auto"`, the dtype will be
            automatically derived. Defaults to `None`. If quantization is enabled, we will override
            this to 'torch.bfloat16'.
        force_auto_device_map (`bool`, optional):
            Whether to force the use of the auto device map. If set to True, the model will be split across
            GPUs and CPU to fit the model in memory. If set to False, a full copy of the model will be loaded
            into each GPU. Defaults to False.

    Returns:
        `Tuple[PreTrainedModel, PreTrainedTokenizerBase]`:
            The loaded model and tokenizer.
    """

    if type(quantization) == str:
        quantization = int(quantization)
    assert (quantization is None) or (
        quantization in [4, 8]
    ), f"Quantization must be 4 or 8, or None for FP32/FP16 training. You passed: {quantization}"

    if force_auto_device_map:
        logging.info("Device map: auto")

    logging.info(f"Loading model from {weights_path}")

    MODEL_FOR_CAUSAL_LM_MAPPING_NAMES.update(
        {
            "mpt": "MPTForCausalLM",
            "RefinedWebModel": "RWForCausalLM",
            "RefinedWeb": "RWForCausalLM",
        }
    )  # MPT and Falcon are not in transformers yet

    config = AutoConfig.from_pretrained(
        weights_path,
        trust_remote_code=True if ("mpt" in weights_path or "falcon" in weights_path) else False,
    )

    torch_dtype = torch_dtype if torch_dtype in ["auto", None] else getattr(torch, torch_dtype)

    tokenizer: PreTrainedTokenizerBase = AutoTokenizer.from_pretrained(
        weights_path,
        add_eos_token=True,
        trust_remote_code=True if ("mpt" in weights_path or "falcon" in weights_path) else False,
    )

    quant_args = {}
    if quantization is not None:
        quant_args = {"load_in_4bit": True} if quantization == 4 else {"load_in_8bit": True}
        if quantization == 4:
            bnb_config = BitsAndBytesConfig(
                load_in_4bit=True,
                bnb_4bit_use_double_quant=True,
                bnb_4bit_quant_type="nf4",
                bnb_4bit_compute_dtype=torch.bfloat16,
            )
            # torch_dtype = torch.bfloat16

        else:
            bnb_config = BitsAndBytesConfig(
                load_in_8bit=True,
            )
        logging.info(f"Bits and Bytes config: {json.dumps(bnb_config.to_dict(),indent=4,ensure_ascii=False)}")
    else:
        # torch_dtype = torch_dtype if torch_dtype in ["auto", None] else getattr(torch, torch_dtype)
        logging.info(f"Loading model with dtype: {torch_dtype}")
        bnb_config = None

    if config.model_type in MODEL_FOR_SEQ_TO_SEQ_CAUSAL_LM_MAPPING_NAMES:
        logging.warning(f"Model {weights_path} is a encoder-decoder model. We will load it as a Seq2SeqLM model.")
        model: PreTrainedModel = AutoModelForSeq2SeqLM.from_pretrained(
            pretrained_model_name_or_path=weights_path,
            device_map="auto" if force_auto_device_map else None,
            torch_dtype=torch_dtype,
            quantization_config=bnb_config,
            **quant_args,
        )

    elif config.model_type in MODEL_FOR_CAUSAL_LM_MAPPING_NAMES:
        logging.warning(f"Model {weights_path} is an encoder-only model. We will load it as a CausalLM model.")
        model: PreTrainedModel = AutoModelForCausalLM.from_pretrained(
            pretrained_model_name_or_path=weights_path,
            device_map="auto" if force_auto_device_map else None,
            torch_dtype=torch_dtype,
            trust_remote_code=True if ("mpt" in weights_path or "falcon" in weights_path) else False,
            quantization_config=bnb_config,
            **quant_args,
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

        if quantization is None:
            # If we are not using quantization, we merge the LoRA layers into the model for faster inference.
            # This is not possible if we are using 4/8 bit quantization.
            model = model.merge_and_unload()

    return model, tokenizer
