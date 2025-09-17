# Import required modules
import requests
import csv

# url to download data
url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=AMZN&apikey=QJZ37Q0YG6D3I1Y8'
r = requests.get(url)
data = r.csv()

# print the data
print(data)

# Write to csv
with open('c:/users/allpo/desktop/content/amzn_stock_data.csv', 'w', newline='') as amzn_stock_data:
    writer = csv.writer(amzn_stock_data)
    writer.writerows(data)