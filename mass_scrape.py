from selenium import webdriver
from selenium.webdriver.common.by import By
import time    

from bs4 import BeautifulSoup
import requests
import csv

import requests

url = "https://www.lttstore.com/products/bits"

data = requests.get(url)

soup = BeautifulSoup(data.text, "html.parser")

pretty_html = soup.prettify()

# Create a file to write to
f = csv.writer(open('screwdriver.csv', 'w'))
f.writerow(['Numerical Rating ', 'Helpful ', 'Not Helpful ', 'Written Review'])

#################

driver = webdriver.Chrome()
driver.get('https://www.lttstore.com/products/bits')
driver.maximize_window()
time.sleep(1)

cookie = driver.find_element_by_xpath('//button[@id="Cookies-button"]')

try:
    cookie.click()
except:
    pass

for _ in range(60):
    for review_data in soup.find_all('div', attrs = {"class":"jdgm-rev__rating"}):
        if (review_data.find("data-score")):
            content = review_data.find("data-score").text
            print(content + ", ")
            f.writerow([content])

    for review_data in soup.find_all('div', attrs = {"class":"jdgm-rev__content"}):
        if (review_data.find("p")):
            content = review_data.find("p").text
            print(content + ", ")
            f.writerow([content])

    next_page = driver.find_element(By.CLASS_NAME, "jdgm-paginate__page jdgm-paginate__next-page")
    next_page.click()
    time.sleep(3)