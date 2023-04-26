# libraries
import os


def get_all_paths(path):
    paths = []
    for root, dirs, files in os.walk(path):
        for name in files + dirs:
            paths.append(os.path.join(root, name))

    paths = [x.replace(path, '') for x in paths]
    paths.sort()

    return paths


# def get_paths_paths_to_delete(master_sub_paths, clone_root_path):
#     # clone_sub_paths paths not present in master_sub_paths
#     paths_to_delete = [clone_root_path + x for x in clone_sub_paths if x not in master_sub_paths]

#     # remove redundant paths.
#     # E.g.: ['folder\', 'folder\a.txt', 'folder\b.txt'] -> ['folder\']
#     paths_to_delete_copy = paths_to_delete.copy()
#     for path in paths_to_delete_copy:

#         i = 0
#         stopper = len(paths_to_delete)
#         while i < stopper:
#             path_delete = paths_to_delete[i]
#             if path != path_delete and path in path_delete:
#                 paths_to_delete.remove(path_delete)
#                 stopper = len(paths_to_delete)
#             else:
#                 i += 1

#     return paths_to_delete


def get_paths_paths_to_delete(master_sub_paths, clone_sub_paths, clone_root_path):
    # clone_sub_paths paths not present in master_sub_paths
    paths_to_delete = [
        clone_root_path + x for x in clone_sub_paths if x not in master_sub_paths
    ]
    paths_to_delete.sort(reverse=True)

    return paths_to_delete


def delete_paths(paths_to_delete):
    for path in paths_to_delete:
        # if path is file
        if '.' in path.split('\\')[-1]:
            os.system(f'del /f /q {path}')
            print(f'Deleted: {path}')
        # if path is folder
        else:
            os.system(f'rmdir /s /q {path}')
            print(f'Deleted: {path}')


def get_paths_to_copy(master_sub_paths, clone_sub_paths):
    paths_to_copy = [x for x in master_sub_paths if x not in clone_sub_paths]

    folders_to_create = []
    for path in paths_to_copy:
        # if path is folder
        if '.' not in path.split('\\')[-1]:
            folders_to_create.append(path)
            paths_to_copy.remove(path)

    # sort in order to avoid creating a subfolder before a root folder
    folders_to_create.sort()

    return folders_to_create, paths_to_copy

def copy_paths(master_root_path, clone_root_path, paths_to_copy, folders_to_create):
    for folder in folders_to_create:
        os.system(f'mkdir {clone_root_path + folder}')
        print(f'Created folder: {folder}')

    for file in paths_to_copy:
        os.system(f'copy {master_root_path + file} {clone_root_path + file}')
        print(f'Copied file: {file}')
