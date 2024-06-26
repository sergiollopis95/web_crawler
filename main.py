# Import the Scraper and Filters classes from the crawler module.
from crawler.scraper import Scraper
from crawler.filters import Filters

def main():
    # Initialize the scraper by creating an instance of the Scraper class.
    scraper = Scraper()
    
    # Use the scraper to scrape the website and store the entries in the database.
    scraper.scrape_and_store()
    
    # Fetch all the stored entries from the database.
    entries = scraper.db.fetch_all_entries()
    
    # Prompt the user to enter the type of filter they want to apply (comments or points).
    filter_type = input("Enter filter type (comments/points): ").strip()
    
    # Check which filter type the user selected and apply the corresponding filter.
    if filter_type == 'comments':
        # Filter the entries by the number of comments and log this action.
        filtered_entries = Filters.filter_by_comments(entries)
        scraper.log_usage('filter_by_comments')
    elif filter_type == 'points':
        # Filter the entries by the number of points and log this action.
        filtered_entries = Filters.filter_by_points(entries)
        scraper.log_usage('filter_by_points')
    else:
        # If the user enters an invalid filter type, print an error message and exit.
        print("Invalid filter type.")
        return

    # Print out each of the filtered entries.
    for entry in filtered_entries:
        print(entry)

# Check if this script is being run directly (as opposed to being imported).
if __name__ == '__main__':
    # If so, call the main function to run the script.
    main()
