import os
import unittest
from transformers import PreTrainedTokenizerBase
from src.dataset.dataset import CollieDataset
import json
import tempfile


def get_dataset(
    tokenizer: PreTrainedTokenizerBase,
    is_encoder_decoder: bool,
    inference: bool,
) -> (CollieDataset, str, str):
    text = """@dataclass
class EnergyAndInfrastructureEvent:
    \"\"\"This class is used to instantiate events that involve Chinese energy and infrastructure projects.\"\"\"
    meeting_attendees: Union[List[str], None] # Persons or organizations that attended the meeting.
    meeting_location: Union[List[str], None] # Location where the meeting happened.
    meeting_topic: Union[List[str], None] # Topic discussed on the meeting
    project_location: Union[List[str], None] # Location of the project
    project_name: Union[List[str], None] # Name of the project
    
# This is the sentence to analyze
sentence = "The Chinese and Rongovian delegations met at the sidelines of the Berlin Development Futures conference to discuss Rongovia's proposed Pangean Reunification Facility.

# The following list contains the events instances that happens in the sentence defined above
result = [
    EnergyAndInfrastructureEvent(
        meeting_attendees=["Chinese", "Rongovian"],
        meeting_location=["Berlin"],
        meeting_topic=["Pangean Reunification Facility"],
        project_location=["Rongovia"],
        project_name=["Pangean Reunification Facility"]
    ),
]"""

    prompt = """@dataclass
class EnergyAndInfrastructureEvent:
    \"\"\"This class is used to instantiate events that involve Chinese energy and infrastructure projects.\"\"\"
    meeting_attendees: Union[List[str], None] # Persons or organizations that attended the meeting.
    meeting_location: Union[List[str], None] # Location where the meeting happened.
    meeting_topic: Union[List[str], None] # Topic discussed on the meeting
    project_location: Union[List[str], None] # Location of the project
    project_name: Union[List[str], None] # Name of the project
    
# This is the sentence to analyze
sentence = "The Chinese and Rongovian delegations met at the sidelines of the Berlin Development Futures conference to discuss Rongovia's proposed Pangean Reunification Facility.

# The following list contains the events instances that happens in the sentence defined above
result = [
"""
    result = """    EnergyAndInfrastructureEvent(
        meeting_attendees=["Chinese", "Rongovian"],
        meeting_location=["Berlin"],
        meeting_topic=["Pangean Reunification Facility"],
        project_location=["Rongovia"],
        project_name=["Pangean Reunification Facility"]
    ),
]"""
    with tempfile.TemporaryDirectory() as tmpdirname:
        with open(os.path.join(tmpdirname, "test.jsonl"), "w", encoding="utf8") as f:
            print(json.dumps({"text": text}, ensure_ascii=False), file=f)

        dataset = CollieDataset(
            tokenizer=tokenizer,
            dataset_path=os.path.join(tmpdirname, "test.jsonl"),
            is_encoder_decoder=is_encoder_decoder,
            max_length=2048,
            inference=inference,
        )

    return dataset, prompt, result


class TestCollieDataset(unittest.TestCase):
    def test_encoder(self):
        from transformers import AutoTokenizer

        tokenizer = AutoTokenizer.from_pretrained(
            (
                "/gaueko1/hizkuntza-ereduak/LLaMA/lm/huggingface/7B/"
                if os.path.exists("/gaueko1/hizkuntza-ereduak/LLaMA/lm/huggingface/7B/")
                else "EleutherAI/gpt-neo-125m"
            ),
            add_eos_token=True,
        )

        if tokenizer.pad_token_id is None:
            tokenizer.pad_token_id = tokenizer.unk_token_id

        # Test Train
        dataset, prompt, result = get_dataset(
            tokenizer=tokenizer,
            is_encoder_decoder=False,
            inference=False,
        )

        model_input = dataset[0]["input_ids"]
        labels = dataset[0]["labels"]
        self.assertEqual(model_input, labels)
        self.assertEqual(
            tokenizer.decode(
                model_input, skip_special_tokens=True, clean_up_tokenization_spaces=False
            ),
            prompt + result,
        )

        # Test Inference
        dataset, prompt, result = get_dataset(
            tokenizer=tokenizer,
            is_encoder_decoder=False,
            inference=True,
        )

        model_input = dataset[0]["input_ids"]
        self.assertFalse("labels" in dataset[0])
        self.assertEqual(
            tokenizer.decode(
                model_input, skip_special_tokens=True, clean_up_tokenization_spaces=False
            ),
            prompt,
        )

    """
    We do not support encoder-decoder models yet. T5/mT5/FlanT5 lack the representation for '\n' or multiple whitespaces
    so they cannot be used with CoLLIE prompt encoding. 
    
    
    def test_encoder_decoder(self):
        from transformers import AutoTokenizer

        tokenizer = AutoTokenizer.from_pretrained("google/mt5-small")
        if tokenizer.pad_token_id is None:
            tokenizer.pad_token_id = tokenizer.unk_token_id
        if tokenizer.decode(tokenizer.encode("\n", add_special_tokens=False)) != "\n":
            #T5 does not have a newline token, so we add one
            tokenizer.add_tokens("\n")
        # Test Train
        dataset, prompt, result = get_dataset(
            tokenizer=tokenizer,
            is_encoder_decoder=True,
            pad_to_max_length=False,
            inference=False,
        )

        model_input = dataset[0]["input_ids"]
        labels = dataset[0]["labels"]
        self.assertEqual(
            tokenizer.decode(
                model_input, skip_special_tokens=True, clean_up_tokenization_spaces=False
            ),
            prompt,
        )
        self.assertEqual(
            tokenizer.decode(
                labels, skip_special_tokens=True, clean_up_tokenization_spaces=False
            ),
            result,
        )

        # Test Inference
        dataset, prompt, result = get_dataset(
            tokenizer=tokenizer,
            is_encoder_decoder=True,
            pad_to_max_length=False,
            inference=True,
        )

        model_input = dataset[0]["input_ids"]
        labels = dataset[0]["labels"]
        self.assertEqual(
            tokenizer.decode(
                model_input, skip_special_tokens=True, clean_up_tokenization_spaces=False
            ),
            prompt,
        )
        self.assertEqual(
            tokenizer.decode(
                labels, skip_special_tokens=True, clean_up_tokenization_spaces=False
            ),
            result,
        )

        #  Test train with pad_to_max_length
        dataset, prompt, result = get_dataset(
            tokenizer=tokenizer,
            is_encoder_decoder=True,
            pad_to_max_length=True,
            inference=False,
        )

        model_input = dataset[0]["input_ids"]
        labels = dataset[0]["labels"]
        self.assertEqual(
            tokenizer.decode(
                model_input, skip_special_tokens=True, clean_up_tokenization_spaces=False
            ),
            prompt,
        )
        self.assertEqual(
            tokenizer.decode(
                labels, skip_special_tokens=True, clean_up_tokenization_spaces=False
            ),
            result,
        )
        self.assertTrue(len(model_input) == 2048)
    """

    def test_dataloader(self):
        from transformers import DataCollatorForSeq2Seq, AutoTokenizer
        from torch.utils.data import DataLoader

        tokenizer = AutoTokenizer.from_pretrained(
            (
                "/gaueko1/hizkuntza-ereduak/LLaMA/lm/huggingface/7B/"
                if os.path.exists("/gaueko1/hizkuntza-ereduak/LLaMA/lm/huggingface/7B/")
                else "EleutherAI/gpt-neo-125m"
            ),
            add_eos_token=True,
        )

        tokenizer.padding_side = "left"

        if tokenizer.pad_token_id is None:
            tokenizer.pad_token_id = tokenizer.unk_token_id

        # Test Train
        dataset, prompt, result = get_dataset(
            tokenizer=tokenizer,
            is_encoder_decoder=False,
            inference=False,
        )

        datacollator = DataCollatorForSeq2Seq(
            tokenizer,
            pad_to_multiple_of=2048,
            return_tensors="pt",
            padding=True,
            label_pad_token_id=-100,
        )

        dataloder = DataLoader(
            dataset, batch_size=1, collate_fn=datacollator, shuffle=False
        )
        batch = [x for x in dataloder][0]

        model_input = batch["input_ids"][0].tolist()
        labels = batch["labels"][0].tolist()
        self.assertEqual(
            tokenizer.decode(
                model_input, skip_special_tokens=True, clean_up_tokenization_spaces=False
            ),
            prompt + result,
        )
        self.assertEqual(
            tokenizer.decode(
                [x for x in labels if x != -100],
                skip_special_tokens=True,
                clean_up_tokenization_spaces=False,
            ),
            prompt + result,
        )
        self.assertEqual(model_input[0], tokenizer.pad_token_id)
        self.assertEqual(labels[0], -100)

        datacollator = DataCollatorForSeq2Seq(
            tokenizer,
            pad_to_multiple_of=2048,
            return_tensors="pt",
            padding=True,
            label_pad_token_id=tokenizer.pad_token_id,
        )

        dataloder = DataLoader(
            dataset, batch_size=1, collate_fn=datacollator, shuffle=False
        )
        batch = [x for x in dataloder][0]

        model_input = batch["input_ids"][0].tolist()
        labels = batch["labels"][0].tolist()
        self.assertEqual(model_input, labels)
        self.assertEqual(
            tokenizer.decode(
                model_input, skip_special_tokens=True, clean_up_tokenization_spaces=False
            ),
            prompt + result,
        )

        self.assertEqual(model_input[0], tokenizer.pad_token_id)
        self.assertEqual(labels[0], tokenizer.pad_token_id)
