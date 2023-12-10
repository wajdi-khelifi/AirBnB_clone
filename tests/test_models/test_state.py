#!/usr/bin/python3
"""Unit tests for State class"""
from models.state import State
import unittest
from datetime import datetime
from models import storage


class TestState(unittest.TestCase):
    """Test cases for State class"""

    def test_attributes(self):
        """Test the attributes of the State instance"""
        my_state = State()
        self.assertTrue(hasattr(my_state, 'id'))
        self.assertTrue(hasattr(my_state, 'created_at'))
        self.assertTrue(hasattr(my_state, 'updated_at'))
        self.assertTrue(hasattr(my_state, '__class__'))
        self.assertTrue(hasattr(my_state, 'name'))

    def test_str_method(self):
        """Test the __str__ method"""
        my_state = State()
        expected_str = "[State] ({}) {}".format(
            my_state.id, my_state.__dict__
        )
        self.assertEqual(str(my_state), expected_str)

    def test_save_method(self):
        """Test the save method"""
        my_state = State()
        original_updated_at = my_state.updated_at
        my_state.save()
        self.assertNotEqual(original_updated_at, my_state.updated_at)

    def test_to_dict_method(self):
        """Test the to_dict method"""
        my_state = State()
        my_state.name = "California"
        state_json = my_state.to_dict()

        self.assertEqual(state_json['id'], my_state.id)
        self.assertEqual(state_json['__class__'], 'State')
        self.assertEqual(state_json['name'], "California")
        self.assertEqual(type(state_json['created_at']), str)
        self.assertEqual(type(state_json['updated_at']), str)

    def test_init_from_dict(self):
        """Test creating an instance from a dictionary"""
        my_state = State()
        my_state.name = "California"
        state_json = my_state.to_dict()

        new_state = State(**state_json)

        self.assertEqual(my_state.id, new_state.id)
        self.assertEqual(
            int(my_state.created_at.timestamp()),
            int(new_state.created_at.timestamp())
        )
        self.assertEqual(
            int(my_state.updated_at.timestamp()),
            int(new_state.updated_at.timestamp())
        )
        self.assertEqual(my_state.name, new_state.name)
        self.assertEqual(
            my_state.__class__.__name__,
            new_state.__class__.__name__
        )


if __name__ == '__main__':
    unittest.main()
