import json
import logging
import os
from typing import List, Optional, Tuple, Union

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
from transformers.utils import is_ipex_available

from .model_utils import find_all_linear_names, get_trainable_parameters


def get_device_map(
    force_auto_device_map: bool, max_memory_MB: int = None, use_better_transformer: bool = False
) -> (str, Union[int, List[int]]):
    """
    Get the device map to use for loading the model

    Args:
        force_auto_device_map (`bool`):
            Whether to force the use of the auto device map. If set to True, the model will be split across
            GPUs and CPU to fit the model in memory. If set to False, a full copy of the model will be loaded
            into each GPU.
        max_memory_MB (`int`):
            Free memory per gpu in MB. Used to compute the device map when force_auto_device_map is set to True.
        use_better_transformer (`bool`, optional):
            Whether to transform the model using Better Transformer library:
            https://huggingface.co/docs/optimum/bettertransformer/overview. Requires optimum
            'https://huggingface.co/docs/optimum/installation'. Defaults to False.

    Returns:
        `str`:
            The device map to use for loading the model
    """
    if force_auto_device_map:
        if os.environ.get("LOCAL_RANK") is not None:
            # raise ValueError(
            #    "Found DDP environment and force_auto_device_map is set to True, this configuration "
            #    "is not supported. If you want to use DPP, set force_auto_device_map to False, so "
            #    "a copy of the model is loaded in each GPU. If you want the split the model across "
            #    "GPUs (force_auto_device_map=True), do not use DDP (launch your script with "
            #    "pyton -m src/run.py config.json). If you are not in a DDP environment but you see "
            #    "this error, you might have manually set the environment variable 'LOCAL_WORLD_SIZE' to a "
            #    "number different than 1, please, remove this environment variable or set it to 1"
            # )
            if torch.cuda.is_available():
                n_gpus = torch.cuda.device_count()
            elif is_ipex_available() and torch.xpu.is_available():
                n_gpus = torch.xpu.device_count()
            else:
                logging.warning("You are in a DDP environment but no GPU is available, this may cause errors later on")
                n_gpus = 0

            max_memory = {i: max_memory_MB for i in range(n_gpus)}
            local_rank = int(os.environ.get("LOCAL_RANK", "0"))
            device_map = {"": local_rank}
            max_memory = {"": max_memory[local_rank]} if max_memory_MB is not None else None

        else:
            logging.warning(
                "Using auto device map, we will split the model across GPUs and CPU to fit the model in memory."
            )
            device_map = "auto"
            max_memory = max_memory_MB
    else:
        max_memory = None
        word_size = int(os.environ.get("LOCAL_WORLD_SIZE", 1))
        if word_size > 1:
            logging.warning(
                "Found DDP environment and force_auto_device_map is set to False, we will load a copy of the model "
                "on each GPU."
            )
            device_map = None  # {"": int(os.environ.get("LOCAL_RANK", 0))}

        else:
            if not use_better_transformer:
                device_map = None
            else:
                logging.warning("Setting device map to 'auto' to use Better Transformers library.")
                device_map = "auto"

    logging.info(f"We will load the model using the following device map: {device_map} and max_memory: {max_memory}")

    return device_map, max_memory


def merge_lora_model(
    weights_path: str,
    lora_weights_name_or_path: str,
    output_path: str,
    torch_dtype: Optional[str] = None,
    use_auth_token: bool = False,
):
    """
    Given a model path and the path to the LoRA weights, merge the LoRA weights into the model and save the merged model
    weights_path (`str`):
            The path to your local model weights and tokenizer. You can also provide a
            huggingface hub model name.
    lora_weights_name_or_path (`str`):
        If the model has been trained with LoRA, path or huggingface hub name to the
        pretrained weights. Defaults to `None`.
    output_path (`str`):
        The path to the output directory where the merged model will be saved.
    torch_dtype (`Optional[str]`, optional):
        The torch dtype to use for the model. If set to `"auto"`, the dtype will be
        automatically derived.
    use_auth_token (`bool`, optional):
        Whether to use an authentication token when loading a private model from huggingface.co.
        Defaults to False.
    """

    logging.info(f"We will merge the LoRA weights from {lora_weights_name_or_path} into the model {weights_path}")
    model, tokenizer = load_model_for_inference(
        weights_path=weights_path,
        lora_weights_name_or_path=lora_weights_name_or_path,
        torch_dtype=torch_dtype,
        use_auth_token=use_auth_token,
    )

    model.config.save_pretrained(output_path)
    model.save_pretrained(output_path)
    tokenizer.save_pretrained(output_path)

    logging.info(f"Model merged and saved in {output_path}")


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
    use_better_transformer: bool = False,
    use_auth_token: bool = False,
    use_flash_attention: bool = False,
    fsdp_training: bool = False,
    max_memory_MB: Optional[int] = None,
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
        use_better_transformer (`bool`, optional):
            Whether to transform the model using Better Transformer library:
            https://huggingface.co/docs/optimum/bettertransformer/overview. Requires optimum
            'https://huggingface.co/docs/optimum/installation'. Defaults to False. NOTE: This
            is a placeholder for future updates, currently, better transformers is not supported for training.
            We will enable this feature in the future if they support custom attention masks for training.
        use_auth_token (`bool`, optional):
            Whether to use an authentication token when loading a private model from huggingface.co.
            Defaults to False.
        use_flash_attention (`bool`, optional):
            Whether to use Flash Attention. Defaults to False. Flash attention must be installed, see:
            'https://github.com/Dao-AILab/flash-attention' for more details.
        fsdp_training: (`bool`, optional):
            Whether Fully Sharded Data Parallelism is enabled for training. Defaults to False.
            Used to prevent casting layers to fp32 if the model is already in fp16, which causes
            an error: ValueError: Must flatten tensors with uniform dtype but got torch.float16 and torch.float32
        max_memory_MB (`int`):
            Free memory per gpu in MB. Used to compute the device map when force_auto_device_map is set to True.
    Raises:
        `ValueError`:
            is raised when `int8_quantization=True` but `use_lora=False`.

    Returns:
        `Tuple[PreTrainedModel, PreTrainedTokenizerBase]`:
            The loaded model and tokenizer.
    """

    if use_better_transformer and use_flash_attention:
        raise ValueError("You cannot use both Better Transformer and Flash Attention at the same time.")

    if type(quantization) == str:
        quantization = int(quantization)
    assert (quantization is None) or (
        quantization in [4, 8]
    ), f"Quantization must be 4 or 8, or None for FP32/FP16 training. You passed: {quantization}"

    if use_better_transformer:
        logging.warning(
            "You have set the flag 'use_better_transformer=True', this is a placeholder for future updates, "
            "currently, better transformers is not supported for training. We will enable this feature in the "
            "future if they support custom attention masks for training. We will override this flag to False. "
            "You can still use BetterTransformers for inference."
        )
        use_better_transformer = False

    if quantization is not None and not use_lora:
        raise ValueError(
            "'Quantization' == 4/8 is only supported with LoRA. If you want "
            "to train a 4/8bits quantified model, you must set `use_lora=True`. If you want to "
            "use a 4/8 bits optimizer, set `quantization=None` and choose a 4/8 bit optimizer using 'optim' "
            "argument (e.g 'adamw_bnb_8bit', 'lion_8bit', 'paged_adamw_8bit', ...)."
        )

    logging.info(f"Loading model model from {model_weights_name_or_path}")
    device_map, max_memory = get_device_map(
        force_auto_device_map=force_auto_device_map,
        max_memory_MB=max_memory_MB,
        use_better_transformer=use_better_transformer,
    )

    MODEL_FOR_CAUSAL_LM_MAPPING_NAMES.update(
        {
            "mpt": "MPTForCausalLM",
            "RefinedWebModel": "RWForCausalLM",
            "RefinedWeb": "RWForCausalLM",
        }
    )  # MPT and Falcon are not in transformers yet

    if use_lora:
        config = AutoConfig.from_pretrained(
            model_weights_name_or_path,
            use_auth_token=use_auth_token,
            trust_remote_code=(
                True if ("mpt" in model_weights_name_or_path or "falcon" in model_weights_name_or_path) else False
            ),
            pretraining_tp=1,  # Fix mat1 and mat2 shapes cannot be multiplied  error with LLaMA-2
            # See https://github.com/huggingface/transformers/pull/24906
        )
    else:
        config = AutoConfig.from_pretrained(
            model_weights_name_or_path,
            use_auth_token=use_auth_token,
            trust_remote_code=(
                True if ("mpt" in model_weights_name_or_path or "falcon" in model_weights_name_or_path) else False
            ),
        )

    tokenizer: PreTrainedTokenizerBase = AutoTokenizer.from_pretrained(
        model_weights_name_or_path,
        use_auth_token=use_auth_token,
        add_eos_token=True,
        trust_remote_code=(
            True if ("mpt" in model_weights_name_or_path or "falcon" in model_weights_name_or_path) else False
        ),
    )

    quant_args = {}
    torch_dtype = torch_dtype if torch_dtype in ["auto", None] else getattr(torch, torch_dtype)

    if quantization is not None:
        quant_args = {"load_in_4bit": True} if quantization == 4 else {"load_in_8bit": True}
        if quantization == 4:
            bnb_config = BitsAndBytesConfig(
                load_in_4bit=True,
                bnb_4bit_use_double_quant=True,
                bnb_4bit_quant_type="nf4",
                bnb_4bit_compute_dtype=torch.float16 if torch_dtype in ["auto", None] else torch_dtype,
            )
            # torch_dtype = torch.bfloat16

        else:
            bnb_config = BitsAndBytesConfig(
                load_in_8bit=True,
            )
        logging.info(f"Bits and Bytes config: {json.dumps(bnb_config.to_dict(),indent=4,ensure_ascii=False)}")
    else:
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
            use_auth_token=use_auth_token,
            device_map=device_map,
            max_memory=max_memory,
            quantization_config=bnb_config,
            torch_dtype=torch_dtype,
            config=config,
            **quant_args,
        )

        model_type = "seq2seq"

    elif config.model_type in MODEL_FOR_CAUSAL_LM_MAPPING_NAMES:
        logging.warning(
            f"Model {model_weights_name_or_path} is an decoder-only model. We will load it as a CausalLM model."
        )
        model: PreTrainedModel = AutoModelForCausalLM.from_pretrained(
            pretrained_model_name_or_path=model_weights_name_or_path,
            use_auth_token=use_auth_token,
            device_map=device_map,
            max_memory=max_memory,
            quantization_config=bnb_config,
            torch_dtype=torch_dtype,
            config=config,
            trust_remote_code=(
                True if ("mpt" in model_weights_name_or_path or "falcon" in model_weights_name_or_path) else False
            ),
            **quant_args,
        )

        # Ensure that the padding token is added to the left of the input sequence.
        tokenizer.padding_side = "left"

        model_type = "causal"

    else:
        raise ValueError(
            f"Model {model_weights_name_or_path} of type {config.model_type} is not supported by CoLLIE."
            "Supported models are:\n"
            f"Seq2SeqLM: {MODEL_FOR_SEQ_TO_SEQ_CAUSAL_LM_MAPPING_NAMES}\n"
            f"CausalLM: {MODEL_FOR_CAUSAL_LM_MAPPING_NAMES}\n"
        )

    if use_better_transformer:
        from optimum.bettertransformer import BetterTransformer

        model = BetterTransformer.transform(model)

    if use_flash_attention:
        from src.model.patch_models.patching import patch_model

        logging.info("Patching model to use flash attention")
        patch_model(model, resid_pdrop=None, flash_attention=True)

    logging.info(f"Model dtype: {model.dtype}")
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
    else:
        if use_gradient_checkpointing:
            model.gradient_checkpointing_enable()

    if use_lora:
        from peft import LoraConfig, PeftModel, TaskType, get_peft_model

        model.enable_input_require_grads()  #  Enables the gradients for the input embeddings

        if lora_weights_name_or_path is None:
            logging.info("No pretrained LORA weights provided, we will initialize the weights randomly.")

            if lora_target_modules is None or (lora_target_modules is not None and len(lora_target_modules) == 0):
                logging.warning(
                    "No target modules provided,  will use the default modules for the"
                    " model in huggingface PEFT library. "
                )
                lora_target_modules = None

            if lora_target_modules == ["all"]:
                lora_target_modules = find_all_linear_names(model, quantization=quantization)

            lora_config = LoraConfig(
                r=lora_r,
                lora_alpha=lora_alpha,
                lora_dropout=lora_dropout,
                bias="none",
                task_type=TaskType.CAUSAL_LM if model_type == "causal" else TaskType.SEQ_2_SEQ_LM,
                target_modules=lora_target_modules,
            )

            model = get_peft_model(model, lora_config)

        else:
            logging.info(f"Loading pretrained LORA weights from {lora_weights_name_or_path}")

            model = PeftModel.from_pretrained(model, lora_weights_name_or_path, use_auth_token=use_auth_token)

        logging.info(f"\nLoRA config:\n{model.peft_config}\n")

    """
    Convert the model layers to the correct dtype
    If LoRA and bf16 is used, we convert the LoRA layers to bf16 for faster training
    """

    if use_lora:
        from peft.tuners.lora import LoraLayer

        for name, module in model.named_modules():
            if isinstance(module, LoraLayer):
                if torch_dtype == torch.bfloat16:
                    logging.debug(f"Converting LoRA layer {name} to {torch_dtype}")
                    module = module.to(torch.bfloat16)

    if not fsdp_training:
        for name, module in model.named_modules():
            if "norm" in name:
                logging.debug(f"Converting layer {name} to {torch.float32}")
                module = module.to(torch.float32)
            if "lm_head" in name or "embed_tokens" in name:
                if hasattr(module, "weight"):
                    if torch_dtype == torch.bfloat16 and module.weight.dtype == torch.float32:
                        logging.debug(f"Converting layer {name} to {torch_dtype}")
                        module = module.to(torch.bfloat16)

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
    use_better_transformer: bool = False,
    use_auth_token: bool = False,
    use_flash_attention: bool = False,
    max_memory_MB: Optional[int] = None,
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
        use_better_transformer (`bool`, optional):
            Whether to transform the model using Better Transformer library:
            https://huggingface.co/docs/optimum/bettertransformer/overview. Requires optimum
            'https://huggingface.co/docs/optimum/installation'. Defaults to False.
        use_auth_token (`bool`, optional):
            Whether to use an authentication token when loading a private model from huggingface.co.
            Defaults to False.
        use_flash_attention (`bool`, optional):
            Whether to use Flash Attention. Defaults to False. Flash attention must be installed, see:
            'https://github.com/Dao-AILab/flash-attention' for more details.
        max_memory_MB (`int`):
            Free memory per gpu in MB. Used to compute the device map when force_auto_device_map is set to True.

    Returns:
        `Tuple[PreTrainedModel, PreTrainedTokenizerBase]`:
            The loaded model and tokenizer.
    """

    if use_better_transformer and use_flash_attention:
        raise ValueError("You cannot use both Better Transformer and Flash Attention at the same time.")

    if type(quantization) == str:
        quantization = int(quantization)
    assert (quantization is None) or (
        quantization in [4, 8]
    ), f"Quantization must be 4 or 8, or None for FP32/FP16 training. You passed: {quantization}"

    logging.info(f"Loading model from {weights_path}")
    device_map, max_memory = get_device_map(
        force_auto_device_map=force_auto_device_map,
        max_memory_MB=max_memory_MB,
        use_better_transformer=use_better_transformer,
    )

    MODEL_FOR_CAUSAL_LM_MAPPING_NAMES.update(
        {
            "mpt": "MPTForCausalLM",
            "RefinedWebModel": "RWForCausalLM",
            "RefinedWeb": "RWForCausalLM",
        }
    )  # MPT and Falcon are not in transformers yet

    if lora_weights_name_or_path is not None:
        config = AutoConfig.from_pretrained(
            weights_path,
            use_auth_token=use_auth_token,
            trust_remote_code=True if ("mpt" in weights_path or "falcon" in weights_path) else False,
            pretraining_tp=1,  # Fix mat1 and mat2 shapes cannot be multiplied  error with LLaMA-2
            # See https://github.com/huggingface/transformers/pull/24906
        )
    else:
        config = AutoConfig.from_pretrained(
            weights_path,
            use_auth_token=use_auth_token,
            trust_remote_code=True if ("mpt" in weights_path or "falcon" in weights_path) else False,
        )

    torch_dtype = torch_dtype if torch_dtype in ["auto", None] else getattr(torch, torch_dtype)

    tokenizer: PreTrainedTokenizerBase = AutoTokenizer.from_pretrained(
        weights_path,
        use_auth_token=use_auth_token,
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
                bnb_4bit_compute_dtype=torch.float16 if torch_dtype in ["auto", None] else torch_dtype,
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
            use_auth_token=use_auth_token,
            device_map=device_map,
            max_memory=max_memory,
            torch_dtype=torch_dtype,
            config=config,
            quantization_config=bnb_config,
            **quant_args,
        )

    elif config.model_type in MODEL_FOR_CAUSAL_LM_MAPPING_NAMES:
        logging.warning(f"Model {weights_path} is an decoder-only model. We will load it as a CausalLM model.")
        model: PreTrainedModel = AutoModelForCausalLM.from_pretrained(
            pretrained_model_name_or_path=weights_path,
            use_auth_token=use_auth_token,
            device_map=device_map,
            max_memory=max_memory,
            torch_dtype=torch_dtype,
            trust_remote_code=True if ("mpt" in weights_path or "falcon" in weights_path) else False,
            config=config,
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

    if use_better_transformer:
        from optimum.bettertransformer import BetterTransformer

        model = BetterTransformer.transform(model)

    if use_flash_attention:
        from src.model.patch_models.patching import patch_model

        logging.info("Patching model to use flash attention")
        patch_model(model, resid_pdrop=None, flash_attention=True)

    logging.info(f"Model dtype: {model.dtype}")
    logging.info("Total model memory footprint: " + str(model.get_memory_footprint() / 1e6) + " MB")

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
        model = PeftModel.from_pretrained(model, lora_weights_name_or_path, use_auth_token=use_auth_token)

        if quantization is None:
            # If we are not using quantization, we merge the LoRA layers into the model for faster inference.
            # This is not possible if we are using 4/8 bit quantization.
            model = model.merge_and_unload()

    return model, tokenizer
