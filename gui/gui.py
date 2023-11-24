import customtkinter as ctk
import button_actions
from objects import DirectorySelector, LeftMenuBuilder, Window, DirectorySelectorBuilder
from constants import *
import utils


root = Window.create_window(window=ctk.CTk(), title=APP_NAME)
cache = utils.read_cache()

# left menu
left_menu = (
    LeftMenuBuilder(window=root.window)
    .build_frame(side=ctk.LEFT, fill=ctk.Y, padx=10, pady=10)
    .build_label(
        text=APP_NAME, font=("TkDefaultFont", 20), side=ctk.TOP, padx=20, pady=10
    )
    .build()
)

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
    )
    .build_label(cache=cache)
    .build()
)

# trigger selector
trigger_object = DirectorySelector(window=root.window, selector_type="destination")
trigger_object.define_frame(x=X_TRIGGER_BUTTON, y=Y_TRIGGER_BUTTON)
trigger_object.define_button(
    text="Start Backup",
    command=lambda: button_actions.open_warning_window(
        root=root, cache=cache, trigger_object=trigger_object
    ),
    padx=0,
    pady=0,
    width=160,
    height=40,
)


root.set_window_geometry(
    window_width=ROOT_WINDOW_WIDTH, window_height=ROOT_WINDOW_HEIGHT
)
root.window.mainloop()
