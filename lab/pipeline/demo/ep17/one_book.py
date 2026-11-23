import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

url = "http://localhost:8000/catalog/page-1.html"
soup = BeautifulSoup(requests.get(url, timeout=10).text, "html.parser")
book = soup.select_one("article.book")

link = book.select_one(".title a")
print(link.get_text(strip=True))
print(link["href"])
print(urljoin(url, link["href"]))
print(book.select_one(".rating")["data-stars"])
print(float(book.select_one(".price").get_text(strip=True).lstrip("$")))
