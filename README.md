# Easy Backup

The aim of this app is, given two folders `origin` and `destination`, be able to detect the differences between the two folders and set `destination` to the same state as `origin`. It has been created with the intention of backing up local folders into hardrives in an efficient way. The code only copies and deletes the newly added or deleted files in `origin`, making it a better option than having to manually figure out the changes yourself or having to overwrite the entire `destination` folder.

## Usage

To use the project, follow these steps:

1. Clone the project.

2. Open the project and run `uv sync` to install dependencies in a virtual environment.

3. Inside `.vscode/tasks.json`, provide your inputs and run the VSCode command `Tasks: Run Task -> Sync`.