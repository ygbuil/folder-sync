import customtkinter as ctk


class Window:
    def __init__(self, window, title):
        self.window = window
        self.title = title

    def set_window_geometry(self, window_width, window_height):
        x_position = (self.window.winfo_screenwidth() - window_width) // 2
        y_position = (self.window.winfo_screenheight() - window_height) // 2

        self.window.geometry(
            f"{window_width}x{window_height}+{x_position}+{y_position}"
        )


class LeftMenu:
    def __init__(self, window):
        self.window = window

    def add_frame(self, **kwargs):
        frame = ctk.CTkFrame(master=self.window)
        frame.pack(**kwargs)
        self.__dict__["frame"] = frame

    def add_label(self, text, font, side, padx, pady):
        app_title = ctk.CTkLabel(master=self.frame, text=text, font=font)
        app_title.pack(side=side, padx=padx, pady=pady)


class ContinueCancel:
    def __init__(self, window):
        self.window = window

    def add_frame(self, **kwargs):
        frame = ctk.CTkFrame(master=self.window, fg_color="transparent")
        frame.pack(**kwargs)
        self.__dict__["frame"] = frame

    def add_button(self, text, command, padx, **kwargs):
        button = ctk.CTkButton(master=self.frame, text=text, command=command, **kwargs)
        button.pack(side=ctk.LEFT, padx=padx)


class DirectorySelector:
    def __init__(self, window, selector_type):
        self.window = window
        self.selector_type = selector_type

    def add_frame(self, x, y):
        frame = ctk.CTkFrame(master=self.window)
        frame.pack()
        frame.place(x=x, y=y)
        self.__dict__["frame"] = frame

    def add_button(self, text, command, padx, pady, **kwargs):
        button = ctk.CTkButton(master=self.frame, text=text, command=command, **kwargs)
        button.pack(side=ctk.LEFT, padx=padx, pady=pady)
        self.__dict__["button"] = button

    def add_label(self, cache):
        directory_label = ctk.CTkLabel(
            master=self.frame,
            text="No origin folder selected."
            if cache[self.selector_type] == ""
            else cache[self.selector_type],
        )
        directory_label.pack(side=ctk.LEFT, padx=10)
        self.__dict__["directory_label"] = directory_label

    def add_progressbar(self, width):
        progress_bar = ctk.CTkProgressBar(
            self.frame, mode="indeterminate", indeterminate_speed=3, width=width
        )
        progress_bar.pack(side=ctk.LEFT, padx=10)
        self.__dict__["progress_bar"] = progress_bar
