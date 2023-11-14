import customtkinter as ctk

class Frame:
    def __init__(self, frame, selected_directory_label=None):
        self.frame = frame
        self.selected_directory_label = selected_directory_label
        
    @classmethod
    def create_frame(cls, window, x_frame, y_frame):
        frame = ctk.CTkFrame(window)
        frame.pack(pady=20)
        frame.place(x=x_frame,y=y_frame)

        return cls(frame=frame)

    def add_button(self, button_text, command, **kwargs):
        button = ctk.CTkButton(
            self.frame,
            text=button_text,
            command=command,
            **kwargs
        )
        button.pack(side="left", padx=0)

    def add_label(self, label_text):
        self.selected_directory_label = ctk.CTkLabel(self.frame, text=label_text)
        self.selected_directory_label.pack(side="left", padx=10)
        

def set_window_geometry(window):
    window_width = 600
    window_height = 600
    x_position = (window.winfo_screenwidth() - window_width) // 2
    y_position = (window.winfo_screenheight() - window_height) // 2

    window.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

