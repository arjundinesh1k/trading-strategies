import pandas as pd
import matplotlib.pyplot as plt

# 1. Load the real data we pulled
df = pd.read_csv("pair_data.csv", index_col=0)
df['ratio'] = df['KO'] / df['PEP']

# 2. StatArb Math: 30-day Rolling Mean and Standard Deviation
# This handles the "Drift" you found (0.34 to 0.48)
window = 30
df['mean'] = df['ratio'].rolling(window=window).mean()
df['std'] = df['ratio'].rolling(window=window).std()

# 3. Calculate the Z-Score (The "Statistical" part)
df['zscore'] = (df['ratio'] - df['mean']) / df['std']

# 4. Generate Signals
# If Z-Score > 2, KO is statistically too expensive (SELL)
# If Z-Score < -2, KO is statistically too cheap (BUY)
df['buy_signal'] = df['zscore'] < -2
df['sell_signal'] = df['zscore'] > 2

# 5. Output the results
print("--- Statistical Arbitrage Signal Report ---")
print(f"Total days analyzed: {len(df)}")
print(f"Number of BUY signals (Z < -2): {df['buy_signal'].sum()}")
print(f"Number of SELL signals (Z > 2): {df['sell_signal'].sum()}")

# Save a plot to prove it works
plt.figure(figsize=(12,6))
plt.plot(df['zscore'], label='Z-Score', color='blue')
plt.axhline(2, color='red', linestyle='--', label='Overvalued (Sell)')
plt.axhline(-2, color='green', linestyle='--', label='Undervalued (Buy)')
plt.axhline(0, color='black', linewidth=1)
plt.title("KO/PEP Statistical Arbitrage: Rolling Z-Score")
plt.legend()
plt.savefig("statarb_signals.png")
print("\nPlot saved as statarb_signals.png")