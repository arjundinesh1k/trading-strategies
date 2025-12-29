import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# 1. DOWNLOAD DATA (No more missing files)
print("Fetching real-time data for NVDA and AMD...")
tickers = ["NVDA", "AMD"]
# Using 2 years of data to capture the recent AI boom
data = yf.download(tickers, period="2y", auto_adjust=True)
df = data['Close'].copy()

def run_momentum(ticker):
    print(f"Analyzing {ticker}...")
    
    # EMA 9 (Fast) and EMA 21 (Slow)
    df[f'{ticker}_EMA9'] = df[ticker].ewm(span=9, adjust=False).mean()
    df[f'{ticker}_EMA21'] = df[ticker].ewm(span=21, adjust=False).mean()

    # RSI (Relative Strength Index) - The Speedometer
    delta = df[ticker].diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=14).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=14).mean()
    rs = gain / loss
    df[f'{ticker}_RSI'] = 100 - (100 / (100 + rs))

    # SIGNAL: Fast EMA > Slow EMA (Acceleration) AND RSI > 50 (Strength)
    df[f'{ticker}_Signal'] = (df[f'{ticker}_EMA9'] > df[f'{ticker}_EMA21']) & (df[f'{ticker}_RSI'] > 50)
    
    return df[f'{ticker}_Signal'].sum()

# 2. RUN THE ENGINE
nvda_days = run_momentum('NVDA')
amd_days = run_momentum('AMD')

print("\n--- Strategy #2: Momentum Report ---")
print(f"NVDA: {nvda_days} days in a confirmed uptrend.")
print(f"AMD:  {amd_days} days in a confirmed uptrend.")

# 3. VISUAL PROOF (For NVDA)
plt.figure(figsize=(12,6))
plt.plot(df['NVDA'], label='NVDA Price', alpha=0.3, color='gray')
plt.plot(df['NVDA_EMA9'], label='Fast EMA (9)', color='green', linewidth=1.5)
plt.plot(df['NVDA_EMA21'], label='Slow EMA (21)', color='red', linewidth=1.5)
plt.fill_between(df.index, df['NVDA'].min(), df['NVDA'].max(), 
                 where=df['NVDA_Signal'], color='green', alpha=0.1, label='Momentum Zone')
plt.title("NVDA Momentum Strategy: Trend Zones")
plt.legend()
plt.savefig("momentum_signals.png")
print("\nPlot saved: momentum_signals.png")