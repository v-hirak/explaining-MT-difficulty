#!/bin/bash

#SBATCH --time=2-00:00:00
#SBATCH --partition=regular
#SBATCH --job-name=mined_data
#SBATCH --mem=256G

DONWLOAD_SCRIPT="thesis/download_metadata.py"
UPDATE_SIZES_SCRIPT="thesis/update_lang_sizes.py"
URLS_PATH="thesis/mined_metadata_urls.txt"
METADATA_DIR="/scratch/s5741467/nllb_train_data/mined"
LANG_SIZES_PATH="thesis/lang_train_size.csv"

source thesis/venv/bin/activate

for i in {0..1612}; do
    echo "Processing index $i";
    python $DONWLOAD_SCRIPT -i $i -u $URLS_PATH -d $METADATA_DIR;
    for file in $METADATA_DIR/*.xz; do
        unxz "$file";
    done
    python $UPDATE_SIZES_SCRIPT -m $METADATA_DIR -s $LANG_SIZES_PATH;
    for file in $METADATA_DIR/*.v1; do
        rm "$file";
    done
    echo "Done";
    echo "";
done

deactivate
