import requests

url = "http://localhost:8000/catalog/reviews.json"
reviews = requests.get(url, timeout=10).json()

for review in reviews:
    print(review["stars"], review["text"])
