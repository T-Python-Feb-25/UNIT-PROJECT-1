import unittest
from unittest.mock import patch, mock_open
import json
import hashlib
from home import User, custom_getpass, register, login, password_reset, update_logins_file, load_users

class TestHomeFunctions(unittest.TestCase):


    @patch('builtins.input', side_effect=['testuser', 'password'])
    @patch('home.custom_getpass', return_value='password')
    def test_login_success(self, mock_getpass, mock_input):
        users = {'testuser': User('testuser', hashlib.sha256('password'.encode()).hexdigest(), is_hashed=True)}
        users, logged_in_user = login(users)
        self.assertIsNotNone(logged_in_user)
        self.assertEqual(logged_in_user.username, 'testuser')

    @patch('builtins.input', side_effect=['testuser', 'wrongpassword'])
    @patch('home.custom_getpass', return_value='wrongpassword')
    def test_login_failure(self, mock_getpass, mock_input):
        users = {'testuser': User('testuser', hashlib.sha256('password'.encode()).hexdigest(), is_hashed=True)}
        users, logged_in_user = login(users)
        self.assertIsNone(logged_in_user)

    @patch('builtins.input', side_effect=['testuser', 'newpassword'])
    @patch('home.custom_getpass', return_value='newpassword')
    @patch('home.update_logins_file')
    def test_password_reset(self, mock_update_logins_file, mock_getpass, mock_input):
        users = {'testuser': User('testuser', hashlib.sha256('password'.encode()).hexdigest(), is_hashed=True)}
        password_reset(users, 'testuser')
        self.assertEqual(users['testuser'].password, hashlib.sha256('newpassword'.encode()).hexdigest())
        mock_update_logins_file.assert_called_once_with(users)

    

    
if __name__ == '__main__':
    unittest.main()
