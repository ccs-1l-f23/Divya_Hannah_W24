from bs4 import BeautifulSoup as bs
import numpy as np
import pandas as pd
import os

html_file = open('/Users/hannahzhang/Desktop/Divya_Hannah_W24/Divya_Hannah_W24/bit_set/bit_csv/html_bit_reviews.csv', 'r')

html_content = html_file.read()
soup = bs(html_content, 'html.parser')
html_file.close()

name_list = []
star_list = []
thumbs_down_list = []
thumbs_up_list = []
reviews = []

# Names

names = soup.findAll("span", {"class": 'jdgm-rev__author'})
for element in names:
    name_list.append(element.next)

name_df = np.array(name_list)

# Star Ratings

for numerical_rating in soup.find_all():
            if "data-score" in numerical_rating.attrs:
                content = numerical_rating["data-score"]
                content = int(content)
                star_list.append(content)

# Not Helpful
                
for not_helpful in soup.find_all():
            if "data-thumb-down-count" in not_helpful.attrs:
                content = not_helpful["data-thumb-down-count"]
                content = int(content)
                thumbs_down_list.append(content)

# Helpful
                
for not_helpful in soup.find_all():
            if "data-thumb-up-count" in not_helpful.attrs:
                content = not_helpful["data-thumb-up-count"]
                content = int(content)
                thumbs_up_list.append(content)
                

# Reviews
                
for review_data in soup.find_all('div', attrs = {"class":"jdgm-rev__content"}):
        if (review_data.find("p")):
            content = review_data.find("p").text
            reviews.append(content)
            



# print(name_list)
# print(star_list)
# print(thumbs_down_list)

dict = {'Name': name_list, "Star Rating": star_list, "Thumbs Up": thumbs_up_list, "Thumbs Down": thumbs_down_list, "Review": reviews}

df = pd.DataFrame(dict)
final_df = df.to_html()

with pd.option_context('display.max_rows', None,
                       'display.max_columns', None
                       ):  
    print(final_df)

# templates/reviews.html

reviews_file = open('templates/reviews.html', 'w')
reviews_file.write(final_df)





