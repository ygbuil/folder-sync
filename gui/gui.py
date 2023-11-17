import tkinter as tk
import json
import customtkinter as ctk
import button_actions
from objects import Frame, set_window_geometry


X_FRAME_ORIGIN = X_FRAME_DESTINSTION = 100
Y_FRAME_ORIGIN = 40
Y_FRAME_DESTINSTION = Y_FRAME_ORIGIN + 50

X_FRAME_TRIGGER = 170
Y_FRAME_TRIGGER = Y_FRAME_DESTINSTION + 65


json_file_path = 'gui/label_cache.json'


with open(json_file_path, 'r') as json_file:
    cache = json.load(json_file)



window = ctk.CTk()
window.title("Smart Backup")


# origin frame
origin_frame = Frame.create_frame(window, frame_type="origin", x_frame=X_FRAME_ORIGIN, y_frame=Y_FRAME_ORIGIN)
origin_frame.add_button(
    button_text="Choose Origin Folder",
    command=lambda: button_actions.choose_directory(origin_frame, cache),
    width=200
)
origin_frame.add_label(label_text="No origin folder selected." if cache["origin"] == "" else cache["origin"])


# backup frame
backup_frame = Frame.create_frame(window, frame_type="destination", x_frame=X_FRAME_DESTINSTION, y_frame=Y_FRAME_DESTINSTION)
backup_frame.add_button(
    button_text="Choose Backup Folder",
    command=lambda: button_actions.choose_directory(backup_frame, cache),
    width=200
)
backup_frame.add_label(label_text="No backup folder selected." if cache["destination"] == "" else cache["destination"])


# trigger button
trigger_backup = Frame.create_frame(window, frame_type="trigger_button", x_frame=X_FRAME_TRIGGER, y_frame=Y_FRAME_TRIGGER)
trigger_backup.add_button(
    button_text="Start Backup",
    command=lambda: button_actions.start_backup(origin_frame.selected_directory),
    height=50,
    width=250
)


set_window_geometry(window)

window.mainloop()
