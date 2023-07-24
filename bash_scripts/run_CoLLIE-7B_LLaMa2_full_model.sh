#!/bin/bash
#SBATCH --job-name=CoLLIE-7B_LLaMa2
#SBATCH --cpus-per-task=16
#SBATCH --gres=gpu:2
#SBATCH --mem=128G
#SBATCH --output=.slurm/CoLLIE-7B_LLaMa2.out.txt
#SBATCH --error=.slurm/CoLLIE-7B_LLaMa2.err.txt

source /ikerlariak/osainz006/venvs/collie/bin/activate

export LC_ALL=en_US.UTF-8
export LANG=en_US.UTF-8
export LANGUAGE=en_US.UTF-8
export TOKENIZERS_PARALLELISM=true
export TRANSFORMERS_NO_ADVISORY_WARNINGS=true
export WANDB_ENTITY=hitz-collie
export WANDB_PROJECT=CoLLIE
export WANDB__SERVICE_WAIT=300

CONFIGS_FOLDER="configs/model_configs"
export PYTHONPATH="$PYTHONPATH:$PWD"
export OMP_NUM_THREADS=16

CONFIGS_FOLDER="configs/model_configs"

torchrun --standalone --nproc_per_node=2 src/run.py ${CONFIGS_FOLDER}/CoLLIE-7B_LLaMa2.yaml