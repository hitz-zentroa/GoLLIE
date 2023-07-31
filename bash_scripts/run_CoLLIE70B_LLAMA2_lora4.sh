#!/bin/bash
#SBATCH --job-name=CoLLIE70B_LLAMA2_lora4
#SBATCH --cpus-per-task=16
#SBATCH --gres=gpu:2
#SBATCH --mem=128G
#SBATCH --output=.slurm/CoLLIE70B_LLAMA2_lora4.out.txt
#SBATCH --error=.slurm/CoLLIE70B_LLAMA2_lora4.err.txt


source /ikerlariak/osainz006/venvs/collie/bin/activate


export LC_ALL=en_US.UTF-8
export LANG=en_US.UTF-8
export LANGUAGE=en_US.UTF-8
export TOKENIZERS_PARALLELISM=true
export TRANSFORMERS_NO_ADVISORY_WARNINGS=true
export WANDB_ENTITY=hitz-collie
export WANDB_PROJECT=CoLLIE
export WANDB__SERVICE_WAIT=300

echo ${CUDA_VISIBLE_DEVICES}

CONFIGS_FOLDER="configs/model_configs"


# Call this script from root directory as: sbatch bash_scripts/run_CoLLIE70B.sh


torchrun --standalone --nproc_per_node=2 src/run.py ${CONFIGS_FOLDER}/CoLLIE-70B_LLaMa2_lora4.yaml