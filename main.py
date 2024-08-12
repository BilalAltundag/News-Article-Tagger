# main.py

from scraper import fetch_articles
from tagger import tag_article
from utils import save_to_csv, print_csv_preview
import time

def main():
    base_url = "https://www.ensonhaber.com/ekonomi"
    articles = fetch_articles(base_url)

    tagged_articles = []
    for article in articles:
        if article['article_text']:
            tags = tag_article(article['article_text'])
            tagged_articles.append({
                'title': article['title'],
                'link': article['link'],
                'article_text': article['article_text'],
                'sentiment': tags.get('sentiment', 'Not Available'),
                'aggressiveness': tags.get('aggressiveness', 'Not Available'),
                'language': tags.get('language', 'Not Available')
            })
            time.sleep(3)  # Wait for 3 seconds before the next iteration

    csv_filename = 'news_articles.csv'
    save_to_csv(csv_filename, tagged_articles)
    print_csv_preview(csv_filename, num_rows=5)

if __name__ == "__main__":
    main()
