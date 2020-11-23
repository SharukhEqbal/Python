import bs4
import requests

# response
result = requests.get("https://www.wikipedia.org/")

# complete result will come as a single string
res_text = result.text

# returns the value in same format as we see in view source
soup = bs4.BeautifulSoup(res_text, "lxml")

# Return a bs4.element.Tag
print(type(soup.select('title')))
# returns all title tag
print(soup.select('title'))

title = soup.select('title')[0].getText()

print(title)

# selects the paragraph tag in the website
paragraph_value = soup.select('p')
print(paragraph_value[0].getText())