#!/bin/bash

CONFIG_DIR="configs/data_configs"
OUTPUT_DIR="data/processed"

python -m src.generate_data \
    --configs \
        ${CONFIG_DIR}/ace_config.json \
        ${CONFIG_DIR}/rams_config.json \
    --output ${OUTPUT_DIR} \
    --overwrite_output_dir
