from backend.main import main


def test_process(origin_folder, destination_folder):
    assert main(origin_folder, destination_folder)[0] == 0
