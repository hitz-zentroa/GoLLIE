#!/bin/bash
#SBATCH --job-name=CoLLIE7B_full_fp16
#SBATCH --cpus-per-task=16
#SBATCH --gres=gpu:4
#SBATCH --mem=128G
#SBATCH --output=.slurm/CoLLIE7B_full_fp16.out.txt
#SBATCH --error=.slurm/CoLLIE7B_full_fp16.err.txt

source /ikerlariak/osainz006/venvs/collie/bin/activate

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

# Call this script from root directory as: sbatch bash_scripts/run_CoLLIE7B.sh


torchrun --standalone --nproc_per_node=4 src/run.py ${CONFIGS_FOLDER}/CoLLIE-7B_fp16.yaml

