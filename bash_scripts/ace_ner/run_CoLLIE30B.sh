#!/bin/bash
#SBATCH --job-name=CoLLIE30B-ace-ner
#SBATCH --cpus-per-task=16
#SBATCH --gres=gpu:1
#SBATCH --mem=128G
#SBATCH --output=.slurm/CoLLIE30B-ace-ner.out.txt
#SBATCH --error=.slurm/CoLLIE30B-ace-ner.err.txt

source /gscratch4/users/osainz006/CoLLIE/venv/collie/bin/activate

export LC_ALL=en_US.UTF-8
export LANG=en_US.UTF-8
export LANGUAGE=en_US.UTF-8
export TOKENIZERS_PARALLELISM=true
export TRANSFORMERS_NO_ADVISORY_WARNINGS=true
export WANDB_ENTITY=hitz-collie
export WANDB_PROJECT=CoLLIE


CONFIGS_FOLDER="configs/model_configs/ace_entities"

# cd ../src || exit

# Call this script from root directory as: sbatch bash_scripts/run_CoLLIE30B.sh

python3 -m src.run  ${CONFIGS_FOLDER}/CoLLIE-30B.yaml

