import json
import customtkinter as ctk
import button_actions
from objects import Frame, set_window_geometry
from constants import *


with open(LABEL_CACHE, "r") as json_file:
    cache = json.load(json_file)


app = ctk.CTk()
app.title(APP_NAME)

# outter_frame = ctk.CTkFrame(app)
# outter_frame.pack(padx=20, pady=20, fill="both", expand=True)

title = ctk.CTkLabel(app, text=APP_NAME, font=("TkDefaultFont", 20))
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


trigger_frame = Frame.create_frame(
    app,
    frame_type="start_button",
    x_frame=X_FRAME_TRIGGER,
    y_frame=Y_FRAME_TRIGGER,
)
trigger_frame.add_button(
    button_text="Start",
    command=lambda: button_actions.btn_function(
        app=app,
        button=trigger_frame.button,
    ),
    width=200,
)


set_window_geometry(app)

app.mainloop()
