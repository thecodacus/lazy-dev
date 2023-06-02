import argparse
from . import develop

# Create the top-level parser
parser = argparse.ArgumentParser()

# Create subparsers for the different subcommands
subparsers = parser.add_subparsers(title='Subcommands', dest='subcommand')

# Import and execute the subcommand modules
develop.setup_parser(subparsers)

# Parse the command-line arguments
args = parser.parse_args()

# Execute the appropriate subcommand
def run():
    if hasattr(args, 'func'):
        args.func(args)








