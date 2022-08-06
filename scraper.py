from re import search
from unittest import result
import requests
from bs4 import BeautifulSoup as bs
import re
import pandas as pd

#get html from craigslist
r = requests.get('https://sfbay.craigslist.org/search/cta?min_price=&max_price=&auto_fuel_type=3&auto_fuel_type=4&auto_title_status=1')

#convert html to beautiful soup object
soup = bs(r.content, 'html.parser')

results = soup.find(class_="rows")
result_elems = results.find_all('li', class_="result-row")
car_info = {"Post_id":[],"Title":[], "Link":[], "Price":[]}
regex = re.compile("result-image gallery")

for row in result_elems:
    car_info['Price'].append(row.find('span', class_="result-price").text.strip())
    car_info['Link'].append(row.find('a', class_=regex)['href'])
    car_info['Title'].append(row.find('a', class_="result-title hdrlnk").text.strip())
    car_info['Post_id'].append(row['data-pid'])