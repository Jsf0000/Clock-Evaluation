# Function to read JSON from a file
import json
import os
import sys

sys.path.append(os.path.abspath('../'))

from Settings import settings

def read_json_file(filename):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        exit()

# Function to write JSON to a file
def write_json_file(filename, data):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)

def restore_json_file():
    with open(settings.FILE_UPDATE_MESSAGES, 'w') as file:
        json.dump(settings.ORIGINAL_MESSAGES, file, indent=4)