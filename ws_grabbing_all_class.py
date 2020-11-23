import bs4
import requests

res = requests.get("https://en.wikipedia.org/wiki/Extraction_(2020_film)")

soup = bs4.BeautifulSoup(res.text, "lxml")

# selecting the class from the website
soup.select('.mw-content-text')
print(soup)

# To iterate upon multiple classes
for item in soup.select('.vector-menu-content'):
    print(item.text)
