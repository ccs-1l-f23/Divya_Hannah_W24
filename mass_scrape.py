from selenium import webdriver
from selenium.webdriver.common.by import By
import time    
from selenium.webdriver.common.action_chains import ActionChains

from bs4 import BeautifulSoup
import scrape_requests
import csv

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


import requests

url = "https://www.lttstore.com/products/bits"

data = scrape_requests.get(url)

soup = BeautifulSoup(data.text, "html.parser")

pretty_html = soup.prettify()

# Create a file to write to
f = csv.writer(open('screwdriver.csv', 'w'))
f.writerow(['Verified Buyer', 'Numerical Rating', 'Helpful', 'Not Helpful', 'Written Review'])

#################

driver = webdriver.Chrome()

driver.get('https://www.lttstore.com/products/bits')
driver.maximize_window()
time.sleep(1)

cookie = driver.find_element("xpath", '//button[@id="Cookies-button"]')

try:
    cookie.click()
except:
    pass

for _ in range(60):
    for review_data in soup.find_all('div', attrs = {"class":"jdgm-rev__content"}):
        if (review_data.find("p")):
            content = review_data.find("p").text
            print(content)
            print("***********************")
            f.writerow([content])
    
    driver.implicitly_wait(20)

    print("Finding next button")
    next_page = driver.find_element(By.CSS_SELECTOR, '.jdgm-paginate__next-page')
    print("Element is visible? " + str(next_page.is_displayed()))
    print("Location:", next_page.location)
    print("Aria Role:", next_page.aria_role)
    print(next_page.get_attribute("data-page"))
    ActionChains(driver).move_to_element(next_page).perform()
    print("Element is visible? " + str(next_page.is_displayed()))
    # next_page = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.jdgm-paginate__next-page')))
    next_page.click()
    print("Next button found: ", next_page)
    print("Next page has been clicked")

    time.sleep(3)

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time    
# from selenium.webdriver.common.action_chains import ActionChains

# from bs4 import BeautifulSoup
# import requests
# import csv

# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC


# url = "https://judge.me/reviews/linus-tech-tips-store.myshopify.com/products/bits"

# data = requests.get(url)

# soup = BeautifulSoup(data.text, "html.parser")

# pretty_html = soup.prettify()

# # Create a file to write to
# f = csv.writer(open('screwdriver.csv', 'w'))
# f.writerow(['Verified Buyer', 'Numerical Rating', 'Helpful', 'Not Helpful', 'Written Review'])

# #################

# driver = webdriver.Chrome()

# driver.get('https://judge.me/reviews/linus-tech-tips-store.myshopify.com/products/bits')
# driver.maximize_window()
# time.sleep(1)

# cookie = driver.find_element(By.CLASS_NAME, "jm-cookie-bar__button")

# try:
#     cookie.click()
# except:
#     pass

# for _ in range(60):
#     for review_data in soup.find_all('div', attrs = {"class":"review__body"}):
#         if (review_data.find("p")):
#             content = review_data.find("p").text
#             print(content)
#             print("***********************")
#             f.writerow([content])
    
#     driver.implicitly_wait(20)

#     print("Finding next button")
#     next_page = driver.find_element(By.CSS_SELECTOR, '.pagination__page-number--icon')
#     print("Element is visible? " + str(next_page.is_displayed()))
#     print("Location:", next_page.location)
#     print("Aria Role:", next_page.aria_role)
#     # print(next_page.get_attribute("data-page"))
#     ActionChains(driver).move_to_element(next_page).perform()
#     print("Element is visible? " + str(next_page.is_displayed()))
#     # next_page = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.jdgm-paginate__next-page')))
#     next_page.click()
#     print("Next button found: ", next_page)
#     print("Next page has been clicked")

#     time.sleep(3)

