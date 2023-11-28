import sys

sys.path.append("/Users/ygbuil/Documents/github/Easy-Backup")
import customtkinter as ctk
import button_actions
from objects import (
    LeftMenuBuilder,
    Window,
    DirectorySelectorBuilder,
    TriggerObjectBuilder,
)
from constants import *
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

from PIL import Image

button_image = ctk.CTkImage(Image.open("gui/arrow.png"), size=(26, 26))
image_button = ctk.CTkLabel(master=root.window, image=button_image, text="")
image_button.place(x=X_ARROW, y=Y_ARROW)
# image_button.pack()

# origin selector
origin_selector = (
    DirectorySelectorBuilder(window=root.window, selector_type="origin")
    .build_frame(x=X_ORIGIN_SELECTOR, y=Y_ORIGIN_SELECTOR)
    .build_button(
        text="Choose Origin Folder",
        command=lambda: button_actions.choose_directory(
            cache=cache, directory_selector=origin_selector
        ),
        padx=0,
        pady=0,
        width=160,
        fg_color=DIRECTORY_SELECTOR_BUTTON_COLOR,
        hover_color=DIRECTORY_SELECTOR_BUTTON_HOVER_COLOR,
    )
    .build_label(cache=cache)
    .build()
)


# destination selector
destination_selector = (
    DirectorySelectorBuilder(window=root.window, selector_type="destination")
    .build_frame(x=X_DESTINATION_SELECTOR, y=Y_DESTINATION_SELECTOR)
    .build_button(
        text="Choose Backup Folder",
        command=lambda: button_actions.choose_directory(
            cache=cache, directory_selector=destination_selector
        ),
        padx=0,
        pady=0,
        width=160,
        fg_color=DIRECTORY_SELECTOR_BUTTON_COLOR,
        hover_color=DIRECTORY_SELECTOR_BUTTON_HOVER_COLOR,
    )
    .build_label(cache=cache)
    .build()
)

# trigger object
trigger_object = (
    TriggerObjectBuilder(window=root.window, selector_type="destination")
    .build_frame(x=X_TRIGGER_BUTTON, y=Y_TRIGGER_BUTTON)
    .build_button(
        text="Start Backup",
        command=lambda: button_actions.open_warning_window(
            root=root, cache=cache, trigger_object=trigger_object
        ),
        padx=0,
        pady=0,
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
