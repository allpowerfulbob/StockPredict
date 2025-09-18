# Import required modules
import requests
import csv
import pandas as pd
import json


# url to download data, replace the API Key with your own
url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=AMZN&apikey=QJZ37Q0YG6D3I1Y8'
r = requests.get(url)
data = r.json()

df = open('c:/users/allpo/desktop/content/amzn_stock_data.csv', 'w', newline='')
cw = csv.writer(df)

c = 0
for stock_data in data:
    if c == 0:
        header = data.keys()
        cw.writerow(header)
        c += 1
        cw.writerow(stock_data.values())

df.close
