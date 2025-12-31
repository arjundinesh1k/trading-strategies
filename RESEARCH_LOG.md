# Quantitative Research & Literature Review

*   **Researcher:** Arjun Dinesh
*   **Institution:** Fulshear High School
*   **Focus:** Computational Finance & Statistical Arbitrage
*   **Timeline:** Grade 9 | Phase 1 (Dec 2025 - Feb 2026)

---

## Phase 1: Optimization & Overfitting Audit (Dec 30, 2025)

### Strategy #1: The "Tuning" Process
*   **Task:** Tested different Z-score thresholds to see which "Rubber Band" stretch produces the best risk-adjusted returns (Sharpe Ratio).
*   **Results:**
    *   2.0 Sigma: 0.42 Sharpe (Too much noise)
    *   2.45 Sigma: 1.26 Sharpe (Possible Overfitting)
    *   **3.0 Sigma: 1.18 Sharpe (Selected for Robustness)**
*   **The Lesson (Overfitting):** Learned that the "perfect" number for past data is often a trap. Choosing a round, conservative number like 3.0 is a better engineering choice because it is more likely to handle future market changes.
*   **Academic Connection:**
    *   **Geometry:** Realized that changing the Z-score is like changing the **Boundaries** of a shape. A tighter boundary (3.0) means fewer points (trades) qualify, but those that do are more "statistically significant."

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

### Paper #9: The Lead-Lag Relationship in Crypto Assets
*   **Authors:** Various (Lead-Lag Methodology)
*   **Key Takeaway:** Explored how "Primary" assets (like Bitcoin) act as a scout for "Secondary" assets (like Coinbase or MicroStrategy). When the primary asset moves, the secondary asset often follows with a measurable time delay.
*   **9th Grade Translation (The Scout):** This is about "The Echo." If someone yells across a canyon (Bitcoin price moves), there is a short delay before you hear the echo (MSTR price moves). If you see the person yell, you can predict the echo is coming.

### Paper #10: The Cross-Section of Expected Stock Returns
*   **Authors:** Fama & French (The "Godfathers" of Quant)
*   **Key Takeaway:** The final proof that market returns are not random. Returns are driven by "Risk Factors" like company size and value-to-price ratios.
*   **9th Grade Translation (The Archetype):** This ties everything together. It proves that there are "rules" to the game. If you follow the rules (like buying "Cheap" companies or "Winning" companies), you have a mathematical edge over people who are just guessing.