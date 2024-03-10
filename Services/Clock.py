# Import necessary libraries
import os
import sys
import time
import logging

# Add parent directory to system path
sys.path.append(os.path.abspath('../'))

# Import CustomLogger class from Utils.Logger module,
# read_json_file function from Utils.Methods module,
# and Constants module from Utils package
from Utils.Logger import CustomLogger
from Utils.Methods import read_json_file
from Utils import Constants

# Import settings module from Settings package
from Settings import settings


# Define a class named Clock
class Clock:
    def __init__(self, log_file_path=settings.LOG_CLOCK, messages_file_path=settings.FILE_UPDATE_MESSAGES):
        # Initialize logger object with the specified log file path and log level set to DEBUG
        self.logger = CustomLogger(log_file_path, log_level=logging.DEBUG)

        # Set the file path for the messages file
        self.messages_file_path = messages_file_path

        # Initialize messages attribute with original messages from settings
        self.messages = settings.ORIGINAL_MESSAGES

        # Record the start time
        self.start_time = time.time()

    # Define a method to determine the correct message to display based on elapsed time
    def display_correct_message(self, elapsed_time):
        # Calculate hours, minutes, and seconds from elapsed time
        hours, remainder = divmod(elapsed_time, 3600)
        minutes, seconds = divmod(remainder, 60)

        # If elapsed time exceeds the limit for changing messages, update messages from the file
        if elapsed_time > settings.LIMIT_TIME_ACCEPT_CHANGE:
            self.messages = read_json_file(self.messages_file_path)

        # Determine the message to display based on seconds, minutes, and hours
        if seconds == 0:
            if minutes == 0 and hours != 0:
                return self.messages["hour_message"]
            else:
                return self.messages["minute_message"]
        else:
            return self.messages["second_message"]

    # Define a method to run the clock
    def clock(self):
        # Infinite loop to keep the clock running
        while True:
            # Get the current time and calculate elapsed time
            current_time = time.time()
            elapsed_time = int(current_time - self.start_time)

            # If elapsed time exceeds the limit for the program to end, log a warning and break the loop
            if elapsed_time > settings.LIMIT_PROGRAM_END:
                self.logger.warning(Constants.END_PROGRAM_MESSAGE)
                break

            # Determine the message to display based on elapsed time
            message_to_display = self.display_correct_message(elapsed_time)

            # Log the message
            self.logger.info(message_to_display)

            # Wait for one second before checking again
            time.sleep(1)
