#!/usr/bin/python3
"""Test Place"""
import unittest
from models.place import Place
from models.base_model import BaseModel


class TestPlace(unittest.TestCase):
    """Test for Place class."""

    def test_attributes(self):
        """Test Place attributes."""
        place = Place()
        place.city_id = "city_1"
        place.user_id = "user_1"
        place.name = "Place Name"
        place.description = "Description of the place"
        place.number_rooms = 2
        place.number_bathrooms = 1
        place.max_guest = 4
        place.price_by_night = 100
        place.latitude = 40.7128
        place.longitude = -74.0060
        place.amenity_ids = ["amenity_1", "amenity_2"]

        self.assertEqual(place.city_id, "city_1")
        self.assertEqual(place.user_id, "user_1")
        self.assertEqual(place.name, "Place Name")
        self.assertEqual(place.description, "Description of the place")
        self.assertEqual(place.number_rooms, 2)
        self.assertEqual(place.number_bathrooms, 1)
        self.assertEqual(place.max_guest, 4)
        self.assertEqual(place.price_by_night, 100)
        self.assertEqual(place.latitude, 40.7128)
        self.assertEqual(place.longitude, -74.0060)
        self.assertEqual(place.amenity_ids, ["amenity_1", "amenity_2"])

    def test_instance_of_base_model(self):
        """Test if Place is an instance of BaseModel."""
        place = Place()
        self.assertIsInstance(place, BaseModel)


if __name__ == '__main__':
    unittest.main()
