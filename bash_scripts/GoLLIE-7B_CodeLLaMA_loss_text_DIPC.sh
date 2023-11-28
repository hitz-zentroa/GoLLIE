#!/bin/bash
#SBATCH --partition=xlong
#SBATCH --job-name=GoLLIE-7B_CodeLLaMA_loss_text
#SBATCH --cpus-per-task=22
#SBATCH --nodes=1
#SBATCH --gres=gpu:a100:1
#SBATCH --mem=100G
#SBATCH --output=.slurm/GoLLIE-7B_CodeLLaMA_loss_text.out.txt
#SBATCH --error=.slurm/GoLLIE-7B_CodeLLaMA_loss_text.err.txt


module load Python
source /scratch/igarcia945/venvs/transformers/bin/activate


export LC_ALL=en_US.UTF-8
export LANG=en_US.UTF-8
export LANGUAGE=en_US.UTF-8
export TOKENIZERS_PARALLELISM=true
export TRANSFORMERS_NO_ADVISORY_WARNINGS=true
export WANDB_ENTITY=hitz-GoLLIE
export WANDB_PROJECT=GoLLIEv1.0
export OMP_NUM_THREADS=16

echo CUDA_VISIBLE_DEVICES "${CUDA_VISIBLE_DEVICES}"


CONFIGS_FOLDER="configs/model_configs"

# Call this script from root directory as: sbatch bash_scripts/GoLLIE-7B_CodeLLaMA.sh


# python3 -m src.run ${CONFIGS_FOLDER}/GoLLIE-7B_CodeLLaMA_BS32_R8.yaml

python3 -m  src.run ${CONFIGS_FOLDER}/GoLLIE-7B_CodeLLaMA_BS128_R128_loss_text.yaml
