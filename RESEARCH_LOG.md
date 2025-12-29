# Quant Research Log

*  **Name:** Arjun Dinesh
*  **Focus:** Computational Finance
*  **Grade:** 9
*  **Location:** Houston Area, TX

---

## Phase 1: Exploration (Dec 2025 - Feb 2026)

### Strategy #1 Performance Audit
*   **Task:** Calculated Sharpe Ratio and Win Rate for KO/PEP StatArb.
*   **Result:** 0.42 Sharpe. 
*   **Academic Connection (Physics/Geometry):**
    *   **Geometry:** Connected the Z-Score to the **Distance Formula**. Calculating the "gap" between prices is mathematically identical to finding the distance between two points on a coordinate plane.
    *   **Physics:** Realized the Sharpe Ratio is a **Signal-to-Noise** calculation. Average return is the signal; Standard Deviation is the "vibration" or noise.

### Paper #1: What Happened to the Quants in August 2007?
*   **Authors:** Khandani & Lo
*   **Key Takeaway:** Even robust math models can fail during "liquidity crunches" when too many funds try to sell the same assets at once. This highlights the importance of "Systemic Risk."

### Paper #2: Pairs Trading: Performance of a Relative-Value Arbitrage Rule
*   **Authors:** Gatev, Goetzmann, & Rouwenhorst
*   **Key Takeaway:** Historical proof that mean-reversion between "twin" stocks (like KO and PEP) can generate consistent profit, proving the market isn't always perfectly efficient.

### Paper #3: Statistical Arbitrage in the U.S. Equities Market
*   **Authors:** Marco Avellaneda and Jeong-Hyun Lee
*   **Key Takeaway:** Research on how using math to find "mean-reverting" patterns in the US market made money, especially by grouping stocks together.

### Paper #4: Returns to Buying Winners and Selling Losers
*   **Authors:** Narasimhan Jegadeesh and Sheridan Titman
*   **Key Takeaway:** Proves that stocks on a "winning streak" tend to keep winning for 3-12 months, a concept known as momentum.

### Paper #5: A Five-Factor Asset Pricing Model
*   **Authors:** Fama & French
*   **Key Takeaway:** Learned that market returns are driven by specific "Factors" (Size, Value, Profitability, Investment, and Market Risk). This provides a roadmap for building more complex alphas in WorldQuant BRAIN.

### Paper #6: Deep Neural Networks for Stock Price Prediction
*   **Authors:** J.B. Heaton, et al.
*   **Key Takeaway:** Explored how AI and Deep Learning can identify non-linear patterns that traditional linear models (like my current Z-score) might miss. This is a potential solution for predicting "Ratio Drift."

---

**Data Audit (Dec 28, 2025):**

*   Performed a ratio check on KO/PEP. Discovered a significant drift from 0.34 (2021) to 0.48 (2025).
*   Lesson Learned: A static ratio strategy is vulnerable to "structural breaks." For Strategy #1 to work, I need to implement a Rolling Mean (looking at the last 20-60 days) rather than a fixed historical average.

*   Verified Strategy #2 using real-time Yahoo Finance data. Discovered that NVDA had ~36% more momentum days than AMD over the last 24 months, validating the dual-EMA crossover model for high-growth tech equities.


**Dec 29, 2025 Audit:**

*   Connected Strategy #1 (StatArb) to Geometry's Distance Formula. Realized Z-score is a measure of "Price Displacement."

*   Connected Strategy #2 (Momentum) to Physics' Kinematics. Realized momentum is the "Velocity" of a price trend.
