import json
import sys
import unittest
import os
from unittest.mock import patch

sys.path.append(os.path.abspath('../'))

from Services.ChangeMessage import UpdateMessages

class TestUpdateMessages(unittest.TestCase):
    def setUp(self):
        self.file_name = "test_messages.json"
        self.test_messages = {
            "second_message": "Test second message",
            "minute_message": "Test minute message",
            "hour_message": "Test hour message"
        }
        with open(self.file_name, "w") as file:
            json.dump(self.test_messages, file)

    def tearDown(self):
        os.remove(self.file_name)

    @patch("Services.ChangeMessage.read_json_file")
    @patch("Services.ChangeMessage.write_json_file")
    @patch("Services.ChangeMessage.CustomLogger")
    def test_update_messages(self, mock_logger, mock_write_json_file, mock_read_json_file):
        second_message = "Updated second message"
        minute_message = "Updated minute message"
        hour_message = "Updated hour message"

        # Mocking read_json_file to return the test messages
        mock_read_json_file.return_value = self.test_messages

        # Creating an instance of UpdateMessages
        update_messages = UpdateMessages(self.file_name)

        # Calling update_messages method
        update_messages.update_messages(second_message, minute_message, hour_message)

        # Asserting that logger.info was called with the correct message
        mock_logger.return_value.info.assert_called_with(json.dumps(self.test_messages, indent=4))

        # Asserting that write_json_file was called with the updated messages
        mock_write_json_file.assert_called_with(self.file_name, {
            "second_message": second_message,
            "minute_message": minute_message,
            "hour_message": hour_message
        })

if __name__ == "__main__":
    unittest.main()
