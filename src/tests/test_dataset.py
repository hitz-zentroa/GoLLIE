import json
import os
import random
import tempfile
import unittest

from src.dataset.dataset import CollieDataset
from transformers import PreTrainedTokenizerBase


def get_dataset(
    tokenizer: PreTrainedTokenizerBase,
    is_encoder_decoder: bool,
    inference: bool,
    prompt_loss_weight: float,
    num_epochs: int = -1,
    max_length: int = 2048,
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
result ="""
    result = """[
    EnergyAndInfrastructureEvent(
        meeting_attendees=["Chinese", "Rongovian"],
        meeting_location=["Berlin"],
        meeting_topic=["Pangean Reunification Facility"],
        project_location=["Rongovia"],
        project_name=["Pangean Reunification Facility"]
    ),
]"""
    if num_epochs == -1:
        with tempfile.TemporaryDirectory() as tmpdirname:
            with open(os.path.join(tmpdirname, "tmp.ee.train.jsonl"), "w", encoding="utf8") as f:
                print(json.dumps({"text": text}, ensure_ascii=False), file=f)

            dataset = CollieDataset(
                tokenizer=tokenizer,
                dataset_path=os.path.join(tmpdirname, "tmp.ee.train.jsonl"),
                is_encoder_decoder=is_encoder_decoder,
                max_length=max_length,
                inference=inference,
                prompt_loss_weight=prompt_loss_weight,
                num_workers=1,
            )

    else:
        # List of random integers with len = num_epochs
        random_seeds = random.sample(range(0, 100000), num_epochs)
        with tempfile.TemporaryDirectory() as tmpdirname:
            for epoch in random_seeds:
                with open(os.path.join(tmpdirname, f"tmp.ee.train.{epoch}.jsonl"), "w", encoding="utf8") as f:
                    print(json.dumps({"text": text}, ensure_ascii=False), file=f)

            dataset = CollieDataset(
                tokenizer=tokenizer,
                dataset_path=os.path.join(tmpdirname, "tmp.ee.train.jsonl"),
                is_encoder_decoder=is_encoder_decoder,
                max_length=max_length,
                inference=inference,
                prompt_loss_weight=prompt_loss_weight,
                num_workers=1,
            )

    return dataset, prompt, result


class TestCollieDataset(unittest.TestCase):
    def test_add_eos(self):
        from transformers import AutoTokenizer

        tokenizer = AutoTokenizer.from_pretrained(
            (
                "/gaueko1/hizkuntza-ereduak/LLaMA/lm/huggingface/7B/"
                if os.path.exists("/gaueko1/hizkuntza-ereduak/LLaMA/lm/huggingface/7B/")
                else "EleutherAI/gpt-neo-125m"
            ),
            add_eos_token=True,
            use_fast=True,
        )

        simple_sentence = "This is a sentence to test if the tokenizer adds eos token."
        simple_sentence_ids = tokenizer(simple_sentence, add_special_tokens=True)
        if simple_sentence_ids["input_ids"][-1] != tokenizer.eos_token_id:
            simple_sentence_ids["input_ids"].append(tokenizer.eos_token_id)
            simple_sentence_ids["attention_mask"].append(1)
            # print(simple_sentence_ids)

        self.assertEqual(
            tokenizer.decode(simple_sentence_ids.input_ids, skip_special_tokens=True),
            simple_sentence,
        )

        self.assertEqual(simple_sentence_ids.input_ids[-1], tokenizer.eos_token_id)

        if tokenizer.pad_token_id is None:
            tokenizer.pad_token_id = tokenizer.unk_token_id

        dataset, _, _ = get_dataset(
            tokenizer=tokenizer,
            is_encoder_decoder=False,
            inference=False,
            prompt_loss_weight=0.05,
        )

        # Check if every instance `input_ids` has `eos_token_id`
        self.assertTrue(
            all(inst.input_ids[-1] == tokenizer.eos_token_id for inst in dataset),
            "There are `input_ids` without `eos_token_ids` at the end.",
        )

        # Check if every instance labels has `eos_token_id`
        self.assertTrue(
            all(inst.labels[-1] == tokenizer.eos_token_id for inst in dataset),
            "There are `labels` without `eos_token_ids` at the end.",
        )

        # Check that at inference we don't have eos token
        dataset, _, _ = get_dataset(
            tokenizer=tokenizer,
            is_encoder_decoder=False,
            inference=True,
            prompt_loss_weight=0.05,
        )

        # Check if every instance `input_ids` does not have `eos_token_id`
        self.assertTrue(
            all(inst.input_ids[-1] != tokenizer.eos_token_id for inst in dataset),
            "There are `input_ids` without `eos_token_ids` at the end.",
        )

    def test_inference_token_ids(self):
        from transformers import AutoTokenizer

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

        text1 = """@dataclass
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

        text2 = """@dataclass
        class EnergyAndInfrastructureEvent:
            \"\"\"This class is used to instantiate events that involve Chinese energy and infrastructure projects.\"\"\"
            meeting_attendees: Union[List[str], None] # Persons or organizations that attended the meeting.
            meeting_location: Union[List[str], None] # Location where the meeting happened.
            meeting_topic: Union[List[str], None] # Topic discussed on the meeting
            project_location: Union[List[str], None] # Location of the project
            project_name: Union[List[str], None] # Name of the project

        # This is the sentence to analyze
        sentence = "The Spanish and French delegations met at the sidelines of the Berlin Development Futures conference to discuss Rongovia's proposed Pangean Reunification Facility.

        # The following list contains the events instances that happens in the sentence defined above
        result = []"""

        with tempfile.TemporaryDirectory() as tmpdirname:
            with open(os.path.join(tmpdirname, "tmp.ee.train.jsonl"), "w", encoding="utf8") as f:
                print(json.dumps({"text": text2}, ensure_ascii=False), file=f)
                print(json.dumps({"text": text1}, ensure_ascii=False), file=f)

            dataset = CollieDataset(
                tokenizer=tokenizer,
                dataset_path=os.path.join(tmpdirname, "tmp.ee.train.jsonl"),
                is_encoder_decoder=False,
                max_length=2048,
                inference=True,
                prompt_loss_weight=0.05,
            )

            self.assertEqual(len(dataset), 2)

            # Check if every instance of `input_ids` end with the same token, so at inference the first token
            # of the prompt is the same for all instances
            self.assertTrue(
                all(inst.input_ids[-1] == dataset[0].input_ids[-1] for inst in dataset),
                "The last token of the `input_ids` is not the same for all instances at inference.",
            )

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
            prompt_loss_weight=0.05,
        )

        model_input = dataset[0]["input_ids"]
        labels = dataset[0]["labels"]
        self.assertEqual(model_input, labels)
        self.assertEqual(
            tokenizer.decode(model_input, skip_special_tokens=True, clean_up_tokenization_spaces=False),
            prompt + " " + result,
        )

        # Test Inference
        dataset, prompt, result = get_dataset(
            tokenizer=tokenizer,
            is_encoder_decoder=False,
            inference=True,
            prompt_loss_weight=0.05,
        )

        model_input = dataset[0]["input_ids"]
        self.assertFalse("labels" in dataset[0])
        self.assertEqual(
            tokenizer.decode(model_input, skip_special_tokens=True, clean_up_tokenization_spaces=False),
            prompt,
        )

    """
    We do not support encoder-decoder models yet. T5/mT5/FlanT5 lack the representation
    for '\n' or multiple whitespaces so they cannot be used with CoLLIE prompt encoding.


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
        from torch.utils.data import DataLoader

        from src.dataset.dataset import DataCollatorForCoLLIE
        from transformers import AutoTokenizer

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
            prompt_loss_weight=0.05,
        )

        datacollator = DataCollatorForCoLLIE(
            tokenizer,
            pad_to_multiple_of=2048,
            return_tensors="pt",
            padding=True,
            label_pad_token_id=-100,
        )

        dataloder = DataLoader(dataset, batch_size=1, collate_fn=datacollator, shuffle=False)
        batch = list(dataloder)[0]

        model_input = batch["input_ids"][0].tolist()
        labels = batch["labels"][0].tolist()
        self.assertEqual(
            tokenizer.decode(model_input, skip_special_tokens=True, clean_up_tokenization_spaces=False),
            prompt + " " + result,
        )
        self.assertEqual(
            tokenizer.decode(
                [x for x in labels if x != -100],
                skip_special_tokens=True,
                clean_up_tokenization_spaces=False,
            ),
            prompt + " " + result,
        )
        self.assertEqual(model_input[0], tokenizer.pad_token_id)
        self.assertEqual(labels[0], -100)

        datacollator = DataCollatorForCoLLIE(
            tokenizer,
            pad_to_multiple_of=2048,
            return_tensors="pt",
            padding=True,
            label_pad_token_id=tokenizer.pad_token_id,
        )

        dataloder = DataLoader(dataset, batch_size=1, collate_fn=datacollator, shuffle=False)
        batch = list(dataloder)[0]

        model_input = batch["input_ids"][0].tolist()
        labels = batch["labels"][0].tolist()
        self.assertEqual(model_input, labels)
        self.assertEqual(
            tokenizer.decode(model_input, skip_special_tokens=True, clean_up_tokenization_spaces=False),
            prompt + " " + result,
        )

        self.assertEqual(model_input[0], tokenizer.pad_token_id)
        self.assertEqual(labels[0], tokenizer.pad_token_id)

    def test_weight_loss_mask(self):
        import numpy as np
        from torch.utils.data import DataLoader

        from src.dataset.dataset import DataCollatorForCoLLIE
        from transformers import AutoTokenizer

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

        # Padding = Max Length , Ignore pad token for loss = True
        for prompt_loss_weight in [0.0, 0.05, 0.2, 0.5]:
            # Test Train
            dataset, prompt, result = get_dataset(
                tokenizer=tokenizer,
                is_encoder_decoder=False,
                inference=False,
                prompt_loss_weight=prompt_loss_weight,
            )

            datacollator = DataCollatorForCoLLIE(
                tokenizer,
                pad_to_multiple_of=2048,
                return_tensors="pt",
                padding="max_length",
                label_pad_token_id=-100,
            )

            dataloder = DataLoader(dataset, batch_size=1, collate_fn=datacollator, shuffle=False)
            batch = list(dataloder)[0]

            model_input = batch["input_ids"][0].tolist()
            labels = batch["labels"][0].tolist()
            loss_weights_mask = batch["loss_weight_mask"][0].tolist()

            self.assertEqual(
                tokenizer.decode(model_input, skip_special_tokens=True, clean_up_tokenization_spaces=False),
                prompt + " " + result,
            )
            self.assertEqual(
                tokenizer.decode(
                    [x for x in labels if x != -100],
                    skip_special_tokens=True,
                    clean_up_tokenization_spaces=False,
                ),
                prompt + " " + result,
            )

            prompt_tokens = tokenizer(
                text=prompt,
                max_length=2048,
                truncation=True,
                padding=False,
                return_tensors=None,
                add_special_tokens=True,
            )["input_ids"]

            # Remove the last token if it is an eos token
            if prompt_tokens[-1] == tokenizer.eos_token_id:
                prompt_tokens = prompt_tokens[:-1]

            result_tokens = tokenizer(
                text=result,
                max_length=2048,
                truncation=True,
                padding=False,
                return_tensors=None,
                add_special_tokens=True,
            )["input_ids"]

            if result_tokens[-1] != tokenizer.eos_token_id:
                result_tokens = result_tokens + [tokenizer.eos_token_id]

            num_pad_tokens = len(labels) - len(prompt_tokens) - len(result_tokens)

            # Test that all pad tokens are 0 in loss_weights_mask
            np.testing.assert_almost_equal(
                loss_weights_mask[:num_pad_tokens],
                [0.0] * num_pad_tokens,
            )

            # Test that all result tokens are 1.0 in loss_weights_mask
            np.testing.assert_almost_equal(
                loss_weights_mask[num_pad_tokens + len(prompt_tokens) :],
                [1.0] * len(result_tokens),
            )

            prompt_tokens_loss = sum(loss_weights_mask[num_pad_tokens : num_pad_tokens + len(prompt_tokens)])
            result_tokens_loss = sum(loss_weights_mask[num_pad_tokens + len(prompt_tokens) :])
            total_loss = prompt_tokens_loss + result_tokens_loss

            # print(f"Prompt loss weight: {prompt_loss_weight}")
            # print(f"Prompt loss: {prompt_tokens_loss}")
            # print(f"Result loss: {result_tokens_loss}")
            # print(f"Total loss: {total_loss}")
            # print()

            # Test that the loss of the prompt tokens is prompt_loss_weight of the total loss
            self.assertAlmostEqual(
                prompt_tokens_loss / total_loss,
                prompt_loss_weight,
                places=5,
            )

            # Test that the loss of the result tokens is (1 - prompt_loss_weight) of the total loss
            self.assertAlmostEqual(
                result_tokens_loss / total_loss,
                1 - prompt_loss_weight,
                places=5,
            )

        # Padding = True , Ignore pad token for loss = True
        for prompt_loss_weight in [0.0, 0.05, 0.2, 0.5]:
            # Test Train
            dataset, prompt, result = get_dataset(
                tokenizer=tokenizer,
                is_encoder_decoder=False,
                inference=False,
                prompt_loss_weight=prompt_loss_weight,
            )

            datacollator = DataCollatorForCoLLIE(
                tokenizer,
                pad_to_multiple_of=2048,
                return_tensors="pt",
                padding=True,
                label_pad_token_id=-100,
            )

            dataloder = DataLoader(dataset, batch_size=1, collate_fn=datacollator, shuffle=False)
            batch = list(dataloder)[0]

            model_input = batch["input_ids"][0].tolist()
            labels = batch["labels"][0].tolist()
            loss_weights_mask = batch["loss_weight_mask"][0].tolist()

            self.assertEqual(
                tokenizer.decode(model_input, skip_special_tokens=True, clean_up_tokenization_spaces=False),
                prompt + " " + result,
            )
            self.assertEqual(
                tokenizer.decode(
                    [x for x in labels if x != -100],
                    skip_special_tokens=True,
                    clean_up_tokenization_spaces=False,
                ),
                prompt + " " + result,
            )

            prompt_tokens = tokenizer(
                text=prompt,
                max_length=2048,
                truncation=True,
                padding=False,
                return_tensors=None,
                add_special_tokens=True,
            )["input_ids"]

            # Remove the last token if it is an eos token
            if prompt_tokens[-1] == tokenizer.eos_token_id:
                prompt_tokens = prompt_tokens[:-1]

            result_tokens = tokenizer(
                text=result,
                max_length=2048,
                truncation=True,
                padding=False,
                return_tensors=None,
                add_special_tokens=True,
            )["input_ids"]

            if result_tokens[-1] != tokenizer.eos_token_id:
                result_tokens = result_tokens + [tokenizer.eos_token_id]

            num_pad_tokens = len(labels) - len(prompt_tokens) - len(result_tokens)

            # Test that all pad tokens are 0 in loss_weights_mask
            np.testing.assert_almost_equal(
                loss_weights_mask[:num_pad_tokens],
                [0.0] * num_pad_tokens,
            )

            # Test that all result tokens are 1.0 in loss_weights_mask
            np.testing.assert_almost_equal(
                loss_weights_mask[num_pad_tokens + len(prompt_tokens) :],
                [1.0] * len(result_tokens),
            )

            prompt_tokens_loss = sum(loss_weights_mask[num_pad_tokens : num_pad_tokens + len(prompt_tokens)])
            result_tokens_loss = sum(loss_weights_mask[num_pad_tokens + len(prompt_tokens) :])
            total_loss = prompt_tokens_loss + result_tokens_loss

            # Test that the loss of the prompt tokens is prompt_loss_weight of the total loss
            self.assertAlmostEqual(
                prompt_tokens_loss / total_loss,
                prompt_loss_weight,
                places=5,
            )

            # Test that the loss of the result tokens is (1 - prompt_loss_weight) of the total loss
            self.assertAlmostEqual(
                result_tokens_loss / total_loss,
                1 - prompt_loss_weight,
                places=5,
            )

        # Padding = "Max len" , Ignore pad token for loss = False
        for prompt_loss_weight in [0.0, 0.05, 0.2, 0.5]:
            # Test Train
            dataset, prompt, result = get_dataset(
                tokenizer=tokenizer,
                is_encoder_decoder=False,
                inference=False,
                prompt_loss_weight=prompt_loss_weight,
            )

            datacollator = DataCollatorForCoLLIE(
                tokenizer,
                pad_to_multiple_of=2048,
                return_tensors="pt",
                padding="max_length",
                label_pad_token_id=tokenizer.pad_token_id,
            )

            dataloder = DataLoader(dataset, batch_size=1, collate_fn=datacollator, shuffle=False)
            batch = list(dataloder)[0]

            model_input = batch["input_ids"][0].tolist()
            labels = batch["labels"][0].tolist()
            loss_weights_mask = batch["loss_weight_mask"][0].tolist()

            self.assertEqual(
                tokenizer.decode(model_input, skip_special_tokens=True, clean_up_tokenization_spaces=False),
                prompt + " " + result,
            )
            self.assertEqual(
                tokenizer.decode(
                    [x for x in labels if x != -100],
                    skip_special_tokens=True,
                    clean_up_tokenization_spaces=False,
                ),
                prompt + " " + result,
            )

            prompt_tokens = tokenizer(
                text=prompt,
                max_length=2048,
                truncation=True,
                padding=False,
                return_tensors=None,
                add_special_tokens=True,
            )["input_ids"]

            # Remove the last token if it is an eos token
            if prompt_tokens[-1] == tokenizer.eos_token_id:
                prompt_tokens = prompt_tokens[:-1]

            result_tokens = tokenizer(
                text=result,
                max_length=2048,
                truncation=True,
                padding=False,
                return_tensors=None,
                add_special_tokens=True,
            )["input_ids"]

            if result_tokens[-1] != tokenizer.eos_token_id:
                result_tokens = result_tokens + [tokenizer.eos_token_id]

            num_pad_tokens = len(labels) - len(prompt_tokens) - len(result_tokens)

            # Test that all pad tokens are 1.0 in loss_weights_mask
            np.testing.assert_almost_equal(
                loss_weights_mask[:num_pad_tokens],
                [1.0] * num_pad_tokens,
            )

            # Test that all result tokens are 1.0 in loss_weights_mask
            np.testing.assert_almost_equal(
                loss_weights_mask[num_pad_tokens + len(prompt_tokens) :],
                [1.0] * len(result_tokens),
            )

            prompt_tokens_loss = sum(loss_weights_mask[num_pad_tokens : num_pad_tokens + len(prompt_tokens)])
            result_tokens_loss = sum(loss_weights_mask[num_pad_tokens + len(prompt_tokens) :])
            total_loss = prompt_tokens_loss + result_tokens_loss

            # Test that the loss of the prompt tokens is prompt_loss_weight of the total loss
            self.assertAlmostEqual(
                prompt_tokens_loss / total_loss,
                prompt_loss_weight,
                places=5,
            )

            # Test that the loss of the result tokens is (1 - prompt_loss_weight) of the total loss
            self.assertAlmostEqual(
                result_tokens_loss / total_loss,
                1 - prompt_loss_weight,
                places=5,
            )

    def test_dataset_rotation(self):
        from src.trainer import ConcatDataset
        from transformers import AutoTokenizer

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

        text1 = """@dataclass
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

        prompt1 = """@dataclass
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
        result ="""
        result1 = """[
            EnergyAndInfrastructureEvent(
                meeting_attendees=["Chinese", "Rongovian"],
                meeting_location=["Berlin"],
                meeting_topic=["Pangean Reunification Facility"],
                project_location=["Rongovia"],
                project_name=["Pangean Reunification Facility"]
            ),
        ]"""

        text2 = """@dataclass
        class EnergyAndInfrastructureEvent:
            \"\"\"This class is used to instantiate events that involve Chinese energy and infrastructure projects.\"\"\"
            meeting_attendees: Union[List[str], None] # Persons or organizations that attended the meeting.
            meeting_location: Union[List[str], None] # Location where the meeting happened.
            meeting_topic: Union[List[str], None] # Topic discussed on the meeting
            project_location: Union[List[str], None] # Location of the project
            project_name: Union[List[str], None] # Name of the project

        # This is the sentence to analyze
        sentence = "The Spanish and French delegations met at the sidelines of the Berlin Development Futures conference to discuss Rongovia's proposed Pangean Reunification Facility.

        # The following list contains the events instances that happens in the sentence defined above
        result = [
            EnergyAndInfrastructureEvent(
                meeting_attendees=["Spanish", "French"],
                meeting_location=["Berlin"],
                meeting_topic=["Pangean Reunification Facility"],
                project_location=["Rongovia"],
                project_name=["Pangean Reunification Facility"]
            ),
        ]"""

        prompt2 = """@dataclass
        class EnergyAndInfrastructureEvent:
            \"\"\"This class is used to instantiate events that involve Chinese energy and infrastructure projects.\"\"\"
            meeting_attendees: Union[List[str], None] # Persons or organizations that attended the meeting.
            meeting_location: Union[List[str], None] # Location where the meeting happened.
            meeting_topic: Union[List[str], None] # Topic discussed on the meeting
            project_location: Union[List[str], None] # Location of the project
            project_name: Union[List[str], None] # Name of the project

        # This is the sentence to analyze
        sentence = "The Spanish and French delegations met at the sidelines of the Berlin Development Futures conference to discuss Rongovia's proposed Pangean Reunification Facility.

        # The following list contains the events instances that happens in the sentence defined above
        result ="""
        result2 = """[
            EnergyAndInfrastructureEvent(
                meeting_attendees=["Spanish", "French"],
                meeting_location=["Berlin"],
                meeting_topic=["Pangean Reunification Facility"],
                project_location=["Rongovia"],
                project_name=["Pangean Reunification Facility"]
            ),
        ]"""

        with tempfile.TemporaryDirectory() as tmpdirname:
            with open(os.path.join(tmpdirname, "tmp.ee.train.8.jsonl"), "w", encoding="utf8") as f:
                print(json.dumps({"text": text1}, ensure_ascii=False), file=f)
            with open(os.path.join(tmpdirname, "tmp.ee.train.42.jsonl"), "w", encoding="utf8") as f:
                print(json.dumps({"text": text2}, ensure_ascii=False), file=f)
                print(json.dumps({"text": text1}, ensure_ascii=False), file=f)

            dataset1 = CollieDataset(
                tokenizer=tokenizer,
                dataset_path=os.path.join(tmpdirname, "tmp.ee.train.jsonl"),
                is_encoder_decoder=False,
                max_length=2048,
                inference=False,
                prompt_loss_weight=0.05,
            )

        dataset3, prompt3, result3 = get_dataset(
            tokenizer=tokenizer,
            is_encoder_decoder=False,
            inference=False,
            prompt_loss_weight=0.05,
        )

        train_dataset = ConcatDataset([dataset1, dataset3])

        self.assertEqual(len(train_dataset), 3)

        model_input = train_dataset[0]["input_ids"]
        labels = train_dataset[0]["labels"]
        self.assertEqual(model_input, labels)
        self.assertEqual(
            tokenizer.decode(model_input, skip_special_tokens=True, clean_up_tokenization_spaces=False),
            prompt1 + " " + result1,
        )
        self.assertNotEqual(
            tokenizer.decode(model_input, skip_special_tokens=True, clean_up_tokenization_spaces=False),
            prompt2 + " " + result2,
        )
        self.assertNotEqual(
            tokenizer.decode(model_input, skip_special_tokens=True, clean_up_tokenization_spaces=False),
            prompt3 + " " + result3,
        )

        model_input = train_dataset[1]["input_ids"]
        labels = train_dataset[1]["labels"]
        self.assertEqual(model_input, labels)
        self.assertEqual(
            tokenizer.decode(model_input, skip_special_tokens=True, clean_up_tokenization_spaces=False),
            prompt1 + " " + result1,
        )
        self.assertNotEqual(
            tokenizer.decode(model_input, skip_special_tokens=True, clean_up_tokenization_spaces=False),
            prompt2 + " " + result2,
        )
        self.assertNotEqual(
            tokenizer.decode(model_input, skip_special_tokens=True, clean_up_tokenization_spaces=False),
            prompt3 + " " + result3,
        )

        model_input = train_dataset[2]["input_ids"]
        labels = train_dataset[2]["labels"]
        self.assertEqual(model_input, labels)
        self.assertEqual(
            tokenizer.decode(model_input, skip_special_tokens=True, clean_up_tokenization_spaces=False),
            prompt3 + " " + result3,
        )

        train_dataset.rotate_split()
        train_dataset.rotate_split()
        train_dataset.rotate_split()
        train_dataset.rotate_split()
        train_dataset.rotate_split()

        self.assertEqual(len(train_dataset), 3)
        model_input = train_dataset[0]["input_ids"]
        labels = train_dataset[0]["labels"]
        self.assertEqual(model_input, labels)
        self.assertEqual(
            tokenizer.decode(model_input, skip_special_tokens=True, clean_up_tokenization_spaces=False),
            prompt2 + " " + result2,
        )
        self.assertNotEqual(
            tokenizer.decode(model_input, skip_special_tokens=True, clean_up_tokenization_spaces=False),
            prompt1 + " " + result1,
        )

        self.assertNotEqual(
            tokenizer.decode(model_input, skip_special_tokens=True, clean_up_tokenization_spaces=False),
            prompt3 + " " + result3,
        )

        model_input = train_dataset[1]["input_ids"]
        labels = train_dataset[1]["labels"]
        self.assertEqual(model_input, labels)
        self.assertEqual(
            tokenizer.decode(model_input, skip_special_tokens=True, clean_up_tokenization_spaces=False),
            prompt1 + " " + result1,
        )
        self.assertNotEqual(
            tokenizer.decode(model_input, skip_special_tokens=True, clean_up_tokenization_spaces=False),
            prompt2 + " " + result2,
        )
        self.assertNotEqual(
            tokenizer.decode(model_input, skip_special_tokens=True, clean_up_tokenization_spaces=False),
            prompt3 + " " + result3,
        )

        model_input = train_dataset[2]["input_ids"]
        labels = train_dataset[2]["labels"]
        self.assertEqual(model_input, labels)
        self.assertEqual(
            tokenizer.decode(model_input, skip_special_tokens=True, clean_up_tokenization_spaces=False),
            prompt3 + " " + result3,
        )
