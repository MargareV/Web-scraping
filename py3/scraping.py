import requests
from bs4 import BeautifulSoup

page = requests.get("http://dataquestio.github.io/web-scraping-pages/simple.html") #downloading a page
#print (page) #some value - 200 = successfull, beginning with 4 or 5 indicates errors
#print(page.status_code) #checking if the download was successful
#print(page.content) #contents of the page

soup = BeautifulSoup(page.content, 'html.parser') #parsing the page and saving it to a variable
#print(soup.prettify()) # to display contents beautifully
#print (list(soup.children)) #to print different types of objects in parsed page
#print ([type(item) for item in list(soup.children)]) #to know what type each object is
html = list(soup.children)[2] #selecting object with index two from the list
#print(list(html.children)) 
body = list(html.children)[3] #as above
#print(list(body.children))
para = list(body.children)[1]
print(para.get_text()) #to print the string between tags