import requests
url= "https://books.toscrape.com/"
from bs4 import beautifulsoup

response = requests.get(url)
print(response.status_code)

soup = beautifulsoup(
    response.text,
    "html.parse"
)

print(soup.title.text)


books = soup.find_all()