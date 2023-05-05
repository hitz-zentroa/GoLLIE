#!/bin/bash
#SBATCH --job-name=CoLLIE7B5%_eval
#SBATCH --cpus-per-task=16
#SBATCH --gres=gpu:1
#SBATCH --mem=128G
#SBATCH --output=.slurm/CoLLIE7B5%_eval.out.txt
#SBATCH --error=.slurm/CoLLIE7B5%_eval.err.txt

source /gscratch4/users/osainz006/CoLLIE/venv/collie/bin/activate

export LC_ALL=en_US.UTF-8
export LANG=en_US.UTF-8
export LANGUAGE=en_US.UTF-8
export TOKENIZERS_PARALLELISM=true
export TRANSFORMERS_NO_ADVISORY_WARNINGS=true
export WANDB_ENTITY=hitz-collie
export WANDB_PROJECT=CoLLIE


python3 -m src.run configs/model_configs/CoLLIE-7B-prompt5%_eval.yaml

