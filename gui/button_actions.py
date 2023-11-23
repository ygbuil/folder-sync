import customtkinter as ctk
import json
import time
import threading
from tkinter import filedialog
from constants import *
from objects import Window, ContinueCancel


def start_backup(origin_directory, destination_directory):
    print("Start")
    print(origin_directory, destination_directory)
    # dummy()
    time.sleep(3)
    print("End")


def btn_function(
    warning_window, trigger_object, origin_directory, destination_directory
):
    warning_window.destroy()
    thread = threading.Thread(
        target=start_backup, args=(origin_directory, destination_directory)
    )
    thread.start()

    # block button
    trigger_object.button.configure(state="disabled")

    # show progressbar
    trigger_object.add_progressbar(width=PROGRESSBAR_WIDTH)

    # start updating progressbar
    update_progressbar(
        warning_window=warning_window,
        button=trigger_object.button,
        progress_bar=trigger_object.progress_bar,
        thread=thread,
    )  # send thread as parameter - so it doesn't need `global`


def update_progressbar(warning_window, button, progress_bar, thread):
    if thread.is_alive():
        # update progressbar
        progress_bar.step()
        # check again after 25ms
        warning_window.after(
            25, update_progressbar, warning_window, button, progress_bar, thread
        )
    else:
        # hide progressbar
        progress_bar.destroy()
        # unblock button
        button.configure(state="normal")


def update_label_cache(cache):
    with open(LABEL_CACHE, "w") as cache_file:
        json.dump(cache, cache_file)


def choose_directory(cache, directory_selector):
    selected_directory = filedialog.askdirectory()

    if selected_directory:
        directory_selector.directory_label.configure(text=selected_directory)
        if directory_selector.selector_type == "origin":
            cache["origin"] = selected_directory
        elif directory_selector.selector_type == "destination":
            cache["destination"] = selected_directory

        update_label_cache(cache)


def open_warning_window(root, cache, trigger_object):
    warning = Window(window=ctk.CTkToplevel(root.window), title="Warning")

    label = ctk.CTkLabel(
        warning.window,
        text=f"You are about to overwrite the content inside\n'{cache['destination']}'\nwith the one inside\n'{cache['origin']}'.\nAre you sure?",
    )
    label.pack()

    cancel_continue_outter = ContinueCancel(window=warning.window)
    cancel_continue_outter.add_frame(side=ctk.BOTTOM, fill=ctk.X, pady=10)

    cancel_continue_inner = ContinueCancel(window=cancel_continue_outter.frame)
    cancel_continue_inner.add_frame()
    cancel_continue_inner.add_button(
        text="Cancel", command=lambda: warning.window.destroy(), padx=5, width=80
    )
    cancel_continue_inner.add_button(
        text="Continue",
        command=lambda: btn_function(
            warning_window=warning.window,
            trigger_object=trigger_object,
            origin_directory=cache["origin"],
            destination_directory=cache["destination"],
        ),
        padx=5,
        width=80,
    )

    warning.set_window_geometry(
        window_width=WARNING_WINDOW_WIDTH,
        window_height=WARNING_WINDOW_HEIGHT,
    )
