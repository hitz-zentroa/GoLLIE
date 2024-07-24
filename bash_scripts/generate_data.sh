#!/bin/bash
#SBATCH --job-name=generate_data
#SBATCH --cpus-per-task=1
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --time=7-00:00:00
#SBATCH --mem=512GB
#SBATCH --gres=gpu:1
#SBATCH --output=/sorgin1/users/neildlf/GoLLIE-dev/out/out.%j
#SBATCH --error=/sorgin1/users/neildlf/GoLLIE-dev/out/err.%j

# Activate virtual environment
source /sorgin1/users/neildlf/gollie/bin/activate

# Print the current working directory
echo "Current working directory: $(pwd)"

# Change to the GoLLIE-dev directory 
cd /sorgin1/users/neildlf/GoLLIE-dev 

# Set the configurations directory
CONFIG_DIR="configs/data_configs"

# Generate data with examples
OUTPUT_DIR="data/processed_w_examples"
srun /sorgin1/users/neildlf/gollie/bin/python -m src.generate_data \
     --configs \
        ${CONFIG_DIR}/ace_config.json \
        ${CONFIG_DIR}/bc5cdr_config.json \
        ${CONFIG_DIR}/broadtwitter_config.json \
        ${CONFIG_DIR}/casie_config.json \
        ${CONFIG_DIR}/conll03_config.json \
        ${CONFIG_DIR}/crossner_ai_config.json \
        ${CONFIG_DIR}/crossner_literature_config.json \
        ${CONFIG_DIR}/crossner_music_config.json \
        ${CONFIG_DIR}/crossner_politics_config.json \
        ${CONFIG_DIR}/crossner_science_config.json \
        ${CONFIG_DIR}/diann_config.json \
        ${CONFIG_DIR}/e3c_config.json \
        ${CONFIG_DIR}/europarl_config.json \
        ${CONFIG_DIR}/fabner_config.json \
        ${CONFIG_DIR}/harveyner_config.json \
        ${CONFIG_DIR}/mitmovie_config.json \
        ${CONFIG_DIR}/mitrestaurant_config.json \
        ${CONFIG_DIR}/mitmovie_config.json \
        ${CONFIG_DIR}/multinerd_config.json \
        ${CONFIG_DIR}/ncbidisease_config.json \
        ${CONFIG_DIR}/ontonotes_config.json \
        ${CONFIG_DIR}/rams_config.json \
        ${CONFIG_DIR}/tacred_config.json \
        ${CONFIG_DIR}/wikievents_config.json \
        ${CONFIG_DIR}/wnut17_config.json \
     --output ${OUTPUT_DIR} \
     --overwrite_output_dir \
     --include_examples

# Generate processed data
OUTPUT_DIR="data/processed"
srun /sorgin1/users/neildlf/gollie/bin/python -m src.generate_data \
     --configs \
        ${CONFIG_DIR}/ace_config.json \
        ${CONFIG_DIR}/bc5cdr_config.json \
        ${CONFIG_DIR}/broadtwitter_config.json \
        ${CONFIG_DIR}/casie_config.json \
        ${CONFIG_DIR}/conll03_config.json \
        ${CONFIG_DIR}/crossner_ai_config.json \
        ${CONFIG_DIR}/crossner_literature_config.json \
        ${CONFIG_DIR}/crossner_music_config.json \
        ${CONFIG_DIR}/crossner_politics_config.json \
        ${CONFIG_DIR}/crossner_science_config.json \
        ${CONFIG_DIR}/diann_config.json \
        ${CONFIG_DIR}/e3c_config.json \
        ${CONFIG_DIR}/europarl_config.json \
        ${CONFIG_DIR}/fabner_config.json \
        ${CONFIG_DIR}/harveyner_config.json \
        ${CONFIG_DIR}/mitmovie_config.json \
        ${CONFIG_DIR}/mitrestaurant_config.json \
        ${CONFIG_DIR}/mitmovie_config.json \
        ${CONFIG_DIR}/multinerd_config.json \
        ${CONFIG_DIR}/ncbidisease_config.json \
        ${CONFIG_DIR}/ontonotes_config.json \
        ${CONFIG_DIR}/rams_config.json \
        ${CONFIG_DIR}/tacred_config.json \
        ${CONFIG_DIR}/wikievents_config.json \
        ${CONFIG_DIR}/wnut17_config.json \
     --output ${OUTPUT_DIR} \
     --overwrite_output_dir

# Generate baseline data
OUTPUT_DIR="data/baseline"
srun /sorgin1/users/neildlf/gollie/bin/python -m src.generate_data \
    --configs \
        ${CONFIG_DIR}/ace_config.json \
        ${CONFIG_DIR}/bc5cdr_config.json \
        ${CONFIG_DIR}/broadtwitter_config.json \
        ${CONFIG_DIR}/casie_config.json \
        ${CONFIG_DIR}/conll03_config.json \
        ${CONFIG_DIR}/crossner_ai_config.json \
        ${CONFIG_DIR}/crossner_literature_config.json \
        ${CONFIG_DIR}/crossner_music_config.json \
        ${CONFIG_DIR}/crossner_politics_config.json \
        ${CONFIG_DIR}/crossner_science_config.json \
        ${CONFIG_DIR}/diann_config.json \
        ${CONFIG_DIR}/e3c_config.json \
        ${CONFIG_DIR}/europarl_config.json \
        ${CONFIG_DIR}/fabner_config.json \
        ${CONFIG_DIR}/harveyner_config.json \
        ${CONFIG_DIR}/mitmovie_config.json \
        ${CONFIG_DIR}/mitrestaurant_config.json \
        ${CONFIG_DIR}/mitmovie_config.json \
        ${CONFIG_DIR}/multinerd_config.json \
        ${CONFIG_DIR}/ncbidisease_config.json \
        ${CONFIG_DIR}/ontonotes_config.json \
        ${CONFIG_DIR}/rams_config.json \
        ${CONFIG_DIR}/tacred_config.json \
        ${CONFIG_DIR}/wikievents_config.json \
        ${CONFIG_DIR}/wnut17_config.json \
    --output ${OUTPUT_DIR} \
    --overwrite_output_dir \
    --baseline