import os
import sys
sys.path.append(os.path.abspath('../'))
import time
import logging
from Utils.Logger import CustomLogger
from Utils.Methods import read_json_file
from Settings import settings
from Utils import Constants

class Clock:
    def __init__(self, log_file_path=settings.LOG_CLOCK, messages_file_path=settings.FILE_UPDATE_MESSAGES):
        self.logger = CustomLogger(log_file_path, log_level=logging.DEBUG)
        self.messages_file_path = messages_file_path
        self.messages = settings.ORIGINAL_MESSAGES
        self.start_time = time.time()

    def display_correct_message(self, elapsed_time):
        hours, remainder = divmod(elapsed_time, 3600)
        minutes, seconds = divmod(remainder, 60)

        if elapsed_time > settings.LIMIT_TIME_ACCEPT_CHANGE:
            self.messages = read_json_file(self.messages_file_path)

        if seconds == 0:
            if minutes == 0 and hours != 0:
                return self.messages["hour_message"]
            else:
                return self.messages["minute_message"]
        else:
            return self.messages["second_message"]

    def clock(self):

        while True:
            current_time = time.time()
            elapsed_time = int(current_time - self.start_time)

            if elapsed_time > settings.LIMIT_PROGRAM_END:  # 3 hours = 10800 seconds
                self.logger.info(Constants.END_PROGRAM_MESSAGE)
                break
            message_to_display = self.display_correct_message(elapsed_time)
            self.logger.info(message_to_display)
            time.sleep(1)  # Wait for a second
