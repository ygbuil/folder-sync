import pytest
from backend import objects


@pytest.mark.parametrize(
    "paths, progress_bar_update_steps",
    [
        ({"files": range(80), "dirs": range(80)}, 40),
        ({"files": range(10), "dirs": range(5)}, 40),
        ({"files": range(10), "dirs": range(5)}, 29),
        ({"files": range(116), "dirs": range(1)}, 40),
        ({"files": range(116), "dirs": range(1)}, 1),
    ],
)
def test_progress_bar_update(paths, progress_bar_update_steps, trigger_object):
    result = progress_bar_update_steps
    mini_step = objects.calculate_steps(
        paths=paths, progress_bar_update_steps=progress_bar_update_steps
    )

    counter = 0

    for _ in paths["files"]:
        counter, progress_bar_update_steps = objects.update_progress_bar(
            counter=counter,
            progress_bar_update_steps=progress_bar_update_steps,
            mini_step=mini_step,
            trigger_object=trigger_object,
        )

    for _ in paths["dirs"]:
        counter, progress_bar_update_steps = objects.update_progress_bar(
            counter=counter,
            progress_bar_update_steps=progress_bar_update_steps,
            mini_step=mini_step,
            trigger_object=trigger_object,
        )

    objects.handle_remaining_steps(
        progress_bar_update_steps=progress_bar_update_steps,
        trigger_object=trigger_object,
    )

    assert trigger_object.steps == result
