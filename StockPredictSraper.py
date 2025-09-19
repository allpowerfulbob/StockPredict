# Import required modules
import requests
import csv
import pandas as pd
import json


# url to download data, replace the API Key with your own
url = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=AMZN&interval=60min&apikey=QJZ37Q0YG6D3I1Y&datatype=csv'
r = requests.get(url)
data = pd.read_csv('c:/users/allpo/desktop/content/amzn_stock_data.csv')

df = open('c:/users/allpo/desktop/content/amzn_stock_data.csv', 'w', newline='')
fieldnames = ['Open', 'High', 'Low', 'Close', 'Volume']
cw = csv.Writer(df, fieldnames=fieldnames)
cw.writeheader()

c = 0
for stock_data in data:
    if c == 0:
        header = stock_data.keys()
        cw.writerow(header)
        c += 1
        cw.writerow(stock_data.values())

df.close
