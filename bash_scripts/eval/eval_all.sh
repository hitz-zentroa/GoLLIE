#!/bin/bash
#SBATCH --job-name=CoLLIE_Eval_ALL
#SBATCH --cpus-per-task=16
#SBATCH --gres=gpu:1
#SBATCH --mem=128G
#SBATCH --output=.slurm/CoLLIE_Eval_ALL.out.txt
#SBATCH --error=.slurm/CoLLIE_Eval_ALL.err.txt


source /ikerlariak/osainz006/venvs/collie/bin/activate


export LC_ALL=en_US.UTF-8
export LANG=en_US.UTF-8
export LANGUAGE=en_US.UTF-8
export TOKENIZERS_PARALLELISM=true
export TRANSFORMERS_NO_ADVISORY_WARNINGS=true
export WANDB_ENTITY=hitz-collie
export WANDB_PROJECT=CoLLIEv1.0

echo CUDA_VISIBLE_DEVICES "${CUDA_VISIBLE_DEVICES}"

CONFIGS_FOLDER="configs/model_configs/eval"
export PYTHONPATH="$PYTHONPATH:$PWD"

# Call this script from root directory as: sbatch bash_scripts/eval_all.sh


python3 -m src.run ${CONFIGS_FOLDER}/Baseline-7B_CodeLLaMA.yaml
python3 -m src.run ${CONFIGS_FOLDER}/CoLLIE-7B_CodeLLaMA.yaml
python3 -m src.run ${CONFIGS_FOLDER}/eval/CoLLIE+-7B_CodeLLaMA.yaml
python3 -m src.run ${CONFIGS_FOLDER}/CoLLIE+-7B_CodeLLaMA_ablation_dropout.yaml
python3 -m src.run ${CONFIGS_FOLDER}/CoLLIE+-7B_CodeLLaMA_ablation_masking.yaml
python3 -m src.run ${CONFIGS_FOLDER}/CoLLIE+-13B_CodeLLaMA.yaml
torchrun --standalone --master_port 37228 --nproc_per_node=2 src/run.py ${CONFIGS_FOLDER}/CoLLIE+-34B_CodeLLaMA.yaml


