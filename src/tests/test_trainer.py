import os
import unittest
from transformers.testing_utils import require_bitsandbytes, require_torch_gpu

from src.model.load_model import load_model_for_training


class TestCollieTrainer(unittest.TestCase):
    @unittest.skipIf(
        not os.path.exists("/gaueko1/hizkuntza-ereduak/LLaMA/lm/huggingface/7B"),
        "No LLaMA model available",
    )
    @require_torch_gpu
    @require_bitsandbytes
    def test_save(self):
        from src.trainer import CollieTrainer
        from src.config import ModelArguments
        from transformers import Seq2SeqTrainingArguments
        from tempfile import TemporaryDirectory

        with TemporaryDirectory() as tmpdirname:
            model_args = ModelArguments(
                model_name_or_path="/gaueko1/hizkuntza-ereduak/LLaMA/lm/huggingface/7B/",
                lora_weights_name_or_path=None,
                torch_dtype="auto",
                use_lora=True,
                int8_quantization=True,
            )

            training_args = Seq2SeqTrainingArguments(
                output_dir=tmpdirname,
            )

            model, _ = load_model_for_training(
                model_weights_name_or_path=model_args.model_name_or_path,
                int8_quantization=model_args.int8_quantization,
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
                any(
                    [elem.startswith("pytorch_model") for elem in os.listdir(tmpdirname)]
                ),
                "If PEFT is used, then the model should not be saved.",
            )

        with TemporaryDirectory() as tmpdirname:
            model_args = ModelArguments(
                model_name_or_path="/gaueko1/hizkuntza-ereduak/LLaMA/lm/huggingface/7B/",
                lora_weights_name_or_path=None,
                torch_dtype="auto",
                use_lora=False,
                int8_quantization=False,
            )

            training_args = Seq2SeqTrainingArguments(
                output_dir=tmpdirname,
            )

            model, _ = load_model_for_training(
                model_weights_name_or_path=model_args.model_name_or_path,
                int8_quantization=model_args.int8_quantization,
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
                any(
                    [elem.startswith("pytorch_model") for elem in os.listdir(tmpdirname)]
                ),
                "If PEFT is not used, then the model have to be saved.",
            )
