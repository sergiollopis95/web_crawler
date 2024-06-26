import requests
from bs4 import BeautifulSoup
import re
from storage import Database

class Scraper:
    # Base URL for the Hacker News website
    BASE_URL = "https://news.ycombinator.com/"

    def __init__(self, db_path='crawler.db'):
        # Initialize the Database class with the provided database path
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


    '''
    TODO: 


    def store_entries(self, entries): Stores the list of entries in the DB.
    def log_usage(self, filter_type): Logs the usage - timestamp & filter type used
    def scrape_and_store(self): performs store_entries() and log_usage() methods
    
    
    '''
   