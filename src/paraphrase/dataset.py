import logging
from typing import List

from fastchat.conversation import get_conv_template
from torch.utils.data import Dataset
from tqdm import tqdm

from src.paraphrase.utils import clean_guidelines
from src.tasks import task_id_to_guidelines
from transformers import BatchEncoding, PreTrainedTokenizerBase


def prepare_data(
    example: str,
    tokenizer: PreTrainedTokenizerBase,
    is_encoder_decoder: bool = False,
    max_length: int = 2048,
    conv_template: str = None,
) -> BatchEncoding:
    """
    Prepare data for training or inference.

    Args:
        example (`str`):
            The example to prepare.
        tokenizer (`PreTrainedTokenizerBase`):
            The tokenizer to use.
        is_encoder_decoder (`bool`, optional):
            Whether the model is an encoder-decoder model. Defaults to `False`.
        max_length (`int`, optional):
            The maximum length of the input. Defaults to `2048`.
        conv_template (`str`, optional):
            The conversation template to use. Defaults to `None`. If `None` we will return the prompt.

    Returns:
        `BatchEncoding`: `BatchEncoding` with the prepared data.
    """

    prompt = (
        "Please, generate a paraphrase of the following text. Ensure that no information is lost in the paraphrase. If"
        " possible rearrange the word order. Write a short explanation of how are you paraphrasing the text.\n"
        'Use the following format: "Explanation: <your explanation>". \n "Paraphrase: <your paraphrase>". \n'
        f'Text: "{example}"'
    )

    if conv_template is not None:
        conv = get_conv_template(conv_template)
        conv.append_message(conv.roles[0], prompt)
        conv.append_message(conv.roles[1], None)
        prompt = conv.get_prompt()

    model_inputs = tokenizer(
        text=prompt,
        max_length=max_length,
        truncation=True,
        padding=False,
        return_tensors=None,
        add_special_tokens=True,
    )

    if not is_encoder_decoder:
        # Remove the last token if it is an eos token
        if model_inputs["input_ids"][-1] == tokenizer.eos_token_id:
            model_inputs["input_ids"] = model_inputs["input_ids"][:-1]
            model_inputs["attention_mask"] = model_inputs["attention_mask"][:-1]

    if "token_type_ids" in model_inputs:
        # LLaMa tokenizer adds token type ids, but we don't need them
        model_inputs.pop("token_type_ids")

    return model_inputs


class ParaphraseDataset(Dataset):
    """
    Dataset for Collie.

    Args:
        tokenizer (`PreTrainedTokenizerBase`):
            The tokenizer to use.
        dataset_name (`str`):
            The name of the dataset.
        language (`str`):
            The language to get the data for.
        is_encoder_decoder (`bool`, optional):
            Whether the model is an encoder-decoder model. Defaults to `False`.
        max_length (`int`, optional):
            The maximum length of the input. Defaults to `2048`.
        conv_template (`str`, optional):
            The conversation template to use. Defaults to `None`. If `None` we will return the prompt.
    """

    def __init__(
        self,
        tokenizer: PreTrainedTokenizerBase,
        dataset_name: str,
        language: str,
        is_encoder_decoder: bool = False,
        max_length: int = 2048,
        conv_template: str = None,
    ):
        self.dataset_name = dataset_name
        self.language = language
        self.is_encoder_decoder = is_encoder_decoder
        self.max_length = max_length
        self.conv_template = conv_template
        guidelines = task_id_to_guidelines(dataset_name)
        guidelines = clean_guidelines(guidelines)
        self.dataset: List[BatchEncoding] = []
        for guideline in tqdm(guidelines.values(), desc="Data Tokenization"):
            for text in guideline[language]:
                # rich.print(f"Guideline: {text}")
                self.dataset.append(prepare_data(text, tokenizer, is_encoder_decoder, max_length, conv_template))

        logging.info(f"Dataset {dataset_name} has {len(self.dataset)} guidelines.")

    def __len__(self):
        return len(self.dataset)

    def __getitem__(self, idx):
        return self.dataset[idx]
