# libraries
import os


def get_sub_paths(path):
    path_dirs = [p.relative_to(path) for p in path.glob('**/*') if p.is_dir()]
    path_files = [p.relative_to(path) for p in path.glob('**/*') if p.is_file()]

    path_dirs.sort()
    path_files.sort()

    sub_paths = {
        'dirs': path_dirs,
        'files': path_files
    }

    return sub_paths


def get_paths_paths_to_delete(master_sub_paths, clone_sub_paths, clone_root_path):
    # clone_sub_paths paths not present in master_sub_paths
    dirs_to_delete = [
        clone_root_path/x for x in clone_sub_paths['dirs'] if x not in
        master_sub_paths['dirs']
    ]
    files_to_delete = [
        clone_root_path/x for x in clone_sub_paths['files'] if x not in
        master_sub_paths['files']
    ]

    # sort in order to avoid deleting a root folder before a sub folder
    dirs_to_delete.sort(reverse=True)

    return dirs_to_delete, files_to_delete


def delete_paths(dirs_to_delete, files_to_delete):
    # delete files
    for f in files_to_delete:
        os.system(f'del /f /q {f}')
        print(f'Deleted file: {f}')

    # delete directories
    for d in dirs_to_delete:
        os.system(f'rmdir /s /q {d}')
        print(f'Deleted directory: {d}')


def get_paths_to_copy(master_sub_paths, clone_sub_paths):
    dirs_to_copy = [
        x for x in master_sub_paths['dirs'] if x not in
        clone_sub_paths['dirs']
    ]
    files_to_copy = [
        x for x in master_sub_paths['files'] if x not in
        clone_sub_paths['files']
    ]

    # sort in order to avoid creating a sub folder before a root folder
    dirs_to_copy.sort()

    return dirs_to_copy, files_to_copy


def copy_paths(master_root_path, clone_root_path, dirs_to_copy, files_to_copy):
    for d in dirs_to_copy:
        os.system(f'mkdir {clone_root_path/d}')
        print(f'Created directory: {d}')

    for f in files_to_copy:
        os.system(f'copy {master_root_path/f} {clone_root_path/f}')
        print(f'Copied file: {f}')
