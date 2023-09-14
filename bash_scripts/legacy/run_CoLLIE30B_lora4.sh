#!/bin/bash
#SBATCH --job-name=CoLLIE30B_lora4
#SBATCH --cpus-per-task=16
#SBATCH --gres=gpu:1
#SBATCH --mem=128G
#SBATCH --output=.slurm/CoLLIE30B_lora_4.out.txt
#SBATCH --error=.slurm/CoLLIE30B_lora_4.err.txt

# El bueno
# source /ikerlariak/osainz006/venvs/collie-new/bin/activate
source /ikerlariak/osainz006/venvs/collie/bin/activate
# source /gscratch4/users/osainz006/CoLLIE/venv/collie/bin/activate

export LC_ALL=en_US.UTF-8
export LANG=en_US.UTF-8
export LANGUAGE=en_US.UTF-8
export TOKENIZERS_PARALLELISM=true
export TRANSFORMERS_NO_ADVISORY_WARNINGS=true
export WANDB_ENTITY=hitz-collie
export WANDB_PROJECT=CoLLIE

echo ${CUDA_VISIBLE_DEVICES}


CONFIGS_FOLDER="configs/model_configs"

# cd ../src || exit

# Call this script from root directory as: sbatch bash_scripts/run_CoLLIE30B.sh

python3 -m src.run ${CONFIGS_FOLDER}/CoLLIE-30B_lora4.yaml
