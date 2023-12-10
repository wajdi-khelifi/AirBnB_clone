#!/usr/bin/python3
"""Test State"""
import unittest
from models.state import State
from models.base_model import BaseModel


class TestState(unittest.TestCase):
    """Test for State class."""

    def test_attributes(self):
        """Test State attributes."""
        state = State()
        state.name = "California"

        self.assertEqual(state.name, "California")

    def test_instance_of_base_model(self):
        """Test if State is an instance of BaseModel."""
        state = State()
        self.assertIsInstance(state, BaseModel)


if __name__ == '__main__':
    unittest.main()
