#!/bin/bash
#SBATCH --job-name=CoLLIE+-7B_CodeLLaMA_FULL_MODEL
#SBATCH --cpus-per-task=16
#SBATCH --gres=gpu:4
#SBATCH --mem=128G
#SBATCH --output=.slurm/CoLLIE+-7B_CodeLLaMA_FULL_MODEL.out.txt
#SBATCH --error=.slurm/CoLLIE+-7B_CodeLLaMA_FULL_MODEL.err.txt


source /ikerlariak/osainz006/venvs/collie/bin/activate


export LC_ALL=en_US.UTF-8
export LANG=en_US.UTF-8
export LANGUAGE=en_US.UTF-8
export TOKENIZERS_PARALLELISM=true
export TRANSFORMERS_NO_ADVISORY_WARNINGS=true
export WANDB_ENTITY=hitz-collie
export WANDB_PROJECT=CoLLIEv1.0

echo CUDA_VISIBLE_DEVICES "${CUDA_VISIBLE_DEVICES}"

export PYTHONPATH="$PYTHONPATH:$PWD"
CONFIGS_FOLDER="configs/model_configs"


# Call this script from root directory as: sbatch bash_scripts/CoLLIE+-7B_CodeLLaMA_FULL_MODEL.sh


torchrun --standalone --master_port 37223 --nproc_per_node=4 src/run.py  ${CONFIGS_FOLDER}/CoLLIE+-7B_CodeLLaMA_eval.yaml