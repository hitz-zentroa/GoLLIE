#!/bin/bash
#SBATCH --job-name=paraphrase
#SBATCH --cpus-per-task=16
#SBATCH --gres=gpu:1
#SBATCH --mem=128G
#SBATCH --output=.slurm/paraphrase.out.txt
#SBATCH --error=.slurm/paraphrase.err.txt

source /ikerlariak/osainz006/venvs/GoLLIE/bin/activate

export LC_ALL=en_US.UTF-8
export LANG=en_US.UTF-8
export LANGUAGE=en_US.UTF-8
export TOKENIZERS_PARALLELISM=true
export TRANSFORMERS_NO_ADVISORY_WARNINGS=true
export WANDB_ENTITY=hitz-GoLLIE
export WANDB_PROJECT=GoLLIE


CONFIGS_FOLDER="configs/pharapharse_config"



python3 -m src.paraphrase.run_paraphrasing ${CONFIGS_FOLDER}/LlaMA2-Chat.yaml

