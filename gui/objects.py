import customtkinter as ctk


class Frame:
    def __init__(
        self,
        frame,
        frame_name,
        selected_directory_label=None,
        button=None,
    ):
        self.frame = frame
        self.frame_name = frame_name
        self.selected_directory_label = selected_directory_label
        self.button = button

    @classmethod
    def create_frame(cls, root, frame_name, x_frame, y_frame):
        frame = ctk.CTkFrame(root)
        frame.pack()
        frame.place(x=x_frame, y=y_frame)

        return cls(frame=frame, frame_name=frame_name)

    def add_button(self, button_text, command, **kwargs):
        button = ctk.CTkButton(self.frame, text=button_text, command=command, **kwargs)
        button.pack(side="left")
        self.button = button

    def add_label(self, label_text):
        self.selected_directory_label = ctk.CTkLabel(self.frame, text=label_text)
        self.selected_directory_label.pack(side="left", padx=10)
