"""
This module defines unit tests for the Scraper class using the unittest framework.
It verifies the functionality of the Scraper class, including fetching entries,
validating their format, and storing and fetching them from a database.

Classes:
--------
TestScraper:
    A class that contains test cases for the Scraper class methods.

Usage:
------
To use this module, run it directly to execute the test cases and verify the 
functionality of the Scraper class.

Example:
--------
    python -m unittest test_scraper.py
"""

import unittest  # Import the unittest module for creating and running tests
from crawler.scraper import Scraper  # Import the Scraper class from the crawler.scraper module

class TestScraper(unittest.TestCase):
    """
    A test case class that contains test cases for the Scraper class methods.

    Methods:
    --------
    setUp():
        Sets up any necessary objects or state before each test.
    
    test_fetch_entries():
        Tests that fetching entries returns a non-empty list.
    
    test_entry_format():
        Tests that fetched entries have the expected format.
    
    test_store_and_fetch_entries():
        Tests storing entries and fetching them from the database.
    """

    def setUp(self):
        """
        Sets up any necessary objects or state before each test.
        """
        self.scraper = Scraper()
        # Create an instance of the Scraper class and assign it to self.scraper

    def test_fetch_entries(self):
        """
        Tests that fetching entries returns a non-empty list.
        """
        entries = self.scraper.fetch_entries()
        # Call the fetch_entries method of the Scraper instance and store the result in entries
        self.assertGreater(len(entries), 0, "Should fetch more than zero entries")
        # Assert that the length of the entries list is greater than 0 with a custom error message

    def test_entry_format(self):
        """
        Tests that fetched entries have the expected format.
        """
        entries = self.scraper.fetch_entries()
        # Call the fetch_entries method of the Scraper instance and store the result in entries
        for entry in entries:
            # Iterate over each entry in the entries list
            self.assertIsInstance(entry, tuple, "Entry should be a tuple")
            # Assert that each entry is an instance of tuple with a custom error message
            self.assertEqual(len(entry), 4, "Entry should have four elements")
            # Assert that each entry has exactly 4 elements with a custom error message
            self.assertIsInstance(entry[0], str, "Number should be a string")
            # Assert that the first element of each entry is a string with a custom error message
            self.assertIsInstance(entry[1], str, "Title should be a string")
            # Assert that the second element of each entry is a string with a custom error message
            self.assertIsInstance(entry[2], int, "Points should be an integer")
            # Assert that the third element of each entry is an integer with a custom error message
            self.assertIsInstance(entry[3], int, "Comments should be an integer")
            # Assert that the fourth element of each entry is an integer with a custom error message

    def test_store_and_fetch_entries(self):
        """
        Tests storing entries and fetching them from the database.
        """
        entries = [
            ('1', 'Test title one', 100, 50),
            ('2', 'Test title two', 200, 30)
        ]
        # Define a list of entries to store
        self.scraper.store_entries(entries)
        # Call the store_entries method to store the entries in the database
        stored_entries = self.scraper.db.fetch_all_entries()
        # Fetch all stored entries from the database
        self.assertGreaterEqual(len(stored_entries), 2, "Should store and fetch at least the number of entries inserted")
        # Assert that the number of stored entries is at least the number of entries inserted, with a custom error message

if __name__ == '__main__':
    unittest.main()
    # Run the unit tests if this script is executed directly
