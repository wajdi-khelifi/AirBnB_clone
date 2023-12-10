#!/usr/bin/python3
"""Unit tests for City class"""
from models.city import City
import unittest
from datetime import datetime
from models import storage


class TestCity(unittest.TestCase):
    """Test cases for City class"""

    def test_attributes(self):
        """Test the attributes of the City instance"""
        my_city = City()
        self.assertTrue(hasattr(my_city, 'id'))
        self.assertTrue(hasattr(my_city, 'created_at'))
        self.assertTrue(hasattr(my_city, 'updated_at'))
        self.assertTrue(hasattr(my_city, '__class__'))
        self.assertTrue(hasattr(my_city, 'state_id'))
        self.assertTrue(hasattr(my_city, 'name'))

    def test_str_method(self):
        """Test the __str__ method"""
        my_city = City()
        expected_str = "[City] ({}) {}".format(
            my_city.id, my_city.__dict__
        )
        self.assertEqual(str(my_city), expected_str)

    def test_save_method(self):
        """Test the save method"""
        my_city = City()
        original_updated_at = my_city.updated_at
        my_city.save()
        self.assertNotEqual(original_updated_at, my_city.updated_at)

    def test_to_dict_method(self):
        """Test the to_dict method"""
        my_city = City()
        my_city.state_id = "CA"
        my_city.name = "San Francisco"
        city_json = my_city.to_dict()

        self.assertEqual(city_json['id'], my_city.id)
        self.assertEqual(city_json['__class__'], 'City')
        self.assertEqual(city_json['state_id'], "CA")
        self.assertEqual(city_json['name'], "San Francisco")
        self.assertEqual(type(city_json['created_at']), str)
        self.assertEqual(type(city_json['updated_at']), str)

    def test_init_from_dict(self):
        """Test creating an instance from a dictionary"""
        my_city = City()
        my_city.state_id = "CA"
        my_city.name = "San Francisco"
        city_json = my_city.to_dict()

        new_city = City(**city_json)

        self.assertEqual(my_city.id, new_city.id)
        self.assertEqual(
            int(my_city.created_at.timestamp()),
            int(new_city.created_at.timestamp())
        )
        self.assertEqual(
            int(my_city.updated_at.timestamp()),
            int(new_city.updated_at.timestamp())
        )
        self.assertEqual(my_city.state_id, new_city.state_id)
        self.assertEqual(my_city.name, new_city.name)
        self.assertEqual(
            my_city.__class__.__name__,
            new_city.__class__.__name__
        )


if __name__ == '__main__':
    unittest.main()
