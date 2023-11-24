import customtkinter as ctk


class Window:
    def __init__(self, window):
        self.window = window

    @classmethod
    def create_window(cls, window, title):
        window.title(title)

        return cls(window=window)

    def set_window_geometry(self, window_width, window_height):
        x_position = (self.window.winfo_screenwidth() - window_width) // 2
        y_position = (self.window.winfo_screenheight() - window_height) // 2

        self.window.geometry(
            f"{window_width}x{window_height}+{x_position}+{y_position}"
        )


class LeftMenu:
    def __init__(self, window):
        self.window = window

    def define_frame(self, **kwargs):
        frame = ctk.CTkFrame(master=self.window)
        frame.pack(**kwargs)
        self.__dict__["frame"] = frame

    def define_label(self, text, font, side, padx, pady):
        app_title = ctk.CTkLabel(master=self.frame, text=text, font=font)
        app_title.pack(side=side, padx=padx, pady=pady)


class LeftMenuBuilder:
    def __init__(self, window):
        self.left_menu = LeftMenu(window=window)

    def build_frame(self, **kwargs):
        self.left_menu.define_frame(**kwargs)
        return self

    def build_label(self, text, font, side, padx, pady):
        self.left_menu.define_label(
            text=text, font=font, side=side, padx=padx, pady=pady
        )
        return self

    def build(self):
        return self.left_menu


class CancelContinue:
    def __init__(self, window):
        self.window = window

    def define_frame(self, **kwargs):
        frame = ctk.CTkFrame(master=self.window, fg_color="transparent")
        frame.pack(**kwargs)
        self.__dict__["frame"] = frame

    def define_button(self, text, command, padx, **kwargs):
        button = ctk.CTkButton(master=self.frame, text=text, command=command, **kwargs)
        button.pack(side=ctk.LEFT, padx=padx)


class CancelContinueBuilder:
    def __init__(self, window):
        self.cancel_continue = CancelContinue(window=window)

    def build_frame(self, **kwargs):
        self.cancel_continue.define_frame(**kwargs)
        return self

    def build_button(self, text, command, padx, **kwargs):
        self.cancel_continue.define_button(
            text=text, command=command, padx=padx, **kwargs
        )
        return self

    def build(self):
        return self.cancel_continue


class DirectorySelector:
    def __init__(self, window, selector_type):
        self.window = window
        self.selector_type = selector_type

    def define_frame(self, x, y):
        frame = ctk.CTkFrame(master=self.window)
        frame.pack()
        frame.place(x=x, y=y)
        self.__dict__["frame"] = frame

    def define_button(self, text, command, padx, pady, **kwargs):
        button = ctk.CTkButton(master=self.frame, text=text, command=command, **kwargs)
        button.pack(side=ctk.LEFT, padx=padx, pady=pady)
        self.__dict__["button"] = button

    def define_label(self, cache):
        directory_label = ctk.CTkLabel(
            master=self.frame,
            text="No origin folder selected."
            if cache[self.selector_type] == ""
            else cache[self.selector_type],
        )
        directory_label.pack(side=ctk.LEFT, padx=10)
        self.__dict__["directory_label"] = directory_label

    def define_progressbar(self, width):
        progress_bar = ctk.CTkProgressBar(
            self.frame, mode="indeterminate", indeterminate_speed=3, width=width
        )
        progress_bar.pack(side=ctk.LEFT, padx=10)
        self.__dict__["progress_bar"] = progress_bar


class DirectorySelectorBuilder:
    def __init__(self, window, selector_type):
        self.directory_selector = DirectorySelector(
            window=window, selector_type=selector_type
        )

    def build_frame(self, x, y):
        self.directory_selector.define_frame(x=x, y=y)
        return self

    def build_button(self, text, command, padx, pady, **kwargs):
        self.directory_selector.define_button(
            text=text, command=command, padx=padx, pady=pady, **kwargs
        )
        return self

    def build_label(self, cache):
        self.directory_selector.define_label(cache=cache)
        return self

    def build_progressbar(self, width):
        self.directory_selector.define_progressbar(width=width)
        return self

    def build(self):
        return self.directory_selector
