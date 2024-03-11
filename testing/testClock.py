# Import necessary libraries and modules
import os
import sys
import unittest
from unittest.mock import MagicMock, patch

# Add parent directory to system path
sys.path.append(os.path.abspath('../'))

# Import settings, Constants and Clock class
import Settings.settings
from Services.Clock import Clock
from Utils import Constants


# Define a test class inheriting from unittest.TestCase
class TestClock(unittest.TestCase):
    # Setup method to prepare for testing
    def setUp(self):
        # Initialize Clock instance with mock logger and messages file path
        self.clock = Clock()
        self.clock.logger = MagicMock()
        self.clock.messages = Settings.settings.ORIGINAL_MESSAGES

    # Test method for display_correct_message function
    # Testing with original messages
    @patch('Services.Clock.read_json_file')
    def test_display_correct_message(self, mock_read_json_file):
        # Mock read_json_file to return original messages
        mock_read_json_file.return_value = Settings.settings.ORIGINAL_MESSAGES

        # Test for different elapsed time scenarios
        self.assertEqual(self.clock.display_correct_message(0), "tick")
        self.assertEqual(self.clock.display_correct_message(30), "tick")
        self.assertEqual(self.clock.display_correct_message(60), "tock")
        self.assertEqual(self.clock.display_correct_message(61), "tick")

        # Test for elapsed time > 600 (to trigger reloading messages from file)
        self.assertEqual(self.clock.display_correct_message(601), "tick")
        self.assertEqual(self.clock.display_correct_message(3600), "bong")
        self.assertEqual(self.clock.display_correct_message(3601), "tick")

    # Test method for changing messages after ten minutes
    @patch('Services.Clock.read_json_file')
    def test_change_message_after_ten_minutes(self, mock_read_json_file):
        # Mock read_json_file to return updated messages after ten minutes
        mock_read_json_file.return_value = {
            "second_message": "second",
            "minute_message": "minute",
            "hour_message": "hour"
        }

        # Test for different elapsed time scenarios
        self.assertEqual(self.clock.display_correct_message(0), "tick")
        self.assertEqual(self.clock.display_correct_message(30), "tick")
        self.assertEqual(self.clock.display_correct_message(60), "tock")
        self.assertEqual(self.clock.display_correct_message(61), "tick")

        # Test for elapsed time > 600 (to trigger reloading messages from file)
        self.assertEqual(self.clock.display_correct_message(601), "second")
        self.assertEqual(self.clock.display_correct_message(3600), "hour")
        self.assertEqual(self.clock.display_correct_message(660), "minute")
        self.assertEqual(self.clock.display_correct_message(3601), "second")

    # Test method for final message when the clock program ends
    @patch('time.time')
    def test_final_message(self, mock_time):
        # Set start_time to simulate the program starting
        start_time = 0

        # Set the return value of time.time() to simulate program ending
        mock_time.return_value = 10801

        # Run the clock program
        self.clock.start_time = 0
        self.clock.clock()

        # Ensure that the logger was called with the end message
        self.clock.logger.warning.assert_called_with(Constants.END_PROGRAM_MESSAGE)


# Entry point for running the tests
if __name__ == '__main__':
    unittest.main()
