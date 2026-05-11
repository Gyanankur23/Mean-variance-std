# 📊 Mean-Variance-Standard Deviation Calculator

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![NumPy](https://img.shields.io/badge/NumPy-1.20%2B-orange)](https://numpy.org/)
[![Pandas](https://img.shields.io/badge/Pandas-1.3%2B-150458)](https://pandas.pydata.org/)
[![SciPy](https://img.shields.io/badge/SciPy-1.7%2B-8CAAE6)](https://scipy.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

A comprehensive Python project demonstrating mean, variance, and standard deviation calculations with **industry-relevant applications** in financial portfolio optimization using Modern Portfolio Theory.

### How to run it on your own machine

1. **Install the requirements**

   ```bash
   $ pip install -r requirements.txt
   ```

2. **Run the examples**

   ```bash
   $ python example_usage.py
   ```

3. **Run the tests**

   ```bash
   $ python -m unittest test_mean_var_std.py
   ```

---

## 📁 Project Structure

```
.
├── mean_var_std.py           # Core calculator (FreeCodeCamp project)
├── portfolio_optimizer.py    # Industry: Portfolio optimization (Markowitz MPT)
├── test_mean_var_std.py      # Unit tests (5 test cases)
├── example_usage.py          # Demonstration scripts
├── requirements.txt          # Dependencies
└── README.md                 # Documentation
```

---

## 🚀 Quick Start

### Basic Calculator

```python
from mean_var_std import calculate

result = calculate([0, 1, 2, 3, 4, 5, 6, 7, 8])

print(result['mean'])                # [[3.0, 4.0, 5.0], [1.0, 4.0, 7.0], 4.0]
print(result['variance'])            # Variance along axes and flattened
print(result['standard deviation']) # Std dev along axes and flattened
```

### Portfolio Optimization

```python
from portfolio_optimizer import PortfolioOptimizer
import pandas as pd

# Load historical returns data
returns = pd.DataFrame({
    'Stock A': [0.01, -0.02, 0.03, ...],
    'Stock B': [0.02, 0.01, -0.01, ...],
})

# Initialize optimizer
optimizer = PortfolioOptimizer(returns)

# Find optimal portfolios
weights, ret, vol = optimizer.min_variance_portfolio()
weights, ret, vol, sharpe = optimizer.max_sharpe_portfolio()
```

---

## ✨ Features

| Feature | Description |
|---------|-------------|
| 📈 **Mean-Variance Analysis** | Core statistical calculations on matrices |
| 💼 **Portfolio Optimization** | Markowitz Modern Portfolio Theory implementation |
| 🎯 **Efficient Frontier** | Generate optimal risk-return portfolios |
| 📉 **Risk Metrics** | VaR, volatility, and Sharpe ratio calculations |
| 🧪 **Unit Tests** | 5 comprehensive test cases |

---

## 💡 Key Concepts

- **Expected Returns** (Mean) — Average historical returns
- **Volatility** (Standard Deviation) — Risk measurement
- **Covariance Matrix** — Asset correlation structure
- **Sharpe Ratio** — Risk-adjusted performance metric
- **Value at Risk (VaR)** — Maximum expected loss

---

## 📊 Example Output

```
BASIC MEAN-VARIANCE-STD CALCULATOR
==================================
Input data: [0, 1, 2, 3, 4, 5, 6, 7, 8]

MEAN:
  Along axis 0 (columns): [3.0, 4.0, 5.0]
  Along axis 1 (rows):    [1.0, 4.0, 7.0]
  Flattened (all data):   4.0

PORTFOLIO OPTIMIZATION
==================================
Maximum Sharpe Ratio Portfolio:
  Stock A: 45.23%
  Stock B: 32.15%
  Stock C: 15.62%
  Bond D:  7.00%
  Expected Return: 12.34%
  Volatility (Std): 8.56%
  Sharpe Ratio: 1.21
```

---

## 🏢 Industry Applications

1. **Asset Management** — Optimal mutual fund construction
2. **Risk Management** — Portfolio VaR and volatility analysis
3. **Quantitative Trading** — Algorithmic rebalancing
4. **Robo-Advisors** — Automated investment allocation
5. **Pension Funds** — Long-term liability matching

---

## 🧮 Mathematical Background

### Mean-Variance Optimization

```
minimize:   σ²(w) = w'Σw
subject to: w'μ = R_target
             Σw = 1
```

Where `w` = weights, `Σ` = covariance matrix, `μ` = expected returns

### Sharpe Ratio

```
Sharpe = (R_p - R_f) / σ_p
```

---

## 📦 Dependencies

```
numpy>=1.20.0
pandas>=1.3.0
scipy>=1.7.0
matplotlib>=3.4.0
seaborn>=0.11.0
```

---

## 📚 Resources

- [Modern Portfolio Theory - Investopedia](https://www.investopedia.com/terms/m/modernportfoliotheory.asp)
- [NumPy Statistics](https://numpy.org/doc/stable/reference/routines.statistics.html)
- [FreeCodeCamp Data Analysis](https://www.freecodecamp.org/learn/data-analysis-with-python/)

---

Built with ❤️ using Python, NumPy & Pandas
