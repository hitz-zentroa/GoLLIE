#!/bin/bash
#SBATCH --job-name=CoLLIE7B_CodeLLaMA-Python_examples_lora4_lora_r_8_all_3e-5
#SBATCH --cpus-per-task=16
#SBATCH --gres=gpu:1
#SBATCH --mem=128G
#SBATCH --output=.slurm/CoLLIE7B_CodeLLaMA-Python_examples_lora4_lora_r_8_all_3e-5.out.txt
#SBATCH --error=.slurm/CoLLIE7B_CodeLLaMA-Python_examples_lora4_lora_r_8_all_3e-5.err.txt


source /ikerlariak/osainz006/venvs/collie/bin/activate


export LC_ALL=en_US.UTF-8
export LANG=en_US.UTF-8
export LANGUAGE=en_US.UTF-8
export TOKENIZERS_PARALLELISM=true
export TRANSFORMERS_NO_ADVISORY_WARNINGS=true
export WANDB_ENTITY=hitz-collie
export WANDB_PROJECT=CoLLIEv1.0

echo ${CUDA_VISIBLE_DEVICES}

CONFIGS_FOLDER="configs/model_configs"


# Call this script from root directory as: sbatch bash_scripts/run_CoLLIE7B.sh


python3 -m src.run ${CONFIGS_FOLDER}/CoLLIE-7B_CodeLLaMA_examples_lora4_flash_together_lora4_lora_r_8_all_3e-5.yaml
