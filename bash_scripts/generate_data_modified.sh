#!/bin/bash

source /gscratch4/users/osainz006/GoLLIE/venv/GoLLIE/bin/activate

CONFIG_DIR="configs/data_configs"

OUTPUT_DIR="data/processed_w_examples"

python -m src.generate_data \
     --configs \
        ${CONFIG_DIR}/crossner_ai_config.json \
        ${CONFIG_DIR}/crossner_literature_config.json \
        ${CONFIG_DIR}/crossner_music_config.json \
        ${CONFIG_DIR}/crossner_politics_config.json \
        ${CONFIG_DIR}/crossner_science_config.json \
        ${CONFIG_DIR}/crossner_ai_wo_misc_config.json \
        ${CONFIG_DIR}/crossner_literature_wo_misc_config.json \
        ${CONFIG_DIR}/crossner_music_wo_misc_config.json \
        ${CONFIG_DIR}/crossner_politics_wo_misc_config.json \
        ${CONFIG_DIR}/crossner_science_wo_misc_config.json \
        ${CONFIG_DIR}/mitmovie_config.json \
        ${CONFIG_DIR}/mitrestaurant_config.json \
     --output ${OUTPUT_DIR} \
     --overwrite_output_dir \
     --include_examples

OUTPUT_DIR="data/processed"


 python -m src.generate_data \
     --configs \
        ${CONFIG_DIR}/crossner_ai_config.json \
        ${CONFIG_DIR}/crossner_literature_config.json \
        ${CONFIG_DIR}/crossner_music_config.json \
        ${CONFIG_DIR}/crossner_politics_config.json \
        ${CONFIG_DIR}/crossner_science_config.json \
        ${CONFIG_DIR}/crossner_ai_wo_misc_config.json \
        ${CONFIG_DIR}/crossner_literature_wo_misc_config.json \
        ${CONFIG_DIR}/crossner_music_wo_misc_config.json \
        ${CONFIG_DIR}/crossner_politics_wo_misc_config.json \
        ${CONFIG_DIR}/crossner_science_wo_misc_config.json \
        ${CONFIG_DIR}/mitmovie_config.json \
        ${CONFIG_DIR}/mitrestaurant_config.json \
     --output ${OUTPUT_DIR} \
     --overwrite_output_dir

# Generate baseline data
OUTPUT_DIR="data/baseline"

python -m src.generate_data \
    --configs \
        ${CONFIG_DIR}/crossner_ai_config.json \
        ${CONFIG_DIR}/crossner_literature_config.json \
        ${CONFIG_DIR}/crossner_music_config.json \
        ${CONFIG_DIR}/crossner_politics_config.json \
        ${CONFIG_DIR}/crossner_science_config.json \
        ${CONFIG_DIR}/crossner_ai_wo_misc_config.json \
        ${CONFIG_DIR}/crossner_literature_wo_misc_config.json \
        ${CONFIG_DIR}/crossner_music_wo_misc_config.json \
        ${CONFIG_DIR}/crossner_politics_wo_misc_config.json \
        ${CONFIG_DIR}/crossner_science_wo_misc_config.json \
        ${CONFIG_DIR}/mitmovie_config.json \
        ${CONFIG_DIR}/mitrestaurant_config.json \
    --output ${OUTPUT_DIR} \
    --overwrite_output_dir \
    --baseline
