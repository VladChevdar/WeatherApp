# Vlad Chevdar | CS302 | August 21
# This test aims to test User class methods

import unittest
from unittest.mock import patch
from User import User
import io
from Weather import Weather, DetailedReport, BriefReport, FunnyReport

class TestUser(unittest.TestCase):
    def setUp(self):
        self.user = User('Vlad', 'Chevdar', 'pass')
        self.location = 'Portland, Oregon'

    def test_display(self):
        with patch('sys.stdout', new_callable=io.StringIO) as fake_stdout:
            self.user.display()
            output = fake_stdout.getvalue()

        expected_output = '\nVlad, Chevdar\nUsername: vladchevdar@weather.com\nPassword: pass\n'
        self.assertEqual(output, expected_output), 'Mismatch in displaying user'

    def test_add_to_history(self):
        self.user.add_to_history(self.location)
        self.assertIn(self.location, self.user._User__report_history)
    
    def test_get_data(self):
        line = self.user.get_data()
        assert(line == 'Vlad|Chevdar|pass|'), "Wrong return"
        new_user = User('Vlad', 'Chevdar')
        line = new_user.get_data()
        assert(line == 'Vlad|Chevdar|default|'), "Wrong (password) return"
    
    def test_compare(self):
        user1 = User('0', '1')
        user2 = User('0', '2')
        assert user1.compare(user2) == -1, 'Wrong comparison return'
        assert user2.compare(user1) == 1, 'Wrong comparison return'
        assert user1.compare(user1) == 0, 'Wrong comparison return'

    def test_clear_all_searches(self):
        self.user.add_to_history(self.location)
        self.user.clear_all_searches()
        self.assertEqual([], self.user._User__report_history)

    @patch.object(Weather, 'get_weather', return_value=True)
    @patch.object(DetailedReport, 'display')
    def test_get_all_weather(self, mock_display, mock_get_weather):
        self.user.add_to_history(self.location)
        report = DetailedReport()
        self.user.get_all_weather(report)
        mock_display.assert_called_once()

    @patch.object(Weather, 'get_weather', return_value=True)
    @patch.object(DetailedReport, 'display')
    def test_get_recent_weather(self, mock_display, mock_get_weather):
        self.user.add_to_history(self.location)
        report = DetailedReport()
        self.user.get_recent_weather(report)

    def test_login(self):
        other_user = User('Vlad', 'Chevdar', 'pass')
        self.assertTrue(self.user.login(other_user)), "Can't login with existing name"
        other_user = User('Mark', 'Chevdar')
        self.assertFalse(self.user.login(other_user)), "Login with non existing name"

if __name__ == '__main__':
    unittest.main()
