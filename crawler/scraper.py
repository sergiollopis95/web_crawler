import requests  # Import the requests library to handle HTTP requests
from bs4 import BeautifulSoup  # Import BeautifulSoup from bs4 to parse HTML content
import re  # Import the regular expressions library for string matching
from .storage import Database  # Import the custom Database class from the storage module
from datetime import datetime  # Import datetime for handling date and time

class Scraper:
    # Define the base URL for the Hacker News website
    BASE_URL = "https://news.ycombinator.com/"

    def __init__(self, db_path='crawler.db'):
        # Initialize the Database instance with the provided database path
        self.db = Database(db_path)
    
    def fetch_entries(self, limit=30):
        # Send a GET request to the base URL and get the response
        response = requests.get(self.BASE_URL)
        # Parse the HTML content of the response using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')
        # Initialize an empty list to store the entries
        entries = []
        # Select all elements with class 'athing', which represent individual news items
        items = soup.select('.athing')
        # Select all elements with class 'subtext', which contain metadata for the news items
        subtexts = soup.select('.subtext')
        
        # Iterate over the items up to the specified limit or the number of items, whichever is smaller
        for i in range(min(limit, len(items))):
            # Get the current news item
            item = items[i]
            # Get the corresponding subtext (metadata) for the current news item
            subtext = subtexts[i]
            # Extract the rank of the news item and strip the trailing period
            number = item.select_one('.rank').text.strip('.')
            # Extract the title of the news item
            title = item.select_one('.storylink').text
            # Extract the points (score) for the news item if available, otherwise set to 0
            points = int(re.search(r'(\d+)\spoints', subtext.text).group(1)) if subtext.select_one('.score') else 0
            # Extract the number of comments for the news item if available, otherwise set to 0
            comments = int(re.search(r'(\d+)\scomments', subtext.text).group(1)) if subtext.select_one('a:nth-last-child(1)') and 'comment' in subtext.select_one('a:nth-last-child(1)').text else 0
            # Append the extracted information as a tuple to the entries list
            entries.append((number, title, points, comments))
        
        # Return the list of entries
        return entries

    def store_entries(self, entries): 
        # Iterate over each entry in the list of entries
        for entry in entries:
            # Insert the entry into the database
            self.db.insert_entry(entry)

    def log_usage(self, filter_type):
        # Get the current timestamp in ISO format
        timestamp = datetime.now().isoformat()
        # Log the usage information with the timestamp and filter type in the database
        self.db.log_usage(timestamp, filter_type)

    def scrape_and_store(self):
        # Fetch the entries from the website
        entries = self.fetch_entries()
        # Store the fetched entries in the database
        self.store_entries(entries)
        # Log the usage of the scrape operation
        self.log_usage('scrape')
    
    

        
        