import customtkinter as ctk
import json
import time
import threading
from tkinter import filedialog
from constants import *
from objects import Window, CancelContinueBuilder
from backend.main import dummy, main


def open_warning_window(root, cache, trigger_object):
    trigger_object.button.configure(state="disabled")

    warning = Window.create_window(window=ctk.CTkToplevel(root.window), title="Warning")
    warning.window.protocol(
        "WM_DELETE_WINDOW", lambda: on_closing(warning, trigger_object)
    )

    # label = ctk.CTkLabel(
    #     warning.window, text=f"Are you sure you want to overwrite everything inside"
    # )
    # label.pack()
    # label = ctk.CTkLabel(
    #     warning.window, text=f'"{cache["destination"]}"'
    # )
    # label.pack()
    # label = ctk.CTkLabel(warning.window, text=f"with the content from")
    # label.pack()
    # label = ctk.CTkLabel(
    #     warning.window, text=f'"{cache["origin"]}"?'
    # )
    # label.pack()
    label = ctk.CTkLabel(
        warning.window,
        text=f'Are you sure you want to overwrite everything inside\n\n"{cache["destination"]}"\n\nwith the content from\n\n"{cache["origin"]}"?',
    )
    label.pack()

    cancel_continue_outter = (
        CancelContinueBuilder(window=warning.window)
        .build_frame(side=ctk.BOTTOM, fill=ctk.X, pady=20)
        .build()
    )
    cancel_continue_inner = (
        CancelContinueBuilder(window=cancel_continue_outter.frame)
        .build_frame()
        .build_button(
            text="Cancel",
            command=lambda: cancel_action(
                warning=warning, trigger_object=trigger_object
            ),
            padx=5,
            width=80,
            fg_color=CANCEL_BUTTON_COLOR,
            hover_color=CANCEL_BUTTON_HOVER_COLOR,
        )
        .build_button(
            text="Continue",
            command=lambda: continue_action(
                warning_window=warning.window,
                trigger_object=trigger_object,
                origin_directory=cache["origin"],
                destination_directory=cache["destination"],
            ),
            padx=5,
            width=80,
            fg_color=CONTINUE_BUTTON_COLOR,
            hover_color=CONTINUE_BUTTON_HOVER_COLOR,
        )
        .build()
    )

    warning.set_window_geometry(
        window_width=WARNING_WINDOW_WIDTH,
        window_height=WARNING_WINDOW_HEIGHT,
    )


def on_closing(warning, trigger_object):
    trigger_object.button.configure(state="normal")
    warning.window.destroy()


def cancel_action(warning, trigger_object):
    trigger_object.button.configure(state="normal")
    warning.window.destroy()


def continue_action(
    warning_window, trigger_object, origin_directory, destination_directory
):
    warning_window.destroy()
    thread = threading.Thread(
        target=start_backup, args=(origin_directory, destination_directory)
    )
    thread.start()

    # spawn progressbar
    trigger_object.define_progressbar(width=PROGRESSBAR_WIDTH)

    update_progressbar(
        warning_window=warning_window,
        button=trigger_object.button,
        progress_bar=trigger_object.progress_bar,
        thread=thread,
    )


def start_backup(origin_directory, destination_directory):
    time.sleep(1)
    main(origin_root_path=origin_directory, destination_root_path=destination_directory)
    print("hey")


def update_progressbar(warning_window, button, progress_bar, thread):
    if thread.is_alive():
        # update progressbar
        progress_bar.step()
        # check again after 25ms
        warning_window.after(
            25, update_progressbar, warning_window, button, progress_bar, thread
        )
    else:
        progress_bar.destroy()
        button.configure(state="normal")


def choose_directory(cache, directory_selector):
    selected_directory = filedialog.askdirectory()

    if selected_directory:
        directory_selector.directory_label.configure(text=selected_directory)
        if directory_selector.selector_type == "origin":
            cache["origin"] = selected_directory
        elif directory_selector.selector_type == "destination":
            cache["destination"] = selected_directory

        update_label_cache(cache)


def update_label_cache(cache):
    with open(LABEL_CACHE, "w") as cache_file:
        json.dump(cache, cache_file)
