#!/usr/bin/python3
"""Unit tests for the City class"""
import unittest
from models.city import City
from datetime import datetime
from models import storage


class TestCity(unittest.TestCase):
    """Test cases for the City class"""

    def setUp(self):
        """Set up a City instance for testing"""
        self.city = City()

    def tearDown(self):
        """Clean up after testing"""
        pass

    def test_attributes(self):
        """Test the existence of required attributes"""
        self.assertTrue(hasattr(self.city, 'state_id'))
        self.assertTrue(hasattr(self.city, 'name'))

    def test_default_values(self):
        """Test default values of City attributes"""
        self.assertEqual(self.city.state_id, "")
        self.assertEqual(self.city.name, "")

    def test_save_reload(self):
        """Test saving and reloading a City instance"""
        self.city.state_id = "CA"
        self.city.name = "Los Angeles"
        self.city.save()
        key = "{}.{}".format(self.city.__class__.__name__, self.city.id)
        reloaded_city = storage.all()[key]
        self.assertEqual(reloaded_city.state_id, "CA")
        self.assertEqual(reloaded_city.name, "Los Angeles")

    def test_to_dict(self):
        """Test conversion of City instance to dictionary"""
        self.city.state_id = "NY"
        self.city.name = "Albany"
        city_dict = self.city.to_dict()
        self.assertEqual(city_dict['state_id'], "NY")
        self.assertEqual(city_dict['name'], "Albany")
        self.assertEqual(city_dict['__class__'], "City")
        self.assertTrue('id' in city_dict)
        self.assertTrue('created_at' in city_dict)
        self.assertTrue('updated_at' in city_dict)

    def test_created_at_updated_at(self):
        """Test the data types of created_at and updated_at attributes"""
        self.assertTrue(isinstance(self.city.created_at, datetime))
        self.assertTrue(isinstance(self.city.updated_at, datetime))


if __name__ == "__main__":
    unittest.main()
