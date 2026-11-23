import requests
from bs4 import BeautifulSoup

url = "http://localhost:8000/catalog/page-1.html"
soup = BeautifulSoup(requests.get(url, timeout=10).text, "html.parser")

print(len(soup.select("#reviews .review")), "reviews found")
print(soup.select_one("#reviews").get_text())
