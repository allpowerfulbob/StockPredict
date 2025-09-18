# Import required modules
import requests
import csv
import pandas as pd
import json
from cryptography.fernet import Fernet

key = Fernet.generate_key()
fernet = Fernet(key)

# url to download data
url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=AMZN&apikey=QJZ37Q0YG6D3I1Y8'
r = requests.get(url)
data = r.json()

# Write to csv
with open('c:/users/allpo/desktop/content/amzn_stock_data.csv', 'w', newline='') as amzn_stock_data:
    writer = csv.writer(amzn_stock_data)
    writer.writerows(data)