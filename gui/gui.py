import tkinter as tk
import customtkinter as ctk
import button_actions
from objects import Frame, set_window_geometry



window = ctk.CTk()
window.title("Smart Backup")


# origin frame
origin_frame = Frame.create_frame(window, x_frame=50, y_frame=40)
origin_frame.add_button(
    button_text="Choose Origin Folder",
    command=lambda: button_actions.choose_directory(origin_frame.selected_directory_label),
    width=200
)
origin_frame.add_label(label_text="No origin folder selected.")


# backup frame
backup_frame = Frame.create_frame(window, x_frame=50, y_frame=90)
backup_frame.add_button(
    button_text="Choose Backup Folder",
    command=lambda: button_actions.choose_directory(backup_frame.selected_directory_label),
    width=200
)
backup_frame.add_label(label_text="No backup folder selected.")


# trigger button
trigger_backup = Frame.create_frame(window, x_frame=50, y_frame=140)
trigger_backup.add_button(
    button_text="Start Backup",
    command=lambda: button_actions.start_backup(1),
    height=50,
    width=400
)


set_window_geometry(window)

window.mainloop()
