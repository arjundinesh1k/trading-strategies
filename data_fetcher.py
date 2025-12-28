import yfinance as yf
import pandas as pd

# Define our pair
tickers = ["KO", "PEP"]

print("Fetching data from Yahoo Finance...")

# We add auto_adjust=True to get clean prices without the MultiIndex headache
# We also use 'Close' instead of 'Adj Close' because auto_adjust handles it
data = yf.download(tickers, start="2020-01-01", end="2025-12-25", auto_adjust=True)

# This selects ONLY the prices and ignores things like Volume
# It also cleans up the "Two-Story House" structure
prices = data['Close']

# Check the results
print("\nSuccess! Here are the latest prices:")
print(prices.tail())

# Save it
prices.to_csv("pair_data.csv")
print("\nFile saved: pair_data.csv")
