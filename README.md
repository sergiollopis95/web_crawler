# web_crawler
Web crawler using Python, utilizing the `requests` and `BeautifulSoup` libraries for web scraping, SQLite for data storage, filtering functionality and usage data logging.

## Project Setup

### Starters
- [x] Create Project Structure

### Business Logic
- [ ] Filter all previous entries with more than five words in the title ordered by the number of comments first.
- [ ] Filter all previous entries with less than or equal to five words in the title ordered by points.
- [ ] Store usage data in SQLite, including at least the request timestamp and a field to identify the applied filter type.
- [ ] Brief documentation explaining the key design decisions I made.
- [ ] Well-explained comments on my code.

### Bonus Points

- [x] Good object-oriented/functional code, avoiding repetition and favoring a consistent organization. Stick to the semantics of chosen language and be as consistent as possible.
- [ ] Correct usage of version control tools, with a good commit history and incremental software delivery practices.
- [ ] Automated testing with any framework or tool of your choice.
- [ ] Clean, well-structured code and who can creatively solve problems.
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