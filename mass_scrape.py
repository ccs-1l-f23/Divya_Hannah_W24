from selenium import webdriver
import time                                                                                                                                                                                                                                                            

driver = webdriver.Chrome()
driver.get('https://www.lttstore.com/products/bits')
driver.maximize_window()
time.sleep(1)

cookie = driver.find_element_by_xpath('//button[@id="Cookies-button"]')

try:
    cookie.click()
except:
    pass

