import requests
from bs4 import BeautifulSoup


page = requests.get("http://dataquestio.github.io/web-scraping-pages/simple.html") #downloading a page
soup = BeautifulSoup(page.content, 'html.parser')
pr = (soup.find_all('p'))
print(pr[0].get_text())