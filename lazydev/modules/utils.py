import os
from typing import List, Dict


class Utilities:
    @staticmethod
    def touch(path):
        with open(path, 'a'):
            os.utime(path, None)

    @staticmethod
    def generate_files_recursively(files: List[Dict], cur_dir: str):
        file_paths = []
        for file in files:
            name = file['name']
            type = file['type']
            item_path = os.path.join(cur_dir, name)
            if type == "file":
                Utilities.touch(item_path)
                file_paths.append(item_path)
                print(f"Created File: {item_path}")
            else:
                if not os.path.exists(item_path):
                    os.makedirs(item_path)
                    print(f"Created Directory: {item_path}")
                if 'files' in file:
                    subfiles: List[Dict] = file['files']
                    sub_file_paths = Utilities.generate_files_recursively(
                        subfiles, item_path)
                    file_paths = file_paths+sub_file_paths
        return file_paths

    @staticmethod
    def generate_files_and_folders(structure: dict, root_dir: str):
        root_dir_name = structure['root_dir_name']
        cur_dir = os.path.join(root_dir, root_dir_name)
        root_dir_path = cur_dir
        if not os.path.exists(cur_dir):
            os.makedirs(cur_dir)
            print(f"Created Directory: {cur_dir}")
        files: List[Dict] = structure['files']
        file_paths = Utilities.generate_files_recursively(
            files=files, cur_dir=cur_dir)
        return root_dir_path, file_paths

    def write_to_file(content: str, file_path: str):
        # Open the file in write mode
        with open(file_path, "w") as file:
            # Write the content to the file
            file.write(content)
