"""e2e testing."""
from backend.entry_points._pipeline import _pipeline


def test_pipeline(origin_folder: str, destination_folder: str) -> None:
    """Entire pipeline. Checks differences between master and clone folders and
    sets clone to be in the same status as master.

    :param origin_root_path: Root path of the master folder.
    :param destination_root_path: Root path of the clone folder.
    :returns: None.
    """
    assert _pipeline(origin_folder, destination_folder)[0] == 0
