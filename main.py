# INF601 - Advanced Programming in Python
# Lindsey Jimenez
# Mini Project 1

import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt

# Empty arrays for each ticker
msftPrices = []
tlryPrices = []
gmePrices = []
nvdaPrices = []
abnbPrices = []

# Data download for MSFT
msftdata = yf.download("MSFT", start="2022-09-02", end="2022-09-18")
for prices in msftdata['Adj Close']:
    msftPrices.append(prices)

# Data download for TLRY
tlrydata = yf.download("TLRY", start="2022-09-02", end="2022-09-18")
for prices in tlrydata['Adj Close']:
    tlryPrices.append(prices)

# Data download for GME
gmedata = yf.download("GME", start="2022-09-02", end="2022-09-18")
for prices in gmedata['Adj Close']:
    gmePrices.append(prices)

# Data download for NVDA
nvdadata = yf.download("NVDA", start="2022-09-02", end="2022-09-18")
for prices in nvdadata['Adj Close']:
    nvdaPrices.append(prices)

# Data download for ABNB
abnbdata = yf.download("ABNB", start="2022-09-02", end="2022-09-18")
for prices in abnbdata['Adj Close']:
    abnbPrices.append(prices)

# Prints each price array
print(msftPrices)
print(tlryPrices)
print(gmePrices)
print(nvdaPrices)
print(abnbPrices)

# Create a NumPy arrays
msftarray = np.array(msftPrices)
tlryarray = np.array(tlryPrices)
gmearray = np.array(gmePrices)
nvdaarray = np.array(nvdaPrices)
abnbarray = np.array(abnbPrices)


# Create matplotlib graph MSFT
fig1 = plt.figure("MSFT")
plt.title("Microsoft : MSFT")
plt.plot(msftarray, 'bo-')
# Saves image and shows
plt.savefig("charts/msft.png")
plt.show()

# Create matplotlib graph TLRY and show
fig2 = plt.figure("TLRY")
plt.title("Tilray : TLRY")
plt.plot(tlryarray, 'bo-')
# Saves image and shows
plt.savefig("charts/tlry.png")
plt.show()

# Create matplotlib graph GME and show
fig3 = plt.figure("GME")
plt.title("GameStop : GME")
plt.plot(gmearray, 'bo-')
# Saves image and shows
plt.savefig("charts/gme.png")
plt.show()

# Create matplotlib graph NVDA and show
fig4 = plt.figure("NVDA")
plt.title("Nvidia : NVDA")
plt.plot(nvdaarray, 'bo-')
# Saves image and shows
plt.savefig("charts/nvda.png")
plt.show()

# Create matplotlib graph ABNB and show
fig5 = plt.figure("ABNB")
plt.title("Airbnb : ABNB")
plt.plot(abnbPrices, 'bo-')
# Saves image and shows
plt.savefig("charts/airbnb.png")
plt.show()



