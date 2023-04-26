# libraries
from pathlib import Path

# local libraries
import objects.main_modules as m


def main(master_root_path, clone_root_path):
    # get all sub paths
    master_sub_paths, clone_sub_paths = m.get_sub_paths(
        master_root_path=master_root_path, clone_root_path=clone_root_path
    )

    # delete clone files not present in master
    m.delete_clone_files(
        master_sub_paths=master_sub_paths, clone_sub_paths=clone_sub_paths,
        clone_root_path=clone_root_path
    )

    # copy files present in master but not in clone
    m.copy_from_master_to_clone(
        master_root_path=master_root_path, clone_root_path=clone_root_path,
        master_sub_paths=master_sub_paths
    )

    # check if both folders are equal
    m.check_if_sucessful(
        master_root_path=master_root_path, clone_root_path=clone_root_path
    )


if __name__ == '__main__':
    main(
        master_root_path = Path('C:/Users/llorenc.buil/master'),
        clone_root_path = Path('C:/Users/llorenc.buil/clone')
    )
