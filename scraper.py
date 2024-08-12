# scraper.py

import requests
from bs4 import BeautifulSoup
import time

def get_article_text(url):
    """Extract the text of an article from a URL."""
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    article_div = soup.find('div', class_='column column-article')
    return article_div.get_text(strip=True) if article_div else "İçerik bulunamadı."

def fetch_articles(base_url):
    """Fetch articles from the base URL and return a list of article data."""
    response = requests.get(base_url)
    soup = BeautifulSoup(response.text, "html.parser")
    news_items = soup.select('section.mb-30 div.list.type-3 div.item')

    articles = []
    for item in news_items:
        title = item.find('h3').get_text(strip=True)
        link = item.find('a')['href']
        full_link = f"https://www.ensonhaber.com{link}"
        article_text = get_article_text(full_link)
        articles.append({
            'title': title,
            'link': full_link,
            'article_text': article_text
        })
        time.sleep(3)  # Wait for 3 seconds between requests
    return articles
