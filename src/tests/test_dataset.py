import os
import unittest
from transformers import PreTrainedTokenizerBase
from src.dataset.dataset import CollieDataset
import json
import tempfile


def get_dataset(
    tokenizer: PreTrainedTokenizerBase,
    is_encoder_decoder: bool,
    pad_to_max_length: bool,
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
            pad_to_max_length=pad_to_max_length,
            inference=inference,
        )

    return dataset, prompt, result


class TestCollieDataset(unittest.TestCase):
    @unittest.skipIf(
        not os.path.exists("/gaueko1/hizkuntza-ereduak/LLaMA/lm/huggingface/7B"),
        "No LLaMA model available",
    )
    def test_encoder(self):
        from transformers import AutoTokenizer

        tokenizer = AutoTokenizer.from_pretrained(
            "/gaueko1/hizkuntza-ereduak/LLaMA/lm/huggingface/7B/"
        )

        # Test Train
        dataset, prompt, result = get_dataset(
            tokenizer=tokenizer,
            is_encoder_decoder=False,
            pad_to_max_length=False,
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
            pad_to_max_length=False,
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

        #  Test train with pad_to_max_length
        dataset, prompt, result = get_dataset(
            tokenizer=tokenizer,
            is_encoder_decoder=False,
            pad_to_max_length=True,
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
        self.assertTrue(len(model_input) == 2048)

    def test_encoder_decoder(self):
        from transformers import AutoTokenizer

        tokenizer = AutoTokenizer.from_pretrained("google/mt5-small")

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

    def test_dataloader(self):
        from transformers import DataCollatorForSeq2Seq, AutoTokenizer
        from torch.utils.data import DataLoader

        tokenizer = AutoTokenizer.from_pretrained(
            "/gaueko1/hizkuntza-ereduak/LLaMA/lm/huggingface/7B/"
        )

        # Test Train
        dataset, prompt, result = get_dataset(
            tokenizer=tokenizer,
            is_encoder_decoder=False,
            pad_to_max_length=True,
            inference=False,
        )

        datacollator = DataCollatorForSeq2Seq(
            tokenizer,
            pad_to_multiple_of=8,
            return_tensors="pt",
            padding=True,
            label_pad_token_id=-100,
        )

        dataloder = DataLoader(
            dataset, batch_size=1, collate_fn=datacollator, shuffle=False
        )
        batch = [x for x in dataloder]

        model_input = batch["input_ids"][0]
        labels = batch["labels"][0]
        self.assertEqual(model_input, labels)
        self.assertEqual(
            tokenizer.decode(
                model_input, skip_special_tokens=True, clean_up_tokenization_spaces=False
            ),
            prompt + result,
        )

        self.assertTrue(len(model_input) == 2048)
        self.assertEqual(model_input[0], -100)

        datacollator = DataCollatorForSeq2Seq(
            tokenizer,
            pad_to_multiple_of=8,
            return_tensors="pt",
            padding=True,
            label_pad_token_id=tokenizer.pad_token_id,
        )

        dataloder = DataLoader(
            dataset, batch_size=1, collate_fn=datacollator, shuffle=False
        )
        batch = [x for x in dataloder]

        model_input = batch[0]["input_ids"][0]
        labels = batch[0]["labels"][0]
        self.assertEqual(model_input, labels)
        self.assertEqual(
            tokenizer.decode(
                model_input, skip_special_tokens=True, clean_up_tokenization_spaces=False
            ),
            prompt + result,
        )

        self.assertTrue(len(model_input) == 2048)
        self.assertEqual(model_input[0], tokenizer.pad_token_id)
