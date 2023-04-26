# libraries
import os


def get_sub_paths(path):
    '''
    Get all the sub paths inside path.

    Parameters
    ----------
    path : pathlib object
        path.

    Returns
    -------
    sub_paths : dict
        Dictionary containing sub paths for both directories and files in path.

    '''

    path_dirs = [
        p.relative_to(path) for p in path.glob('**/*') if p.is_dir()
    ]
    path_files = [
        p.relative_to(path) for p in path.glob('**/*') if p.is_file()
    ]

    path_dirs.sort()
    path_files.sort()

    sub_paths = {
        'dirs': path_dirs,
        'files': path_files
    }

    return sub_paths


def get_paths_paths_to_delete(
    master_sub_paths, clone_sub_paths, clone_root_path
):
    '''
    Gets directories and files present in clone but missing in master, since
    they will need to be deleted from clone.

    Parameters
    ----------
    master_sub_paths : list
        Sub paths of master.
    clone_sub_paths : list
        Sub paths of clone.
    clone_root_path : pathlib object
        Root path of clone folder.

    Returns
    -------
    paths_to_delete : dict
        Dictionary containing the directories and files to delete.

    '''

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

    paths_to_delete = {'dirs': dirs_to_delete, 'files': files_to_delete}

    return paths_to_delete


def delete_paths(paths_to_delete, operating_system):
    '''
    Executes commands to delete the paths_to_delete.

    Parameters
    ----------
    paths_to_delete : dict
        Dictionary containing the directories and files to delete.
    operating_system : str
        Type of OS. Options: 'windows' or 'mac'.

    Returns
    -------
    None.

    '''

    # delete files
    for f in paths_to_delete['files']:
        if operating_system == 'windows':
            os.system(f'del {f}')
        elif operating_system == 'mac':
            os.system(f'rm {f}')
        print(f'Deleted file: {f}')

    # delete directories
    for d in paths_to_delete['dirs']:
        if operating_system == 'windows':
            os.system(f'rmdir /q {d}')
        elif operating_system == 'mac':
            os.system(f'rmdir {d}')
        print(f'Deleted directory: {d}')


def get_paths_to_copy(master_sub_paths, clone_sub_paths):
    '''
    Gets directories and files present in master but missing in clone, since
    they will need to be copied from master to clone.

    Parameters
    ----------
    master_sub_paths : list
        Sub paths of master.
    clone_sub_paths : list
        Sub paths of clone.

    Returns
    -------
    paths_to_copy : dict
        Dictionary containing the directories and files to delete.

    '''

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

    paths_to_copy = {'dirs': dirs_to_copy, 'files': files_to_copy}

    return paths_to_copy


def copy_paths(
    master_root_path, clone_root_path, paths_to_copy, operating_system
):
    '''
    Executes commands to copy the paths_to_copy.

    Parameters
    ----------
    master_root_path : pathlib object
        Root path of master folder.
    clone_root_path : pathlib object
        Root path of clone folder.
    paths_to_copy : dict
        Dictionary containing the directories and files to delete.
    operating_system : str
        Type of OS. Options: 'windows' or 'mac'.

    Returns
    -------
    None.

    '''

    for d in paths_to_copy['dirs']:
        os.system(f'mkdir {clone_root_path/d}')
        print(f'Created directory: {d}')

    for f in paths_to_copy['files']:
        if operating_system == 'windows':
            os.system(f'copy {master_root_path/f} {clone_root_path/f}')
        elif operating_system == 'mac':
            os.system(f'cp {master_root_path/f} {clone_root_path/f}')
        print(f'Copied file: {f}')
