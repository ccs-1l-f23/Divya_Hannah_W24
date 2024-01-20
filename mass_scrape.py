from selenium import webdriver
import time                                                                                                                                                                                                                                                            

driver = webdriver.Chrome(executable_path='/Users/hannahzhang/Downloads/chromedriver_mac_arm64/chromedriver.exe')
driver.get('https://www.lttstore.com/products/bits')
driver.maximize_window()
time.sleep(1)

