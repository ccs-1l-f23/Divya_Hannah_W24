from selenium import webdriver
from selenium.webdriver.common.by import By
import time    

from bs4 import BeautifulSoup
import requests
import csv

url = "https://www.hollisterco.com/shop/us/p/feel-good-oversized-zip-up-hoodie-55075320?categoryId=12631&faceout=model&seq=10"

data = requests.get(url)

soup = BeautifulSoup(data.text, "html.parser")

pretty_html = soup.prettify()

# Create a file to write to
f = csv.writer(open('hoodie.csv', 'w'))
f.writerow(['Verified Buyer', 'Numerical Rating', 'Helpful', 'Not Helpful', 'Written Review'])

#################

driver = webdriver.Chrome()
driver.get('https://www.hollisterco.com/shop/us/p/feel-good-oversized-zip-up-hoodie-55075320?categoryId=12631&faceout=model&seq=10')
driver.maximize_window()
time.sleep(1)

# cookie = driver.find_element_by_xpath('//button[@id="Cookies-button"]')

# try:
#     cookie.click()
# except:
#     pass

for _ in range(60):
    for review_data in soup.find_all('div', attrs = {"class":"jdgm-rev__content"}):
        if (review_data.find("p")):
            content = review_data.find("p").text
            print(content)
            print("***********************")
            f.writerow([content])

    next_page = driver.find_element(By.CLASS_NAME, "jdgm-paginate__page jdgm-paginate__next-page")
    next_page.click()
    time.sleep(3)