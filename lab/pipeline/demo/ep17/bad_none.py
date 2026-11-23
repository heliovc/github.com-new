import requests
from bs4 import BeautifulSoup

url = "http://localhost:8000/catalog/page-1.html"
soup = BeautifulSoup(requests.get(url, timeout=10).text, "html.parser")

for book in soup.select("article.book"):
    price = book.select_one(".prices").get_text(strip=True)
    print(price)
