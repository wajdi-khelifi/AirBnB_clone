#!/usr/bin/python3
"""Unit tests for Amenity class"""
from models.amenity import Amenity
import unittest
from datetime import datetime
from models import storage


class TestAmenity(unittest.TestCase):
    """Test cases for Amenity class"""

    def test_attributes(self):
        """Test the attributes of the Amenity instance"""
        my_amenity = Amenity()
        self.assertTrue(hasattr(my_amenity, 'id'))
        self.assertTrue(hasattr(my_amenity, 'created_at'))
        self.assertTrue(hasattr(my_amenity, 'updated_at'))
        self.assertTrue(hasattr(my_amenity, '__class__'))
        self.assertTrue(hasattr(my_amenity, 'name'))

    def test_str_method(self):
        """Test the __str__ method"""
        my_amenity = Amenity()
        expected_str = "[Amenity] ({}) {}".format(
            my_amenity.id, my_amenity.__dict__
        )
        self.assertEqual(str(my_amenity), expected_str)

    def test_save_method(self):
        """Test the save method"""
        my_amenity = Amenity()
        original_updated_at = my_amenity.updated_at
        my_amenity.save()
        self.assertNotEqual(original_updated_at, my_amenity.updated_at)

    def test_to_dict_method(self):
        """Test the to_dict method"""
        my_amenity = Amenity()
        my_amenity.name = "Swimming Pool"
        amenity_json = my_amenity.to_dict()

        self.assertEqual(amenity_json['id'], my_amenity.id)
        self.assertEqual(amenity_json['__class__'], 'Amenity')
        self.assertEqual(amenity_json['name'], "Swimming Pool")
        self.assertEqual(type(amenity_json['created_at']), str)
        self.assertEqual(type(amenity_json['updated_at']), str)

    def test_init_from_dict(self):
        """Test creating an instance from a dictionary"""
        my_amenity = Amenity()
        my_amenity.name = "Swimming Pool"
        amenity_json = my_amenity.to_dict()

        new_amenity = Amenity(**amenity_json)

        self.assertEqual(my_amenity.id, new_amenity.id)
        self.assertEqual(
            int(my_amenity.created_at.timestamp()),
            int(new_amenity.created_at.timestamp())
        )
        self.assertEqual(
            int(my_amenity.updated_at.timestamp()),
            int(new_amenity.updated_at.timestamp())
        )
        self.assertEqual(my_amenity.name, new_amenity.name)
        self.assertEqual(
            my_amenity.__class__.__name__,
            new_amenity.__class__.__name__
        )


if __name__ == '__main__':
    unittest.main()
