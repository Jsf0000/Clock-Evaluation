import logging

class CustomLogger:
    # Define color codes
    COLOR_CODES = {
        'HEADER': '\033[95m',
        'OKBLUE': '\033[94m',
        'OKGREEN': '\033[92m',
        'WARNING': '\033[93m',
        'FAIL': '\033[91m',
        'ENDC': '\033[0m',
        'BOLD': '\033[1m',
        'UNDERLINE': '\033[4m'
    }

    def __init__(self, log_file_name, log_level=logging.INFO):
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(log_level)

        # Create a file handler and set the log level
        file_handler = logging.FileHandler(log_file_name)
        file_handler.setLevel(log_level)

        # Create a console handler and set the log level
        console_handler = logging.StreamHandler()
        console_handler.setLevel(log_level)

        # Create a formatter
        formatter = logging.Formatter('%(asctime)s- %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

        # Set the formatter for both handlers
        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)

        # Add the handlers to the logger
        self.logger.addHandler(file_handler)
        self.logger.addHandler(console_handler)

    def color_message(self, message, color):
        return f"{self.COLOR_CODES[color]}  {message}  {self.COLOR_CODES['ENDC']}"

    def info(self, message):
        self.logger.info(self.color_message(message, 'OKGREEN'))

    def warning(self, message):
        self.logger.warning(self.color_message(message, 'WARNING'))

    def error(self, message):
        self.logger.error(self.color_message(message, 'FAIL'))

    def exception(self, message):
        self.logger.exception(self.color_message(message, 'FAIL'))
