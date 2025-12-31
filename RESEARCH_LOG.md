# Quantitative Research Log

*   **Researcher:** Arjun Dinesh
*   **Focus:** Computational Finance
*   **Grade:** 9 | Phase 1 (Dec 2025)

---

## 🔬 Strategy Methodology & Performance Audits

### Strategy #1: Statistical Arbitrage (Mean Reversion)
*   **Methodology:** This strategy identifies price gaps between two related assets (KO and PEP). It uses a 30-day "Rolling Mean" (average) to determine the center point and a "Z-Score" to measure how far the current price has moved from that center.
*   **Results & Optimization:**
    *   **Initial Test (2.0 Sigma):** Produced a 0.42 Sharpe Ratio. The model was too sensitive to small price wiggles (market noise).
    *   **Final Test (3.0 Sigma):** Produced a **1.18 Sharpe Ratio**. By increasing the requirement for a trade, the model only acts on large, significant price gaps.
*   **Geometry Connection:** The Z-Score functions as a **Distance Formula**. It calculates the numerical distance between the current price and the 30-day average. 
*   **Physics Connection:** The Sharpe Ratio measures **Signal-to-Noise**. The average profit is the "Signal," and the standard deviation (price volatility) is the "Noise."

### Strategy #2: Momentum (Trend Persistence)
*   **Methodology:** This strategy tracks the "winning streak" of high-growth stocks like NVDA. It uses two Exponential Moving Averages (EMA): a 9-day (fast) and a 21-day (slow). 
*   **Signals:** When the 9-day average moves above the 21-day average, it indicates the price is trending upward. We use the RSI (Relative Strength Index) to confirm the trend is strong (RSI > 50).
*   **Performance Metrics (NVDA):**
    *   **Sharpe Ratio:** 0.95
    *   **Max Drawdown:** -47.67%
*   **Key Finding:** Momentum is highly profitable (74% return) but carries high "Account Risk." The -47% Drawdown shows the largest peak-to-trough decline, meaning the strategy requires strict exit rules to protect capital.
*   **Physics Connection:** Modeled price movement as **Velocity** and the EMA crossover as **Acceleration** (the rate at which the price trend is speeding up).

---

## 📚 Literature Review (Papers 1-10)

### Paper #1: What Happened to the Quants in August 2007? (Khandani & Lo)
*   **Summary:** Analysis of the "Quant Meltdown." Highlights how systemic liquidity shocks can cause simultaneous failures in independent mathematical models.

### Paper #2: Pairs Trading (Gatev, et al.)
*   **Summary:** Foundational research on relative-value arbitrage. Established the "Distance Method" for identifying cointegrated equity pairs.

### Paper #3: Statistical Arbitrage in the U.S. Equities Market (Avellaneda & Lee)
*   **Summary:** Detailed the use of Principal Component Analysis (PCA) to extract signals from market noise. 

### Paper #4: Returns to Buying Winners and Selling Losers (Jegadeesh & Titman)
*   **Summary:** Academic proof of the Momentum anomaly. Found that trend persistence typically lasts between 3 to 12 months.

### Paper #5: A Five-Factor Asset Pricing Model (Fama & French)
*   **Summary:** Extended the CAPM model to include factors like Size, Value, and Profitability. Essential for multi-factor alpha construction.

### Paper #6: Deep Neural Networks for Stock Price Prediction (Heaton, et al.)
*   **Summary:** Explored non-linear pattern recognition through deep learning. Potential solution for modeling non-stationary data (Ratio Drift).

### Paper #7: Network Momentum across Asset Classes (Oxford-Man)
*   **Summary:** Investigated how lead-lag relationships function across connected assets (e.g., NVDA leading AMD). 

### Paper #8: Optimal Execution of Portfolio Transactions (Almgren & Chriss)
*   **Summary:** Modeled the "Market Impact" of large trades. Essential for understanding the friction between theoretical models and real-world execution.

### Paper #9: The Lead-Lag Relationship in Crypto Assets (Hou & Moskowitz)
*   **Summary:** Examines the delayed reaction of smaller, "lagging" assets to news already reflected in "leading" primary assets. This confirms that market friction prevents information from being absorbed instantly across all related securities.

### Paper #10: The Cross-Section of Expected Stock Returns (Fama & French)
*   **Summary:** One of the most influential papers in finance. It replaced the single-factor model with a multi-factor approach, proving that company size and book-to-market equity are high-probability predictors of future returns.