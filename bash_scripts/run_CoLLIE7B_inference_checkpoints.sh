#!/bin/bash
#SBATCH --job-name=CoLLIE7B_eval
#SBATCH --cpus-per-task=16
#SBATCH --gres=gpu:2
#SBATCH --mem=128G
#SBATCH --output=.slurm/CoLLIE7B_eval.out.txt
#SBATCH --error=.slurm/CoLLIE7B_eval.err.txt

source /gscratch4/users/osainz006/CoLLIE/venv/collie/bin/activate

export LC_ALL=en_US.UTF-8
export LANG=en_US.UTF-8
export LANGUAGE=en_US.UTF-8
export TOKENIZERS_PARALLELISM=true
export TRANSFORMERS_NO_ADVISORY_WARNINGS=true
export WANDB_ENTITY=hitz-collie
export WANDB_PROJECT=CoLLIE


CONFIGS_FOLDER="configs/model_configs/tmp"

export PYTHONPATH="$PYTHONPATH:$PWD"
# cd ../src || exit

# Call this script from root directory as: sbatch bash_scripts/run_CoLLIE7B.sh
torchrun --standalone --nproc_per_node=2 src/run.py ${CONFIGS_FOLDER}/CoLLIE-7B_optim_AdamW_lr_3e4_cosine.yaml
torchrun --standalone --nproc_per_node=2 src/run.py ${CONFIGS_FOLDER}/CoLLIE-7B_optim_AdamW_lr_3e4_cosine_ignore_prompt_loss.yaml
torchrun --standalone --nproc_per_node=2 src/run.py ${CONFIGS_FOLDER}/CoLLIE-7B_optim_AdamW_lr_3e4_constant.yaml
torchrun --standalone --nproc_per_node=2 src/run.py ${CONFIGS_FOLDER}/CoLLIE-7B_optim_AdamW_lr_3e4_constant_ignore_prompt_loss.yaml

# python3 trainer.py ../CoLLIE_configs/CoLLIE-7B_eval.yaml
