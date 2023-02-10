import os
import tarfile
from pathlib import Path

import click
import gdown

url = "https://drive.google.com/file/d/1eNJn7rX2OE9UKrrknmvClt3IK2cUTRjB/view"


def download_data(url, data_path, quiet=False, fuzzy=True):
    """Download the data from Google Drive."""
    tar_file = str(data_path / "data.tar.xz")
    data_path.mkdir(parents=True, exist_ok=True)

    gdown.download(url=url, output=tar_file, quiet=quiet, fuzzy=fuzzy)


def extract_data(data_path, tar_file):
    """Extract the resulting tar file."""
    with tarfile.open(tar_file) as f:
        f.extractall(data_path)


def clean_up(tar_file):
    """Remove the tar after extraction."""
    os.remove(tar_file)


@click.command()
@click.option("--url", default=url, help="URL of the data in Google Drive.")
@click.option(
    "--data-folder", "-o", default="data", help="Folder in which to save the data."
)
@click.option(
    "--quiet/--verbose",
    "-q/-v",
    default=False,
    help="Flag to not show the download bar.",
)
@click.option(
    "--fuzzy/--no-fuzzy",
    "-f/-e",
    default=True,
    help="Flag to extract id from fuzzy url.",
)
def main(url, data_folder, quiet, fuzzy):
    """Click CLI to use as an entry point."""
    data_path = Path(data_folder)
    tar_file = str(data_path / "data.tar.xz")
    data_path.mkdir(parents=True, exist_ok=True)

    download_data(url, data_path, quiet, fuzzy)

    if not quiet:
        click.echo("Extracting the data...")
    extract_data(data_path, tar_file)

    if not quiet:
        click.echo("Cleaning up...")
    clean_up(tar_file)


if __name__ == "__main__":
    main()
