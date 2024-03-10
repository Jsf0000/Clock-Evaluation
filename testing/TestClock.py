import os
import sys
import unittest
from unittest.mock import MagicMock, patch

sys.path.append(os.path.abspath('../'))

import Settings.settings
from Services.Clock import Clock

class TestClock(unittest.TestCase):
    def setUp(self):
        # Initialize Clock instance with mock logger and messages file path
        self.clock = Clock()
        self.clock.logger = MagicMock()
        self.clock.messages = Settings.settings.ORIGINAL_MESSAGES

    # testing with original messages
    @patch('Services.Clock.read_json_file')
    def test_display_correct_message(self, mock_read_json_file):
        mock_read_json_file.return_value = Settings.settings.ORIGINAL_MESSAGES
        # Test for different elapsed time scenarios
        self.assertEqual(self.clock.display_correct_message(0), "tock")
        self.assertEqual(self.clock.display_correct_message(30), "tick")
        self.assertEqual(self.clock.display_correct_message(60), "tock")
        self.assertEqual(self.clock.display_correct_message(61), "tick")

        # Test for elapsed time > 600 (to trigger reloading messages from file)
        self.assertEqual(self.clock.display_correct_message(601), "tick")
        self.assertEqual(self.clock.display_correct_message(3600), "bong")
        self.assertEqual(self.clock.display_correct_message(3601), "tick")

    @patch('Services.Clock.read_json_file')
    def test_change_message_after_ten_minutes(self, mock_read_json_file):
        mock_read_json_file.return_value = {
            "second_message": "second",
            "minute_message": "minute",
            "hour_message": "hour"
        }
        # Test for different elapsed time scenarios
        self.assertEqual(self.clock.display_correct_message(0), "tock")
        self.assertEqual(self.clock.display_correct_message(30), "tick")
        self.assertEqual(self.clock.display_correct_message(60), "tock")
        self.assertEqual(self.clock.display_correct_message(61), "tick")

        # Test for elapsed time > 600 (to trigger reloading messages from file)
        self.assertEqual(self.clock.display_correct_message(601), "second")
        self.assertEqual(self.clock.display_correct_message(3600), "hour")
        self.assertEqual(self.clock.display_correct_message(660), "minute")
        self.assertEqual(self.clock.display_correct_message(3601), "second")

    @patch('time.time')
    def test_final_message(self, mock_time):
        # Set start_time to simulate the program starting
        start_time = 0

        # Set the return value of time.time() to current_time
        mock_time.return_value = 10801

        self.clock.start_time = 0
        self.clock.clock()

        # Ensure that the logger was called with the end message
        self.clock.logger.info.assert_called_with("Clock program has ended.")


if __name__ == '__main__':
    unittest.main()