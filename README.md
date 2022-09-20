### INF601 - Advanced Programming in Python
#### *Lindsey Jimenez*
# **Mini Project 1**

> This project downloads the closing price for five stock tickers (MSFT, TLRY, GME, AVDA, ABNB)
> over a span of ten days. It uses this data to creates five line charts to display the information.

## Prequisites
Before you begin, ensure you have met the following requirements:
> * You have installed the latest version of python
> * You have installed all required plugins `pip install -r requirements.txt`

## Using Mini Project 1 
To use Mini Project 1, follow these steps:
> * Create and empty array for your ticker prices `tickerPrice = []`
> * Download the tickers data for specified date range and store it in a variable `tickerData = yf.download("tickerName", start="2022-09-02", end="2022-09-18")`
> * Create a loop to adjust each tickers closing price and add the value to your array `for prices in tickerData['Adj Close']:
    tickerPrice.append(prices)`
> * Print the array `print(msftPrices)`
> * Create NumPy array `tickerarray = np.array(tickerPrices)`
> * Create mathplotlib graph `plt.plot(tickerarray)`
> * Customize as desired, ie. `plt.plot(msftarray, 'bo-')` or `plt.title("Microsoft : MSFT")`
> * Save the chart as a png `plt.savefig("charts/msft.png")`
> * Show the chart `plt.show()`

## Contributing to Mini Project 1
To contribute to Mini Project 1, follow these steps:

1. Fork this repository.
2. Create a branch: `git checkout -b <branch_name>`.
3. Make your changes and commit them: `git commit -m '<commit_message>'`
4. Push to the original branch: `git push origin <project_name>/<location>`
5. Create the pull request.

Alternatively see the GitHub documentation on [creating a pull request](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request).

## Contributors
Thanks to the following people who have contributed: 
* [@linnyelijim](https://github.com/linnyelijim) 