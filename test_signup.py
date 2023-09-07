# Vlad Chevdar | CS302 | August 21
# This test aims to test the sign up method
import pytest
import unittest
from Main import sign_up, User, AVL
from unittest.mock import patch, MagicMock

class TestSignUp(unittest.TestCase):
    def setUp(self):
        self.tree = MagicMock()

    @patch('builtins.input', side_effect=['Vlad', 'Chevdar', 'password', 'password'])
    def test_sign_up_success(self, mock_input):
        self.tree.find.return_value = False
        with patch('Main.User') as MockUser:
            user = MockUser.return_value
            self.tree.get_user.return_value = user
            result = sign_up(self.tree)
            self.assertEqual(result, user)
            self.tree.insert.assert_called_once_with(user)

    @patch('builtins.input', side_effect=['Vlad', 'Chevdar', 'password', 'wrong_password', 'password', 'password'])
    def test_sign_up_wrong_password(self, mock_input):
        self.tree.find.return_value = False
        with patch('Main.User') as MockUser:
            user = MockUser.return_value
            self.tree.get_user.return_value = user
            result = sign_up(self.tree)
            self.assertEqual(result, user)
            self.tree.insert.assert_called_once_with(user)

    @patch('builtins.input', side_effect=['Vlad', 'Chevdar'])
    def test_sign_up_user_already_registered(self, mock_input):
        self.tree.find.return_value = True
        result = sign_up(self.tree)
        self.assertFalse(result)
        self.tree.insert.assert_not_called()

if __name__ == '__main__':
    unittest.main()