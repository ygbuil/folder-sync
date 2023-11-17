import customtkinter as ctk


class Frame:
    def __init__(
        self, frame, frame_type, selected_directory_label=None, selected_directory=None
    ):
        self.frame = frame
        self.frame_type = frame_type
        self.selected_directory_label = selected_directory_label
        self.selected_directory = selected_directory

    @classmethod
    def create_frame(cls, window, frame_type, x_frame, y_frame):
        frame = ctk.CTkFrame(window)
        frame.pack(pady=20)
        frame.place(x=x_frame, y=y_frame)

        return cls(frame=frame, frame_type=frame_type)

    def add_button(self, button_text, command, **kwargs):
        button = ctk.CTkButton(self.frame, text=button_text, command=command, **kwargs)
        button.pack(side="left", padx=0)

    def add_label(self, label_text):
        self.selected_directory_label = ctk.CTkLabel(self.frame, text=label_text)
        self.selected_directory_label.pack(side="left", padx=10)


# def update_cache()


def set_window_geometry(window):
    window_width = 600
    window_height = 600
    x_position = (window.winfo_screenwidth() - window_width) // 2
    y_position = (window.winfo_screenheight() - window_height) // 2

    window.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")
