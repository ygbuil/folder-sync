# ruff: noqa: E402
import sys
import os
import customtkinter as ctk

sys.path.append(os.getcwd())

import button_actions
from objects import (
    LeftMenuBuilder,
    Window,
    TriggerObjectBuilder,
    DirectorySelectorBuilder,
    add_image,
)
from constants import (
    APP_NAME,
    TITLE_FONT,
    ARROW_PATH,
    ARROW_SIZE,
    X_ARROW,
    Y_ARROW,
    X_ORIGIN_SELECTOR,
    Y_ORIGIN_SELECTOR,
    DIRECTORY_SELECTOR_BUTTON_COLOR,
    DIRECTORY_SELECTOR_BUTTON_HOVER_COLOR,
    X_DESTINATION_SELECTOR,
    Y_DESTINATION_SELECTOR,
    TRIGGER_BUTTON_COLOR,
    TRIGGER_BUTTON_HOVER_COLOR,
    X_TRIGGER_BUTTON,
    Y_TRIGGER_BUTTON,
    ROOT_WINDOW_HEIGHT,
    ROOT_WINDOW_WIDTH,
)
import utils


root = Window.create_window(window=ctk.CTk(), title=APP_NAME)
cache = utils.read_cache()

# left menu
left_menu = (
    LeftMenuBuilder(window=root.window)
    .build_frame(side=ctk.LEFT, fill=ctk.Y, padx=10, pady=10)
    .build_label(text=APP_NAME, font=TITLE_FONT, side=ctk.TOP, padx=20, pady=10)
    .build()
)

# down arrow
add_image(
    window=root.window, image_path=ARROW_PATH, size=ARROW_SIZE, x=X_ARROW, y=Y_ARROW
)

# origin selector
origin_selector = (
    DirectorySelectorBuilder(
        window=root.window,
        selector_type="origin",
        x=X_ORIGIN_SELECTOR,
        y=Y_ORIGIN_SELECTOR,
    )
    .build_button(
        text="Choose Origin Folder",
        command=lambda: button_actions.choose_directory(
            cache=cache, directory_selector=origin_selector
        ),
        width=160,
        fg_color=DIRECTORY_SELECTOR_BUTTON_COLOR,
        hover_color=DIRECTORY_SELECTOR_BUTTON_HOVER_COLOR,
    )
    .build_label(cache=cache)
    .build()
)

# destination selector
destination_selector = (
    DirectorySelectorBuilder(
        window=root.window,
        selector_type="destination",
        x=X_DESTINATION_SELECTOR,
        y=Y_DESTINATION_SELECTOR,
    )
    .build_button(
        text="Choose Origin Folder",
        command=lambda: button_actions.choose_directory(
            cache=cache, directory_selector=destination_selector
        ),
        width=160,
        fg_color=DIRECTORY_SELECTOR_BUTTON_COLOR,
        hover_color=DIRECTORY_SELECTOR_BUTTON_HOVER_COLOR,
    )
    .build_label(cache=cache)
    .build()
)

# trigger object
trigger_object = (
    TriggerObjectBuilder(window=root.window, x=X_TRIGGER_BUTTON, y=Y_TRIGGER_BUTTON)
    .build_button(
        text="Start Backup",
        command=lambda: button_actions.open_warning_window(
            root=root, cache=cache, trigger_object=trigger_object
        ),
        width=160,
        height=40,
        fg_color=TRIGGER_BUTTON_COLOR,
        hover_color=TRIGGER_BUTTON_HOVER_COLOR,
    )
    .build()
)

root.set_window_geometry(
    window_width=ROOT_WINDOW_WIDTH, window_height=ROOT_WINDOW_HEIGHT
)

if __name__ == "__main__":
    root.window.mainloop()
