# Import necessary libraries
import os
import sys

# Add the parent directory to the sys.path to ensure correct import
sys.path.append(os.path.abspath('../'))

# Import Custom Module
from Utils.Logger import CustomLogger
from Settings import settings

# define logger to use
logger = CustomLogger(settings.LOG_CONTROLLER_CHANGE_MESSAGE)


# Import necessary modules
from Services.Clock import Clock  # Importing Clock class from Clock module
from Utils import Methods  # Importing Methods module from Utils package

try:
    # Call the restore_json_file method from Methods module to restore JSON file
    Methods.restore_json_file()

    # Create an instance of the Clock class
    clock_instance = Clock()

    # Call the clock method of the clock_instance
    clock_instance.clock()

except Exception as e:  # Catch any exceptions that occur during execution
    logger.error(f"An error occurred: {e}")  # Log the error message if an exception occurs
