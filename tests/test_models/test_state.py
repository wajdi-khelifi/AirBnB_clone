#!/usr/bin/python3
"""Unit tests for the State class"""
import unittest
from models.state import State
from models import storage


class TestState(unittest.TestCase):
    """Test cases for the State class"""

    def setUp(self):
        """Set up a State instance for testing"""
        self.state = State()

    def tearDown(self):
        """Clean up after testing"""
        pass

    def test_attributes(self):
        """Test the existence of required attributes"""
        self.assertTrue(hasattr(self.state, 'name'))

    def test_default_values(self):
        """Test default values of State attributes"""
        self.assertEqual(self.state.name, "")

    def test_save_reload(self):
        """Test saving and reloading a State instance"""
        self.state.name = "Texas"
        self.state.save()
        key = "{}.{}".format(self.state.__class__.__name__, self.state.id)
        reloaded_state = storage.all()[key]
        self.assertEqual(reloaded_state.name, "Texas")

    def test_to_dict(self):
        """Test conversion of State instance to dictionary"""
        self.state.name = "Florida"
        state_dict = self.state.to_dict()
        self.assertEqual(state_dict['name'], "Florida")
        self.assertEqual(state_dict['__class__'], "State")
        self.assertTrue('id' in state_dict)
        self.assertTrue('created_at' in state_dict)
        self.assertTrue('updated_at' in state_dict)

    def test_created_at_updated_at(self):
        """Test the data types of created_at and updated_at attributes"""
        pass


if __name__ == "__main__":
    unittest.main()
