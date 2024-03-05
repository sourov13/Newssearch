import requests

def search_news(query, start_date, api_key, sort_by='popularity', count=5):
    endpoint = "https://newsapi.org/v2/everything"
    params = {
        "q": query,
        "from": start_date,
        "sortBy": sort_by,
        "apiKey": api_key,
        "pageSize": count,
    }

    try:
        response = requests.get(endpoint, params=params)
        
        # Check rate limit headers
        print("Rate Limit Headers:")
        print("Limit:", response.headers.get('X-RateLimit-Limit'))
        print("Remaining:", response.headers.get('X-RateLimit-Remaining'))
        print("Reset Time:", response.headers.get('X-RateLimit-Reset'))

        data = response.json()

        if data["status"] == "ok" and "articles" in data:
            for i, article in enumerate(data["articles"], start=1):
                title = article.get("title", "Title not available")
                description = article.get("description", "Description not available")
                url = article.get("url", "URL not available")
                published_at = article.get("publishedAt", "Date not available")

                print(f"Article {i}: {title}\nDescription: {description}\nURL: {url}\nPublished At: {published_at}\n")
        else:
            print("No news articles found.")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    search_query = input("Enter the search query: ")
    start_date = input("Enter the start date (YYYY-MM-DD): ")
    api_key = "aaaa1111111111112222222"  # Replace with your News API key

    search_news(search_query, start_date, api_key)
