import json
import customtkinter as ctk
from constants import *


def initialize_app(title):
    root = ctk.CTk()
    root.title(title)

    return root


def read_cache():
    with open(LABEL_CACHE, "r") as json_file:
        return json.load(json_file)


def set_window_geometry(window, window_width, window_height):
    x_position = (window.winfo_screenwidth() - window_width) // 2
    y_position = (window.winfo_screenheight() - window_height) // 2

    window.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")
