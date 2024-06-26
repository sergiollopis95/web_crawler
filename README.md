# web_crawler
Web crawler using Python, utilizing the `requests` and `BeautifulSoup` libraries for web scraping, SQLite for data storage, filtering functionality and usage data logging.

# Project Overview

## Directory Structure

- `crawler/`: Contains the main scraper, filter, and storage logic.
- `tests/`: Contains unit tests for the components.
- `main.py`: Entry point for running the scraper and filtering entries.
- `requirements.txt`: Lists the Python dependencies.
- `README.md`: Project documentation.

## Design Decisions

- **Python**: Chosen for its simplicity and powerful libraries for web scraping and database operations.
- **SQLite**: Used for lightweight, file-based storage.
- **Object-Oriented Design**: For modular and maintainable code.
- **Logging**: Usage logs stored in the same SQLite database.

# Project Setup

### Starters
- [x] Create Project Structure

### Business Logic
- [x] Filter all previous entries with more than five words in the title ordered by the number of comments first.
- [x] Filter all previous entries with less than or equal to five words in the title ordered by points.
- [x] Store usage data in SQLite, including at least the request timestamp and a field to identify the applied filter type.
- [x] Brief documentation explaining the key design decisions I made.
- [x] Commenting my code throughout.

### Bonus Points

- [x] Good object-oriented/functional code, avoiding repetition and favoring a consistent organization. Stick to the semantics of chosen language and be as consistent as possible.
- [x] Correct usage of version control tools, with a good commit history and incremental software delivery practices.
- [ ] Automated testing with any framework or tool of your choice.
- [x] Clean, well-structured code and who can creatively solve problems.
- [x] README file to guide through my work.
- [x] Submit the result to GitHub.

## Project Structure

```plaintext
WEB_CRAWLER/
├── crawler
│   ├── __init__.py
│   ├── scraper.py
│   ├── filters.py
│   └── storage.py
├── tests
│   ├── __init__.py
│   ├── test_scraper
│   ├── test_filters.py
│   └── test_storage.py
├── main.py
├── requirements.txt
├── LICENSE
├── README.md
└── .gitignore

