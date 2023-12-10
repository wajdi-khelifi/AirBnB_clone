#!/usr/bin/python3
"""Unit tests for the Place class"""
import unittest
from models.place import Place
from datetime import datetime
from models import storage


class TestPlace(unittest.TestCase):
    """Test cases for the Place class"""

    def setUp(self):
        """Set up a Place instance for testing"""
        self.place = Place()

    def tearDown(self):
        """Clean up after testing"""
        pass

    def test_attributes(self):
        """Test the existence of required attributes"""
        self.assertTrue(hasattr(self.place, 'city_id'))
        self.assertTrue(hasattr(self.place, 'user_id'))
        self.assertTrue(hasattr(self.place, 'name'))
        self.assertTrue(hasattr(self.place, 'description'))
        self.assertTrue(hasattr(self.place, 'number_rooms'))
        self.assertTrue(hasattr(self.place, 'number_bathrooms'))
        self.assertTrue(hasattr(self.place, 'max_guest'))
        self.assertTrue(hasattr(self.place, 'price_by_night'))
        self.assertTrue(hasattr(self.place, 'latitude'))
        self.assertTrue(hasattr(self.place, 'longitude'))
        self.assertTrue(hasattr(self.place, 'amenity_ids'))

    def test_default_values(self):
        """Test default values of Place attributes"""
        self.assertEqual(self.place.city_id, "")
        self.assertEqual(self.place.user_id, "")
        self.assertEqual(self.place.name, "")
        self.assertEqual(self.place.description, "")
        self.assertEqual(self.place.number_rooms, 0)
        self.assertEqual(self.place.number_bathrooms, 0)
        self.assertEqual(self.place.max_guest, 0)
        self.assertEqual(self.place.price_by_night, 0)
        self.assertEqual(self.place.latitude, 0.0)
        self.assertEqual(self.place.longitude, 0.0)
        self.assertEqual(self.place.amenity_ids, [])

    def test_save_reload(self):
        """Test saving and reloading a Place instance"""
        self.place.city_id = "123"
        self.place.user_id = "456"
        self.place.name = "Sunny Beach House"
        self.place.description = "A charming beachfront property"
        self.place.number_rooms = 2
        self.place.number_bathrooms = 1
        self.place.max_guest = 4
        self.place.price_by_night = 100
        self.place.latitude = 37.7749
        self.place.longitude = -122.4194
        self.place.amenity_ids = ["789", "012"]
        self.place.save()
        key = "{}.{}".format(self.place.__class__.__name__, self.place.id)
        reloaded_place = storage.all()[key]
        self.assertEqual(reloaded_place.city_id, "123")
        self.assertEqual(reloaded_place.user_id, "456")
        self.assertEqual(reloaded_place.name, "Sunny Beach House")
        self.assertEqual(
            reloaded_place.description, "A charming beachfront property")
        self.assertEqual(reloaded_place.number_rooms, 2)
        self.assertEqual(reloaded_place.number_bathrooms, 1)
        self.assertEqual(reloaded_place.max_guest, 4)
        self.assertEqual(reloaded_place.price_by_night, 100)
        self.assertEqual(reloaded_place.latitude, 37.7749)
        self.assertEqual(reloaded_place.longitude, -122.4194)
        self.assertEqual(reloaded_place.amenity_ids, ["789", "012"])

    def test_to_dict(self):
        """Test conversion of Place instance to dictionary"""
        self.place.city_id = "987"
        self.place.user_id = "654"
        self.place.name = "Mountain Cabin"
        self.place.description = "A cozy cabin in the mountains"
        self.place.number_rooms = 3
        self.place.number_bathrooms = 2
        self.place.max_guest = 6
        self.place.price_by_night = 200
        self.place.latitude = 34.0522
        self.place.longitude = -118.2437
        self.place.amenity_ids = ["345", "678"]
        place_dict = self.place.to_dict()
        self.assertEqual(place_dict['city_id'], "987")
        self.assertEqual(place_dict['user_id'], "654")
        self.assertEqual(place_dict['name'], "Mountain Cabin")
        self.assertEqual(place_dict['description'], "A cozy cabin in the mountains")
        self.assertEqual(place_dict['number_rooms'], 3)
        self.assertEqual(place_dict['number_bathrooms'], 2)
        self.assertEqual(place_dict['max_guest'], 6)
        self.assertEqual(place_dict['price_by_night'], 200)
        self.assertEqual(place_dict['latitude'], 34.0522)
        self.assertEqual(place_dict['longitude'], -118.2437)
        self.assertEqual(place_dict['amenity_ids'], ["345", "678"])
        self.assertEqual(place_dict['__class__'], "Place")
        self.assertTrue('id' in place_dict)
        self.assertTrue('created_at' in place_dict)
        self.assertTrue('updated_at' in place_dict)

    def test_created_at_updated_at(self):
        """Test the data types of created_at and updated_at attributes"""
        self.assertTrue(isinstance(self.place.created_at, datetime))
        self.assertTrue(isinstance(self.place.updated_at, datetime))


if __name__ == "__main__":
    unittest.main()
