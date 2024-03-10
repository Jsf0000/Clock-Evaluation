# Import necessary libraries
import argparse
import os
import sys

# Add the parent directory to the sys.path to ensure correct import
sys.path.append(os.path.abspath('../'))

# Import Custom Module
from Utils.Logger import CustomLogger
from Settings import settings

# Define logger to use
logger = CustomLogger(settings.LOG_CONTROLLER_CHANGE_MESSAGE)

# Import necessary modules
from Services.ChangeMessage import UpdateMessages  # Importing UpdateMessages class from ChangeMessage module
from Settings import settings  # Importing settings module from Settings package

# Constants
FILE_NAME = settings.FILE_UPDATE_MESSAGES  # FILE_NAME stores the path to the file containing update messages

# Parse command-line arguments
parser = argparse.ArgumentParser(description="Update messages in a JSON object.")  # Create ArgumentParser object
parser.add_argument("--second_message", help="Message for seconds", type=str)  # Add argument for second_message
parser.add_argument("--minute_message", help="Message for minutes", type=str)  # Add argument for minute_message
parser.add_argument("--hour_message", help="Message for hours", type=str)  # Add argument for hour_message
args = parser.parse_args()  # Parse the arguments provided by the user

try:
    # Create an instance of the UpdateMessages class
    updater = UpdateMessages()

    # Call the update_messages method of the updater instance with provided arguments
    updater.update_messages(second_message=args.second_message, minute_message=args.minute_message,
                            hour_message=args.hour_message)

except Exception as e:  # Catch any exceptions that occur during execution
    logger.error(f"An error occurred: {e}")  # Log the error message if an exception occurs
