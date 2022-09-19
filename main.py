#INF601 - Advanced Programming in Python
#Lindsey Jimenez
#Mini Project 1

import yfinance as yf

data = yf.download("MSFT", start="2022-09-02", end="2022-09-18")

msftPrices = []

for prices in data['Adj Close']:
    msftPrices.append(prices)

print(msftPrices)