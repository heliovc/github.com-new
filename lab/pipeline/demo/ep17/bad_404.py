import requests

url = "http://localhost:8000/catalog/page-4.html"
response = requests.get(url, timeout=10)
print(response.status_code)
response.raise_for_status()
