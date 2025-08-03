"""e2e testing."""

from pathlib import Path

from folder_sync.cli._pipeline import _pipeline


def test_pipeline(origin_folder: str, destination_folder: str) -> None:
    """Entire pipeline. Checks differences between origin and destination folders and
    sets destination to be in the same status as origin.

    Args:
        origin_folder: Root path of the origin folder.
        destination_folder: Root path of the destination folder.

    Returns:
        None
    """
    assert _pipeline(Path(origin_folder), Path(destination_folder)) == 0
