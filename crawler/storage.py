"""
This module defines the Database class for interacting with a SQLite database.
It provides methods to create tables, insert entries, log usage events, and fetch entries.
The module uses the sqlite3 library for database operations.

Classes:
--------
Database:
    A class to manage the SQLite database operations, including creating tables,
    inserting entries, logging usage, and fetching data.

Usage:
------
To use this module, create an instance of the Database class and call its 
methods to perform database operations.

Example:
--------
    from database import Database

    db = Database('my_database.db')
    db.insert_entry(('1', 'Test Title', 100, 50))
    db.log_usage('2023-01-01T00:00:00', 'test_filter')
    entries = db.fetch_all_entries()
    for entry in entries:
        print(entry)
"""

import sqlite3  # Import the SQLite3 library to handle the database operations.

class Database:
    """
    A class to manage the SQLite database operations, including creating tables,
    inserting entries, logging usage, and fetching data.

    Methods:
    --------
    __init__(db_path):
        Initializes the Database with the given SQLite database path.
    
    create_tables():
        Creates the necessary tables in the database if they don't exist.
    
    insert_entry(entry):
        Inserts a new entry into the 'entries' table.
    
    log_usage(timestamp, filter_type):
        Logs the usage event into the 'usage' table.
    
    fetch_all_entries():
        Fetches all entries from the 'entries' table.
    """
    
    def __init__(self, db_path):
        """
        Initializes the Database class with the path to the SQLite database.
        
        Parameters:
        -----------
        db_path : str
            The path to the SQLite database file.
        """
        self.conn = sqlite3.connect(db_path)
        self.create_tables()
        
    def create_tables(self):
        """
        Creates the necessary tables in the database if they don't exist.
        """
        with self.conn:
            self.conn.execute('''
                CREATE TABLE IF NOT EXISTS entries (
                    id INTEGER PRIMARY KEY,    -- Unique identifier for each entry, serves as the primary key
                    number TEXT,               -- Rank number of the news item as a string
                    title TEXT,                -- Title of the news item
                    points INTEGER,            -- Points (score) of the news item
                    comments INTEGER           -- Number of comments on the news item
                )
            ''')
            self.conn.execute('''
                CREATE TABLE IF NOT EXISTS usage (
                    id INTEGER PRIMARY KEY,    -- Primary key for the table
                    timestamp TEXT,            -- Timestamp of the logged event
                    filter_type TEXT           -- Type of filter used during the event
                )
            ''')
            
    def insert_entry(self, entry):
        """
        Inserts a new entry into the 'entries' table.
        
        Parameters:
        -----------
        entry : tuple
            A tuple containing the values to be inserted into the 'entries' table.
            The tuple should be in the format (number, title, points, comments).
        """
        with self.conn:
            self.conn.execute('''
                INSERT INTO entries (number, title, points, comments) 
                VALUES (?, ?, ?, ?)
            ''', entry)
        
    def log_usage(self, timestamp, filter_type):
        """
        Logs the usage event into the 'usage' table.
        
        Parameters:
        -----------
        timestamp : str
            The timestamp of the usage event in ISO format.
        filter_type : str
            The type of filter used during the event.
        """
        with self.conn:
            self.conn.execute('''
                INSERT INTO usage (timestamp, filter_type) 
                VALUES (?, ?)
            ''', (timestamp, filter_type))
        
    def fetch_all_entries(self):
        """
        Fetches all entries from the 'entries' table.
        
        Returns:
        --------
        list of tuple
            A list of tuples, each containing the number, title, points, and comments of a news item.
        """
        cursor = self.conn.cursor()
        cursor.execute('SELECT number, title, points, comments FROM entries')
        return cursor.fetchall()
