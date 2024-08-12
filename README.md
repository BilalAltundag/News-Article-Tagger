# News Article Tagger

## Project Overview

The News Article Tagger is a Python project that scrapes news articles from a specified website, analyzes their content using a language model, and classifies each article based on sentiment, aggressiveness, and language. The results are then exported to a CSV file for further analysis.

## Features

- **Web Scraping:** Extracts news article titles, links, and content from a specified news website.
- **Text Classification:** Utilizes a language model to determine the sentiment, aggressiveness, and language of each article.
- **CSV Export:** Saves the classified articles and their metadata to a CSV file for easy review and analysis.

## How It Works

1. **Scraping:** The `scraper.py` module fetches news articles from the given base URL and extracts their content.
2. **Tagging:** The `tagger.py` module uses a language model to classify the articles based on sentiment, aggressiveness, and language.
3. **Saving:** The `utils.py` module saves the classified data to a CSV file and prints a preview of the results.
4. **Execution:** The `main.py` module integrates the scraping, tagging, and saving processes into a seamless workflow.

## Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/yourusername/your-repo-name.git
   ```
Navigate to the Project Directory:

```bash
cd your-repo-name
```
Install Required Libraries: Ensure you have Python installed, then install the required libraries:
basic

```
pip install -r requirements.txt
```
Create a requirements.txt file with the following content:

```
langchain_core
langchain_openai
langchain_google_genai
langchain_community
requests
beautifulsoup4
```

Set Up Environment Variables: Add your Google API key to your environment variables:

```
export GOOGLE_API_KEY='your-google-api-key'
```

Usage
To run the script and start the article scraping and classification process:


```
python main.py
Contributing
Contributions are welcome! Please submit issues, feature requests, or pull requests. Ensure your changes are well-documented and tested.
```

License
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgments
LangChain for the language model integration.
BeautifulSoup for web scraping.
Requests for HTTP requests.

### Notes:

- **Replace `yourusername` and `your-repo-name`** with your actual GitHub username and repository name.
- **Replace `'your-google-api-key'`** with your actual Google API key.
- **Add a LICENSE file** if your project is open-source, specifying the license terms. 

This `README.md` provides a comprehensive overview of your project, installation instructions, usage guidelines, and contribution details.
