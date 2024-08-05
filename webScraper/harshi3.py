import requests
from bs4 import BeautifulSoup
import re
url="https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets"
r=requests.get(url)
soup=BeautifulSoup(r.text,"lxml")
data=soup.find_all(["h4","a","p"])
print(data)
data1=soup.find_all(string="Galaxy Tab")
print(data1)
data3=soup.find_all(string=re.compile("Idea"))
print(data3)
print(len(data3))