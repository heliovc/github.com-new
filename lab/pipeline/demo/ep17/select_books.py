import requests
from bs4 import BeautifulSoup

url = "http://localhost:8000/catalog/page-1.html"
response = requests.get(url, timeout=10)
soup = BeautifulSoup(response.text, "html.parser")

books = soup.select("article.book")
print(len(books), "books found")

for book in books:
    title = book.select_one(".title").get_text(strip=True)
    price = book.select_one(".price").get_text(strip=True)
    print(title, "|", price)
