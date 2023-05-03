import os
import unittest

from src.dataset.dataset import DataCollatorForCoLLIE
from src.model.load_model import load_model_for_training
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
                any(elem.startswith("pytorch_model") for elem in os.listdir(tmpdirname)),
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
                any(elem.startswith("pytorch_model") for elem in os.listdir(tmpdirname)),
                "If PEFT is not used, then the model have to be saved.",
            )

    def test_compute_loss(self):
        from tempfile import TemporaryDirectory

        from torch.utils.data import DataLoader

        from src.tests.test_dataset import get_dataset
        from src.trainer import CollieTrainer
        from transformers import AutoModelForCausalLM, AutoTokenizer, Seq2SeqTrainingArguments, Trainer

        with TemporaryDirectory() as tmpdirname:
            training_args = Seq2SeqTrainingArguments(
                output_dir=tmpdirname,
            )

            model = AutoModelForCausalLM.from_pretrained("EleutherAI/gpt-neo-125m").to("cpu")

            tokenizer = AutoTokenizer.from_pretrained("EleutherAI/gpt-neo-125m", add_eos_token=True)

            tokenizer.padding_side = "left"

            if tokenizer.pad_token_id is None:
                tokenizer.pad_token_id = tokenizer.unk_token_id

            collie_trainer = CollieTrainer(model=model, args=training_args)
            collie_trainer.model = collie_trainer.model.to("cpu")
            trainer = Trainer(model=model, args=training_args)
            trainer.model = trainer.model.to("cpu")

            dataset, prompt, result = get_dataset(
                tokenizer=tokenizer,
                is_encoder_decoder=False,
                inference=False,
                prompt_loss_weight=0.0,
            )

            datacollator = DataCollatorForCoLLIE(
                tokenizer,
                pad_to_multiple_of=2048,
                return_tensors="pt",
                padding=True,
                label_pad_token_id=-100,
            )

            dataloader = DataLoader(dataset, batch_size=1, collate_fn=datacollator, shuffle=False)
            inputs = list(dataloader)[0]
            inputs = {key: value.to("cpu") for key, value in inputs.items()}

            collie_loss = collie_trainer.compute_loss(model=model, inputs=inputs, return_outputs=False)

            inputs = list(dataloader)[0]
            inputs = {key: value.to("cpu") for key, value in inputs.items() if key not in ["loss_weight_mask"]}
            original_loss = trainer.compute_loss(model=model, inputs=inputs, return_outputs=False)

            self.assertAlmostEqual(collie_loss.item(), original_loss.item())
