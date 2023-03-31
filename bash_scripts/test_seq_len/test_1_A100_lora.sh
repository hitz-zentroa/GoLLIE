#!/bin/bash
#SBATCH --job-name=CoLLIE_seqlen_1_A100
#SBATCH --cpus-per-task=16
#SBATCH --gres=gpu:1
#SBATCH --mem=128G
#SBATCH --output=CoLLIE_seqlen_1_A100.out.txt
#SBATCH --error=CoLLIE_seqlen_1_A100.err.txt

source /ikerlariak/igarcia945/envs/pytorch2/bin/activate

export LC_ALL=en_US.UTF-8
export LANG=en_US.UTF-8
export LANGUAGE=en_US.UTF-8
export TOKENIZERS_PARALLELISM=true
export TRANSFORMERS_NO_ADVISORY_WARNINGS="true"

cd ../..

accelerate launch --mixed_precision fp16 src/test_context_batch_size.py \
--optimizer_name adamW \
--use_lora \
--int8_quantization \
--model_name_or_path /gaueko1/hizkuntza-ereduak/LLaMA/lm/huggingface/65B/

accelerate launch --mixed_precision fp16 src/test_context_batch_size.py \
--optimizer_name adamW \
--use_lora \
--int8_quantization \
--model_name_or_path /gaueko1/hizkuntza-ereduak/LLaMA/lm/huggingface/30B/

accelerate launch --mixed_precision fp16 src/test_context_batch_size.py \
--optimizer_name adamW \
--use_lora \
--int8_quantization \
--model_name_or_path /gaueko1/hizkuntza-ereduak/LLaMA/lm/huggingface/13B/

accelerate launch --mixed_precision fp16 src/test_context_batch_size.py \
--optimizer_name adamW \
--use_lora \
--int8_quantization \
--model_name_or_path /gaueko1/hizkuntza-ereduak/LLaMA/lm/huggingface/7B/




