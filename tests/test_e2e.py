"""e2e testing."""
from folder_sync.entry_points._pipeline import _pipeline


def test_pipeline(origin_folder: str, destination_folder: str) -> None:
    """Entire pipeline. Checks differences between origin and destination folders and
    sets destination to be in the same status as origin.

    :param origin_root_path: Root path of the origin folder.
    :param destination_root_path: Root path of the destination folder.
    :returns: None.
    """
    assert _pipeline(origin_folder, destination_folder)[0] == 0
