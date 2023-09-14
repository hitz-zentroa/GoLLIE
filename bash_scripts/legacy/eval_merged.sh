#!/bin/bash
#SBATCH --job-name=Eval-CoLLIE-Merged
#SBATCH --cpus-per-task=16
#SBATCH --gres=gpu:2
#SBATCH --mem=128G
#SBATCH --output=.slurm/Eval-CoLLIE-Merged.out.txt
#SBATCH --error=.slurm/Eval-CoLLIE-Merged.err.txt


source /ikerlariak/osainz006/venvs/collie/bin/activate


export LC_ALL=en_US.UTF-8
export LANG=en_US.UTF-8
export LANGUAGE=en_US.UTF-8
export TOKENIZERS_PARALLELISM=true
export TRANSFORMERS_NO_ADVISORY_WARNINGS=true
export WANDB_ENTITY=hitz-collie
export WANDB_PROJECT=CoLLIE-merged
export WANDB__SERVICE_WAIT=300
export OMP_NUM_THREADS=16

export PYTHONPATH="$PYTHONPATH:$PWD"


echo ${CUDA_VISIBLE_DEVICES}

CONFIGS_FOLDER="configs/model_configs/eval_merged_model"



torchrun --standalone --nproc_per_node=2 src/run.py ${CONFIGS_FOLDER}/QLoRA-4bits-merged.yaml
torchrun --standalone --nproc_per_node=2 src/run.py ${CONFIGS_FOLDER}/QLoRA-4bits-unmerged.yaml
torchrun --standalone --nproc_per_node=2 src/run.py ${CONFIGS_FOLDER}/QLoRA-8bits-merged.yaml
torchrun --standalone --nproc_per_node=2 src/run.py ${CONFIGS_FOLDER}/QLoRA-8bits-unmerged.yaml
torchrun --standalone --nproc_per_node=2 src/run.py ${CONFIGS_FOLDER}/QLoRA-bf16-merged.yaml
torchrun --standalone --nproc_per_node=2 src/run.py ${CONFIGS_FOLDER}/QLoRA-fp16-merged.yaml