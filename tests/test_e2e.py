from backend.main import main


def test_process(origin_folder, destination_folder, trigger_object):
    assert main(origin_folder, destination_folder, trigger_object)[0] == 0
