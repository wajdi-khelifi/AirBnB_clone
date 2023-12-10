#!/usr/bin/python3
"""Unit tests for Review class"""
from models.review import Review
import unittest
from datetime import datetime
from models import storage


class TestReview(unittest.TestCase):
    """Test cases for Review class"""

    def test_attributes(self):
        """Test the attributes of the Review instance"""
        my_review = Review()
        self.assertTrue(hasattr(my_review, 'id'))
        self.assertTrue(hasattr(my_review, 'created_at'))
        self.assertTrue(hasattr(my_review, 'updated_at'))
        self.assertTrue(hasattr(my_review, '__class__'))
        self.assertTrue(hasattr(my_review, 'place_id'))
        self.assertTrue(hasattr(my_review, 'user_id'))
        self.assertTrue(hasattr(my_review, 'text'))

    def test_str_method(self):
        """Test the __str__ method"""
        my_review = Review()
        expected_str = "[Review] ({}) {}".format(
            my_review.id, my_review.__dict__
        )
        self.assertEqual(str(my_review), expected_str)

    def test_save_method(self):
        """Test the save method"""
        my_review = Review()
        original_updated_at = my_review.updated_at
        my_review.save()
        self.assertNotEqual(original_updated_at, my_review.updated_at)

    def test_to_dict_method(self):
        """Test the to_dict method"""
        my_review = Review()
        my_review.place_id = "123"
        my_review.user_id = "456"
        my_review.text = "Great experience!"
        review_json = my_review.to_dict()

        self.assertEqual(review_json['id'], my_review.id)
        self.assertEqual(review_json['__class__'], 'Review')
        self.assertEqual(review_json['place_id'], "123")
        self.assertEqual(review_json['user_id'], "456")
        self.assertEqual(review_json['text'], "Great experience!")
        self.assertEqual(type(review_json['created_at']), str)
        self.assertEqual(type(review_json['updated_at']), str)

    def test_init_from_dict(self):
        """Test creating an instance from a dictionary"""
        my_review = Review()
        my_review.place_id = "123"
        my_review.user_id = "456"
        my_review.text = "Great experience!"
        review_json = my_review.to_dict()

        new_review = Review(**review_json)

        self.assertEqual(my_review.id, new_review.id)
        self.assertEqual(
            int(my_review.created_at.timestamp()),
            int(new_review.created_at.timestamp())
        )
        self.assertEqual(
            int(my_review.updated_at.timestamp()),
            int(new_review.updated_at.timestamp())
        )
        self.assertEqual(my_review.place_id, new_review.place_id)
        self.assertEqual(my_review.user_id, new_review.user_id)
        self.assertEqual(my_review.text, new_review.text)
        self.assertEqual(
            my_review.__class__.__name__,
            new_review.__class__.__name__
        )


if __name__ == '__main__':
    unittest.main()
