#!/bin/bash
#SBATCH --account=hitz-exclusive
#SBATCH --partition=hitz-exclusive
#SBATCH --job-name=paraphrase-llama-8b
#SBATCH --cpus-per-task=22
#SBATCH --nodes=1
#SBATCH --gres=gpu:a100:2
#SBATCH --output=.slurm/paraphrase-llama-8b.out.txt
#SBATCH --error=.slurm/paraphrase-llama-8b.err.txt

module load CUDA/12.2.2
module load Python
source /scratch/igarcia945/venvs/transformers/bin/activate

export LC_ALL=en_US.UTF-8
export LANG=en_US.UTF-8
export LANGUAGE=en_US.UTF-8
export TOKENIZERS_PARALLELISM=true
export TRANSFORMERS_NO_ADVISORY_WARNINGS=true
export WANDB_ENTITY=hitz-GoLLIE
export WANDB_PROJECT=GoLLIE


echo CUDA_VISIBLE_DEVICES "${CUDA_VISIBLE_DEVICES}"

CONFIGS_FOLDER="configs/pharapharse_config"
export PYTHONPATH="$PYTHONPATH:$PWD"

torchrun --standalone --master_port 37227 --nproc_per_node=2 src/paraphrase/run_paraphrasing.py ${CONFIGS_FOLDER}/llama3-8b.yaml

