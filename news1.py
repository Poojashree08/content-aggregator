import requests
from bs4 import BeautifulSoup

r = requests.get("https://www.hindustantimes.com/india-news/")
soup = BeautifulSoup(r.content, 'html.parser')

newsDivs = soup.findAll("div", {"class": "media-heading headingfour"})
for n in newsDivs:
    print(n.text)