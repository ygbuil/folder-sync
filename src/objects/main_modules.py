# local libraries
import objects.objects as o


def get_subpaths(master_root_path, clone_root_path):
    master_sub_paths = o.get_all_paths(path=master_root_path)
    clone_sub_paths = o.get_all_paths(path=clone_root_path)

    return master_sub_paths, clone_sub_paths


def delete_clone_files(master_sub_paths, clone_sub_paths, clone_root_path):
    paths_to_delete = o.get_paths_paths_to_delete(
        master_sub_paths=master_sub_paths, clone_sub_paths=clone_sub_paths,
        clone_root_path=clone_root_path
    )
    o.delete_paths(paths_to_delete=paths_to_delete)


def copy_from_master_to_clone(
    master_root_path, clone_root_path, master_sub_paths
):
    # get clone_sub_paths again, since deletitions may have just been performed
    clone_sub_paths = o.get_all_paths(path=clone_root_path)

    # copy from master to clone
    folders_to_create, paths_to_copy = o.get_paths_to_copy(
        master_sub_paths=master_sub_paths, clone_sub_paths=clone_sub_paths
    )
    o.copy_paths(
        master_root_path=master_root_path, clone_root_path=clone_root_path,
        paths_to_copy=paths_to_copy, folders_to_create=folders_to_create
    )


def check_if_both_folders_are_equal(master_root_path, clone_root_path):
    master_sub_paths = o.get_all_paths(path=master_root_path)
    clone_sub_paths = o.get_all_paths(path=clone_root_path)

    if master_sub_paths == clone_sub_paths:
        print('Process sucessful! both folder are now equal.')
