#!/bin/bash
#SBATCH --job-name=CoLLIE+-34B_CodeLLaMA
#SBATCH --cpus-per-task=16
#SBATCH --gres=gpu:2
#SBATCH --mem=128G
#SBATCH --output=.slurm/CoLLIE+-34B_CodeLLaMA.out.txt
#SBATCH --error=.slurm/CoLLIE+-34B_CodeLLaMA.err.txt


source /ikerlariak/osainz006/venvs/collie/bin/activate


export LC_ALL=en_US.UTF-8
export LANG=en_US.UTF-8
export LANGUAGE=en_US.UTF-8
export TOKENIZERS_PARALLELISM=true
export TRANSFORMERS_NO_ADVISORY_WARNINGS=true
export WANDB_ENTITY=hitz-collie
export WANDB_PROJECT=CoLLIEv1.0

echo CUDA_VISIBLE_DEVICES "${CUDA_VISIBLE_DEVICES}"

export PYTHONPATH="$PYTHONPATH:$PWD"

# Call this script from root directory as: sbatch bash_scripts/runs/CoLLIE+-34B_CodeLLaMA.sh

for i in 2 3
do
CONFIGS_FOLDER="configs/model_configs/runs/$i"
torchrun --standalone --master_port 37229 --nproc_per_node=2 src/run.py ${CONFIGS_FOLDER}/CoLLIE+-34B_CodeLLaMA.yaml
done
