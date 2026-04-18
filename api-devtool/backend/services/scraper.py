import requests
from bs4 import BeautifulSoup

def scrape_api_docs(url):
    try:
        headers = {
            "User-Agent": "Mozilla/5.0"
        }

        response = requests.get(url, headers=headers, timeout=10)

        soup = BeautifulSoup(response.text, "html.parser")

        # 🔥 Extract useful tags only (better than full text)
        texts = []

        for tag in soup.find_all(["h1", "h2", "h3", "p", "code"]):
            texts.append(tag.get_text(strip=True))

        cleaned_text = " ".join(texts)

        return cleaned_text[:6000]

    except Exception as e:
        return f"Error: {str(e)}"