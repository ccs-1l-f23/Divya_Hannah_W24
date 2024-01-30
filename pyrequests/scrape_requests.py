# import requests
# from requests_html import HTMLSession
# from bs4 import BeautifulSoup

# response = requests.get('https://judge.me/reviews/reviews_for_widget?url=linus-tech-tips-store.myshopify.com&shop_domain=linus-tech-tips-store.myshopify.com&platform=shopify&page=2&per_page=5&product_id=6692255891559')

# soup = BeautifulSoup(response.text, 'html.parser')
# print(soup)


import requests
from bs4 import BeautifulSoup
import csv

results = []
page_number = 1

while True:
    response = requests.get(f"https://judge.me/reviews/reviews_for_widget?url=linus-tech-tips-store.myshopify.com&shop_domain=linus-tech-tips-store.myshopify.com&platform=shopify&page={page_number}&per_page=5&product_id=6692255891559")

    soup = BeautifulSoup(response.content, 'html.parser')
    # text = soup.find_all("class":"jdgm-rev__body")
    results.append(soup)

    if page_number == 61:
        break

    page_number = page_number + 1

print(results)

with open('reviews.csv', 'a') as csv_file:
 writer = csv.writer(csv_file)
 for result in results:
    writer.writerow(result)






