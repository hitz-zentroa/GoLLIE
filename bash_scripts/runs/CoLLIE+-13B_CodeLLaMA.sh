#!/bin/bash
#SBATCH --job-name=CoLLIE+-13B_CodeLLaMA
#SBATCH --cpus-per-task=16
#SBATCH --gres=gpu:1
#SBATCH --mem=128G
#SBATCH --output=.slurm/CoLLIE+-13B_CodeLLaMA.out.txt
#SBATCH --error=.slurm/CoLLIE+-13B_CodeLLaMA.err.txt


source /ikerlariak/osainz006/venvs/collie/bin/activate


export LC_ALL=en_US.UTF-8
export LANG=en_US.UTF-8
export LANGUAGE=en_US.UTF-8
export TOKENIZERS_PARALLELISM=true
export TRANSFORMERS_NO_ADVISORY_WARNINGS=true
export WANDB_ENTITY=hitz-collie
export WANDB_PROJECT=CoLLIEv1.0

echo CUDA_VISIBLE_DEVICES "${CUDA_VISIBLE_DEVICES}"

# Call this script from root directory as: sbatch bash_scripts/CoLLIE+-13B_CodeLLaMA.sh

for i in 2 3
do
CONFIGS_FOLDER="configs/model_configs/runs/$i"
python3 -m src.run ${CONFIGS_FOLDER}/CoLLIE+-13B_CodeLLaMA.yaml
done
