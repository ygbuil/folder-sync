from tkinter import filedialog

def choose_directory(label):
    directory_path = filedialog.askdirectory()
    if directory_path:
        # Update the label with the selected directory_path
        label.configure(text=directory_path)


def start_backup(x):
    print(x)