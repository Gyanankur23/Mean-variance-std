# Mean-Variance-Standard Deviation Calculator

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![NumPy](https://img.shields.io/badge/NumPy-1.20%2B-orange)](https://numpy.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

A comprehensive Python project demonstrating mean, variance, and standard deviation calculations with **industry-relevant applications** in financial portfolio optimization (Modern Portfolio Theory).

## Project Overview

This repository contains:
1. **FreeCodeCamp Project Solution** - Basic calculator for the Data Analysis certification
2. **Industry Application** - Portfolio optimization using Markowitz Mean-Variance Analysis
3. **Risk Metrics** - Financial risk calculations used in quantitative finance

## Files Structure

```
Mean-variance-std/
├── mean_var_std.py              # Core calculator (FreeCodeCamp project)
├── portfolio_optimizer.py        # Industry: Portfolio optimization
├── test_mean_var_std.py          # Unit tests
├── example_usage.py              # Demonstration scripts
├── requirements.txt              # Dependencies
└── README.md                     # Documentation
```

## Installation

```bash
# Clone the repository
git clone https://github.com/Gyanankur23/Mean-variance-std.git
cd Mean-variance-std

# Install dependencies
pip install -r requirements.txt
```

## Quick Start

### Basic Calculator (FreeCodeCamp)

```python
from mean_var_std import calculate

# Input: list of 9 numbers
result = calculate([0, 1, 2, 3, 4, 5, 6, 7, 8])

print(result['mean'])       # [[3.0, 4.0, 5.0], [1.0, 4.0, 7.0], 4.0]
print(result['variance'])   # Variance along axes and flattened
print(result['standard deviation'])  # Std dev along axes and flattened
```

### Industry Application: Portfolio Optimization

```python
from portfolio_optimizer import PortfolioOptimizer
import pandas as pd

# Historical returns data
returns = pd.DataFrame({
    'Stock A': [0.01, -0.02, 0.03, ...],
    'Stock B': [0.02, 0.01, -0.01, ...],
    ...
})

# Initialize optimizer
optimizer = PortfolioOptimizer(returns)

# Find optimal portfolios
weights, ret, vol = optimizer.min_variance_portfolio()
weights, ret, vol, sharpe = optimizer.max_sharpe_portfolio()

# Calculate risk metrics
std = optimizer.portfolio_std(weights)
variance = optimizer.portfolio_variance(weights)
```

## Features

### Core Module (`mean_var_std.py`)
- Calculate mean, variance, standard deviation across matrix axes
- Process 3x3 matrices from 9-element lists
- Returns flattened and axis-specific statistics

### Portfolio Optimizer (`portfolio_optimizer.py`)
- **Mean-Variance Optimization**: Implements Markowitz Modern Portfolio Theory
- **Efficient Frontier**: Generate random portfolios for visualization
- **Minimum Variance Portfolio**: Lowest risk portfolio allocation
- **Maximum Sharpe Ratio**: Optimal risk-adjusted returns portfolio
- **Risk Metrics**: Portfolio std deviation, variance calculations

### Key Financial Concepts Demonstrated
1. **Expected Returns** (Mean) - Average historical returns
2. **Volatility** (Standard Deviation) - Risk measurement
3. **Covariance Matrix** - Asset correlation structure
4. **Sharpe Ratio** - Risk-adjusted performance metric
5. **Value at Risk (VaR)** - Maximum expected loss

## Running Examples

```bash
# Run all demonstrations
python example_usage.py

# Run unit tests
python -m unittest test_mean_var_std.py

# Run specific test
python -m unittest test_mean_var_std.MeanVarStdTests.test_calculate_values
```

## Example Output

```
BASIC MEAN-VARIANCE-STD CALCULATOR
============================================================
Input data: [0, 1, 2, 3, 4, 5, 6, 7, 8]

--- Results ---
MEAN:
  Along axis 0 (columns): [3.0, 4.0, 5.0]
  Along axis 1 (rows): [1.0, 4.0, 7.0]
  Flattened (all data): 4.0

PORTFOLIO OPTIMIZATION (INDUSTRY APPLICATION)
============================================================
Maximum Sharpe Ratio Portfolio:
  Stock A: 45.23%
  Stock B: 32.15%
  Stock C: 15.62%
  Bond D: 7.00%
  Expected Return: 12.34%
  Volatility (Std): 8.56%
  Sharpe Ratio: 1.21
```

## Mathematical Background

### Mean-Variance Optimization

The portfolio optimization problem minimizes variance for a given expected return:

```
minimize:   σ²(w) = w'Σw
subject to: w'μ = R_target
             Σw = 1
```

Where:
- `w` = portfolio weights vector
- `Σ` = covariance matrix of returns
- `μ` = expected returns vector
- `σ²` = portfolio variance

### Sharpe Ratio

```
Sharpe = (R_p - R_f) / σ_p
```

Where:
- `R_p` = portfolio return
- `R_f` = risk-free rate
- `σ_p` = portfolio standard deviation

## Industry Use Cases

1. **Asset Management**: Constructing optimal mutual fund portfolios
2. **Risk Management**: Calculating portfolio VaR and volatility
3. **Quantitative Trading**: Algorithmic portfolio rebalancing
4. **Robo-Advisors**: Automated investment allocation
5. **Pension Funds**: Long-term liability matching portfolios

## Testing

```bash
# Run all tests
python -m unittest discover -v

# Run with coverage
pip install coverage
coverage run -m unittest test_mean_var_std.py
coverage report
```

## Dependencies

| Package | Version | Purpose |
|---------|---------|---------|
| numpy | ≥1.20.0 | Matrix operations, statistics |
| pandas | ≥1.3.0 | Data handling, time series |
| scipy | ≥1.7.0 | Optimization algorithms |
| matplotlib | ≥3.4.0 | Visualization (optional) |
| seaborn | ≥0.11.0 | Statistical plots (optional) |

## Contributing

Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Add tests for new functionality
4. Submit a pull request

## License

MIT License - see LICENSE file for details.

## Acknowledgments

- FreeCodeCamp for the project foundation
- Harry Markowitz for Modern Portfolio Theory (1952)
- Quantitative finance community for best practices

## Resources

- [Modern Portfolio Theory - Investopedia](https://www.investopedia.com/terms/m/modernportfoliotheory.asp)
- [NumPy Statistics Documentation](https://numpy.org/doc/stable/reference/routines.statistics.html)
- [FreeCodeCamp Data Analysis Certification](https://www.freecodecamp.org/learn/data-analysis-with-python/)

---

**Built with Python for learning and industry applications.**
