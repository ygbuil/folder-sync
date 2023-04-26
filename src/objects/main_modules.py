# local libraries
import objects.objects as o


def get_sub_paths(master_root_path, clone_root_path):
    '''
    Get all the sub paths inside path.

    Parameters
    ----------
    master_root_path : pathlib object
        Root path of master folder.
    clone_root_path : pathlib object
        Root path of clone folder.

    Returns
    -------
    master_sub_paths : dict
        Dictionary containing sub paths for master.
    clone_sub_paths : dict
        Dictionary containing sub paths for clone.

    '''

    master_sub_paths = o.get_sub_paths(path=master_root_path)
    clone_sub_paths = o.get_sub_paths(path=clone_root_path)

    return master_sub_paths, clone_sub_paths


def delete_clone_files(
    master_sub_paths, clone_sub_paths, clone_root_path, operating_system
):
    '''
    Delete files present in clone but missing in master.

    Parameters
    ----------
    master_sub_paths : dict
        Dictionary containing sub paths for master.
    clone_sub_paths : dict
        Dictionary containing sub paths for clone.
    clone_root_path : pathlib object
        Root path of clone folder.
    operating_system : str
        Type of OS. Options: 'windows' or 'mac'.

    Returns
    -------
    None.

    '''

    paths_to_delete = o.get_paths_paths_to_delete(
        master_sub_paths=master_sub_paths, clone_sub_paths=clone_sub_paths,
        clone_root_path=clone_root_path
    )

    o.delete_paths(
        paths_to_delete=paths_to_delete, operating_system=operating_system
    )


def copy_from_master_to_clone(
    master_root_path, clone_root_path, master_sub_paths
):
    '''
    Copy files present in master but missing in clone (from master to clone).

    Parameters
    ----------
    master_root_path : TYPE
        DESCRIPTION.
    clone_root_path : TYPE
        DESCRIPTION.
    master_sub_paths : TYPE
        DESCRIPTION.

    Returns
    -------
    None.

    '''

    # get clone_sub_paths again, since deletitions may have just been performed
    clone_sub_paths = o.get_sub_paths(path=clone_root_path)

    # copy from master to clone
    paths_to_copy = o.get_paths_to_copy(
        master_sub_paths=master_sub_paths, clone_sub_paths=clone_sub_paths
    )

    o.copy_paths(
        master_root_path=master_root_path, clone_root_path=clone_root_path,
        paths_to_copy=paths_to_copy
    )


def test_if_sucessful(master_root_path, clone_root_path):
    '''
    Checks if the process went successfully, that is, master and clone folders
    are equal after all the change.

    Parameters
    ----------
    master_root_path : pathlib object
        Root path of master folder.
    clone_root_path : pathlib object
        Root path of clone folder.

    Returns
    -------
    None.

    '''

    master_sub_paths = o.get_sub_paths(path=master_root_path)
    clone_sub_paths = o.get_sub_paths(path=clone_root_path)

    if master_sub_paths == clone_sub_paths:
        print('Process successful! both folder are now equal.')
    else:
        print('Something went wrong. Master and clone folders are not equal.')
