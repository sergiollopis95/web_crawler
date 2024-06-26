import requests
from bs4 import BeautifulSoup

# URL to scrape
url = 'http://example.com'

# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the content of the page
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Example: Extract the title of the page
    title = soup.title.string
    print(f'Title of the page: {title}')
    
    # Example: Extract all links on the page
    links = soup.find_all('a')
    for link in links:
        print(link.get('href'))
else:
    print(f'Failed to retrieve the page. Status code: {response.status_code}')
