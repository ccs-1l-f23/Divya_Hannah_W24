from bs4 import BeautifulSoup
import csv
import requests
import urllib

results = []
page_number = 1
f = csv.writer(open('screwdriver.csv', 'w'))
url = "https://judge.me/reviews/reviews_for_widget?url=linus-tech-tips-store.myshopify.com&shop_domain=linus-tech-tips-store.myshopify.com&platform=shopify&page={page_number}&per_page=5&product_id=6692255891559"

while True:
    response = requests.get(url)
    request = urllib.request.urlopen(url)
    request.add_header('Accept-Encoding', 'utf-8')
    response = urllib.urlopen(request)

    soup = BeautifulSoup(response.read().decode('utf-8', 'ignore'))
    results.append(soup)

    f.writerow(['Numerical Ratings:'])

    for numerical_rating in soup.find_all():
        if "data-score" in numerical_rating.attrs:
            content = numerical_rating["data-score"]
            print(content)
            f.writerow([content])

    print("**************")
    f.writerow(['Helpful:'])

    for helpful in soup.find_all():
        if "data-thumb-up-count" in helpful.attrs:
            content = helpful["data-thumb-up-count"]
            print(content)
            f.writerow([content])

    print("**************")
    f.writerow(['Not helpful:'])

    for not_helpful in soup.find_all():
        if "data-thumb-down-count" in not_helpful.attrs:
            content = not_helpful["data-thumb-up-count"]
            print(content)
            f.writerow([content])
        
    print("**************")
    f.writerow(['Written Reviews:'])

    for review_data in soup.find_all('div', attrs = {"class":"jdgm-rev__content"}):
        if (review_data.find("p")):
            content = review_data.find("p").text
            print(content)
            print("-----")
            f.writerow([content])

    if page_number == 61:
        break

    page_number = page_number + 1