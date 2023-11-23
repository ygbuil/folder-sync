import customtkinter as ctk


class DirectorySelector:
    def __init__(
        self,
        window,
        selector_type,
        button=None,
        directory_label=None,
    ):
        self.window = window
        self.selector_type = selector_type
        self.button = button
        self.directory_label = directory_label

    def add_button(self, text, width, command, x, y):
        button = ctk.CTkButton(
            master=self.window, text=text, width=width, command=command
        )
        button.place(x=x, y=y)
        self.button = button

    def add_label(self, cache, x, y):
        directory_label = ctk.CTkLabel(
            master=self.window,
            text="No origin folder selected."
            if cache[self.selector_type] == ""
            else cache[self.selector_type],
        )
        directory_label.place(x=x, y=y)
        self.directory_label = directory_label

        # frame = ctk.CTkFrame(self.window)
        # frame.place(x=x, y=y)

        # directory_label = ctk.CTkLabel(
        #     master=frame,
        #     text="No origin folder selected."
        #     if cache[self.selector_type] == ""
        #     else cache[self.selector_type]
        # )
        # self.directory_label = directory_label
        # directory_label.pack(side=ctk.LEFT, padx=0, pady=0)


class DirectorySelector:
    def __init__(
        self,
        window,
        selector_type,
        frame=None,
        button=None,
        directory_label=None,
    ):
        self.window = window
        self.selector_type = selector_type
        self.frame = frame
        self.button = button
        self.directory_label = directory_label

    def add_frame(self, x, y):
        frame = ctk.CTkFrame(self.window)
        frame.pack()
        frame.place(x=x, y=y)
        self.frame = frame

    def add_button(self, text, width, command):
        button = ctk.CTkButton(
            master=self.frame, text=text, width=width, command=command
        )
        button.pack(side=ctk.LEFT)
        self.button = button

    def add_label(self, cache):
        directory_label = ctk.CTkLabel(
            master=self.frame,
            text="No origin folder selected."
            if cache[self.selector_type] == ""
            else cache[self.selector_type],
        )
        self.directory_label = directory_label
        directory_label.pack(side=ctk.LEFT, padx=10)
