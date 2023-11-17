import time
import threading
import json
import customtkinter as ctk
import button_actions
from objects import Frame, set_window_geometry
from constants import *


with open(LABEL_CACHE, "r") as json_file:
    cache = json.load(json_file)


app = ctk.CTk()
app.title("Smart Backup")


oytter_frame = ctk.CTkFrame(app)
oytter_frame.pack(padx=20, pady=20, fill="both", expand=True)

title = ctk.CTkLabel(app, text="Smart Backup")
title.pack(pady=10, padx=10)


# origin frame
origin_frame = Frame.create_frame(
    app, frame_type="origin", x_frame=X_FRAME_ORIGIN, y_frame=Y_FRAME_ORIGIN
)
origin_frame.add_button(
    button_text="Choose Origin Folder",
    command=lambda: button_actions.choose_directory(origin_frame, cache),
    width=200,
)
origin_frame.add_label(
    label_text="No origin folder selected."
    if cache["origin"] == ""
    else cache["origin"]
)

#
# backup frame
backup_frame = Frame.create_frame(
    app,
    frame_type="destination",
    x_frame=X_FRAME_DESTINSTION,
    y_frame=Y_FRAME_DESTINSTION,
)
backup_frame.add_button(
    button_text="Choose Backup Folder",
    command=lambda: button_actions.choose_directory(backup_frame, cache),
    width=200,
)
backup_frame.add_label(
    label_text="No backup folder selected."
    if cache["destination"] == ""
    else cache["destination"]
)


def start_backup(x, y):
    print("Start")
    time.sleep(3)
    print("End")


def btn_function():
    x = 100
    y = 100

    boolean_progress_bar = threading.Thread(target=start_backup, args=(x, y))
    boolean_progress_bar.start()

    # block button
    button.configure(state="disabled")

    # show progressbar
    progress_bar.pack(pady=40)

    # start updating progressbar
    update_progressbar(
        boolean_progress_bar
    )  # send thread as parameter - so it doesn't need `global`


def update_progressbar(thread):
    if thread.is_alive():
        # update progressbar
        progress_bar.step()
        # check again after 25ms
        app.after(25, update_progressbar, thread)
    else:
        # hide progressbar
        progress_bar.pack_forget()
        # unblock button
        button.configure(state="normal")


progress_bar = ctk.CTkProgressBar(app, mode="indeterminate", indeterminate_speed=3)

button = ctk.CTkButton(app, text="Start", command=btn_function)
button.pack(pady=10)


set_window_geometry(app)

app.mainloop()
