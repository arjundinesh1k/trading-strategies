# Quantitative Research & Literature Review

*   **Researcher:** Arjun Dinesh
*   **Institution:** Fulshear High School
*   **Focus:** Computational Finance & Statistical Arbitrage
*   **Timeline:** Grade 9 | Phase 1 (Dec 2025 - Feb 2026)

---

## 🔬 Strategy Methodology & Performance Audits

### Strategy #1: Statistical Arbitrage (Pairs Trading)
*   **Methodology:** Implemented a rolling 30-day Z-Score model to analyze the price ratio between KO and PEP. 
*   **Backtest Metrics:** 
    *   **Annualized Sharpe Ratio:** 0.42
    *   **Win Rate:** 49.18%
*   **Key Finding (The Drift):** Identified a structural break in the historical price ratio, drifting from 0.34 (2021) to 0.48 (2025). This confirms that price relationships are **non-stationary**, requiring an adaptive rolling-window approach to maintain a tradable signal.
*   **Academic Intersection:** 
    *   **Geometry:** Analyzed price divergence as a **Coordinate Distance** problem.
    *   **Physics:** Evaluated the Sharpe Ratio as a **Signal-to-Noise Ratio (SNR)**; optimizing for higher signal density relative to market volatility.

### Strategy #2: Time-Series Momentum (Trend Persistence)
*   **Methodology:** Developed a dual-factor model utilizing Exponential Moving Average (EMA) crossovers (9/21 day) and Relative Strength Index (RSI) filters (> 50).
*   **Backtest Metrics (NVDA):**
    *   **Annualized Sharpe Ratio:** 0.95
    *   **Max Drawdown:** -47.67%
*   **Key Finding:** Confirmed high **Trend Persistence** in semiconductor equities. While the Sharpe Ratio is superior to Strategy #1, the significant **Max Drawdown** indicates substantial tail risk, requiring advanced risk management (e.g., stop-losses or volatility scaling).
*   **Academic Intersection:** 
    *   **Physics:** Modeled momentum as **Price Velocity** and used EMA crossovers as a proxy for **Acceleration**.

---

## 📚 Literature Review (Papers 1-8)

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