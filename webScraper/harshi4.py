import requests
import pandas as pd
from bs4 import BeautifulSoup

url="https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets"
r=requests.get(url)
soup=BeautifulSoup(r.text,"lxml")
names=soup.find_all("a",class_="title")
print(names)
product_name=[]
for i in names:
    name=i.text
    product_name.append(name)
print(product_name)
prices=soup.find_all("h4",class_="price float-end card-title pull-right")
prices_list=[]
for i in prices:
    price=i.text
    prices_list.append(price)
print(prices_list)
desc=soup.find_all("p",class_="description card-text")
desc_list=[]
for i in desc:
    des=i.text
    desc_list.append(des)
print(desc_list)
reviews=soup.find_all("p",class_="review-count float-end")
reviews_list=[]
for i in reviews:
    rew=i.text
    reviews_list.append(rew)
print(reviews_list)
df=pd.DataFrame({"Product Name": product_name,"Prices":prices_list,"Desciption":desc_list,"Number of reviews":reviews_list})
print(df)
df.to_excel("product_details.xls")

