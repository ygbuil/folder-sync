# local libraries
import objects.objects as o


def get_sub_paths(master_root_path, clone_root_path):
    master_sub_paths = o.get_sub_paths(path=master_root_path)
    clone_sub_paths = o.get_sub_paths(path=clone_root_path)

    return master_sub_paths, clone_sub_paths


def delete_clone_files(master_sub_paths, clone_sub_paths, clone_root_path):
    dirs_to_delete, files_to_delete = o.get_paths_paths_to_delete(
        master_sub_paths=master_sub_paths, clone_sub_paths=clone_sub_paths,
        clone_root_path=clone_root_path
    )

    o.delete_paths(
        dirs_to_delete=dirs_to_delete, files_to_delete=files_to_delete
    )


def copy_from_master_to_clone(
    master_root_path, clone_root_path, master_sub_paths
):
    # get clone_sub_paths again, since deletitions may have just been performed
    clone_sub_paths = o.get_sub_paths(path=clone_root_path)

    # copy from master to clone
    dirs_to_copy, files_to_copy = o.get_paths_to_copy(
        master_sub_paths=master_sub_paths, clone_sub_paths=clone_sub_paths
    )

    o.copy_paths(
        master_root_path=master_root_path, clone_root_path=clone_root_path,
        dirs_to_copy=dirs_to_copy, files_to_copy=files_to_copy
    )


def check_if_sucessful(master_root_path, clone_root_path):
    master_sub_paths = o.get_sub_paths(path=master_root_path)
    clone_sub_paths = o.get_sub_paths(path=clone_root_path)

    if master_sub_paths == clone_sub_paths:
        print('Process sucessful! both folder are now equal.')
    else:
        print('Something went wrong. Master and clone folders are not equal.')
