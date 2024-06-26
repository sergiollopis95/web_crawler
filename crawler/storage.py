import sqlite3  # Import the SQLite3 library to handle the database operations

class Database:
    # Initialize the Database class with the path to the SQLite database
    def __init__(self, db_path):
        # Connect to the SQLite database specified by db_path
        self.conn = sqlite3.connect(db_path)
        # Create the required tables if they don't already exist
        self.create_tables()
        
    # Method to create the necessary tables in the database
    def create_tables(self):
        # Use a context manager to handle the database connection
        with self.conn:
            # Execute a SQL command to create the 'entries' table if it doesn't exist
            self.conn.execute('''
                CREATE TABLE IF NOT EXISTS entries (
                    id INTEGER PRIMARY KEY,    # Primary key for the table
                    number TEXT,               # Rank number of the news item
                    title TEXT,                # Title of the news item
                    points INTEGER,            # Points (score) of the news item
                    comments INTEGER           # Number of comments on the news item
                )
            ''')
            # Execute a SQL command to create the 'usage' table if it doesn't exist
            self.conn.execute('''
                CREATE TABLE IF NOT EXISTS usage (
                    id INTEGER PRIMARY KEY,    # Primary key for the table
                    timestamp TEXT,            # Timestamp of the logged event
                    filter_type TEXT           # Type of filter used during the event
                )
            ''')

        