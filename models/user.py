#!/usr/bin/python3
"""
Contains the User class
"""

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
import hashlib


class User(BaseModel, Base):
    """This class defines a user by various attributes"""
    __tablename__ = 'users'
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)

    def __init__(self, *args, **kwargs):
        """Initializes the user instance"""
        super().__init__(*args, **kwargs)
        if 'password' in kwargs:
            self.password = self._hash_password(kwargs['password'])

    def __setattr__(self, name, value):
        """Custom __setattr__ to handle password hashing"""
        if name == 'password':
            value = self._hash_password(value)
        super().__setattr__(name, value)

    def _hash_password(self, password):
        """Hashes the password using MD5"""
        return hashlib.md5(password.encode()).hexdigest()

