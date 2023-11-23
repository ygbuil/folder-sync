import customtkinter as ctk
import button_actions
from objects import DirectorySelector, LeftMenu, Window
from constants import *
import utils


root = Window(window=ctk.CTk(), title=APP_NAME)
cache = utils.read_cache()

# left menu
left_menu = LeftMenu(window=root.window)
left_menu.add_frame(side=ctk.LEFT, fill=ctk.Y, padx=10, pady=10)
left_menu.add_label(
    text=APP_NAME, font=("TkDefaultFont", 20), side=ctk.TOP, padx=20, pady=10
)

# origin selector
origin_selector = DirectorySelector(window=root.window, selector_type="origin")
origin_selector.add_frame(x=X_ORIGIN_BUTTON, y=Y_ORIGIN_BUTTON)
origin_selector.add_button(
    text="Choose Origin Folder",
    command=lambda: button_actions.choose_directory(
        cache=cache, directory_selector=origin_selector
    ),
    padx=0,
    pady=0,
    width=160,
)
origin_selector.add_label(cache=cache)

# origin selector
destination_selector = DirectorySelector(
    window=root.window, selector_type="destination"
)
destination_selector.add_frame(x=X_DESTINATION_BUTTON, y=Y_DESTINATION_BUTTON)
destination_selector.add_button(
    text="Choose Backup Folder",
    command=lambda: button_actions.choose_directory(
        cache=cache, directory_selector=destination_selector
    ),
    padx=0,
    pady=0,
    width=160,
)
destination_selector.add_label(cache=cache)

# trigger selector
trigger_object = DirectorySelector(window=root.window, selector_type="destination")
trigger_object.add_frame(x=X_TRIGGER_BUTTON, y=Y_TRIGGER_BUTTON)
trigger_object.add_button(
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
