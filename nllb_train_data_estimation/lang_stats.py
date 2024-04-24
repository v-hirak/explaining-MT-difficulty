"""Module for calculating language statistics."""


import os
from collections import defaultdict


class Flores:
    """Class for calculating language statistics in the FLORES+ dataset.

    The dataset can be found at: https://github.com/openlanguagedata/flores.
    """

    def __init__(self, path: str) -> None:
        """Initialize the class."""
        if not isinstance(path, str):
            raise TypeError("The path to dataset must be a string.")
        self.path = path
        self.dev_path = f"{path}/dev"
        self.devtest_path = f"{path}/devtest"

    @property
    def files(self) -> dict[str, list[str]]:
        """List of files for dev and devtest splits."""
        return {
            "dev": os.listdir(self.dev_path),
            "devtest": os.listdir(self.devtest_path)
        }

    @property
    def num_files(self) -> dict[str, int]:
        """Number of files in dev and devtest splits."""
        return {
            "dev": len(self.files["dev"]),
            "devtest": len(self.files["devtest"])
        }

    @property
    def langs(self) -> dict[str, set[str]]:
        """Set of languages for dev and devtest splits."""
        return {
            "dev": {file[4:7] for file in self.files["dev"]},
            "devtest": {file[8:11] for file in self.files["devtest"]}
        }

    @property
    def num_langs(self) -> dict[str, int]:
        """Number of languages in dev and devtest splits."""
        return {
            "dev": len(self.langs["dev"]),
            "devtest": len(self.langs["devtest"])
        }

    @property
    def dev_only_langs(self) -> set[str]:
        """Languages only found in dev split."""
        return self.langs["dev"] - self.langs["devtest"]


class PublicData:
    """Class for calculating language statistics in the Public Data dataset."""

    EXCLUDED_FILES = ["cached_lm_test.en", "test.fm.prob", "get_zero_shot_pairs.py",
                      "zeroshotcorpstats", "README", "train.tsv", ".DS_Store"]

    # Mapping of ISO 639-1 codes to ISO 639-3 codes
    ISO_MAP = {"bn": "ben", "en": "eng", "fr": "fra", "gu": "guj", "hi": "hin",
               "kn": "kan", "ml": "mal", "mr": "mar", "or": "ory", "pa": "pan",
               "ta": "tam", "te": "tel", "ur": "urd"}

    def __init__(self, path: str) -> None:
        """Initialize the class."""
        if not isinstance(path, str):
            raise TypeError("The path to dataset must be a string.")
        self.path = path

    @property
    def file_paths(self) -> list[str]:
        """Function foo."""
        file_paths = []
        for parent_dir, _, dir_file_names in os.walk(self.path):
            dir_file_names = [n for n in dir_file_names if n not in self.EXCLUDED_FILES]
            dir_file_paths = [parent_dir + "/" + name for name in dir_file_names]
            file_paths.extend(dir_file_paths)
        return file_paths

    def get_lang_sizes(self) -> dict[str, int]:
        """Get the number of sentences for each language."""
        lang_sizes = defaultdict(int)
        for path in self.file_paths:
            lang = path.split(".")[-1]
            lang = self.ISO_MAP.get(lang, lang)
            with open(path) as file:
                num_sents = len(file.readlines())
                lang_sizes[lang] += num_sents
        return lang_sizes

def main():
    """Main function."""


if __name__ == "__main__":
    main()
