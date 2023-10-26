#!/bin/bash
#SBATCH --job-name=GoLLIE-7B_CodeLLaMA_hparam_eval
#SBATCH --cpus-per-task=16
#SBATCH --gres=gpu:2
#SBATCH --mem=200G
#SBATCH --output=.slurm/GoLLIE-7B_CodeLLaMA_hparam_eval.out.txt
#SBATCH --error=.slurm/GoLLIE-7B_CodeLLaMA_hparam_eval.err.txt


source /ikerlariak/osainz006/venvs/collie/bin/activate


export LC_ALL=en_US.UTF-8
export LANG=en_US.UTF-8
export LANGUAGE=en_US.UTF-8
export TOKENIZERS_PARALLELISM=true
export TRANSFORMERS_NO_ADVISORY_WARNINGS=true
export WANDB_ENTITY=hitz-collie
export WANDB_PROJECT=GoLLIEv1.0
export OMP_NUM_THREADS=16
#export PYTORCH_CUDA_ALLOC_CONF=garbage_collection_threshold:0.6,max_split_size_mb:128

echo CUDA_VISIBLE_DEVICES "${CUDA_VISIBLE_DEVICES}"

export PYTHONPATH="$PYTHONPATH:$PWD"
CONFIGS_FOLDER="configs/model_configs"

# Call this script from root directory as: sbatch bash_scripts/GoLLIE-7B_CodeLLaMA.sh

# FT
torchrun --standalone --master_port 37223 --nproc_per_node=2  src/run.py configs/model_configs/eval/GoLLIE-7B_CodeLLaMA_train_full_model.yaml
# FT PROMPT LOSS 0.05
#torchrun --standalone --master_port 37227 --nproc_per_node=4  src/run.py configs/model_configs/eval/GoLLIE-7B_CodeLLaMA_train_full_model_prompt_loss_0.05.yaml
