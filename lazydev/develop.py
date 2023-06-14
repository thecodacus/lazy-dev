from argparse import _SubParsersAction, ArgumentParser
import os
from dotenv import load_dotenv
from .modules.developer import Developer


def setup_parser(sub_parsers: _SubParsersAction):
    # putting import inside so that code can be moved to saperate files and we dont keep the import at top of this file
    # Create the argument parser
    parser = sub_parsers.add_parser(
        name='develop', help='develop command for new project creation')

    # Add the "--requirements" argument with the "-r" shortcut
    parser.add_argument('--requirement', '-r', required=True,
                        type=str, help='The initial requirement')

    # Add the "--directory" argument with the "-d" shortcut
    parser.add_argument('--directory', '-d', default="./code",
                        type=str, help='The directory path to put generated files')

    parser.add_argument('--model', '-m', default="gpt-3.5-turbo-16k", type=str,
                        help='GPT Mode to use. options: gpt-3.5-turbo, gpt-3.5-turbo-16k, gpt-4, ')

    parser.set_defaults(func=run)

    return parser


def run(args):

    requirement = args.requirement
    directory = args.directory
    load_dotenv()
    api_key = os.environ.get('OPENAI_API_KEY')
    model = args.model
    developer = Developer(requirement=requirement,
                          root_dir=directory, openai_api_key=api_key, model=model)
    developer.develop()
