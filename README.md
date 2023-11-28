# Easy Backup

The aim of this code is that, given two computer folders `master` and `clone`, be able to detect the differences between the two folders and set them to the same state. The `master` folder is the goal status to achieve in `clone`. The code copies missing files in `clone` (from `master`), as well as deletes files present in `clone` but missing in `master`. This is useful for large folders, where the naive solution to this problem (deleting `clone` and copy paste the entire `master`) would take a significant amount of time, and with this solution only the necessary files are copied/deleted.

## How to use it?

To use it, you just need to pass the path of your `master` and `clone` folders to the main function, found in `src/main.py`, and then run `main.py`.

*Disclaimer: Making a mistake with the path declaration could have fatal consequences and delete a lot of files in your computer. Be careful and use at your own risk.*

## Motivation of the project

I created this code to automate the backup of my computer. I keep all my important files in a "master" folder in my computer, and I periodically copy this folder into a hard drive "clone" folder. The code allows me to just copy the changes detected in "master" and not have to worry about remembering what has changed since the last backup.
