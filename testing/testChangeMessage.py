# Import necessary libraries and modules
import json
import sys
import unittest
import os
from unittest.mock import patch

# Add parent directory to system path
sys.path.append(os.path.abspath('../'))

# Import the class to be tested
from Services.ChangeMessage import UpdateMessages


# Define a test class inheriting from unittest.TestCase
class TestUpdateMessages(unittest.TestCase):
    # Setup method to prepare for testing
    def setUp(self):
        # Define the file name for test messages
        self.file_name = "test_messages.json"

        # Define test messages
        self.test_messages = {
            "second_message": "Test second message",
            "minute_message": "Test minute message",
            "hour_message": "Test hour message"
        }

        # Write test messages to a JSON file
        with open(self.file_name, "w") as file:
            json.dump(self.test_messages, file)

    # Teardown method to clean up after testing
    def tearDown(self):
        # Remove the test JSON file
        os.remove(self.file_name)

    # Test method for update_messages function
    @patch("Services.ChangeMessage.read_json_file")
    @patch("Services.ChangeMessage.write_json_file")
    @patch("Services.ChangeMessage.CustomLogger")
    def test_update_messages(self, mock_logger, mock_write_json_file, mock_read_json_file):
        # Define updated messages
        second_message = "Updated second message"
        minute_message = "Updated minute message"
        hour_message = "Updated hour message"

        # Mocking read_json_file to return the test messages
        mock_read_json_file.return_value = self.test_messages

        # Creating an instance of UpdateMessages with the test file name
        update_messages = UpdateMessages(self.file_name)

        # Calling update_messages method with updated messages
        update_messages.update_messages(second_message, minute_message, hour_message)

        # Asserting that logger.info was called with the correct message
        mock_logger.return_value.info.assert_called_with(json.dumps(self.test_messages, indent=4))

        # Asserting that write_json_file was called with the updated messages
        mock_write_json_file.assert_called_with(self.file_name, {
            "second_message": second_message,
            "minute_message": minute_message,
            "hour_message": hour_message
        })


# Entry point for running the tests
if __name__ == "__main__":
    unittest.main()
