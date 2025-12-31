# Quantitative Research Log

*   **Researcher:** Arjun Dinesh
*   **Grade:** 9 | Phase 1 (Dec 2025)
*   **Location:** Houston Area, TX
*   **Focus:** Computational Finance & Statistical Research

---

## 🔬 Strategy Methodology & Performance Audits

### Strategy #1: Statistical Arbitrage (Mean Reversion)
*   **Assets:** KO (Coca-Cola) / PEP (PepsiCo)
*   **Methodology:** Analyzed the price ratio between two cointegrated assets. Used a 30-day rolling mean to establish a baseline and a Z-score to measure price divergence.
*   **Results:**
    *   Initial testing at a 2.0 Sigma threshold showed high market noise and a 0.42 Sharpe Ratio.
    *   Optimized to a **3.0 Sigma threshold**, resulting in a **1.18 Sharpe Ratio**.
*   **Key Finding:** Higher thresholds improve strategy "robustness" by filtering out insignificant price wiggles and only trading extreme statistical anomalies.

### Strategy #2: Momentum (Trend Persistence)
*   **Assets:** NVDA / AMD
*   **Methodology:** Developed a trend-following model using Exponential Moving Average (EMA) crossovers (9-day vs. 21-day) and an RSI strength filter (> 50).
*   **Results (NVDA):**
    *   **Annualized Sharpe Ratio:** 0.95
    *   **Max Drawdown:** -47.67%
*   **Key Finding:** Momentum strategies on high-growth equities can produce significant returns (74% in this audit), but carry high "Drawdown" risk—the measure of the largest decline from a peak.

### Strategy #3: Cross-Asset Lead-Lag
*   **Assets:** BTC-USD (Lead) / MSTR (Lag)
*   **Methodology:** Performed a correlation-shift analysis to see if Bitcoin price action predicts MicroStrategy stock moves with a 1-day delay.
*   **Finding:** The daily correlation of 0.6087 dropped to 0.5671 when Bitcoin was shifted by 1 day.
*   **Conclusion:** The lead-lag relationship is near-instant at the daily frequency, suggesting the market is efficient and no tradable lag exists for low-frequency investors.

---

## 📚 Literature Review (Papers 1-10)

### Paper #1: What Happened to the Quants in August 2007? (Khandani & Lo)
*   Analyzed the "Quant Meltdown" where independent mathematical models failed simultaneously due to sudden market-wide selling (Systemic Risk).

### Paper #2: Pairs Trading (Gatev, et al.)
*   Established the foundational "Distance Method" for identifying two stocks that move together, proving that relative-value trading can be profitable.

### Paper #3: Statistical Arbitrage in the U.S. Equities Market (Avellaneda & Lee)
*   Explored using Principal Component Analysis (PCA) to find trading signals within market data while ignoring random noise.

### Paper #4: Returns to Buying Winners and Selling Losers (Jegadeesh & Titman)
*   The primary academic proof of Momentum; showed that stocks that perform well tend to continue performing well for 3-12 months.

### Paper #5: A Five-Factor Asset Pricing Model (Fama & French)
*   Introduced "Factor Investing," proving that stock returns are driven by specific traits like company size, value, and profitability.

### Paper #6: Deep Neural Networks for Stock Price Prediction (Heaton, et al.)
*   Investigated how AI can find non-linear patterns in price data that traditional linear math might miss.

### Paper #7: Network Momentum across Asset Classes (Oxford-Man)
*   Researched how momentum spills over from one asset to another (e.g., how one sector leader influences its competitors).

### Paper #8: Optimal Execution of Portfolio Transactions (Almgren & Chriss)
*   Modeled "Market Impact"—the reality that large trades change the price of a stock, creating "friction" for the trader.

### Paper #9: The Lead-Lag Relationship in Crypto Assets (Hou & Moskowitz)
*   Studied the delayed reaction of smaller assets to information already contained in larger, "leading" assets.

### Paper #10: The Cross-Section of Expected Stock Returns (Fama & French)
*   The definitive proof that market returns are not random and can be predicted by analyzing company-specific risk factors.

---

## 🛠 End of Year Milestone (Dec 31, 2025)
*   **Project Status:** Phase 1 (Exploration) completed 2 months ahead of schedule.
*   **Next Objective:** Transition to Python Mastery and Academic Front-running (AP Physics 1 / Geometry) to maintain 4.0 GPA requirements.