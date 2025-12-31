# Quantitative Research Log

*   **Researcher:** Arjun Dinesh
*   **Focus:** Computational Finance
*   **Grade:** 9 | Phase 1 (Dec 2025)

---

## 📈 Active Strategies

### Strategy #1: Statistical Arbitrage (Mean Reversion)
*   **Assets:** KO (Coke) / PEP (Pepsi)
*   **Status:** ✅ BACKTESTED & OPTIMIZED
*   **Performance:** **1.18 Sharpe Ratio** (Z-Score Threshold: 3.0)
*   **Finding:** Identified that high-frequency "noise" was lowering performance. Moving to a conservative 3.0 threshold improved the quality of trades and strategy robustness.

### Strategy #2: Momentum Trend Following
*   **Assets:** NVDA / AMD
*   **Status:** ✅ BACKTESTED
*   **Performance:** **0.95 Sharpe Ratio** (74.14% Total Return)
*   **Risk Note:** Strategy carries a **-47.67% Max Drawdown**. While highly profitable, it requires significant risk tolerance during sector corrections.

### Strategy #3: Cross-Asset Lead-Lag
*   **Assets:** BTC-USD (Lead) / MSTR (Lag)
*   **Status:** ✅ RESEARCH COMPLETED
*   **Finding:** Analyzed the "Echo Effect" between Bitcoin and MicroStrategy. Found that at a daily frequency, the correlation (0.6087) is near-instant.
*   **Conclusion:** No tradable 1-day lag exists, suggesting the market is efficient in pricing the BTC-MSTR relationship.

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
*   **Summary:** Research on how "Leader" assets (like Bitcoin) influence "Follower" assets (like MSTR). Established that while links exist, information is usually absorbed too fast for low-frequency trading.

### Paper #10: The Cross-Section of Expected Stock Returns (Fama & French)
*   **Summary:** Proved that company size and "Value" are the primary drivers of stock returns. This is the foundational paper for all factor-based quantitative research.

---

## 🛠 End of Year Audit (Dec 31, 2025)
*   **Total Papers Read:** 10/10 (Goal Met)
*   **Strategies Verified:** 3 (Mean Reversion, Momentum, Lead-Lag)
*   **Python Progress:** Mastered basic data fetching (yfinance) and initial data manipulation (Pandas filtering/slicing).
*   **Algebra 1 Connections:** Applied concepts of Mean, Standard Deviation, and Slope to financial time-series data.