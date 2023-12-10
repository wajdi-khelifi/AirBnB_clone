#!/usr/bin/python3
"""Unit tests for Place class"""
from models.place import Place
import unittest
from datetime import datetime
from models import storage


class TestPlace(unittest.TestCase):
    """Test cases for Place class"""

    def test_attributes(self):
        """Test the attributes of the Place instance"""
        my_place = Place()
        self.assertTrue(hasattr(my_place, 'id'))
        self.assertTrue(hasattr(my_place, 'created_at'))
        self.assertTrue(hasattr(my_place, 'updated_at'))
        self.assertTrue(hasattr(my_place, '__class__'))
        self.assertTrue(hasattr(my_place, 'city_id'))
        self.assertTrue(hasattr(my_place, 'user_id'))
        self.assertTrue(hasattr(my_place, 'name'))
        self.assertTrue(hasattr(my_place, 'description'))
        self.assertTrue(hasattr(my_place, 'number_rooms'))
        self.assertTrue(hasattr(my_place, 'number_bathrooms'))
        self.assertTrue(hasattr(my_place, 'max_guest'))
        self.assertTrue(hasattr(my_place, 'price_by_night'))
        self.assertTrue(hasattr(my_place, 'latitude'))
        self.assertTrue(hasattr(my_place, 'longitude'))
        self.assertTrue(hasattr(my_place, 'amenity_ids'))

    def test_str_method(self):
        """Test the __str__ method"""
        my_place = Place()
        expected_str = "[Place] ({}) {}".format(
            my_place.id, my_place.__dict__
        )
        self.assertEqual(str(my_place), expected_str)

    def test_save_method(self):
        """Test the save method"""
        my_place = Place()
        original_updated_at = my_place.updated_at
        my_place.save()
        self.assertNotEqual(original_updated_at, my_place.updated_at)

    def test_to_dict_method(self):
        """Test the to_dict method"""
        my_place = Place()
        my_place.city_id = "SF"
        my_place.user_id = "123"
        my_place.name = "Cozy Apartment"
        my_place.description = "A comfortable place to stay"
        my_place.number_rooms = 2
        my_place.number_bathrooms = 1
        my_place.max_guest = 4
        my_place.price_by_night = 100
        my_place.latitude = 37.7749
        my_place.longitude = -122.4194
        my_place.amenity_ids = ["wifi", "kitchen", "parking"]
        place_json = my_place.to_dict()

        self.assertEqual(place_json['id'], my_place.id)
        self.assertEqual(place_json['__class__'], 'Place')
        self.assertEqual(place_json['city_id'], "SF")
        self.assertEqual(place_json['user_id'], "123")
        self.assertEqual(place_json['name'], "Cozy Apartment")
        self.assertEqual(
                place_json['description'],
                "A comfortable place to stay"
                )
        self.assertEqual(place_json['number_rooms'], 2)
        self.assertEqual(place_json['number_bathrooms'], 1)
        self.assertEqual(place_json['max_guest'], 4)
        self.assertEqual(place_json['price_by_night'], 100)
        self.assertEqual(place_json['latitude'], 37.7749)
        self.assertEqual(place_json['longitude'], -122.4194)
        self.assertEqual(place_json['amenity_ids'], ["wifi", "kitchen", "parking"])
        self.assertEqual(type(place_json['created_at']), str)
        self.assertEqual(type(place_json['updated_at']), str)

    def test_init_from_dict(self):
        """Test creating an instance from a dictionary"""
        my_place = Place()
        my_place.city_id = "SF"
        my_place.user_id = "123"
        my_place.name = "Cozy Apartment"
        my_place.description = "A comfortable place to stay"
        my_place.number_rooms = 2
        my_place.number_bathrooms = 1
        my_place.max_guest = 4
        my_place.price_by_night = 100
        my_place.latitude = 37.7749
        my_place.longitude = -122.4194
        my_place.amenity_ids = ["wifi", "kitchen", "parking"]
        place_json = my_place.to_dict()

        new_place = Place(**place_json)

        self.assertEqual(my_place.id, new_place.id)
        self.assertEqual(
            int(my_place.created_at.timestamp()),
            int(new_place.created_at.timestamp())
        )
        self.assertEqual(
            int(my_place.updated_at.timestamp()),
            int(new_place.updated_at.timestamp())
        )
        self.assertEqual(my_place.city_id, new_place.city_id)
        self.assertEqual(my_place.user_id, new_place.user_id)
        self.assertEqual(my_place.name, new_place.name)
        self.assertEqual(my_place.description, new_place.description)
        self.assertEqual(my_place.number_rooms, new_place.number_rooms)
        self.assertEqual(my_place.number_bathrooms, new_place.number_bathrooms)
        self.assertEqual(my_place.max_guest, new_place.max_guest)
        self.assertEqual(my_place.price_by_night, new_place.price_by_night)
        self.assertEqual(my_place.latitude, new_place.latitude)
        self.assertEqual(my_place.longitude, new_place.longitude)
        self.assertEqual(my_place.amenity_ids, new_place.amenity_ids)
        self.assertEqual(
            my_place.__class__.__name__,
            new_place.__class__.__name__
        )


if __name__ == '__main__':
    unittest.main()
