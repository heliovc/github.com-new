import requests

url = "http://localhost:8000/catalog/page-1.html"
response = requests.get(url, timeout=10)

print(response.status_code)
print(len(response.text), "characters")
print(response.text[:160])
