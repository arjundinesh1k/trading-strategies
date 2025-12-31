import yfinance as yf
import pandas as pd

# 1. Fetch the Leader and the Follower
print("Fetching Lead-Lag data...")
assets = ["BTC-USD", "MSTR"]
data = yf.download(assets, period="1y", interval="1d", auto_adjust=True)['Close']

# 2. THE PYTHON SKILL: Correlation
# This measures how much they 'mirror' each other
normal_corr = data['BTC-USD'].corr(data['MSTR'])

# 3. THE LEAD-LAG TEST: Shift BTC by 1 day
# We want to see if BTC 'Yesterday' predicts MSTR 'Today'
data['BTC_Yesterday'] = data['BTC-USD'].shift(1)
lead_lag_corr = data['BTC_Yesterday'].corr(data['MSTR'])

print(f"\n--- Lead-Lag Research Report ---")
print(f"Normal Correlation: {normal_corr:.4f}")
print(f"Lead-Lag (BTC leads MSTR) Correlation: {lead_lag_corr:.4f}")

if lead_lag_corr > normal_corr:
    print("\nRESULT: BTC is a LEADER. Its moves predict MSTR's next day.")
else:
    print("\nRESULT: The relationship is near-instant. No tradable lag found.")