#!/bin/bash

source /gscratch4/users/osainz006/CoLLIE/venv/collie/bin/activate

CONFIG_DIR="configs/data_configs"
OUTPUT_DIR="data/processed"

python -m src.generate_data \
    --configs \
        ${CONFIG_DIR}/ace_config.json \
        ${CONFIG_DIR}/bc5cdr_config.json \
        ${CONFIG_DIR}/conll03_config.json \
        ${CONFIG_DIR}/diann_config.json \
        ${CONFIG_DIR}/europarl_config.json \
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

python -m src.generate_data \
    --configs \
        ${CONFIG_DIR}/ace_config.json \
        ${CONFIG_DIR}/bc5cdr_config.json \
        ${CONFIG_DIR}/conll03_config.json \
        ${CONFIG_DIR}/diann_config.json \
        ${CONFIG_DIR}/europarl_config.json \
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
