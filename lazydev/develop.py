

import os
from dotenv import load_dotenv

from lazydev.modules.prompts import PrompBook
from .modules.developer import Developer



def parse_args():
    # putting import inside so that code can be moved to saperate files and we dont keep the import at top of this file
    import argparse
    # Create the argument parser
    parser = argparse.ArgumentParser(description='Lazy Dev Argguments')

    # Add the "--requirements" argument with the "-r" shortcut
    parser.add_argument('--requirement', '-r', required=True, type=str, help='The initial requirement')

    # Add the "--directory" argument with the "-d" shortcut
    parser.add_argument('--directory', '-d', default="./code", type=str, help='The directory path to put generated files')


    args = parser.parse_args()

    return args 

if __name__ == "__main__":
    # print(PrompBook.design_folder_structure("","",""))
    args=parse_args()
    requirement = args.requirement
    directory= args.directory
    load_dotenv()
    api_key = os.environ.get('OPENAI_API_KEY')
    developer =Developer(requirement=requirement,root_dir=directory,openai_api_key=api_key)
    developer.develop()