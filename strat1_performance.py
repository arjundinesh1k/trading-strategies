import pandas as pd
import numpy as np

# 1. Load our data and our Z-Score logic
df = pd.read_csv("pair_data.csv", index_col=0)
df['ratio'] = df['KO'] / df['PEP']
df['mean'] = df['ratio'].rolling(window=30).mean()
df['std'] = df['ratio'].rolling(window=30).std()
df['zscore'] = (df['ratio'] - df['mean']) / df['std']

# 2. Simulate "The Trade" (Simplified Version)
# If Z < -2, we are 'Long' the ratio (+1)
# If Z > 2, we are 'Short' the ratio (-1)
df['position'] = 0
df.loc[df['zscore'] < -3, 'position'] = 1
df.loc[df['zscore'] > 3, 'position'] = -1

# 3. Calculate Returns
# Daily Return of the ratio
df['returns'] = df['ratio'].pct_change()
# Strategy Return = Position (Yesterday) * Return (Today)
df['strat_returns'] = df['position'].shift(1) * df['returns']

# 4. THE METRICS (The "MIT" Numbers)
win_rate = (df['strat_returns'] > 0).sum() / (df['strat_returns'] != 0).sum()
average_return = df['strat_returns'].mean()
std_dev = df['strat_returns'].std()
# Annualized Sharpe Ratio (Average / Std * Square Root of Trading Days in a Year)
sharpe = (average_return / std_dev) * np.sqrt(252)

print("--- Strategy #1 Performance Report ---")
print(f"Annualized Sharpe Ratio: {sharpe:.2f}")
print(f"Win Rate: {win_rate:.2%}")
print(f"Daily Standard Deviation: {std_dev:.4f}")