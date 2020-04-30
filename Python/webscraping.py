from bs4 import BeautifulSoup

import requests, re
data = requests.get('https://www.nike.com/t/air-force-1-07-mens-shoe-TjqcX1/CJ0952-100').content
soup = BeautifulSoup(data, "html.parser")
span = soup.find("h1", {"class":"product_information_title___2rG9M product_title gl-heading gl-heading--m"})
title = span.text
span = soup.find("span", {"class":"gl-price__value gl-price__value--sale"})
price = span.text

print("item %s has price of %s" % (title, price))

#print(type(soup))
#print(soup.prettify()[:100])
#for link in soup.find_all('a'): print(link.get('href'))
