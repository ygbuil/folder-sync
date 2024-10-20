from backend.entry_points._pipeline import _pipeline


def test_process(origin_folder, destination_folder, trigger_object) -> None:
    assert _pipeline(origin_folder, destination_folder, trigger_object)[0] == 0
