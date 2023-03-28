#!/bin/bash

CONFIG_DIR="configs"
OUTPUT_DIR="data/processed"

python -m src.generate_data \
    --configs \
        ${CONFIG_DIR}/ace_config.json \
    --output ${OUTPUT_DIR} \
    --overwrite_output_dir
