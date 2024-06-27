"""
This module defines the Scraper class for scraping data from Hacker News
and storing it in a database. It utilizes the BeautifulSoup library for
parsing HTML content, the requests library for making HTTP requests, 
and a custom Database class for database operations. Regular expressions 
are used for string matching to extract specific parts of the HTML content.

Classes:
--------
Scraper:
    A class to scrape data from Hacker News and store it in a database.

Usage:
------
To use this module, create an instance of the Scraper class and call its 
methods to fetch entries from Hacker News, store them in the database, 
and log the usage.

Example:
--------
    from crawler.scraper import Scraper

    scraper = Scraper()
    entries = scraper.fetch_entries()
    scraper.store_entries(entries)
    scraper.log_usage('example_filter')
"""

import re  # Import the regular expressions library for string matching.
from datetime import datetime  # Import datetime for handling date and time.
import requests  # Import the requests library to handle HTTP requests.
from bs4 import BeautifulSoup  # Import BeautifulSoup from bs4 to parse HTML content.
from .storage import Database  # Import the custom Database class from the storage module.


class Scraper:
    """
    A class to scrape data from Hacker News and store it in a database.
    
    Attributes:
    -----------
    BASE_URL : str
        The base URL of the Hacker News website.
    
    Methods:
    --------
    __init__(db_path='crawler.db'):
        Initializes the Scraper with a database connection.
    
    fetch_entries(limit=30):
        Fetches and parses entries from Hacker News.
    
    store_entries(entries):
        Stores the fetched entries in the database.
    
    log_usage(filter_type):
        Logs the usage information in the database.
    
    scrape_and_store():
        Orchestrates the scraping, storing, and logging operations.
    """
    BASE_URL = "https://news.ycombinator.com/"
    
    def __init__(self, db_path='crawler.db'):
        """
        Initializes the Scraper with a database connection.
        
        Parameters:
        -----------
        db_path : str, optional
            The path to the database file (default is 'crawler.db').
        """
        self.db = Database(db_path)    
        
    def fetch_entries(self, limit=30):
        """
        Fetches and parses entries from Hacker News.
        
        Parameters:
        -----------
        limit : int, optional
            The maximum number of entries to fetch (default is 30).
        
        Returns:
        --------
        list of tuple
            A list of tuples, each containing the number, title, points, and comments of a news item.
        """
        response = requests.get(self.BASE_URL, timeout=30)
        soup = BeautifulSoup(response.text, 'html.parser')
        entries = []
        items = soup.select('.athing')
        subtexts = soup.select('.subtext')
        comments = 0
        
        for i in range(min(limit, len(items))):
            item = items[i]
            subtext = subtexts[i]
            
            number = item.select_one('.rank').text.strip('.')
            title = item.select_one('.titleline').text
            clean_title = re.sub(r'\s*\([^)]*\)', '', title)
            points = int(re.search(r'(\d+)\spoints', subtext.text).group(1)) if subtext.select_one('.score') else 0

            comments_link = subtext.find_all('a', string=re.compile(r'\d+\scomments'))

            if comments_link:
                comments_text = comments_link[0].text
                comments_match = re.search(r'(\d+)\scomments', comments_text.replace('\xa0', ' '))
                if comments_match:
                    comments = int(comments_match.group(1))
                    
            entries.append((number, clean_title, points, comments))
        
        return entries

    def store_entries(self, entries):
        """
        Stores the fetched entries in the database.
        
        Parameters:
        -----------
        entries : list of tuple
            A list of tuples, each containing the number, title, points, and comments of a news item.
        """
        for entry in entries:
            self.db.insert_entry(entry)

    def log_usage(self, filter_type):
        """
        Logs the usage information in the database.
        
        Parameters:
        -----------
        filter_type : str
            The type of filter applied during the scrape operation.
        """
        timestamp = datetime.now().isoformat()
        self.db.log_usage(timestamp, filter_type)

    def scrape_and_store(self):
        """
        Orchestrates the scraping, storing, and logging operations.
        """
        entries = self.fetch_entries()
        self.store_entries(entries)
        self.log_usage('scrape')
