import json
from tkinter import filedialog


def update_label_cache(cache):
    with open("gui/label_cache.json", "w") as cache_file:
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


def start_backup(x):
    print(x)