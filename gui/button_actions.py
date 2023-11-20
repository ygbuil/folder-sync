import customtkinter as ctk
import json
import time
import threading
from tkinter import filedialog
from constants import *


def start_backup(origin_directory, destination_directory):
    print("Start")
    print(origin_directory, destination_directory)
    # dummy()
    time.sleep(3)
    print("End")


def btn_function(root, trigger_frame, origin_directory, destination_directory):
    thread = threading.Thread(
        target=start_backup, args=(origin_directory, destination_directory)
    )
    thread.start()

    # block button
    trigger_frame.button.configure(state="disabled")

    # show progressbar
    progress_bar = ctk.CTkProgressBar(
        trigger_frame.frame, mode="indeterminate", indeterminate_speed=3
    )
    progress_bar.pack(side="left", padx=20)

    # start updating progressbar
    update_progressbar(
        root=root, button=trigger_frame.button, progress_bar=progress_bar, thread=thread
    )  # send thread as parameter - so it doesn't need `global`


def update_progressbar(root, button, progress_bar, thread):
    if thread.is_alive():
        # update progressbar
        progress_bar.step()
        # check again after 25ms
        root.after(25, update_progressbar, root, button, progress_bar, thread)
    else:
        # hide progressbar
        progress_bar.pack_forget()
        # unblock button
        button.configure(state="normal")


def update_label_cache(cache):
    with open(LABEL_CACHE, "w") as cache_file:
        json.dump(cache, cache_file)


def choose_directory(self, cache):
    selected_directory = filedialog.askdirectory()

    if selected_directory:
        self.selected_directory_label.configure(text=selected_directory)

        if self.frame_name == "origin":
            cache["origin"] = selected_directory
        elif self.frame_name == "destination":
            cache["destination"] = selected_directory

        update_label_cache(cache)
