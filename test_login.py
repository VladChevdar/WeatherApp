# Vlad Chevdar | CS302 | August 21
# This test aims to test the login method
import pytest
import unittest
from Main import log_in, User, AVL
from unittest.mock import patch, MagicMock

class TestLogIn(unittest.TestCase):

    def setUp(self):
        self.tree = MagicMock()

    @patch('builtins.input', side_effect=['Vlad', 'Chevdar', 'password'])
    def test_log_in_success(self, mock_input):
        with patch('Main.User') as MockUser:
            user = MockUser.return_value
            self.tree.find.return_value = True
            self.tree.verify.return_value = True
            self.tree.get_user.return_value = user
            result = log_in(self.tree)
            self.assertEqual(result, user)

    @patch('builtins.input', side_effect=['Vlad', 'Chevdar', 'wrong_password', 'wrong_password', 'password'])
    def test_log_in_wrong_password(self, mock_input):
        with patch('Main.User') as MockUser:
            user = MockUser.return_value
            self.tree.find.return_value = True
            self.tree.verify.side_effect = [False, False, True]
            self.tree.get_user.return_value = user
            result = log_in(self.tree)
            self.assertEqual(result, user)

    @patch('builtins.input', side_effect=['Vlad', 'Chevdar', 'wrong_password', 'wrong_password', 'wrong_password'])
    def test_log_in_exhausted_attempts(self, mock_input):
        with patch('Main.User') as MockUser:
            user = MockUser.return_value
            self.tree.find.return_value = True
            self.tree.verify.return_value = False
            result = log_in(self.tree)
            self.assertFalse(result)

    @patch('builtins.input', side_effect=['John', 'Smith'])
    def test_log_in_no_account(self, mock_input):
        with patch('Main.User') as MockUser:
            user = MockUser.return_value
            self.tree.find.return_value = False
            result = log_in(self.tree)
            self.assertFalse(result)
