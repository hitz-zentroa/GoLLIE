#!/bin/bash
#SBATCH --job-name=GoLLIE-34B_CodeLLaMA
#SBATCH --cpus-per-task=16
#SBATCH --gres=gpu:2
#SBATCH --mem=128G
#SBATCH --output=.slurm/GoLLIE-34B_CodeLLaMA.out.txt
#SBATCH --error=.slurm/GoLLIE-34B_CodeLLaMA.err.txt


source /ikerlariak/osainz006/venvs/GoLLIE/bin/activate


export LC_ALL=en_US.UTF-8
export LANG=en_US.UTF-8
export LANGUAGE=en_US.UTF-8
export TOKENIZERS_PARALLELISM=true
export TRANSFORMERS_NO_ADVISORY_WARNINGS=true
export WANDB_ENTITY=hitz-GoLLIE
export WANDB_PROJECT=GoLLIEv1.0

echo CUDA_VISIBLE_DEVICES "${CUDA_VISIBLE_DEVICES}"

export PYTHONPATH="$PYTHONPATH:$PWD"
CONFIGS_FOLDER="configs/model_configs/eval"

# Call this script from root directory as: sbatch bash_scripts/GoLLIE-34B_CodeLLaMA.sh

torchrun --standalone --master_port 37228 --nproc_per_node=2 src/run.py ${CONFIGS_FOLDER}/GoLLIE-34B_CodeLLaMA.yaml

