#!/usr/bin/python3
"""Test City"""
import unittest
from models.city import City
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
    """Test for City class."""

    def test_attributes(self):
        """Test City attributes."""
        city = City()
        city.state_id = "state_1"
        city.name = "City Name"

        self.assertEqual(city.state_id, "state_1")
        self.assertEqual(city.name, "City Name")

    def test_instance_of_base_model(self):
        """Test if City is an instance of BaseModel."""
        city = City()
        self.assertIsInstance(city, BaseModel)


if __name__ == '__main__':
    unittest.main()
