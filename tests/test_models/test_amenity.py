#!/usr/bin/python3
"""Unit tests for the Amenity class"""
import unittest
from models.amenity import Amenity
from datetime import datetime
from models import storage


class TestAmenity(unittest.TestCase):
    """Test cases for the Amenity class"""

    def setUp(self):
        """Set up an Amenity instance for testing"""
        self.amenity = Amenity()

    def tearDown(self):
        """Clean up after testing"""
        pass

    def test_attributes(self):
        """Test the existence of required attributes"""
        self.assertTrue(hasattr(self.amenity, 'name'))

    def test_default_values(self):
        """Test default values of Amenity attributes"""
        self.assertEqual(self.amenity.name, "")

    def test_save_reload(self):
        """Test saving and reloading an Amenity instance"""
        self.amenity.name = "Sauna"
        self.amenity.save()
        key = "{}.{}".format(self.amenity.__class__.__name__, self.amenity.id)
        reloaded_amenity = storage.all()[key]
        self.assertEqual(reloaded_amenity.name, "Sauna")

    def test_to_dict(self):
        """Test conversion of Amenity instance to dictionary"""
        self.amenity.name = "Movie Theater"
        amenity_dict = self.amenity.to_dict()
        self.assertEqual(amenity_dict['name'], "Movie Theater")
        self.assertEqual(amenity_dict['__class__'], "Amenity")
        self.assertTrue('id' in amenity_dict)
        self.assertTrue('created_at' in amenity_dict)
        self.assertTrue('updated_at' in amenity_dict)

    def test_created_at_updated_at(self):
        """Test the data types of created_at and updated_at attributes"""
        self.assertTrue(isinstance(self.amenity.created_at, datetime))
        self.assertTrue(isinstance(self.amenity.updated_at, datetime))


if __name__ == "__main__":
    unittest.main()
