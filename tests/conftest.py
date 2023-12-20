import pytest
import os


def create_structure(base_path, items):
    for name, content in items.items():
        path = os.path.join(base_path, name)
        if isinstance(content, dict):
            os.mkdir(path)
            create_structure(path, content)
        else:
            with open(path, "w") as file:
                file.write(content)


@pytest.fixture
def origin_folder(tmpdir):
    structure = {
        "origin": {
            "file_1.txt": "",
            "file_2.txt": "",
            "folder_1": {"file_3.txt": "", "file_4.txt": ""},
            "folder_2": {},
        }
    }

    create_structure(str(tmpdir), structure)

    return str(tmpdir.join("origin"))


@pytest.fixture
def destination_folder(tmpdir):
    structure = {
        "destination": {
            "file_1.txt": "",
            "file_2.txt": "",
            "file_to_delete_1.txt": "",
            "folder_1": {"file_3.txt": "", "file_to_delete_2.txt": ""},
            "folder_to_delete_1": {},
        }
    }

    create_structure(str(tmpdir), structure)

    return str(tmpdir.join("destination"))


@pytest.fixture
def trigger_object():
    class TriggerObject:
        def __init__(self):
            self.steps = 0

        def step_progress_bar(self):
            self.steps += 1

    return TriggerObject()
