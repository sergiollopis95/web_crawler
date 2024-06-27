"""
This module contains unit tests for the Filters class from the crawler.filters module.
It uses the unittest framework to verify the functionality of the filtering methods provided by the Filters class.

Classes:
--------
TestFilters:
    A class that contains test cases for the Filters class methods.

Usage:
------
To run the tests, execute this module directly. The unittest framework will discover and run all test cases.

Example:
--------
    python -m unittest test_filters.py
"""

import unittest  # Import the unittest module for creating and running tests
from crawler.filters import Filters  # Import the Filters class from the crawler.filters module

class TestFilters(unittest.TestCase):
    """
    A test case class that contains test cases for the Filters class methods.

    Methods:
    --------
    setUp():
        Sets up any necessary objects or state before each test.
    
    test_filter_by_comments():
        Tests the filter_by_comments method of the Filters class.
    
    test_filter_by_points():
        Tests the filter_by_points method of the Filters class.
    """

    def setUp(self):
        """
        Sets up any necessary objects or state before each test.
        
        Initializes a list of entries with sample data.
        """
        self.entries = [
            ('1', 'Short title', 50, 10),
            ('2', 'This is a longer title with more words', 100, 20),
            ('3', 'Another long title example', 150, 5),
            ('4', 'Tiny', 20, 2),
            ('5', 'Just right', 70, 15)
        ]

    def test_filter_by_comments(self):
        """
        Tests the filter_by_comments method of the Filters class.

        Verifies that the method filters entries with titles containing more than 5 words
        and sorts them by the number of comments in descending order.
        """
        filtered_entries = Filters.filter_by_comments(self.entries)
        self.assertGreater(len(filtered_entries), 0, "Should filter out entries with more than 5 words in the title")
        self.assertEqual(filtered_entries[0][1], 'This is a longer title with more words', "Should return entry with most comments first")

    def test_filter_by_points(self):
        """
        Tests the filter_by_points method of the Filters class.

        Verifies that the method filters entries with titles containing 5 or fewer words
        and sorts them by the number of points in descending order.
        """
        filtered_entries = Filters.filter_by_points(self.entries)
        self.assertGreater(len(filtered_entries), 0, "Should filter out entries with 5 or fewer words in the title")
        self.assertEqual(filtered_entries[0][1], 'Another long title example', "Titles should match expected order")
        self.assertEqual(filtered_entries[0][2], 150, "Points should match expected order")

if __name__ == '__main__':
    unittest.main()  # Run the unit tests if this script is executed directly
