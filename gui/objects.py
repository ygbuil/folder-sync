import customtkinter as ctk
from PIL import Image


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


class DirectorySelector:
    def __init__(self, window, selector_type, x, y):
        self.window = window
        self.selector_type = selector_type
        self.x = x
        self.y = y

    def define_button(self, text, command, **kwargs):
        button = ctk.CTkButton(master=self.window, text=text, command=command, **kwargs)
        button.pack()
        button.place(x=self.x, y=self.y)
        self.__dict__["button"] = button

    def define_label(self, cache):
        directory_label = ctk.CTkLabel(
            master=self.window,
            text=cache[self.selector_type],
        )
        directory_label.place(x=self.x + 170, y=self.y - 1)
        self.__dict__["directory_label"] = directory_label


class DirectorySelectorBuilder:
    def __init__(self, window, selector_type, x, y):
        self.root_window_widget = DirectorySelector(
            window=window, selector_type=selector_type, x=x, y=y
        )

    def build_button(self, text, command, **kwargs):
        self.root_window_widget.define_button(text=text, command=command, **kwargs)
        return self

    def build_label(self, cache):
        self.root_window_widget.define_label(cache=cache)
        return self

    def build(self):
        return self.root_window_widget


class TriggerObject:
    def __init__(self, window, x, y):
        self.window = window
        self.x = x
        self.y = y
        self.progressbar_steps = 0
        self.exit_message = None
        self.exit_message_label = None

    def define_button(self, text, command, **kwargs):
        button = ctk.CTkButton(master=self.window, text=text, command=command, **kwargs)
        button.pack()
        button.place(x=self.x, y=self.y)
        self.__dict__["button"] = button

    def define_progressbar(self, width):
        progress_bar = ctk.CTkProgressBar(
            self.window, determinate_speed=0.5, width=width
        )
        progress_bar.set(0)
        progress_bar.place(x=self.x + 170, y=self.y + 17)
        self.__dict__["progress_bar"] = progress_bar

    def step_progress_bar(self):
        self.progress_bar.step()
        self.progressbar_steps += 1
        print(self.progressbar_steps)

    def define_label(self):
        exit_message_label = ctk.CTkLabel(
            master=self.window,
            text=self.exit_message,
        )
        exit_message_label.place(x=self.x + 170, y=self.y + 5)
        self.exit_message_label = exit_message_label


class TriggerObjectBuilder:
    def __init__(self, window, x, y):
        self.root_window_widget = TriggerObject(window=window, x=x, y=y)

    def build_button(self, text, command, **kwargs):
        self.root_window_widget.define_button(text=text, command=command, **kwargs)
        return self

    def build(self):
        return self.root_window_widget


class CancelContinue:
    def __init__(self, window):
        self.window = window

    def define_frame(self, **kwargs):
        frame = ctk.CTkFrame(master=self.window, fg_color="transparent")
        frame.pack(**kwargs)
        self.__dict__["frame"] = frame

    def define_button(self, text, command, padx, width, fg_color, hover_color):
        button = ctk.CTkButton(
            master=self.frame,
            text=text,
            command=command,
            width=width,
            fg_color=fg_color,
            hover_color=hover_color,
        )
        button.pack(side=ctk.LEFT, padx=padx)


class CancelContinueBuilder:
    def __init__(self, window):
        self.cancel_continue = CancelContinue(window=window)

    def build_frame(self, **kwargs):
        self.cancel_continue.define_frame(**kwargs)
        return self

    def build_button(self, text, command, padx, width, fg_color, hover_color):
        self.cancel_continue.define_button(
            text=text,
            command=command,
            padx=padx,
            width=width,
            fg_color=fg_color,
            hover_color=hover_color,
        )
        return self

    def build(self):
        return self.cancel_continue


def add_image(window, image_path, size, x, y):
    button_image = ctk.CTkImage(Image.open(image_path), size=size)
    image_button = ctk.CTkLabel(master=window, image=button_image, text="")
    image_button.place(x=x, y=y)
