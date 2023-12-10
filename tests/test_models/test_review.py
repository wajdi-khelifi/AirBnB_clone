#!/usr/bin/python3
"""Unit tests for the Review class"""
import unittest
from models.review import Review
from datetime import datetime
from models import storage


class TestReview(unittest.TestCase):
    """Test cases for the Review class"""

    def setUp(self):
        """Set up a Review instance for testing"""
        self.review = Review()

    def tearDown(self):
        """Clean up after testing"""
        pass

    def test_attributes(self):
        """Test the existence of required attributes"""
        self.assertTrue(hasattr(self.review, 'place_id'))
        self.assertTrue(hasattr(self.review, 'user_id'))
        self.assertTrue(hasattr(self.review, 'text'))

    def test_default_values(self):
        """Test default values of Review attributes"""
        self.assertEqual(self.review.place_id, "")
        self.assertEqual(self.review.user_id, "")
        self.assertEqual(self.review.text, "")

    def test_save_reload(self):
        """Test saving and reloading a Review instance"""
        self.review.place_id = "123"
        self.review.user_id = "456"
        self.review.text = "Fantastic stay!"
        self.review.save()
        key = "{}.{}".format(self.review.__class__.__name__, self.review.id)
        reloaded_review = storage.all()[key]
        self.assertEqual(reloaded_review.place_id, "123")
        self.assertEqual(reloaded_review.user_id, "456")
        self.assertEqual(reloaded_review.text, "Fantastic stay!")

    def test_to_dict(self):
        """Test conversion of Review instance to dictionary"""
        self.review.place_id = "789"
        self.review.user_id = "012"
        self.review.text = "Lovely place, highly recommended"
        review_dict = self.review.to_dict()
        self.assertEqual(review_dict['place_id'], "789")
        self.assertEqual(review_dict['user_id'], "012")
        self.assertEqual(review_dict['text'], "Lovely place, highly recommended")
        self.assertEqual(review_dict['__class__'], "Review")
        self.assertTrue('id' in review_dict)
        self.assertTrue('created_at' in review_dict)
        self.assertTrue('updated_at' in review_dict)

    def test_created_at_updated_at(self):
        """Test the data types of created_at and updated_at attributes"""
        self.assertTrue(isinstance(self.review.created_at, datetime))
        self.assertTrue(isinstance(self.review.updated_at, datetime))


if __name__ == "__main__":
    unittest.main()
