from backend.entry_points._pipeline import _pipeline


def test_process(origin_folder, destination_folder) -> None:
    assert _pipeline(origin_folder, destination_folder)[0] == 0
