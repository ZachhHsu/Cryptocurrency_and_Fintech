import math as ma
import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf

tickers = ['BTC-USD', 'ETH-USD', '^GSPC', '^IXIC']
prices = yf.download(tickers, '2018-01-01', '2022-04-01')['Adj Close']

# Remove a day if there is no price in either S&P500 or Ether on that day
for t in prices.index:
    sp500_price = prices.loc[t, '^GSPC']
    eth_price = prices.loc[t, 'ETH-USD']
    if ma.isnan(sp500_price) or ma.isnan(eth_price):
        prices = prices.drop(index=t)
    
# Plot the prices
prices.plot()
plt.legend(loc='upper left')
plt.xticks(rotation = 20)
plt.grid(True)
plt.show()

# Stock returns
rets = prices.pct_change()

# Average daily returns
dayrets = rets.mean(skipna=True)
print('---------------------')
print('Average Daily Returns')
print(dayrets)

# Correlation
correls = rets.corr()
print('----------------------')
print('Correlation of Returns')
print(correls)

# Standard deviation of returns
stdevs = rets.std(skipna=True)
print('-----------------------------')
print('Standard Deviation of Returns')
print(stdevs)

# Annualized volatility = Daily volatility * squared-root of 252
log_rets = np.log(1 + prices.pct_change())
volatility = log_rets.std(skipna=True)*252**.5
print('--------------------------------')
print('Annualized Volatility of Returns')
print(volatility)

# Beta = corr(BTC, SP500) x stdev(BTC) / stdev(SP500)
stdev_btc = stdevs['BTC-USD']
stdev_eth = stdevs['ETH-USD']
stdev_nasdaq = stdevs['^IXIC']
stdev_sp500 = stdevs['^GSPC']
corr_btc_sp500 = correls.loc['BTC-USD', '^GSPC']
corr_eth_sp500 = correls.loc['ETH-USD', '^GSPC']
corr_nasdaq_sp500 = correls.loc['^IXIC', '^GSPC']
beta_btc = corr_btc_sp500 * stdev_btc / stdev_sp500
beta_eth = corr_eth_sp500 * stdev_eth / stdev_sp500
beta_nasdaq = corr_nasdaq_sp500 * stdev_nasdaq / stdev_sp500

print('--------------------------------')
print('Beta of BTC =', beta_btc)
print('Beta of ETH =', beta_eth)
print('Beta of Nasdaq =', beta_nasdaq)

