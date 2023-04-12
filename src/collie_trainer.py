from transformers import Seq2SeqTrainer, PreTrainedModel
from transformers.modeling_utils import unwrap_model
import os
import torch
from typing import Optional
from transformers.trainer import logger, TRAINING_ARGS_NAME
from transformers.utils import SAFE_WEIGHTS_NAME, WEIGHTS_NAME, is_safetensors_available

if is_safetensors_available():
    import safetensors.torch


class CollieTrainer(Seq2SeqTrainer):
    # Modify the Seq2SeqTrainer from transformers to only save the LoRA weights if we are using a LoRA model
    # Original trainer saves the full state dict. It doesn't make sense for us to create a full copy
    # of LLaMA weights each time we save a checkpoint since we do not modify them.
    def _save(self, output_dir: Optional[str] = None, state_dict=None):
        # If we are executing this function, we are the process zero, so we don't check for that.
        output_dir = output_dir if output_dir is not None else self.args.output_dir
        os.makedirs(output_dir, exist_ok=True)
        logger.info(f"Saving model checkpoint to {output_dir}")
        # Save a trained model and configuration using `save_pretrained()`.
        # They can then be reloaded using `from_pretrained()

        # Find out if the model is a LoRA Peft Model
        try:
            from peft import PeftModel, LoraModel

            if isinstance(unwrap_model(self.model), PeftModel):
                if isinstance(unwrap_model(self.model).base_model, LoraModel):
                    unwrap_model(self.model).save_pretrained(
                        output_dir,
                    )
                    return
        except ImportError:
            pass

        if not isinstance(self.model, PreTrainedModel):
            if state_dict is None:
                state_dict = self.model.state_dict()

            if isinstance(unwrap_model(self.model), PreTrainedModel):
                unwrap_model(self.model).save_pretrained(
                    output_dir,
                    state_dict=state_dict,
                    safe_serialization=self.args.save_safetensors,
                )
            else:
                logger.info(
                    "Trainer.model is not a `PreTrainedModel`, only saving its state"
                    " dict."
                )
                if self.args.save_safetensors:
                    safetensors.torch.save_file(
                        state_dict, os.path.join(output_dir, SAFE_WEIGHTS_NAME)
                    )
                else:
                    torch.save(state_dict, os.path.join(output_dir, WEIGHTS_NAME))
        else:
            self.model.save_pretrained(
                output_dir,
                state_dict=state_dict,
                safe_serialization=self.args.save_safetensors,
            )

        if self.tokenizer is not None:
            self.tokenizer.save_pretrained(output_dir)

        # Good practice: save your training arguments together with the trained model
        torch.save(self.args, os.path.join(output_dir, TRAINING_ARGS_NAME))
