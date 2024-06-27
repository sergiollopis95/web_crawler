# web_crawler
Web crawler using Python, utilizing the `requests` and `BeautifulSoup` libraries for web scraping, `tabulate` for creating table grids, `SQLite` for data storage, filtering functionality, and usage data logging.

> **Note**: Ensure you have [Python](https://www.python.org/downloads/) installed on your system before starting with this project.

# Project Overview

## Directory Structure

- `crawler/`: Contains the main scraper, filter, and storage logic.
- `tests/`: Contains unit tests for the components.
- `main.py`: Entry point for running the scraper and filtering entries.
- `requirements.txt`: Lists the Python dependencies.
- `README.md`: Project documentation.

> **Alert**: Make sure to review the directory structure to understand where each component resides before making changes.

## Design Decisions

- **Python**: Chosen for its simplicity and powerful libraries for web scraping and database operations.
- **Libraries**: `BeautifulSoup` for parsing HTML content, `requests` for handling HTTP requests, and `tabulate` for creating table grids to properly display data.
- **SQLite**: Used for lightweight, file-based storage.
- **Object-Oriented Design**: For modular and maintainable code.
- **Logging**: Usage logs stored in the same SQLite database.

> **Note**: The use of these libraries and design decisions ensures the application is easy to maintain and extend.

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

- [x] Good object-oriented/functional code, avoiding repetition and favoring a consistent organization. Stick to the semantics of the chosen language and be as consistent as possible.
- [x] Correct usage of version control tools, with a good commit history and incremental software delivery practices.
- [x] Automated testing with any framework or tool of your choice.
- [x] Clean, well-structured code.
- [x] README file to guide through my work.
- [x] Submit the result to GitHub.

### Additional Tips

- **Environment Setup**: Use virtual environments to manage dependencies.
  ```bash
  python -m venv venv
  source venv/bin/activate  # On Windows use `venv\Scripts\activate`
  pip install -r requirements.txt

- **Running the Scraper**: To run the scraper and apply filters:

```bash
python main.py
```

- **Testing**: Run the tests to ensure everything is working as expected:

```bash
python -m unittest discover tests
```

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
│   ├── test_scraper.py
│   ├── test_filters.py
│   └── test_storage.py
├── main.py
├── requirements.txt
├── LICENSE
├── README.md
└── .gitignore

### Additional Tips

- **Environment Setup**: Use virtual environments to manage dependencies.
  ```bash
  python -m venv venv
  source venv/bin/activate  # On Windows use `venv\Scripts\activate`
  pip install -r requirements.txt

- **Running the Scraper**: To run the scraper and apply filters:

```bash
python main.py

- **Testing**: Run the tests to ensure everything is working as expected:

```bash
python -m unittest discover tests
