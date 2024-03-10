import argparse
import os
import sys

sys.path.append(os.path.abspath('../'))

from Services.ChangeMessage import UpdateMessages
from Settings import settings


FILE_NAME = settings.FILE_UPDATE_MESSAGES
# Parse command-line arguments
parser = argparse.ArgumentParser(description="Update messages in a JSON object.")
parser.add_argument("--second_message", help="Message for seconds", type=str)
parser.add_argument("--minute_message", help="Message for minutes", type=str)
parser.add_argument("--hour_message", help="Message for hours", type=str)
args = parser.parse_args()

updater = UpdateMessages()
updater.update_messages(second_message=args.second_message, minute_message=args.minute_message,
                        hour_message=args.hour_message)