from bs4 import BeautifulSoup
import Divya_Hannah_W24.scrape_requests as scrape_requests
import csv
import requests


url = "https://www.lttstore.com/products/bits"
data = requests.get(url)

file = open("reviews_page2.html", "r") 
index = file.read() 

soup = BeautifulSoup(index, "html.parser")
pretty_html = soup.prettify()

# Create a file to write to
f = csv.writer(open('screwdriver.csv', 'w'))
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