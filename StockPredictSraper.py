# Import required modules
import requests
import csv
import pandas as pd
import json
import urllib.parse

# Ask user to insert a stock to track
params = input("What stock would you like to get data for?")

# Use urllib to amend the url with params
passed_params = urllib.parse.urlencode(params)
first_part_final_url = f'{https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=}'
second_part_final_url = f'&interval=60min&apikey=QJZ37Q0YG6D3I1Y&datatype=csv'
final_url = (first_part_final_url) + (passed_params) + (second_part_final_url)
# url to download data, replace the API Key with your own
r = requests.get(final_url)
data = open('c:/users/allpo/desktop/content/amzn_stock_data.csv', 'w', newline='')

cw = csv.writer(data)

c = 0
for stock_data in data:
    if c == 0:
        header = stock_data.keys()
        cw.writerow(header)
        c += 1
        cw.writerow(stock_data.values())

    data.close

else: ad = open('c:/users/allpo/desktop/content/amzn_stock_data.csv', 'a', newline='')
writer_obj = csv.writer(ad)
writer_obj.writerow(data)

ad.close