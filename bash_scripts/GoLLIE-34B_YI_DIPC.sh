#!/bin/bash
#SBATCH --account=ixa
#SBATCH --partition=ixa
#SBATCH --job-name=GoLLIE-34B_Yi
#SBATCH --cpus-per-task=22
#SBATCH --nodes=1
#SBATCH --gres=gpu:a100:8
#SBATCH --mem=900G
#SBATCH --output=.slurm/GoLLIE-34B_Yi.out.txt
#SBATCH --error=.slurm/GoLLIE-34B_Yi.err.txt


module load Python
source /scratch/igarcia945/venvs/transformers/bin/activate


export LC_ALL=en_US.UTF-8
export LANG=en_US.UTF-8
export LANGUAGE=en_US.UTF-8
export TOKENIZERS_PARALLELISM=true
export TRANSFORMERS_NO_ADVISORY_WARNINGS=true
export WANDB_ENTITY=hitz-collie
export WANDB_PROJECT=GoLLIEv1.0
export OMP_NUM_THREADS=16

echo CUDA_VISIBLE_DEVICES "${CUDA_VISIBLE_DEVICES}"



# Call this script from root directory as: sbatch bash_scripts/GoLLIE-7B_CodeLLaMA.sh


# python3 -m src.run ${CONFIGS_FOLDER}/GoLLIE-7B_CodeLLaMA_BS32_R8.yaml
export PYTHONPATH="$PYTHONPATH:$PWD"
torchrun --standalone --master_port 37229 --nproc_per_node=8 src/run.py configs/model_configs/GoLLIE-YI34B_BS128_R128.yaml
torchrun --standalone --master_port 37229 --nproc_per_node=8 src/run.py configs/model_configs/eval/GoLLIE-YI34B_BS128_R128.yaml


