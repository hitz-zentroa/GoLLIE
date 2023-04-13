#!/bin/bash
#SBATCH --job-name=CoLLIE7B_zeroshot
#SBATCH --cpus-per-task=16
#SBATCH --gres=gpu:1
#SBATCH --mem=128G
#SBATCH --output=.slurm/CoLLIE7B_zeroshot.out
#SBATCH --error=.slurm/CoLLIE7B_zeroshot.err

source /gscratch4/users/osainz006/CoLLIE/venv/collie/bin/activate

export LC_ALL=en_US.UTF-8
export LANG=en_US.UTF-8
export LANGUAGE=en_US.UTF-8
export TOKENIZERS_PARALLELISM=true
export TRANSFORMERS_NO_ADVISORY_WARNINGS=true
export WANDB_ENTITY=hitz-collie
export WANDB_PROJECT=CoLLIE


CONFIGS_FOLDER="configs/model_configs/zero-shot"

# cd ../src || exit

# Call this script from root directory as: sbatch bash_scripts/run_CoLLIE7B.sh


python3 src/run.py ${CONFIGS_FOLDER}/CoLLIE-7B_int8.yaml
python3 src/run.py ${CONFIGS_FOLDER}/CoLLIE-7B_fp16.yaml





