import requests
from bs4 import BeautifulSoup

def scrape_api_docs(url):
    try:
        response = requests.get(url, timeout=10)
        soup = BeautifulSoup(response.text, "html.parser")

        text = soup.get_text(separator=" ")

        return text[:4000]

    except Exception as e:
        return f"Error: {str(e)}"