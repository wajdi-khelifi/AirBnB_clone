#!/usr/bin/python3
"""Test Amenity"""
import unittest
from models.amenity import Amenity
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
    """Test for Amenity class."""

    def test_attributes(self):
        """Test Amenity attributes."""
        amenity = Amenity()
        amenity.name = "Wifi"

        self.assertEqual(amenity.name, "Wifi")

    def test_instance_of_base_model(self):
        """Test if Amenity is an instance of BaseModel."""
        amenity = Amenity()
        self.assertIsInstance(amenity, BaseModel)


if __name__ == '__main__':
    unittest.main()
