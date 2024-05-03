"""This script is used to download the compressed metadata of mined NLLB train data."""


import argparse
import os
from urllib.request import urlretrieve


def download_metadata(url_idx: int, urls_path: str, download_dir: str) -> None:
    """Download metadata file from the given URL index into the given directory."""

    with open(urls_path) as f:
        url = [line.strip() for line in f.readlines()][url_idx]
        urlretrieve(url, filename=os.path.join(download_dir, url.split("/")[-1]))


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("--url_idx", "-i", type=int, required=True,
                        help="Index of the compressed metadata file URL to download.")
    parser.add_argument("--urls_path", "-u", type=str, required=True,
                        help="Path to .txt file containing download URLs.")
    parser.add_argument("--download_dir", "-d", type=str, required=True,
                        help="Directory to download the compressed metadata file.")
    args = parser.parse_args()

    download_metadata(args.url_idx, args.urls_path, args.download_dir)
