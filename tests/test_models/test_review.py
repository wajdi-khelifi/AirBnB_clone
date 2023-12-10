#!/usr/bin/python3
"""Test Review"""
import unittest
from models.review import Review
from models.base_model import BaseModel


class TestReview(unittest.TestCase):
    """Test for Review class."""

    def test_attributes(self):
        """Test Review attributes."""
        review = Review()
        review.place_id = "place_1"
        review.user_id = "user_1"
        review.text = "This is a review text."

        self.assertEqual(review.place_id, "place_1")
        self.assertEqual(review.user_id, "user_1")
        self.assertEqual(review.text, "This is a review text.")

    def test_instance_of_base_model(self):
        """Test if Review is an instance of BaseModel."""
        review = Review()
        self.assertIsInstance(review, BaseModel)


if __name__ == '__main__':
    unittest.main()
