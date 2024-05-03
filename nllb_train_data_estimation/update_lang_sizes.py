"""This script is used to get language size from uncompressed metadata file."""


import argparse
import os

import pandas as pd


COL_NAMES = ["wet_file_url", "document_sha1", "document_url", "line_num_in_doc",
             "paragraph_digest", "sentence_digest", "lid_score", "laser_score",
             "direction", "language", "line_number_in_direction"]


def get_lang_sizes(metadata_dir: str) -> dict[str, int]:
    """Get the sizes of the mined NLLB training data for each language."""

    for filename in os.listdir(metadata_dir):
        df_mined = pd.read_csv(
            os.path.join(metadata_dir, filename),
            delimiter=" ",
            names=COL_NAMES
        )
        lang_src = df_mined.iloc[-2]["language"]
        num_lines_src = int(df_mined.iloc[-2]["line_number_in_direction"])
        lang_tgt = df_mined.iloc[-1]["language"]
        num_lines_tgt = int(df_mined.iloc[-1]["line_number_in_direction"])
        lang_sizes_mined = {lang_src: num_lines_src, lang_tgt: num_lines_tgt}

    return lang_sizes_mined


def update_lang_sizes(lang_sizes_mined: dict[str, int], lang_sizes_path: str) -> None:
    """Update the language sizes file with the mined data language sizes."""

    df_sizes = pd.read_csv(lang_sizes_path)
    if "num_sents_mined" not in df_sizes.columns:
        df_sizes["num_sents_mined"] = 0

    for lang, size in lang_sizes_mined.items():
        if lang in df_sizes["lang"].values:
            df_sizes.loc[df_sizes["lang"] == lang, "num_sents_mined"] += size
        else:
            df_sizes = df_sizes.append(
                {"lang": lang, "num_sents_mined": size}, ignore_index=True
            )

    df_sizes.fillna(0, inplace=True)
    df_sizes = df_sizes.astype(
        {"num_sents_publ": int, "num_sents_seed": int, "num_sents_gerl": int}
    )
    df_sizes.sort_values("lang", inplace=True, ignore_index=True)

    df_sizes.to_csv(lang_sizes_path, index=False)


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("--metadata_dir", "-m", type=str, required=True,
                        help="Directory with the uncompressed metadata file.")
    parser.add_argument("--lang_sizes_path", "-s", type=str, required=True,
                        help="Path to .csv file containing language sizes.")
    args = parser.parse_args()

    lang_sizes_mined = get_lang_sizes(args.metadata_dir, COL_NAMES)
    update_lang_sizes(lang_sizes_mined, args.lang_sizes_path)
