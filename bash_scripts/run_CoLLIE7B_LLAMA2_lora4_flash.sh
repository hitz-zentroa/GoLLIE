#!/bin/bash
#SBATCH --job-name=CoLLIE7B_lora4_flash
#SBATCH --cpus-per-task=16
#SBATCH --gres=gpu:1
#SBATCH --mem=128G
#SBATCH --output=.slurm/CoLLIE7B_lora_4_flash.out.txt
#SBATCH --error=.slurm/CoLLIE7B_lora_4_flash.err.txt


source /ikerlariak/osainz006/venvs/collie/bin/activate


export LC_ALL=en_US.UTF-8
export LANG=en_US.UTF-8
export LANGUAGE=en_US.UTF-8
export TOKENIZERS_PARALLELISM=true
export TRANSFORMERS_NO_ADVISORY_WARNINGS=true
export WANDB_ENTITY=hitz-collie
export WANDB_PROJECT=CoLLIE

echo ${CUDA_VISIBLE_DEVICES}

CONFIGS_FOLDER="configs/model_configs"


# Call this script from root directory as: sbatch bash_scripts/run_CoLLIE7B.sh


python3 -m src.run_flash_att ${CONFIGS_FOLDER}/run_CoLLIE7B_LLAMA2_lora4_flash.sh
python3 -m src.run ${CONFIGS_FOLDER}/run_CoLLIE7B_LLAMA2_lora4_flash_eval.sh
