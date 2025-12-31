# Quantitative Trading Research & Strategy Development
### Focus: Computational Finance | Statistical Arbitrage | Market Microstructure

This repository serves as a professional portfolio and research log for my journey into quantitative finance. My objective is to build a foundation in mathematical modeling and data-driven strategy development, with a specific focus on mean reversion and momentum anomalies.

---

## 🚀 Research Roadmap (2025 - 2028)
*A multi-year commitment to mastering financial engineering.*

- **Phase 1: Exploration (Current)** - Literature review, Python data mastery, and building foundational strategies.
- **Phase 2: Mentor & Scale (Starting March 2026)** - Academic mentorship, advanced statistical testing, and ISEF submission.
- **Phase 3: Deep Optimization (2027-2028)** - WorldQuant BRAIN Alpha development and published research.

---

## 📈 Active Strategies

### Strategy #1: Statistical Arbitrage (Mean Reversion)
*   **Assets:** KO (Coca-Cola) / PEP (PepsiCo)
*   **Status:** ✅ BACKTESTED & OPTIMIZED
*   **Performance Metrics (Audit Dec 30, 2025):** 
    *   **Annualized Sharpe Ratio:** 1.18
    *   **Threshold:** 3.0 Sigma (Z-Score)
*   **Research Finding:** Initially achieved a 0.42 Sharpe with a 2.0 threshold. Optimization testing showed a "peak" at 2.45 (1.26 Sharpe), but a **3.0 threshold** was selected for "Robustness." 
*   **Analysis:** By using a more conservative 3.0 threshold, the strategy filters out market noise and only trades during extreme price divergences. This reduces the risk of **Overfitting**—picking a number that worked perfectly in the past but might fail in the future.

### Strategy #2: Momentum Trend Following (NVDA/AMD)
*   **Status:** ✅ BACKTESTED & VERIFIED
*   **Performance Metrics (Audit Dec 30, 2025):** 
    *   **NVDA Sharpe Ratio:** 0.95 (High Performance)
    *   **NVDA Total Return:** 74.14%
    *   **NVDA Max Drawdown:** -47.67% (Significant Risk)
*   **Analysis:** The Dual-EMA model excels at capturing the "AI Expansion" trend. However, the high drawdown suggests the need for a "Stop-Loss" mechanism or a volatility-adjusting position size to protect capital during sector rotations.

---

## 📚 Research Log
I maintain a detailed [Research Log](RESEARCH_LOG.md) documenting my review of 10+ academic papers in quantitative finance, including works by Andrew Lo (MIT) and Eugene Fama (Nobel Laureate).

---

## 🛠 Tech Stack
- **Language:** Python 3.x
- **Libraries:** Pandas, NumPy, Matplotlib, YFinance
- **Environment:** GitHub Codespaces / VS Code

---

## ⚖️ License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 📫 Contact
**Arjun Dinesh** 
**Email: arjun.dinesh.1k@gmail.com**
*Aspiring Quant & Researcher | Fulshear High School '29*
