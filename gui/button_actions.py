import json
import time
import threading
from tkinter import filedialog
from constants import *


def start_backup(x, y):
    print("Start")
    time.sleep(3)
    print("End")


def btn_function(app, button, progress_bar):
    x = 100
    y = 100

    thread = threading.Thread(target=start_backup, args=(x, y))
    thread.start()

    # block button
    button.configure(state="disabled")

    # show progressbar
    progress_bar.pack(pady=40)

    # start updating progressbar
    update_progressbar(
        app=app, button=button, progress_bar=progress_bar, thread=thread
    )  # send thread as parameter - so it doesn't need `global`


def update_progressbar(app, button, progress_bar, thread):
    if thread.is_alive():
        # update progressbar
        progress_bar.step()
        # check again after 25ms
        app.after(25, update_progressbar, app, button, progress_bar, thread)
    else:
        # hide progressbar
        progress_bar.pack_forget()
        # unblock button
        button.configure(state="normal")


def update_label_cache(cache):
    with open(LABEL_CACHE, "w") as cache_file:
        json.dump(cache, cache_file)


def choose_directory(self, cache):
    directory_path = filedialog.askdirectory()

    if directory_path:
        self.selected_directory = directory_path
        self.selected_directory_label.configure(text=directory_path)

        if self.frame_type == "origin":
            cache["origin"] = self.selected_directory
        elif self.frame_type == "destination":
            cache["destination"] = self.selected_directory

        update_label_cache(cache)
