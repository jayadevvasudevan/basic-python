import requests
from bs4 import BeautifulSoup

def scrape_quotes(url):
    # Send a GET request to the URL
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the content of the page with BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Find all quote elements on the page
        quotes = soup.find_all('div', class_='quote')
        
        # Extract the text and author for each quote
        scraped_quotes = []
        for quote in quotes:
            text = quote.find('span', class_='text').get_text()
            author = quote.find('small', class_='author').get_text()
            scraped_quotes.append({'text': text, 'author': author})
        
        return scraped_quotes
    else:
        print("Failed to retrieve the webpage.")
        return []

if __name__ == "__main__":
    url = "http://quotes.toscrape.com"
    quotes = scrape_quotes(url)
    
    for idx, quote in enumerate(quotes, start=1):
        print(f"Quote {idx}: '{quote['text']}' by {quote['author']}")
