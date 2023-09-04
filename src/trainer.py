import bisect
import logging
import os
from typing import Callable, Dict, List, Optional, Tuple, Union

import torch
import torch.nn as nn
from rich.progress import Progress, SpinnerColumn, TimeElapsedColumn
from torch.utils.data import Dataset
from torch.utils.data.dataset import Iterable, IterableDataset, T_co

from src.config import ModelArguments
from src.dataset.dataset import CollieDataset
from transformers import (
    DataCollator,
    PreTrainedModel,
    PreTrainedTokenizerBase,
    Seq2SeqTrainer,
    Seq2SeqTrainingArguments,
    TrainerControl,
    TrainerState,
    TrainingArguments,
)
from transformers.modeling_utils import unwrap_model
from transformers.models.auto.modeling_auto import MODEL_FOR_CAUSAL_LM_MAPPING_NAMES
from transformers.trainer import TRAINING_ARGS_NAME, logger
from transformers.trainer_callback import TrainerCallback
from transformers.trainer_utils import EvalPrediction, has_length
from transformers.utils import SAFE_WEIGHTS_NAME, WEIGHTS_NAME, is_safetensors_available


if is_safetensors_available():
    import safetensors.torch


class RichProgressCallback(TrainerCallback):
    """
    A [`TrainerCallback`] that displays the progress of training or evaluation.
    """

    def __init__(self):
        self.training_bar = None
        self.training_task = None
        self.prediction_bar = None
        self.prediction_task = None

    def on_train_begin(self, args, state, control, **kwargs):
        if state.is_local_process_zero:
            self.training_bar = Progress(
                SpinnerColumn(),
                *Progress.get_default_columns(),
                TimeElapsedColumn(),
                auto_refresh=False,
            )

            self.training_bar.start()
            self.training_task = self.training_bar.add_task("[cyan]Training: ", total=state.max_steps)
        self.current_step = 0

    def on_step_end(self, args, state, control, **kwargs):
        if state.is_local_process_zero:
            self.training_bar.update(
                self.training_task,
                advance=state.global_step - self.current_step,
                refresh=True,
            )
            self.current_step = state.global_step

    def on_prediction_step(self, args, state, control, eval_dataloader=None, **kwargs):
        if state.is_local_process_zero and has_length(eval_dataloader):
            if self.prediction_bar is None:
                self.prediction_bar = Progress(
                    SpinnerColumn(),
                    *Progress.get_default_columns(),
                    TimeElapsedColumn(),
                    auto_refresh=False,
                )
                self.prediction_bar.start()
                self.prediction_task = self.prediction_bar.add_task("[cyan]Predicting: ", total=len(eval_dataloader))
            self.prediction_bar.update(self.prediction_task, advance=1, refresh=True)

    def on_evaluate(self, args, state, control, **kwargs):
        if state.is_local_process_zero:
            if self.prediction_bar is not None:
                self.prediction_bar.stop()
            self.prediction_bar = None
            self.prediction_task = None

    def on_predict(self, args, state, control, **kwargs):
        if state.is_local_process_zero:
            if self.prediction_bar is not None:
                self.prediction_bar.stop()
            self.prediction_bar = None
            self.prediction_task = None

    def on_log(self, args, state, control, logs=None, **kwargs):
        pass

    def on_train_end(self, args, state, control, **kwargs):
        if state.is_local_process_zero:
            self.training_bar.stop()
            self.training_bar = None
            self.training_task = None


class CollieTrainer(Seq2SeqTrainer):
    """
    The CollieTrainer is an adaptation of the 🤗 Transformers Trainer.

    Args:
        model ([`PreTrainedModel`] or `torch.nn.Module`, *optional*):
            The model to train, evaluate or use for predictions. If not provided, a `model_init` must be passed.
            <Tip>
            [`Trainer`] is optimized to work with the [`PreTrainedModel`] provided by the library. You can still use
            your own models defined as `torch.nn.Module` as long as they work the same way as the 🤗 Transformers
            models.
            </Tip>
        args ([`TrainingArguments`], *optional*):
            The arguments to tweak for training. Will default to a basic instance of [`TrainingArguments`] with the
            `output_dir` set to a directory named *tmp_trainer* in the current directory if not provided.
        data_collator (`DataCollator`, *optional*):
            The function to use to form a batch from a list of elements of `train_dataset` or `eval_dataset`. Will
            default to [`default_data_collator`] if no `tokenizer` is provided, an instance of
            [`DataCollatorWithPadding`] otherwise.
        train_dataset (`torch.utils.data.Dataset` or `torch.utils.data.IterableDataset`, *optional*):
            The dataset to use for training. If it is a [`~datasets.Dataset`], columns not accepted by the
            `model.forward()` method are automatically removed.
            Note that if it's a `torch.utils.data.IterableDataset` with some randomization and you are training in a
            distributed fashion, your iterable dataset should either use a internal attribute `generator` that is a
            `torch.Generator` for the randomization that must be identical on all processes (and the Trainer will
            manually set the seed of this `generator` at each epoch) or have a `set_epoch()` method that internally
            sets the seed of the RNGs used.
        eval_dataset (Union[`torch.utils.data.Dataset`, Dict[str, `torch.utils.data.Dataset`]), *optional*):
             The dataset to use for evaluation. If it is a [`~datasets.Dataset`], columns not accepted by the
             `model.forward()` method are automatically removed. If it is a dictionary, it will evaluate on each
             dataset prepending the dictionary key to the metric name.
        tokenizer ([`PreTrainedTokenizerBase`], *optional*):
            The tokenizer used to preprocess the data. If provided, will be used to automatically pad the inputs to the
            maximum length when batching inputs, and it will be saved along the model to make it easier to rerun an
            interrupted training or reuse the fine-tuned model.
        model_init (`Callable[[], PreTrainedModel]`, *optional*):
            A function that instantiates the model to be used. If provided, each call to [`~Trainer.train`] will start
            from a new instance of the model as given by this function.
            The function may have zero argument, or a single one containing the optuna/Ray Tune/SigOpt trial object, to
            be able to choose different architectures according to hyper parameters (such as layer count, sizes of
            inner layers, dropout probabilities etc).
        compute_metrics (`Callable[[EvalPrediction], Dict]`, *optional*):
            The function that will be used to compute metrics at evaluation. Must take a [`EvalPrediction`] and return
            a dictionary string to metric values.
        callbacks (List of [`TrainerCallback`], *optional*):
            A list of callbacks to customize the training loop. Will add those to the list of default callbacks
            detailed in [here](callback).
            If you want to remove one of the default callbacks used, use the [`Trainer.remove_callback`] method.
        optimizers (`Tuple[torch.optim.Optimizer, torch.optim.lr_scheduler.LambdaLR]`, *optional*): A tuple
            containing the optimizer and the scheduler to use. Will default to an instance of [`AdamW`] on your model
            and a scheduler given by [`get_linear_schedule_with_warmup`] controlled by `args`.
        preprocess_logits_for_metrics (`Callable[[torch.Tensor, torch.Tensor], torch.Tensor]`, *optional*):
            A function that preprocess the logits right before caching them at each evaluation step. Must take two
            tensors, the logits and the labels, and return the logits once processed as desired. The modifications made
            by this function will be reflected in the predictions received by `compute_metrics`.
            Note that the labels (second parameter) will be `None` if the dataset does not have them.
    Important attributes:
        - **model** -- Always points to the core model. If using a transformers model, it will be a [`PreTrainedModel`]
          subclass.
        - **model_wrapped** -- Always points to the most external model in case one or more other modules wrap the
          original model. This is the model that should be used for the forward pass. For example, under `DeepSpeed`,
          the inner model is wrapped in `DeepSpeed` and then again in `torch.nn.DistributedDataParallel`. If the inner
          model hasn't been wrapped, then `self.model_wrapped` is the same as `self.model`.
        - **is_model_parallel** -- Whether or not a model has been switched to a model parallel mode (different from
          data parallelism, this means some of the model layers are split on different GPUs).
        - **place_model_on_device** -- Whether or not to automatically place the model on the device - it will be set
          to `False` if model parallel or deepspeed is used, or if the default
          `TrainingArguments.place_model_on_device` is overridden to return `False` .
        - **is_in_train** -- Whether or not a model is currently running `train` (e.g. when `evaluate` is called while
          in `train`)
    """

    def __init__(
        self,
        model: Union[PreTrainedModel, nn.Module] = None,
        args: TrainingArguments = None,
        data_collator: Optional[DataCollator] = None,
        train_dataset: Optional[Dataset] = None,
        eval_dataset: Optional[Union[Dataset, Dict[str, Dataset]]] = None,
        tokenizer: Optional[PreTrainedTokenizerBase] = None,
        model_init: Optional[Callable[[], PreTrainedModel]] = None,
        compute_metrics: Optional[Callable[[EvalPrediction], Dict]] = None,
        callbacks: Optional[List[TrainerCallback]] = None,
        optimizers: Tuple[torch.optim.Optimizer, torch.optim.lr_scheduler.LambdaLR] = (
            None,
            None,
        ),
        preprocess_logits_for_metrics: Optional[Callable[[torch.Tensor, torch.Tensor], torch.Tensor]] = None,
    ):
        if callbacks is None:
            callbacks = [RotateDatasetCallback()]
        else:
            callbacks.append(RotateDatasetCallback())

        self.first_train_batch = True

        # HuggingFace mad TrainingArguments inmutable and therefore the next function crashes
        # We made TrainingArguments mutable again
        TrainingArguments.__setattr__ = object.__setattr__

        # Ensure that the values are floats
        args.set_optimizer(
            name=args.optim,
            learning_rate=float(args.learning_rate),
            weight_decay=float(args.weight_decay),
            beta1=float(args.adam_beta1),
            beta2=float(args.adam_beta2),
            epsilon=float(args.adam_epsilon),
            args=args.optim_args,
        )

        super().__init__(
            model=model,
            args=args,
            data_collator=data_collator,
            train_dataset=train_dataset,
            eval_dataset=eval_dataset,
            tokenizer=None,  # We don't want to save the tokenizer with the model or use it for padding
            model_init=model_init,
            compute_metrics=compute_metrics,
            callbacks=callbacks,
            optimizers=optimizers,
            preprocess_logits_for_metrics=preprocess_logits_for_metrics,
        )
        # Change the tqdm progress callback with `RichProgressCallback`
        # _prev_progress_callback = self.pop_callback(ProgressCallback)
        # if _prev_progress_callback:
        #    self.add_callback(RichProgressCallback)

        if tokenizer is not None:
            # We want the tokenizer to decode the first training batch for debugging purposes
            self.tokenizer = tokenizer
        else:
            self.tokenizer = None

    def compute_loss(self, model, inputs, return_outputs=False):
        """
        How the loss is computed by Trainer. By default, all models return the loss in the first element.
        Subclass and override for custom behavior.
        """

        if "labels" in inputs:
            labels = inputs.pop("labels")
        else:
            raise ValueError("You should supply a labels key to compute the loss")

        if "loss_weight_mask" in inputs:
            loss_weight_mask = inputs.pop("loss_weight_mask")
        else:
            raise ValueError("You should supply a loss_weight_mask key to compute the loss")

        # Print first batch of training data for debugging
        if self.first_train_batch:
            self.first_train_batch = False
            print_input_ids = inputs["input_ids"][:8].clone().detach().cpu()
            print_attention_mask = inputs["attention_mask"][:8].clone().detach().cpu()
            print_labels = labels[:8].clone().detach().cpu()
            print_loss_weight_mask = loss_weight_mask[:8].clone().detach().cpu()

            print("*** First batch of training data ***")
            print("-- input_ids --")
            if self.tokenizer is not None:
                print_input_ids[print_input_ids == -100] = self.tokenizer.pad_token_id
                print(self.tokenizer.batch_decode(print_input_ids))
            else:
                print(print_input_ids.tolist())
            print("-- attention_mask --")
            print(print_attention_mask.tolist())
            print("-- labels --")
            if self.tokenizer is not None:
                print_labels[print_labels == -100] = self.tokenizer.pad_token_id
                print(self.tokenizer.batch_decode(print_labels))
            else:
                print(print_labels[:8].tolist())
            print("-- loss_weight_mask --")
            print(print_loss_weight_mask.tolist())
            print()

        outputs = model(**inputs, use_cache=False)

        logits = outputs["logits"] if isinstance(outputs, dict) else outputs[0]

        model_name = unwrap_model(model)._get_name()
        if model_name in MODEL_FOR_CAUSAL_LM_MAPPING_NAMES.values() or model_name == "PeftModelForCausalLM":
            logits = logits[..., :-1, :].contiguous()
            labels = labels[..., 1:].contiguous()
            loss_weight_mask = loss_weight_mask[..., 1:].contiguous()

        logits = logits.view(-1, logits.size(-1))
        labels = labels.view(-1)
        loss_weight_mask = loss_weight_mask.view(-1)
        loss_fct = nn.CrossEntropyLoss(reduction="none", ignore_index=-100)

        loss = loss_fct(logits, labels)
        loss = torch.sum(loss * loss_weight_mask) / torch.sum(loss_weight_mask)

        return (loss, outputs) if return_outputs else loss

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
        # try:
        #     from peft import PeftModel, LoraModel

        #     if isinstance(unwrap_model(self.model), PeftModel):
        #         if isinstance(unwrap_model(self.model).base_model, LoraModel):
        #             unwrap_model(self.model).save_pretrained(
        #                 output_dir,
        #             )
        #             return
        # except ImportError:
        #     pass

        try:
            from peft import PeftModel
        except ImportError:
            PeftModel = None

        if not isinstance(self.model, PreTrainedModel) and not (PeftModel and isinstance(self.model, PeftModel)):
            if state_dict is None:
                state_dict = self.model.state_dict()

            if isinstance(unwrap_model(self.model), PreTrainedModel):
                unwrap_model(self.model).save_pretrained(
                    output_dir,
                    state_dict=state_dict,
                    safe_serialization=self.args.save_safetensors,
                )
            else:
                logger.info("Trainer.model is not a `PreTrainedModel`, only saving its state dict.")
                if self.args.save_safetensors:
                    safetensors.torch.save_file(state_dict, os.path.join(output_dir, SAFE_WEIGHTS_NAME))
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


class ConcatDataset(Dataset[T_co]):
    r"""Dataset as a concatenation of multiple datasets.

    This class is useful to assemble different existing datasets.

    Args:
        datasets (sequence): List of datasets to be concatenated
    """
    datasets: List[CollieDataset]
    cumulative_sizes: List[int]

    @staticmethod
    def cumsum(sequence):
        r, s = [], 0
        for e in sequence:
            l = len(e)
            r.append(l + s)
            s += l
        return r

    def __init__(self, datasets: Iterable[CollieDataset]) -> None:
        super().__init__()
        self.datasets = list(datasets)
        assert len(self.datasets) > 0, "datasets should not be an empty iterable"  # type: ignore[arg-type]
        for d in self.datasets:
            assert not isinstance(d, IterableDataset), "ConcatDataset does not support IterableDataset"
        self.cumulative_sizes = self.cumsum(self.datasets)

    def __len__(self):
        return self.cumulative_sizes[-1]

    def __getitem__(self, idx):
        if idx < 0:
            if -idx > len(self):
                raise ValueError("absolute value of index should not exceed dataset length")
            idx = len(self) + idx
        dataset_idx = bisect.bisect_right(self.cumulative_sizes, idx)
        if dataset_idx == 0:
            sample_idx = idx
        else:
            sample_idx = idx - self.cumulative_sizes[dataset_idx - 1]
        return self.datasets[dataset_idx][sample_idx]

    @property
    def cummulative_sizes(self):
        logging.warning("cummulative_sizes attribute is renamed to cumulative_sizes", DeprecationWarning, stacklevel=2)
        return self.cumulative_sizes

    def rotate_split(self):
        for x in self.datasets:
            x.rotate_split()
        self.cumulative_sizes = self.cumsum(self.datasets)


class RotateDatasetCallback(TrainerCallback):
    def on_epoch_end(self, args: TrainingArguments, state: TrainerState, control: TrainerControl, **kwargs):
        if "train_dataloader" in kwargs:
            kwargs["train_dataloader"].dataset.rotate_split()
        else:
            logging.warning("No train_dataloader in kwargs. Skipping rotate_split()")


def get_correct_torch_dtype(
    quantization: int,
    model_args: ModelArguments,
    training_args: Seq2SeqTrainingArguments,
) -> "str":
    """
    Returns the correct torch dtype based on the model and training arguments (if quantization is enabled).

    Args:
        quantization (`int`, optional):
            '4' or '8' for 4 bits or 8 bits quantization or None for 16/32bits training. Defaults to `None`.
        model_args (:class:`~transformers.ModelArguments`):
            The model arguments.
        training_args (:class:`~transformers.Seq2SeqTrainingArguments`):
            The training arguments.

    Returns:
        :obj:`str`: The correct torch dtype.
    """

    if isinstance(quantization, str):
        quantization = int(quantization)

    if quantization in [4, 8]:
        if training_args.fp16:
            if model_args.torch_dtype in ["auto", None]:
                logging.warning(
                    "Quantification and fp16 are enabled, but torch_dtype is not set. Setting torch_dtype to float16."
                )

            elif model_args.torch_dtype != "float16":
                logging.warning(
                    f"Quantification and fp16 are enabled, but torch_dtype is set to {model_args.torch_dtype}. "
                    "This can cause issues. We will override torch_dtype to float16."
                )
            return "float16"

        elif training_args.bf16:
            if model_args.torch_dtype in ["auto", None]:
                logging.warning(
                    "Quantification and bf16 are enabled, but torch_dtype is not set. Setting torch_dtype to bfloat16."
                )
            elif model_args.torch_dtype != "bfloat16":
                logging.warning(
                    f"Quantification and bf16 are enabled, but torch_dtype is set to {model_args.torch_dtype}. "
                    "This can cause issues. We will override torch_dtype to bfloat16."
                )
            return "bfloat16"

    return model_args.torch_dtype
