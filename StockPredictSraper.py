# Import required modules
import requests
import csv
import pandas as pd
import json


# url to download data, replace the API Key with your own
url = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=AMZN&interval=60min&apikey=QJZ37Q0YG6D3I1Y&datatype=csv'
r = requests.get(url)
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

else: dp = open('c:/users/allpo/desktop/content/amzn_stock_data.csv', 'a', newline='')
writer_obj = csv.writer(dp)
writer_obj.writerow(data)

dp.close