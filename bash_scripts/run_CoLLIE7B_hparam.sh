#!/bin/bash
#SBATCH --job-name=CoLLIE7B_hparams
#SBATCH --cpus-per-task=16
#SBATCH --gres=gpu:1
#SBATCH --mem=128G
#SBATCH --output=.slurm/CoLLIE7B_hparams.out
#SBATCH --error=.slurm/CoLLIE7B_hparams.err

source /gscratch4/users/osainz006/CoLLIE/venv/collie/bin/activate

export LC_ALL=en_US.UTF-8
export LANG=en_US.UTF-8
export LANGUAGE=en_US.UTF-8
export TOKENIZERS_PARALLELISM=true
export TRANSFORMERS_NO_ADVISORY_WARNINGS=true
export WANDB_ENTITY=hitz-collie
export WANDB_PROJECT=CoLLIE


CONFIGS_FOLDER="configs/model_configs/hparams"

# cd ../src || exit

# Call this script from root directory as: sbatch bash_scripts/run_CoLLIE7B.sh

# COSINE SCHEDULER
python3 -m src.run ${CONFIGS_FOLDER}/CoLLIE-7B_optim_AdamW_lr_3e4_cosine.yaml
python3 -m src.run ${CONFIGS_FOLDER}/CoLLIE-7B_optim_AdamW_lr_3e4_cosine_ignore_prompt_loss.yaml

#CONSTANT SCHEDULER
python3 -m src.run ${CONFIGS_FOLDER}/CoLLIE-7B_optim_AdamW_lr_3e4_constant.yaml
python3 -m src.run ${CONFIGS_FOLDER}/CoLLIE-7B_optim_AdamW_lr_3e4_constant_ignore_prompt_loss.yaml

#Big Lora
python3 -m src.run ${CONFIGS_FOLDER}/CoLLIE-7B_optim_AdamW_lr_3e4_cosine_bigLora.yaml
python3 -m src.run ${CONFIGS_FOLDER}/CoLLIE-7B_optim_AdamW_lr_3e4_cosine_bigLora_ignore_prompt_loss.yaml


# OTHER OPTIMIZERS
#python3 src/run.py ${CONFIGS_FOLDER}/CoLLIE-7B_optim_FusedAdamW_lr_3e4_cosine.yaml
#python3 src/run.py ${CONFIGS_FOLDER}/CoLLIE-7B_optim_AdaFactor_lr_1e4_cosine.yaml

