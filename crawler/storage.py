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
                    id INTEGER PRIMARY KEY,    -- Unique identifier for each entry, serves as the primary key
                    number TEXT,               -- Rank number of the news item as a string
                    title TEXT,                -- Title of the news item
                    points INTEGER,            -- Points (score) of the news item
                    comments INTEGER           -- Number of comments on the news item
                )
            ''')
            # Execute a SQL command to create the 'usage' table if it doesn't exist
            self.conn.execute('''
                CREATE TABLE IF NOT EXISTS usage (
                    id INTEGER PRIMARY KEY,    -- Primary k ey for the table
                    timestamp TEXT,            -- Timestamp of the logged event
                    filter_type TEXT           -- Type of filter used during the event
                )
            ''')
            
    # Method to insert a new entry into the 'entries' table
    def insert_entry(self, entry):
        # Use a context manager to handle the database connection
        with self.conn:
            # Execute a SQL command to insert the provided entry data into the 'entries' table
            self.conn.execute('''
                INSERT INTO entries (number, title, points, comments) 
                VALUES (?, ?, ?, ?)
            ''', entry)  # The entry parameter is a tuple containing the values to be inserted
        
    # Method to log the usage event into the 'usage' table
    def log_usage(self, timestamp, filter_type):
        # Use a context manager to handle the database connection
        with self.conn:
            # Execute a SQL command to insert the timestamp and filter type into the 'usage' table
            self.conn.execute('''
                INSERT INTO usage (timestamp, filter_type) 
                VALUES (?, ?)
            ''', (timestamp, filter_type))  # The parameters are the timestamp and filter type of the usage event
        
    # Method to fetch all entries from the 'entries' table
    def fetch_all_entries(self):
        # Create a cursor object to interact with the database
        cursor = self.conn.cursor()
        # Execute a SQL command to select all relevant columns from the 'entries' table
        cursor.execute('SELECT number, title, points, comments FROM entries')
        # Fetch all the results and return them as a list of tuples
        return cursor.fetchall()
