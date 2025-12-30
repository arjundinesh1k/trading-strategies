import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 1. Fetch Fresh Data (The Evidence)
tickers = ["NVDA", "AMD"]
data = yf.download(tickers, period="2y", auto_adjust=True)['Close']

def get_performance(ticker):
    df = data[[ticker]].copy()
    
    # 2. Re-calculate the Logic (EMA 9, EMA 21, RSI)
    df['EMA9'] = df[ticker].ewm(span=9, adjust=False).mean()
    df['EMA21'] = df[ticker].ewm(span=21, adjust=False).mean()
    
    delta = df[ticker].diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=14).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=14).mean()
    rs = gain / loss
    df['RSI'] = 100 - (100 / (100 + rs))

    # 3. POSITION LOGIC (The "Shift" fix to prevent cheating)
    df['signal'] = (df['EMA9'] > df['EMA21']) & (df['RSI'] > 50)
    df['position'] = df['signal'].shift(1).fillna(0).astype(int)

    # 4. CALC RETURNS
    df['daily_ret'] = df[ticker].pct_change()
    df['strat_ret'] = df['position'] * df['daily_ret']
    
    # 5. METRICS
    cum_ret = (1 + df['strat_ret']).prod() - 1
    win_rate = len(df[df['strat_ret'] > 0]) / len(df[df['strat_ret'] != 0])
    sharpe = (df['strat_ret'].mean() / df['strat_ret'].std()) * np.sqrt(252)
    
    # Max Drawdown (The Scariest Drop)
    cum_wealth = (1 + df['strat_ret']).cumprod()
    peak = cum_wealth.cummax()
    drawdown = (cum_wealth - peak) / peak
    max_dd = drawdown.min()

    return {
        "Total Return": f"{cum_ret:.2%}",
        "Sharpe Ratio": round(sharpe, 2),
        "Win Rate": f"{win_rate:.2%}",
        "Max Drawdown": f"{max_dd:.2%}"
    }

print("--- Strategy #2: NVDA Performance ---")
print(get_performance("NVDA"))
print("\n--- Strategy #2: AMD Performance ---")
print(get_performance("AMD"))