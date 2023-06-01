import subprocess

def read_config():
    import json
    # Opening JSON file
    f = open('./config.json')
    
    # returns JSON object as 
    # a dictionary
    data = json.load(f)
    
    f.close()
    return data


def parse_args():
    # putting import inside so that code can be moved to saperate files and we dont keep the import at top of this file
    import argparse
    # Create the argument parser
    parser = argparse.ArgumentParser(description='Lazy Dev Argguments')

    # Add the "--task" argument with the "-t" shortcut
    parser.add_argument('--run', '-r', type=str, help='The script to run')

    args = parser.parse_args()

    return args 


def execute_config_script(script_name:str,config:dict):
    scripts:dict=config['scripts']
    command:str=scripts[script_name]

    # Execute the command
    result = subprocess.run(command, shell=True, capture_output=True, text=True)

    # Check the return code
    if result.returncode == 0:
        # Command was successful
        print("Command executed successfully.")
        # Print the command output
        print("Command output:")
        print(result.stdout)
    else:
        # Command failed
        print("Command failed with return code:", result.returncode)
        # Print the error message
        print("Error message:")
        print(result.stderr)


if __name__ == "__main__":
    args=parse_args()
    command = args.run
    config=read_config()
    execute_config_script(command,config)


