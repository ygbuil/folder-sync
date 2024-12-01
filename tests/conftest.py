"""Fixtures for testing."""

from pathlib import Path

import pytest


@pytest.fixture
def origin_folder(tmpdir: str) -> str:
    """Create folder structure for origin directory.

    :param tmpdir: Temporary directory used by pytest.
    :returns: tmpdir and origin.
    """
    structure = {
        "origin": {
            "file_1.txt": "",
            "file_2.txt": "",
            "folder_1": {"file_3.txt": "", "file_4.txt": ""},
            "folder_2": {},
        },
    }

    _create_structure(str(tmpdir), structure)

    return str(tmpdir.join("origin"))


@pytest.fixture
def destination_folder(tmpdir: str) -> str:
    """Create folder structure for destination directory.

    :param tmpdir: Temporary directory used by pytest.
    :returns: tmpdir and destination.
    """
    structure = {
        "destination": {
            "file_1.txt": "",
            "file_2.txt": "",
            "file_to_delete_1.txt": "",
            "folder_1": {"file_3.txt": "", "file_to_delete_2.txt": ""},
            "folder_to_delete_1": {},
        },
    }

    _create_structure(str(tmpdir), structure)

    return str(tmpdir.join("destination"))


def _create_structure(base_path: str, items: dict) -> None:
    """Create file structure for testing.

    :param base_path: Base path to create the forlder structure.
    :param items: Dictionary with all the nested folder and files.
    :returns: None.
    """
    for name, content in items.items():
        path = Path(base_path) / Path(name)
        if isinstance(content, dict):
            Path.mkdir(path)
            _create_structure(path, content)
        else:
            with Path.open(path, "w") as file:
                file.write(content)
