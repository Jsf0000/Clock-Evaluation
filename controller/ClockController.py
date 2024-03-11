# Import necessary libraries
import os
import sys

# Add the parent directory to the sys.path to ensure correct import
sys.path.append(os.path.abspath('../'))


# Import necessary modules
from Services.Clock import Clock  # Importing Clock class from Clock module
from Utils import Methods  # Importing Methods module from Utils package

# Create an instance of the Clock class
clock_instance = Clock()

try:
    # Call the restore_json_file method from Methods module to restore JSON file
    Methods.restore_json_file()

    # Call the clock method of the clock_instance
    clock_instance.clock()

except Exception as e:  # Catch any exceptions that occur during execution
    print("Error")
    clock_instance.logger.error(f"An error occurred: {e}")  # Log the error message if an exception occurs
