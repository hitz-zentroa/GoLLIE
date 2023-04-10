#!/bin/bash
#SBATCH --job-name=CoLLIE7B
#SBATCH --cpus-per-task=16
#SBATCH --gres=gpu:1
#SBATCH --mem=128G
#SBATCH --output=.slurm/CoLLIE7B.out.txt
#SBATCH --error=.slurm/CoLLIE7B.err.txt

source /gscratch4/users/osainz006/CoLLIE/venv/collie/bin/activate

export LC_ALL=en_US.UTF-8
export LANG=en_US.UTF-8
export LANGUAGE=en_US.UTF-8
export TOKENIZERS_PARALLELISM=true
export TRANSFORMERS_NO_ADVISORY_WARNINGS=true
export WANDB_PROJECT=CoLLIE

cd ../src || exit

python3 trainer.py ../CoLLIE_configs/CoLLIE-7B.yaml

# python3 trainer.py ../CoLLIE_configs/CoLLIE-7B_eval.yaml
