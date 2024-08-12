# utils.py

import csv

def save_to_csv(filename, articles):
    """Save the articles with tags to a CSV file."""
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Title', 'Link', 'Article Text', 'Sentiment', 'Aggressiveness', 'Language'])
        for article in articles:
            writer.writerow([article['title'], article['link'], article['article_text'], article['sentiment'], article['aggressiveness'], article['language']])
        print(f"Data saved to {filename}")

def print_csv_preview(filename, num_rows=5):
    """Print a preview of the CSV file."""
    with open(filename, mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        for i, row in enumerate(reader):
            if i < num_rows:
                print(row)
