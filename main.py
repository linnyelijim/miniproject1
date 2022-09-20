# INF601 - Advanced Programming in Python
# Lindsey Jimenez
# Mini Project 1

import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt

msftPrices = []
tlryPrices = []
gmePrices = []
nvdaPrices = []
abnbPrices = []

msftdata = yf.download("MSFT", start="2022-09-02", end="2022-09-18")
for prices in msftdata['Adj Close']:
    msftPrices.append(prices)

tlrydata = yf.download("TLRY", start="2022-09-02", end="2022-09-18")
for prices in tlrydata['Adj Close']:
    tlryPrices.append(prices)

gmedata = yf.download("GME", start="2022-09-02", end="2022-09-18")
for prices in gmedata['Adj Close']:
    gmePrices.append(prices)

nvdadata = yf.download("NVDA", start="2022-09-02", end="2022-09-18")
for prices in nvdadata['Adj Close']:
    nvdaPrices.append(prices)

abnbdata = yf.download("ABNB", start="2022-09-02", end="2022-09-18")
for prices in abnbdata['Adj Close']:
    abnbPrices.append(prices)

print(msftPrices)
print(tlryPrices)
print(gmePrices)
print(nvdaPrices)
print(abnbPrices)

# Create a NumPy array
msftarray = np.array(msftPrices)
tlryarray = np.array(tlryPrices)
gmearray = np.array(gmePrices)
nvdaarray = np.array(nvdaPrices)
abnbarray = np.array(abnbPrices)

# Create matplotlib graph
plt.plot(msftarray)
plt.plot(tlryarray)
plt.plot(gmearray)
plt.plot(nvdaarray)
plt.plot(abnbPrices)

# Show the graph
plt.show()


