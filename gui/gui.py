import customtkinter as ctk
import button_actions
from objects import Frame
from constants import *
import utils


root = utils.initialize_app(title=APP_NAME)
cache = utils.read_cache()


title_frame = Frame.create_frame(
    root, frame_name="title", x_frame=X_TITLE, y_frame=Y_TITLE
)
title = ctk.CTkLabel(title_frame.frame, text=APP_NAME, font=("TkDefaultFont", 20))
title.pack()


# origin frame
origin_frame = Frame.create_frame(
    root, frame_name="origin", x_frame=X_FRAME_ORIGIN, y_frame=Y_FRAME_ORIGIN
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
destination_frame = Frame.create_frame(
    root,
    frame_name="destination",
    x_frame=X_FRAME_DESTINSTION,
    y_frame=Y_FRAME_DESTINSTION,
)
destination_frame.add_button(
    button_text="Choose Backup Folder",
    command=lambda: button_actions.choose_directory(destination_frame, cache),
    width=200,
)
destination_frame.add_label(
    label_text="No backup folder selected."
    if cache["destination"] == ""
    else cache["destination"]
)


trigger_frame = Frame.create_frame(
    root,
    frame_name="start_button",
    x_frame=X_FRAME_TRIGGER,
    y_frame=Y_FRAME_TRIGGER,
)
trigger_frame.add_button(
    button_text="Start",
    command=lambda: button_actions.btn_function(
        root=root,
        trigger_frame=trigger_frame,
        origin_directory=cache["origin"],
        destination_directory=cache["destination"],
    ),
    width=200,
)


def f():
    print("Continue")


def open_warning_window(origin_directory, destination_directory):
    warning_window = ctk.CTkToplevel(root)
    warning_window.title("Warning")

    warning_frame = Frame.create_frame(
        warning_window,
        frame_name="warning",
        x_frame=20,
        y_frame=20,
    )
    warning_frame.add_button(
        button_text="Cancel",
        command=lambda: warning_window.destroy(),
        width=40,
    )
    warning_frame.add_button(
        button_text="Continue",
        command=f,
        width=40,
    )

    """ warning_frame = Frame.create_frame(
        warning_window,
        frame_name="warning",
        x_frame=80,
        y_frame=20,
    )
    warning_frame.add_button(
        button_text="Cancel",
        command=lambda: g(window=warning_window),
        width=40,
    )
    warning_frame.add_button(
        button_text="Continue",
        command=f,
        width=40,
    ) """

    label = ctk.CTkLabel(
        warning_window,
        text=f"You are about to replace the content from {origin_directory} with the one from {destination_directory}. Are you sure?",
    )
    label.pack()
    utils.set_window_geometry(
        window=warning_window,
        window_width=WARNING_WINDOW_WIDTH,
        window_height=WARNING_WINDOW_HEIGHT,
    )


test_frame = Frame.create_frame(
    root,
    frame_name="test",
    x_frame=X_FRAME_TRIGGER,
    y_frame=Y_FRAME_TRIGGER + 50,
)
test_frame.add_button(
    button_text="test",
    command=lambda: open_warning_window(
        origin_directory=cache["origin"], destination_directory=cache["destination"]
    ),
    width=200,
)


utils.set_window_geometry(
    window=root, window_width=ROOT_WINDOW_WIDTH, window_height=ROOT_WINDOW_HEIGHT
)

root.mainloop()
