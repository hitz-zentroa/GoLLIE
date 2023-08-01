#!/bin/bash

source /gscratch4/users/osainz006/CoLLIE/venv/collie/bin/activate

CONFIG_DIR="configs/data_configs"
OUTPUT_DIR="data/processed"


 python -m src.generate_data \
     --configs \
        ${CONFIG_DIR}/e3c_config.json \
        ${CONFIG_DIR}/broadtwitter_config.json \
        ${CONFIG_DIR}/fabner_config.json \
        ${CONFIG_DIR}/harveyner_config.json \
        ${CONFIG_DIR}/multinerd_config.json \
     --output ${OUTPUT_DIR} \
     --overwrite_output_dir

# Generate baseline data
OUTPUT_DIR="data/baseline"

python -m src.generate_data \
    --configs \
        ${CONFIG_DIR}/e3c_config.json \
        ${CONFIG_DIR}/broadtwitter_config.json \
        ${CONFIG_DIR}/fabner_config.json \
        ${CONFIG_DIR}/harveyner_config.json \
        ${CONFIG_DIR}/multinerd_config.json \
    --output ${OUTPUT_DIR} \
    --overwrite_output_dir \
    --baseline
