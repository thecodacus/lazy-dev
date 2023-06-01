import os
from typing import List, Dict

class Utilities:
    @staticmethod
    def touch(path):
        with open(path, 'a'):
            os.utime(path, None)

    @staticmethod
    def generate_files_recursively(files:List[Dict],cur_dir:str):
        for file in files:
            name=file['name']
            type=file['type']
            item_path=os.path.join(cur_dir,name)
            if type=="file":
                Utilities.touch(item_path)
                print(f"Created File: {item_path}")
            else:
                if not os.path.exists(item_path):
                    os.makedirs(item_path)
                    print(f"Created Directory: {item_path}")
                subfiles:List[Dict]=file['files']
                Utilities.generate_files_recursively(subfiles,item_path)

    @staticmethod
    def generate_files_and_folders(structure:dict,root_dir:str):
        root_dir_name=structure['root_dir_name']
        cur_dir=os.path.join(root_dir,root_dir_name)
        if not os.path.exists(cur_dir):
            os.makedirs(cur_dir)
            print(f"Created Directory: {cur_dir}")
        files:List[Dict]=structure['files']
        Utilities.generate_files_recursively(files=files,cur_dir=cur_dir)
