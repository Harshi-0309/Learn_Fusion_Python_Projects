import requests
from bs4 import BeautifulSoup
url="https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets"

r=requests.get(url)
soup=BeautifulSoup(r.text,"lxml")
#print(soup.find('div'))
price=soup.find("h4",{"class":"price float-end card-title pull-right"})
print(price.string)
desc=(soup.find("p",{"class":"description card-text"}))
print(desc.string)
a=soup.find("p",class_="description card-text")
print(a.string)

