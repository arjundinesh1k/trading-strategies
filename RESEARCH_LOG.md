# Quant Research Log

*  **Name:** Arjun Dinesh
*  **Focus:** Computational Finance
*  **Grade:** 9
*  **Location:** Houston Area, TX

---

## Phase 1: Exploration (Dec 2025 - Feb 2026)

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

---

**Data Audit (Dec 28, 2025):**

Performed a ratio check on KO/PEP. Discovered a significant drift from 0.34 (2021) to 0.48 (2025).
Lesson Learned: A static ratio strategy is vulnerable to "structural breaks." For Strategy #1 to work, I need to implement a Rolling Mean (looking at the last 20-60 days) rather than a fixed historical average.

Verified Strategy #2 using real-time Yahoo Finance data. Discovered that NVDA had ~36% more momentum days than AMD over the last 24 months, validating the dual-EMA crossover model for high-growth tech equities.
