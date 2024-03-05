# News API Search Script

This Python script utilizes the News API to search for news articles based on a given query and start date.

## Requirements

- Python 3.x
- Requests library (install via `pip install requests`)
- News API key (get from https://newsapi.org/)

## Usage

1. Clone or download the repository.
2. Install the required dependencies (`pip install requests`).
3. Obtain a News API key from https://newsapi.org/ and replace `'YOUR_API_KEY'` in the script with your actual API key.
4. Run the script (`python news_search.py`) and follow the prompts to enter the search query and start date.

## Script Details

- The script prompts the user to input a search query and start date (in the format YYYY-MM-DD).
- It sends a request to the News API to retrieve news articles based on the provided query and start date.
- The script prints the title, description, URL, and published date of each article found.
- It also checks for rate limit headers in the API response to display rate limit information.

## Credits

This script uses the News API (https://newsapi.org/) to retrieve news articles.

