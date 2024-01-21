#!/usr/bin/python3
from bs4 import BeautifulSoup
import requests
import csv

url = "https://www.lttstore.com/products/bits"

data = requests.get(url)

soup = BeautifulSoup(data.text, "html.parser")

pretty_html = soup.prettify()

# print(pretty_html)

# Create a file to write to
f = csv.writer(open('screwdriver.csv', 'w'))
f.writerow(['Verified Buyer', 'Numerical Rating', 'Helpful', 'Not Helpful', 'Written Review'])

for review_data in soup.find_all('div', attrs = {"class":"jdgm-rev__content"}):
    if (review_data.find("p")):
      content = review_data.find("p").text
      print(content)
      print("***********************")
      f.writerow([content])
