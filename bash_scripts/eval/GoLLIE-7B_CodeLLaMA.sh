#!/bin/bash
#SBATCH --job-name=GoLLIE-7B_CodeLLaMA_eval
#SBATCH --cpus-per-task=16
#SBATCH --gres=gpu:4
#SBATCH --mem=100G
#SBATCH --output=.slurm/GoLLIE-7B_CodeLLaMA_eval.out.txt
#SBATCH --error=.slurm/GoLLIE-7B_CodeLLaMA_eval.err.txt


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
CONFIGS_FOLDER="configs/model_configs/eval"

# Call this script from root directory as: sbatch bash_scripts/GoLLIE-7B_CodeLLaMA.sh


# python3 -m src.run ${CONFIGS_FOLDER}/GoLLIE-7B_CodeLLaMA_BS32_R8.yaml

torchrun --standalone --master_port 37229 --nproc_per_node=4  src/run.py ${CONFIGS_FOLDER}/GoLLIE-7B_CodeLLaMA.yaml
