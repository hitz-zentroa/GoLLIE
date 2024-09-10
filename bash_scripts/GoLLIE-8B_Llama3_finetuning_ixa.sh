#!/bin/bash

#SBATCH --job-name=GoLLIE-8B-Llama3_finetuning
#SBATCH --cpus-per-task=22
#SBATCH --nodes=1
#SBATCH --time=3-00:00:00
#SBATCH --gres=gpu:6
#SBATCH --mem=200G
#SBATCH --output=/sorgin1/users/neildlf/GoLLIE-dev/out/GoLLIE-8B-Llama3_finetuning.out.txt
#SBATCH --error=/sorgin1/users/neildlf/GoLLIE-dev/out/GoLLIE-8B-Llama3_finetuning.err.txt

#module load CUDA/12.1
#module load Python
source /sorgin1/users/neildlf/gollie/bin/activate

export LC_ALL=en_US.UTF-8
export LANG=en_US.UTF-8
export LANGUAGE=en_US.UTF-8
export TOKENIZERS_PARALLELISM=true
export TRANSFORMERS_NO_ADVISORY_WARNINGS=true
export WANDB_ENTITY=neilus03
export WANDB_PROJECT=GoLLIEv2.0
export OMP_NUM_THREADS=16

echo CUDA_VISIBLE_DEVICES "${CUDA_VISIBLE_DEVICES}"

# Call this script from root directory as: sbatch bash_scripts/GoLLIE-8B_Llama3_ixa.sh

# Add project root to PYTHONPATH
export PYTHONPATH="$PYTHONPATH:/sorgin1/users/neildlf/GoLLIE-dev/" 

# *** IMPORTANT: Change working directory to project root ***
cd /sorgin1/users/neildlf/GoLLIE-dev/

# Now torchrun should execute with the correct working directory
torchrun --standalone --master_port 37227 --nproc_per_node=6 src/run.py configs/model_configs/finetuning/GoLLIE-8B_LLama3_BS128_R128_finetuning.yaml
torchrun --standalone --master_port 37227 --nproc_per_node=6 src/run.py configs/model_configs/eval/GoLLIE-8B_Llama3_BS128_R128_finetuning.yaml
