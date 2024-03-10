# Import necessary libraries
import json
import logging
import os
import sys

# Add parent directory to system path
sys.path.append(os.path.abspath('../'))

# Import CustomLogger class from Utils.Logger module
from Utils.Logger import CustomLogger

# Import read_json_file and write_json_file functions from Utils.Methods module
from Utils.Methods import read_json_file, write_json_file

# Import Constants module from Utils package and settings module from Settings package
from Utils import Constants
from Settings import settings


class UpdateMessages:
    def __init__(self, file_name=settings.FILE_UPDATE_MESSAGES):
        # Initialize file_name attribute with default value from settings or the one provided
        self.file_name = file_name

        # Initialize logger object using CustomLogger class with log_level set to DEBUG
        self.logger = CustomLogger(settings.LOG_CHANGE_MESSAGE, log_level=logging.DEBUG)

    # Define a method named update_messages
    def update_messages(self, second_message=None, minute_message=None, hour_message=None):
        # Read JSON object from the file
        json_object = read_json_file(self.file_name)

        # Update JSON object with provided messages if provided
        if second_message:
            json_object["second_message"] = second_message
        if minute_message:
            json_object["minute_message"] = minute_message
        if hour_message:
            json_object["hour_message"] = hour_message

        # Log information about the updated messages
        self.logger.info(Constants.UPDATED_MESSAGES)
        self.logger.info(json.dumps(json_object, indent=4))  # Convert JSON object to string with indentation

        # Write the updated JSON object back to the file
        write_json_file(self.file_name, json_object)

