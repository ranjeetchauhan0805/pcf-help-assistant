import requests
from bs4 import BeautifulSoup

def scrape_page(url, filename):
    response = requests.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")
    text = soup.get_text(separator="\n", strip=True)
    with open("data/raw/" + filename, "w", encoding="utf-8") as f:
        f.write(text)
    print(text[:500])

if __name__ == "__main__":
    scrape_page("https://www.positivechangefoundation.com/about", "about.txt")