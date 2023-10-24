#!/bin/bash
#SBATCH --job-name=GoLLIE-7B_CodeLLaMA_hparam
#SBATCH --cpus-per-task=16
#SBATCH --gres=gpu:4
#SBATCH --mem=200G
#SBATCH --output=.slurm/GoLLIE-7B_CodeLLaMA_hparam.out.txt
#SBATCH --error=.slurm/GoLLIE-7B_CodeLLaMA_hparam.err.txt


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
torchrun --standalone --master_port 37227 --nproc_per_node=4  src/run.py ${CONFIGS_FOLDER}/GoLLIE-7B_CodeLLaMA_train_full_model.yaml
# BS 32 R 8
torchrun --standalone --master_port 37227 --nproc_per_node=4  src/run.py ${CONFIGS_FOLDER}/GoLLIE-7B_CodeLLaMA_BS32_R8.yaml
# BS 128 R 8
torchrun --standalone --master_port 37227 --nproc_per_node=4  src/run.py ${CONFIGS_FOLDER}/GoLLIE-7B_CodeLLaMA_BS128_R8.yaml
# BS 32 R 64
torchrun --standalone --master_port 37227 --nproc_per_node=4  src/run.py ${CONFIGS_FOLDER}/GoLLIE-7B_CodeLLaMA_BS32_R64.yaml
# BS 32 R 64
torchrun --standalone --master_port 37227 --nproc_per_node=4  src/run.py ${CONFIGS_FOLDER}/GoLLIE-7B_CodeLLaMA_BS128_R64.yaml
# BS 32 R 128
torchrun --standalone --master_port 37227 --nproc_per_node=4  src/run.py ${CONFIGS_FOLDER}/GoLLIE-7B_CodeLLaMA_BS32_R128.yaml
# BS 128 R 128
torchrun --standalone --master_port 37227 --nproc_per_node=4  src/run.py configs/model_configs/eval/GoLLIE-7B_CodeLLaMA_BS128_R128.yaml
# VS 128 R 128 LR 1e-4
torchrun --standalone --master_port 37227 --nproc_per_node=4  src/run.py configs/model_configs/eval/GoLLIE-7B_CodeLLaMA_BS128_R128_LR1e4.yaml
# BS 128 R128 PROMPT LOSS 0.05
torchrun --standalone --master_port 37227 --nproc_per_node=4  src/run.py ${CONFIGS_FOLDER}/GoLLIE-7B_CodeLLaMA_BS128_R128_prompt_loss_0.05.yaml
# FT PROMPT LOSS 0.05
torchrun --standalone --master_port 37227 --nproc_per_node=4  src/run.py ${CONFIGS_FOLDER}/GoLLIE-7B_CodeLLaMA_train_full_model_prompt_loss_0.05.yaml

