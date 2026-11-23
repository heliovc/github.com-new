import time
import requests
import pandas as pd
from bs4 import BeautifulSoup
from urllib.parse import urljoin

BASE = "http://localhost:8000/catalog/page-{}.html"
rows = []

for page in range(1, 4):
    url = BASE.format(page)
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")

    for book in soup.select("article.book"):
        link = book.select_one(".title a")
        rows.append({
            "title": link.get_text(strip=True),
            "author": book.select_one(".author").get_text(strip=True).removeprefix("by "),
            "price": float(book.select_one(".price").get_text(strip=True).lstrip("$")),
            "stars": int(book.select_one(".rating")["data-stars"]),
            "in_stock": book.select_one(".stock").get_text(strip=True) == "In stock",
            "link": urljoin(url, link["href"]),
        })
    print(f"Page {page}: {len(rows)} books so far")
    time.sleep(1)

df = pd.DataFrame(rows)
df.to_csv("books.csv", index=False)
print("Saved", len(df), "books to books.csv")
