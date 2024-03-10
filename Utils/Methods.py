# Import necessary libraries and modules
import json
import os
import sys

# Add parent directory to system path to enable imports
sys.path.append(os.path.abspath('../'))

# Import settings module from Settings package
from Settings import settings

# Function to read JSON data from a file
def read_json_file(filename):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        exit()

# Function to write JSON data to a file
def write_json_file(filename, data):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)

# Function to restore the original JSON file
def restore_json_file():
    with open(settings.FILE_UPDATE_MESSAGES, 'w') as file:
        json.dump(settings.ORIGINAL_MESSAGES, file, indent=4)
