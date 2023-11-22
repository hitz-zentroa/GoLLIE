#!/bin/bash


CONFIG_DIR="configs/data_configs"

OUTPUT_DIR="data/processed_w_examples_no_noise"

python -m src.generate_data \
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
     --include_examples \
     --remove_masking \
     --remove_dropout \
     --do_not_shuffle

OUTPUT_DIR="data/processed_no_noise"


 python -m src.generate_data \
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
     --remove_masking \
     --remove_dropout \
     --do_not_shuffle

# Generate baseline data
OUTPUT_DIR="data/baseline_no_noise"

python -m src.generate_data \
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
    --baseline \
    --remove_masking \
    --remove_dropout \
    --do_not_shuffle
