import os
import unittest

import psutil

from src.dataset.dataset import DataCollatorForCoLLIE
from src.model.load_model import load_model
from transformers.testing_utils import require_bitsandbytes, require_torch_gpu


class TestCollieTrainer(unittest.TestCase):
    @unittest.skipIf(
        not os.path.exists("/gaueko1/hizkuntza-ereduak/LLaMA/lm/huggingface/7B"),
        "No LLaMA model available",
    )
    @require_torch_gpu
    @require_bitsandbytes
    def test_save(self):
        from tempfile import TemporaryDirectory

        from src.config import ModelArguments
        from src.trainer import CollieTrainer
        from transformers import Seq2SeqTrainingArguments

        with TemporaryDirectory() as tmpdirname:
            model_args = ModelArguments(
                model_name_or_path="/gaueko1/hizkuntza-ereduak/LLaMA/lm/huggingface/7B/",
                lora_weights_name_or_path=None,
                torch_dtype="auto",
                use_lora=True,
                quantization=4,
            )

            training_args = Seq2SeqTrainingArguments(
                output_dir=tmpdirname,
            )

            model, _ = load_model(
                inference=False,
                model_weights_name_or_path=model_args.model_name_or_path,
                quantization=model_args.quantization,
                use_lora=model_args.use_lora,
                lora_target_modules=model_args.lora_target_modules,
                torch_dtype=model_args.torch_dtype,
            )

            trainer = CollieTrainer(model=model, args=training_args)
            trainer.save_model()

            self.assertTrue(
                os.path.exists(os.path.join(tmpdirname, "adapter_model.bin")),
                "If PEFT is used, then the adapter must be saved.",
            )
            self.assertFalse(
                any(elem.startswith("pytorch_model") for elem in os.listdir(tmpdirname)),
                "If PEFT is used, then the model should not be saved.",
            )

        with TemporaryDirectory() as tmpdirname:
            model_args = ModelArguments(
                model_name_or_path="/gaueko1/hizkuntza-ereduak/LLaMA/lm/huggingface/7B/",
                lora_weights_name_or_path=None,
                torch_dtype="auto",
                use_lora=False,
                quantization=None,
            )

            training_args = Seq2SeqTrainingArguments(
                output_dir=tmpdirname,
            )

            model, _ = load_model(
                inference=False,
                model_weights_name_or_path=model_args.model_name_or_path,
                quantization=model_args.quantization,
                use_lora=model_args.use_lora,
                lora_target_modules=model_args.lora_target_modules,
                torch_dtype=model_args.torch_dtype,
            )

            trainer = CollieTrainer(model=model, args=training_args)
            trainer.save_model()

            self.assertFalse(
                os.path.exists(os.path.join(tmpdirname, "adapter_model.bin")),
                "If PEFT is not used, then no adapter must be saved.",
            )
            self.assertTrue(
                any(elem.startswith("pytorch_model") for elem in os.listdir(tmpdirname)),
                "If PEFT is not used, then the model have to be saved.",
            )

    @unittest.skipIf(psutil.virtual_memory().total / (1 << 30) < 15, "Not enough RAM available to run the test")
    def test_compute_loss(self):
        from tempfile import TemporaryDirectory

        from torch.utils.data import DataLoader

        from src.model.load_model import load_model
        from src.tests.test_dataset import get_dataset
        from src.trainer import CollieTrainer
        from transformers import Seq2SeqTrainingArguments, Trainer

        with TemporaryDirectory() as tmpdirname:
            training_args = Seq2SeqTrainingArguments(
                output_dir=tmpdirname,
            )

            model, tokenizer = load_model(
                inference=False,
                model_weights_name_or_path="EleutherAI/gpt-neo-125m",
                quantization=None,
                use_lora=False,
                lora_target_modules=None,
                torch_dtype="float32",
            )

            collie_trainer = CollieTrainer(model=model, args=training_args)
            collie_trainer.model = collie_trainer.model.to("cpu")
            trainer = Trainer(model=model, args=training_args)
            trainer.model = trainer.model.to("cpu")

            dataset, prompt, result = get_dataset(
                tokenizer=tokenizer,
                is_encoder_decoder=False,
                inference=False,
                prompt_loss_weight=0.0,
                max_length=tokenizer.model_max_length,
            )

            datacollator = DataCollatorForCoLLIE(
                tokenizer,
                pad_to_multiple_of=tokenizer.model_max_length,
                return_tensors="pt",
                padding=True,
                label_pad_token_id=-100,
            )

            dataloader = DataLoader(dataset, batch_size=1, collate_fn=datacollator, shuffle=False)
            inputs = list(dataloader)[0]
            inputs = {key: value.to("cpu") for key, value in inputs.items()}
            not_result_mask = inputs["loss_weight_mask"] < 1.0

            collie_loss = collie_trainer.compute_loss(model=model, inputs=inputs, return_outputs=False)

            inputs = list(dataloader)[0]
            inputs = {key: value.to("cpu") for key, value in inputs.items() if key not in ["loss_weight_mask"]}
            inputs["labels"][not_result_mask] = -100

            model_loss = model(**inputs).loss
            original_loss = trainer.compute_loss(model=model, inputs=inputs, return_outputs=False)

            self.assertAlmostEqual(model_loss.item(), original_loss.item(), delta=1e-5)
            self.assertAlmostEqual(collie_loss.item(), original_loss.item(), delta=1e-5)

    @unittest.skipIf(psutil.virtual_memory().total / (1 << 30) < 15, "Not enough RAM available to run the test")
    def test_compute_loss_lora(self):
        from tempfile import TemporaryDirectory

        from torch.utils.data import DataLoader

        from src.model.load_model import load_model
        from src.tests.test_dataset import get_dataset
        from src.trainer import CollieTrainer
        from transformers import Seq2SeqTrainingArguments, Trainer

        with TemporaryDirectory() as tmpdirname:
            training_args = Seq2SeqTrainingArguments(
                output_dir=tmpdirname,
            )

            model, tokenizer = load_model(
                inference=False,
                model_weights_name_or_path="EleutherAI/gpt-neo-125m",
                quantization=None,
                use_lora=True,
                torch_dtype="float32",
            )

            collie_trainer = CollieTrainer(model=model, args=training_args)
            collie_trainer.model = collie_trainer.model.to("cpu")
            trainer = Trainer(model=model, args=training_args)
            trainer.model = trainer.model.to("cpu")

            dataset, prompt, result = get_dataset(
                tokenizer=tokenizer,
                is_encoder_decoder=False,
                inference=False,
                prompt_loss_weight=0.0,
                max_length=tokenizer.model_max_length,
            )

            datacollator = DataCollatorForCoLLIE(
                tokenizer,
                pad_to_multiple_of=tokenizer.model_max_length,
                return_tensors="pt",
                padding=True,
                label_pad_token_id=-100,
            )

            dataloader = DataLoader(dataset, batch_size=1, collate_fn=datacollator, shuffle=False)
            inputs = list(dataloader)[0]
            inputs = {key: value.to("cpu") for key, value in inputs.items()}
            not_result_mask = inputs["loss_weight_mask"] < 1.0

            collie_loss = collie_trainer.compute_loss(model=model, inputs=inputs, return_outputs=False)

            inputs = list(dataloader)[0]
            inputs = {key: value.to("cpu") for key, value in inputs.items() if key not in ["loss_weight_mask"]}
            inputs["labels"][not_result_mask] = -100

            model_loss = model(**inputs).loss
            original_loss = trainer.compute_loss(model=model, inputs=inputs, return_outputs=False)

            self.assertAlmostEqual(model_loss.item(), original_loss.item(), delta=1e-5)
            self.assertAlmostEqual(collie_loss.item(), original_loss.item(), delta=1e-5)
