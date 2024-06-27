"""
This module contains unit tests for the Database class from the crawler.storage module.
It uses the unittest framework to verify the functionality of the database operations
provided by the Database class.

Classes:
--------
TestDatabase:
    A class that contains test cases for the Database class methods.

Usage:
------
To run the tests, execute this module directly. The unittest framework will discover and run all test cases.

Example:
--------
    python -m unittest test_database.py
"""

import unittest  # Import the unittest module for creating and running tests
import os  # Import the os module for interacting with the operating system
from crawler.storage import Database  # Import the Database class from the crawler.storage module

class TestDatabase(unittest.TestCase):
    """
    A test case class that contains test cases for the Database class methods.

    Methods:
    --------
    setUp():
        Sets up any necessary objects or state before each test.
    
    tearDown():
        Cleans up any necessary objects or state after each test.
    
    test_insert_entry():
        Tests the insert_entry method of the Database class.
    
    test_log_usage():
        Tests the log_usage method of the Database class.
    
    test_fetch_all_entries():
        Tests the fetch_all_entries method of the Database class.
    """

    def setUp(self):
        """
        Sets up any necessary objects or state before each test.

        Initializes a test database and creates the required tables.
        """
        self.db_path = 'test_crawler.db'
        self.db = Database(self.db_path)
        self.db.create_tables()

    def tearDown(self):
        """
        Cleans up any necessary objects or state after each test.

        Closes the database connection and removes the test database file if it exists.
        """
        self.db.conn.close()
        if os.path.exists(self.db_path):
            os.remove(self.db_path)

    def test_insert_entry(self):
        """
        Tests the insert_entry method of the Database class.

        Verifies that an entry can be inserted into the database and fetched correctly.
        """
        entry = ('1', 'Test title', 100, 50)
        self.db.insert_entry(entry)
        entries = self.db.fetch_all_entries()
        self.assertIn(entry, entries, "Inserted entry should be present in the database")

    def test_log_usage(self):
        """
        Tests the log_usage method of the Database class.

        Verifies that a usage log entry can be inserted into the database and fetched correctly.
        """
        self.db.log_usage('2024-01-01T00:00:00', 'test_filter')
        cursor = self.db.conn.cursor()
        cursor.execute('SELECT * FROM usage')
        usage_logs = cursor.fetchall()
        self.assertEqual(len(usage_logs), 1, "There should be one usage log entry")
        self.assertEqual(usage_logs[0][1], '2024-01-01T00:00:00', "Timestamp should match")
        self.assertEqual(usage_logs[0][2], 'test_filter', "Filter type should match")

    def test_fetch_all_entries(self):
        """
        Tests the fetch_all_entries method of the Database class.

        Verifies that multiple entries can be inserted into the database and fetched correctly.
        """
        entries = [
            ('1', 'Test title one', 100, 50),
            ('2', 'Test title two', 200, 30)
        ]
        for entry in entries:
            self.db.insert_entry(entry)
        fetched_entries = self.db.fetch_all_entries()
        self.assertGreaterEqual(len(fetched_entries), 2, "Should fetch all inserted entries")

if __name__ == '__main__':
    unittest.main()
    # Run the unit tests if this script is executed directly
