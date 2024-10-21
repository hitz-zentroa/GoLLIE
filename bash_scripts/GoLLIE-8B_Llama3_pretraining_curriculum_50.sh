#!/bin/bash

#SBATCH --job-name=GoLLIE-8B-Llama3-curriculum_50
#SBATCH --cpus-per-task=22
#SBATCH --nodes=1
#SBATCH --time=3-00:00:00
#SBATCH --gres=gpu:4
#SBATCH --mem=200G
#SBATCH --output=/sorgin1/users/neildlf/GoLLIE-dev/out/GoLLIE-8B-Llama3_pretraining_curriculum_50.out.txt
#SBATCH --error=/sorgin1/users/neildlf/GoLLIE-dev/out/GoLLIE-8B-Llama3_pretraining_curriculum_50.err.txt

# Activate your Python environment
source /sorgin1/users/neildlf/gollie/bin/activate

# Set environment variables
export LC_ALL=en_US.UTF-8
export LANG=en_US.UTF-8
export LANGUAGE=en_US.UTF-8
export TOKENIZERS_PARALLELISM=true
export TRANSFORMERS_NO_ADVISORY_WARNINGS=true
export WANDB_ENTITY=neilus03
export WANDB_PROJECT=GoLLIEv2.0-pretraining
export OMP_NUM_THREADS=16

echo CUDA_VISIBLE_DEVICES "${CUDA_VISIBLE_DEVICES}"

# Change to the project root directory
cd /sorgin1/users/neildlf/GoLLIE-dev/

# Add project root to PYTHONPATH
export PYTHONPATH="$PYTHONPATH:/sorgin1/users/neildlf/GoLLIE-dev/"

# Execute the training script with the new configuration
torchrun --standalone --master_port 37227 --nproc_per_node=4 src/run.py configs/model_configs/pretrain/GoLLIE-8B_Llama3_pretrain_curriculum_50.yaml
