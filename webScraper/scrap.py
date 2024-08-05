import requests
from bs4 import BeautifulSoup
url="https://kaashiv.com/"
r=requests.get(url)
soup=BeautifulSoup(r.text,"html.parser")
print(soup.find("title"))
print(soup.find("title").string)
print(soup.find(id="hero"))
print(soup.find(class_="banner"))
print(soup.find("a",class_="courses__content__title"))
print(soup.find("a",class_="courses__content__title").string)
print(soup.find_all("a",class_="courses__content__title"))
on_intern=soup.find_all("a",class_="courses__content__title")
for i in on_intern:
    print(i.prettify(),end="\n\n")
for i in on_intern:
    print(i.string)
for i in on_intern:
    print(i)
intern=soup.find_all("div",class_="courses__wapper")
for j in intern:
    print(j.prettify,end="\n\n")

for j in intern:
    image=j.find("img",class_="courses__top__image")
    link=j.find("a",class_="courses__content__title")
    price=j.find("div",class_="courses__col-right courses__content__price")
    print("Course:",link.text)
    print("image:",image['src'])
    print("fees:",price.text,end="\n\n")