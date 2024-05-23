#!/bin/bash
#SBATCH --account=hitz-exclusive
#SBATCH --partition=hitz-exclusive
#SBATCH --job-name=paraphrase-llama-8b
#SBATCH --cpus-per-task=22
#SBATCH --nodes=1
#SBATCH --gres=gpu:a100:1
#SBATCH --output=.slurm/paraphrase-llama-8b.out.txt
#SBATCH --error=.slurm/paraphrase-llama-8b.err.txt

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


python3 -m src.paraphrase.run_paraphrasing ${CONFIGS_FOLDER}/llama3-8b.yaml

