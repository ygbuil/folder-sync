import customtkinter as ctk
import constants as ct


def set_window_geometry(app):
    x_position = (app.winfo_screenwidth() - ct.WINDOW_WIDTH) // 2
    y_position = (app.winfo_screenheight() - ct.WINDOW_HEIGHT) // 2

    app.geometry(f"{ct.WINDOW_WIDTH}x{ct.WINDOW_HEIGHT}+{x_position}+{y_position}")


class Frame:
    def __init__(
        self,
        frame,
        frame_type,
        selected_directory_label=None,
        selected_directory=None,
        button=None,
    ):
        self.frame = frame
        self.frame_type = frame_type
        self.selected_directory_label = selected_directory_label
        self.selected_directory = selected_directory
        self.button = button

    @classmethod
    def create_frame(cls, app, frame_type, x_frame, y_frame):
        frame = ctk.CTkFrame(app)
        frame.pack(pady=20)
        frame.place(x=x_frame, y=y_frame)

        return cls(frame=frame, frame_type=frame_type)

    def add_button(self, button_text, command, **kwargs):
        button = ctk.CTkButton(self.frame, text=button_text, command=command, **kwargs)
        button.pack(side="left", padx=0)
        self.button = button

    def add_label(self, label_text):
        self.selected_directory_label = ctk.CTkLabel(self.frame, text=label_text)
        self.selected_directory_label.pack(side="left", padx=10)
