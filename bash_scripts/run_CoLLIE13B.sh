#!/bin/bash
#SBATCH --job-name=CoLLIE7B
#SBATCH --cpus-per-task=16
#SBATCH --gres=gpu:1
#SBATCH --mem=128G
#SBATCH --output=.slurm/CoLLIE7B.out.txt
#SBATCH --error=.slurm/CoLLIE7B.err.txt

source /gscratch4/users/osainz006/CoLLIE/venv/collie/bin/activate

export LC_ALL=en_US.UTF-8
export LANG=en_US.UTF-8
export LANGUAGE=en_US.UTF-8
export TOKENIZERS_PARALLELISM=true
export TRANSFORMERS_NO_ADVISORY_WARNINGS=true
export WANDB_ENTITY=hitz-collie
export WANDB_PROJECT=CoLLIE


CONFIGS_FOLDER="configs/model_configs"

# cd ../src || exit

# Call this script from root directory as: sbatch bash_scripts/run_CoLLIE7B.sh
python3 src/run.py ${CONFIGS_FOLDER}/CoLLIE-7B_evalcheckpoints.yaml
python3 src/run.py ${CONFIGS_FOLDER}/CoLLIE-13B.yaml
# python3 trainer.py ../CoLLIE_configs/CoLLIE-7B_eval.yaml
