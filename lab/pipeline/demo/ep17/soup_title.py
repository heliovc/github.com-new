import requests
from bs4 import BeautifulSoup

url = "http://localhost:8000/catalog/page-1.html"
response = requests.get(url, timeout=10)
soup = BeautifulSoup(response.text, "html.parser")

print(soup.title.get_text())
print(soup.find("h2").get_text())
