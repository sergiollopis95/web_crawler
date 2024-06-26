import sqlite3

class Database:
    def __init__(self, db_path):
        self.conn = sqlite3.connect(db_path)
        
    def create_tables(self):
        with self.conn:
            self.conn.execute('''
                CREATE TABLE IF NOT EXISTS entries (
                    id INTEGER PRIMARY KEY,
                    number TEXT,
                    title TEXT,
                    points INTEGER,
                    comments INTEGER
                )
            ''')
            self.conn.execute('''
                CREATE TABLE IF NOT EXISTS usage (
                    id INTEGER PRIMARY KEY,
                    timestamp TEXT,
                    filter_type TEXT
                )
            ''')
        