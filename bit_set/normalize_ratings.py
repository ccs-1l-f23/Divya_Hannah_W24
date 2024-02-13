import pandas as pd
from sklearn.preprocessing import StandardScaler
import numpy as np
import csv

ratings = []
revised_ratings = []
with open('bit_csv/scraped_bit_reviews.csv') as html_obj:
    found_ratings = False
    for line in html_obj:
        if "Helpful" in line:
            found_ratings = False
        if found_ratings:
            ratings.append(line)
        if "Numerical Ratings" in line:
            found_ratings = True

    for rating in ratings:
        rating = rating.replace('\n', ' ')
        revised_rating = int(rating)
        revised_ratings.append(revised_rating)

    revised_ratings = np.array(revised_ratings)

    print(revised_ratings)
    # print(len(revised_ratings))

### Normalizing Star Reviews

data = revised_ratings.reshape(-1,1)
print(data)

scaler = StandardScaler()
print(scaler.fit(data))
print(scaler.mean_)
# print(scaler.transform(data))

