#!/bin/bash
#SBATCH --job-name=CoLLIE7B_fsdp
#SBATCH --cpus-per-task=16
#SBATCH --gres=gpu:1
#SBATCH --mem=128G
#SBATCH --output=.slurm/CoLLIE7B_fsdp.out.txt
#SBATCH --error=.slurm/CoLLIE7B_fsdp.err.txt

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


torchrun --standalone --nproc_per_node=2 src/run.py  ${CONFIGS_FOLDER}/CoLLIE-7B-fsdp.yaml
