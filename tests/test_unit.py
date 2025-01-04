"""Unit testing module."""

from pathlib import Path

import pytest

from src.folder_sync.entry_points._pipeline import _pipeline


@pytest.mark.parametrize(
    "subsequent_dir",
    [
        [""],
        ["file_1.txt"],
        ["file_2.txt"],
        ["folder_1"],
        ["folder_1", "file_3.txt"],
        ["folder_1", "file_4.txt"],
        ["folder_2"],
    ],
)
def test_origin_folder_creation(origin_folder: str, subsequent_dir: list) -> None:
    """Test the creation of origin folder.

    Args:
        origin_folder: Root path of the origin folder.
        subsequent_dir: Folder structure inside origin_folder.

    Returns:
        None
    """
    assert (Path(origin_folder) / Path(*subsequent_dir)).exists()


@pytest.mark.parametrize(
    "subsequent_dir",
    [
        [""],
        ["file_1.txt"],
        ["file_2.txt"],
        ["file_to_delete_1.txt"],
        ["folder_1"],
        ["folder_1", "file_3.txt"],
        ["folder_1", "file_to_delete_2.txt"],
        ["folder_to_delete_1"],
    ],
)
def test_destination_folder_creation(destination_folder: str, subsequent_dir: list) -> None:
    """Test the creation of destination folder.

    Args:
        destination_folder: Root path of the destination folder.
        subsequent_dir: Folder structure inside destination_folder.

    Returns:
        None
    """
    assert (Path(destination_folder) / Path(*subsequent_dir)).exists()


def test_last_modified_change(origin_folder: str, destination_folder: str) -> None:
    """Test the last modified change of a file.

    Args:
        origin_folder: Root path of the origin folder.
        destination_folder: Root path of the destination folder.

    Returns:
        None
    """
    with Path.open(Path(origin_folder) / "file_1.txt", "w") as file:
        file.write("b")

    with Path.open(Path(destination_folder) / "file_1.txt", "r") as file:
        assert file.read() == "a"

    _pipeline(origin_folder, destination_folder)

    with Path.open(Path(destination_folder) / "file_1.txt", "r") as file:
        assert file.read() == "b"
