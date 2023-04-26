import os

master_path = 'C:\\Users\\llorenc.buil\\master'
clone_path = 'C:\\Users\\llorenc.buil\\clone'


def get_all_paths(path):
    paths = []
    for root, dirs, files in os.walk(path):
        for name in files + dirs:
            paths.append(os.path.join(root, name))

    paths = [x.replace(path, '') for x in paths]
    paths.sort()

    return paths


def get_paths_paths_to_delete(master_paths, clone_path):
    # clone_paths paths not present in master_paths
    paths_to_delete = [clone_path + x for x in clone_paths if x not in master_paths]

    # remove redundant paths.
    # E.g.: ['folder\', 'folder\a.txt', 'folder\b.txt'] -> ['folder\']
    paths_to_delete_copy = paths_to_delete.copy()
    for path in paths_to_delete_copy:

        i = 0
        stopper = len(paths_to_delete)
        while i < stopper:
            path_delete = paths_to_delete[i]
            if path != path_delete and path in path_delete:
                paths_to_delete.remove(path_delete)
                stopper = len(paths_to_delete)
            else:
                i += 1

    return paths_to_delete


def get_paths_paths_to_delete_v2(master_paths, clone_path):
    # clone_paths paths not present in master_paths
    paths_to_delete = [
        clone_path + x for x in clone_paths if x not in master_paths
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


def get_paths_to_copy(master_paths, clone_paths):
    paths_to_copy = [x for x in master_paths if x not in clone_paths]

    folders_to_create = []
    for path in paths_to_copy:
        # if path is folder
        if '.' not in path.split('\\')[-1]:
            folders_to_create.append(path)
            paths_to_copy.remove(path)

    # sort in order to avoid creating a subfolder before a root folder
    folders_to_create.sort()

    return folders_to_create, paths_to_copy

def copy_paths(master_path, clone_path, paths_to_copy, folders_to_create):
    for folder in folders_to_create:
        os.system(f'mkdir {clone_path+folder}')
        print(f'Created folder: {folder}')

    for file in paths_to_copy:
        os.system(f'copy {master_path+file} {clone_path+file}')
        print(f'Copied file: {file}')


def check_if_both_folders_are_equal():
    master_paths = get_all_paths(path=master_path)
    clone_paths = get_all_paths(path=clone_path)

    if master_paths == clone_paths:
        print('Process sucessful! both folder are now equal.')





# get all paths in both the master and clone folder
master_paths = get_all_paths(path=master_path)
clone_paths = get_all_paths(path=clone_path)


# delete clone files not present in master
paths_to_delete = get_paths_paths_to_delete_v2(
    master_paths=master_paths, clone_path=clone_path
)
delete_paths(paths_to_delete=paths_to_delete)


# get all paths in the clone folder, since it has been modified
clone_paths = get_all_paths(path=clone_path)
folders_to_create, paths_to_copy = get_paths_to_copy(
    master_paths=master_paths, clone_paths=clone_paths
)
copy_paths(master_path, clone_path, paths_to_copy, folders_to_create)


check_if_both_folders_are_equal()
