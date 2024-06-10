#!/usr/bin/python3
import unittest
from models.user import create_user

class TestUser(unittest.TestCase):
    """Test cases for the create_user function in the User model."""

    def test_create_user_success(self):
        """Test creating a user with valid input."""
        user_data = {
            'username': 'testuser',
            'password': 'testpass',
            'email': 'test@example.com'
        }
        user = create_user(**user_data)
        self.assertEqual(user.username, 'testuser')
        self.assertEqual(user.password, 'testpass')
        self.assertEqual(user.email, 'test@example.com')

    def test_create_user_missing_username(self):
        """Test creating a user with missing username."""
        user_data = {
            'password': 'testpass',
            'email': 'test@example.com'
        }
        with self.assertRaises(ValueError):
            create_user(**user_data)

    # Add more test cases as needed

if __name__ == '__main__':
    unittest.main()

