import requests
from bs4 import BeautifulSoup

url = "https://seths.blog/top-100/"
response = requests.get(url)
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")

headings = soup.find_all("h4")
for heading in headings:
    print(heading.text.strip())
