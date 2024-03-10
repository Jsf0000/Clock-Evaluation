import json
import logging
import os
import sys

sys.path.append(os.path.abspath('../'))
from Utils.Logger import CustomLogger
from Utils.Methods import read_json_file, write_json_file
from Utils import Constants
from Settings import settings


class UpdateMessages:
    def __init__(self, file_name=settings.FILE_UPDATE_MESSAGES):
        self.file_name = file_name
        self.logger = CustomLogger(settings.LOG_CHANGE_MESSAGE, log_level=logging.DEBUG)

    def update_messages(self, second_message=None, minute_message=None, hour_message=None):

        # JSON object to update
        json_object = read_json_file(self.file_name)

        # Update JSON object with provided command-line arguments
        if second_message:
            json_object["second_message"] = second_message
        if minute_message:
            json_object["minute_message"] = minute_message
        if hour_message:
            json_object["hour_message"] = hour_message

        # Convert the updated JSON object to a string and print it
        self.logger.info(Constants.UPDATED_MESSAGES)
        self.logger.info(json.dumps(json_object, indent=4))

        write_json_file(self.file_name, json_object)
