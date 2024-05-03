"""This script is used to estimate the size of the mined NLLB training data."""


import os
from collections import defaultdict
from urllib.request import urlretrieve

import pandas as pd


URLS_PATH = "/home4/s5741467/thesis/mined_metadata_urls.txt"
MINED_PATH = "/projects/s5741467/thesis/nllb_train_data/mined"
LANG_SIZES_PATH = "/home4/s5741467/thesis/lang_train_size.csv"

COL_NAMES = ["wet_file_url", "document_sha1", "document_url", "line_num_in_doc",
             "paragraph_digest", "sentence_digest", "lid_score", "laser_score",
             "direction", "language", "line_number_in_direction"]


def download_metadata(urls_path: str, download_dir: str) -> None:
    """Download metadata files from the given URLs into the given directory."""

    with open(urls_path) as f:
        urls = [line.strip() for line in f.readlines()][764:]  # Checkpoint

    for i, url in enumerate(urls, start=1):
        urlretrieve(url, filename=os.path.join(download_dir, url.split("/")[-1]))
        print(f"File {i}")


def get_lang_sizes(metadata_dir: str, col_names: list[str]) -> dict[str, int]:
    """Get the sizes of the mined NLLB training data for each language."""

    lang_sizes_mined = defaultdict(int)

    for filename in os.listdir(metadata_dir):
        df_mined = pd.read_csv(
            os.path.join(metadata_dir, filename),
            delimiter=" ",
            names=col_names
        )
        lang_src = df_mined.iloc[-2]["language"]
        num_lines_src = int(df_mined.iloc[-2]["line_number_in_direction"])
        lang_tgt = df_mined.iloc[-1]["language"]
        num_lines_tgt = int(df_mined.iloc[-1]["line_number_in_direction"])
        lang_sizes_mined[lang_src] += num_lines_src
        lang_sizes_mined[lang_tgt] += num_lines_tgt

    return lang_sizes_mined


def update_lang_sizes(lang_sizes_mined: dict[str, int], lang_sizes_path: str) -> None:
    """Update the language sizes file with the mined data language sizes."""

    df_sizes = pd.read_csv(lang_sizes_path)
    df_sizes["num_sents_mined"] = df_sizes["lang"].map(lang_sizes_mined)
    df_sizes.to_csv(lang_sizes_path, index=False)


def main() -> None:

    download_metadata(URLS_PATH, MINED_PATH)
    # lang_sizes_mined = get_lang_sizes(MINED_PATH, COL_NAMES)
    # update_lang_sizes(lang_sizes_mined, LANG_SIZES_PATH)


if __name__ == "__main__":
    main()
