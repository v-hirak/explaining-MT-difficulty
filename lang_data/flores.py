"""Module for handling FLORES+ dataset."""


import os


class Flores:
    """Class for basic handling for the FLORES+ dataset.

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
    def langs(self) -> dict[str, list[str]]:
        """List of languages in the dataset."""
        return {
            "dev": [file[4:] for file in self.files["dev"]],
            "devtest": [file[8:] for file in self.files["devtest"]]
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
        return set(self.langs["dev"]) - set(self.langs["devtest"])

    @property
    def langs_with_scripts(self) -> dict[str, list[tuple[str, str]]]:
        """List of languages and their scripts for dev and devtest splits."""
        return {
            "dev": [(l.split("_")[0], l.split("_")[1]) for l in self.langs["dev"]],
            "devtest": [(l.split("_")[0], l.split("_")[1]) for l in self.langs["devtest"]]
        }


def main():
    """Main function."""


if __name__ == "__main__":
    main()
