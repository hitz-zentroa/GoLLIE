#!/bin/bash
#SBATCH --partition=xlong
#SBATCH --job-name=GoLLIE-7B_CodeLLaMA_FULL_MODEL
#SBATCH --cpus-per-task=16
#SBATCH --gres=gpu:4
#SBATCH --mem=128G
#SBATCH --output=.slurm/GoLLIE-7B_CodeLLaMA_FULL_MODEL.out.txt
#SBATCH --error=.slurm/GoLLIE-7B_CodeLLaMA_FULL_MODEL.err.txt


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
CONFIGS_FOLDER="configs/model_configs"


# Call this script from root directory as: sbatch bash_scripts/GoLLIE-7B_CodeLLaMA_train_full_model.sh

pip install flash-attn --no-build-isolation
pip install git+https://github.com/HazyResearch/flash-attention.git#subdirectory=csrc/rotary

torchrun --standalone --master_port 37223 --nproc_per_node=4 src/run.py  ${CONFIGS_FOLDER}/GoLLIE-7B_CodeLLaMA_train_full_model.yaml