#!/bin/bash
#SBATCH --job-name=CoLLIE7B_deepspeed
#SBATCH --cpus-per-task=16
#SBATCH --gres=gpu:1
#SBATCH --mem=128G
#SBATCH --output=.slurm/CoLLIE7B_deepspeed.out.txt
#SBATCH --error=.slurm/CoLLIE7B_deepspeed.err.txt

source /gscratch4/users/osainz006/CoLLIE/venv/collie/bin/activate

export LC_ALL=en_US.UTF-8
export LANG=en_US.UTF-8
export LANGUAGE=en_US.UTF-8
export TOKENIZERS_PARALLELISM=true
export TRANSFORMERS_NO_ADVISORY_WARNINGS=true
export WANDB_ENTITY=hitz-collie
export WANDB_PROJECT=CoLLIE


CONFIGS_FOLDER="configs/model_configs"

export PYTHONPATH="$PYTHONPATH:$PWD"
# cd ../src || exit


deepspeed src/run.py ${CONFIGS_FOLDER}/CoLLIE-7B-deepspeed.yaml
