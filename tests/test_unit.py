"""Unit testing module."""

import os

import pytest


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

    :param origin_folder: Root path of the origin folder.
    :param subsequent_dir: Folder structure inside origin_folder.
    :returns: None.
    """
    assert os.path.exists(os.path.join(origin_folder, *subsequent_dir))  # noqa: PTH110, PTH118


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

    :param destination_folder: Root path of the destination folder.
    :param subsequent_dir: Folder structure inside destination_folder.
    :returns: None.
    """
    assert os.path.exists(os.path.join(destination_folder, *subsequent_dir))  # noqa: PTH110, PTH118
