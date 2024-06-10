#!/usr/bin/python3
"""Defines unittests for models/engine/file_storage.py."""
import unittest
from models.engine.file_storage import FileStorage
from models.state import State
from models import storage


class TestFileStorage(unittest.TestCase):
    """Unittests for testing the FileStorage class."""

    def setUp(self):
        """Set up for the tests"""
        self.storage = FileStorage()
        self.storage.reload()

    def test_get(self):
        """Test that get retrieves an object by class and id"""
        state = State(name="California")
        self.storage.new(state)
        self.storage.save()
        state_id = state.id
        self.assertEqual(self.storage.get(State, state_id), state)
        self.assertIsNone(self.storage.get(State, "nonexistent_id"))

    def test_count(self):
        """Test that count returns the number of objects"""
        initial_count = self.storage.count()
        initial_state_count = self.storage.count(State)
        state = State(name="California")
        self.storage.new(state)
        self.storage.save()
        self.assertEqual(self.storage.count(), initial_count + 1)
        self.assertEqual(self.storage.count(State), initial_state_count + 1)

