import customtkinter as ctk
import button_actions
from objects import DirectorySelector
from constants import *
import utils


root = utils.initialize_app(title=APP_NAME)
cache = utils.read_cache()
frame = ctk.CTkFrame(root, width=180)
frame.pack(side=ctk.LEFT, fill=ctk.Y, padx=10, pady=10)
app_title = ctk.CTkLabel(frame, text=APP_NAME, font=("TkDefaultFont", 20))
app_title.pack(side=ctk.TOP, padx=20, pady=10)

# # origin selector
# origin_selector = DirectorySelector(window=root, selector_type="origin")
# origin_selector.add_button(text="Choose Origin Folder", width=160, command=lambda: button_actions.choose_directory(cache=cache, directory_selector=origin_selector), x=X_ORIGIN_BUTTON, y=Y_ORIGIN_BUTTON)
# origin_selector.add_label(cache=cache, x=X_ORIGIN_LABEL, y=Y_ORIGIN_LABEL)

# # destination selector
# destination_selector = DirectorySelector(window=root, selector_type="destination")
# destination_selector.add_button(text="Choose Backup Folder", width=160, command=lambda: button_actions.choose_directory(cache=cache, directory_selector=destination_selector), x=X_DESTINATION_BUTTON, y=Y_DESTINATION_BUTTON)
# destination_selector.add_label(cache=cache, x=X_DESTINATION_LABEL, y=Y_DESTINATION_LABEL)

# # trigger button
# trigger_button = ctk.CTkButton(master=root, text="Start Backup", width=160, height=40, command=lambda: open_warning_window(
#         origin_directory=cache["origin"], destination_directory=cache["destination"]
#     ))
# trigger_button.place(x=X_TRIGGER_BUTTON, y=Y_TRIGGER_BUTTON)

# origin selector
origin_selector = DirectorySelector(window=root, selector_type="origin")
origin_selector.add_frame(x=X_ORIGIN_BUTTON, y=Y_ORIGIN_BUTTON)
origin_selector.add_button(
    text="Choose Origin Folder",
    width=160,
    command=lambda: button_actions.choose_directory(
        cache=cache, directory_selector=origin_selector
    ),
)
origin_selector.add_label(cache=cache)

# origin selector
destination_selector = DirectorySelector(window=root, selector_type="destination")
destination_selector.add_frame(x=X_DESTINATION_BUTTON, y=Y_DESTINATION_BUTTON)
destination_selector.add_button(
    text="Choose Backup Folder",
    width=160,
    command=lambda: button_actions.choose_directory(
        cache=cache, directory_selector=destination_selector
    ),
)
destination_selector.add_label(cache=cache)

# # trigger button
# trigger_button = DirectorySelector(window=root, selector_type="destination")
# trigger_button.add_frame(x=X_TRIGGER_BUTTON, y=Y_TRIGGER_BUTTON)
# trigger_button.add_button(text="Start Backup", width=160, command=lambda: open_warning_window(
#         origin_directory=cache["origin"], destination_directory=cache["destination"]
#     ))

# trigger button
trigger_button = ctk.CTkButton(
    master=root,
    text="Start Backup",
    width=160,
    height=40,
    command=lambda: open_warning_window(
        origin_directory=cache["origin"], destination_directory=cache["destination"]
    ),
)
trigger_button.place(x=X_TRIGGER_BUTTON, y=Y_TRIGGER_BUTTON)


def open_warning_window(origin_directory, destination_directory):
    warning_window = ctk.CTkToplevel(root)
    warning_window.title("Warning")

    label = ctk.CTkLabel(
        warning_window,
        text=f"You are about to replace the content from {origin_directory} with the one from {destination_directory}. Are you sure?",
    )
    label.place(x=10, y=10)

    cancel_button = ctk.CTkButton(
        master=warning_window, text="Cancel", command=lambda: warning_window.destroy()
    )
    cancel_button.place(x=10, y=100)

    continue_button = ctk.CTkButton(
        master=warning_window,
        text="Continue",
        command=lambda: button_actions.btn_function(
            window=root,
            warning_window=warning_window,
            trigger_button=trigger_button,
            origin_directory=cache["origin"],
            destination_directory=cache["destination"],
        ),
    )
    continue_button.place(x=200, y=100)

    utils.set_window_geometry(
        window=warning_window,
        window_width=WARNING_WINDOW_WIDTH,
        window_height=WARNING_WINDOW_HEIGHT,
    )


utils.set_window_geometry(
    window=root, window_width=ROOT_WINDOW_WIDTH, window_height=ROOT_WINDOW_HEIGHT
)

root.mainloop()
