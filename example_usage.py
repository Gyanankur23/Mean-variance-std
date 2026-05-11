"""
Example usage demonstrating mean-variance-std calculations
and portfolio optimization in finance.
"""

import numpy as np
import pandas as pd
from mean_var_std import calculate
from portfolio_optimizer import PortfolioOptimizer, calculate_asset_statistics


def demo_basic_calculator():
    """Demonstrate the basic mean-variance-std calculator."""
    print("=" * 60)
    print("BASIC MEAN-VARIANCE-STD CALCULATOR")
    print("=" * 60)
    
    # Example data
    data = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    
    print(f"\nInput data: {data}")
    print("Matrix form (3x3):")
    matrix = np.array(data).reshape(3, 3)
    print(matrix)
    
    result = calculate(data)
    
    print("\n--- Results ---")
    for key, values in result.items():
        print(f"\n{key.upper()}:")
        print(f"  Along axis 0 (columns): {values[0]}")
        print(f"  Along axis 1 (rows):    {values[1]}")
        print(f"  Flattened (all data):   {values[2]}")


def demo_portfolio_optimization():
    """Demonstrate portfolio optimization using mean-variance analysis."""
    print("\n" + "=" * 60)
    print("PORTFOLIO OPTIMIZATION (INDUSTRY APPLICATION)")
    print("=" * 60)
    
    # Simulate historical returns for 4 assets
    np.random.seed(42)
    days = 252 * 2  # 2 years of daily data
    
    # Create sample return data
    assets = ['Stock A', 'Stock B', 'Stock C', 'Bond D']
    
    # Different risk-return profiles
    returns_data = {
        'Stock A': np.random.normal(0.001, 0.02, days),  # High return, high vol
        'Stock B': np.random.normal(0.0005, 0.015, days), # Medium profile
        'Stock C': np.random.normal(0.0003, 0.01, days), # Lower risk
        'Bond D': np.random.normal(0.0001, 0.005, days)   # Low risk
    }
    
    returns_df = pd.DataFrame(returns_data)
    
    print("\n--- Asset Statistics ---")
    stats = calculate_asset_statistics(returns_df)
    print(stats.round(6))
    
    # Initialize optimizer
    optimizer = PortfolioOptimizer(returns_df)
    
    print("\n--- Portfolio Optimization ---")
    
    # Minimum variance portfolio
    min_var_weights, min_var_ret, min_var_vol = optimizer.min_variance_portfolio()
    print("\nMinimum Variance Portfolio:")
    for asset, weight in zip(assets, min_var_weights):
        print(f"  {asset}: {weight:.2%}")
    print(f"  Expected Return: {min_var_ret:.4%}")
    print(f"  Volatility (Std): {min_var_vol:.4%}")
    
    # Maximum Sharpe ratio portfolio
    max_sharpe_weights, max_sharpe_ret, max_sharpe_vol, sharpe = optimizer.max_sharpe_portfolio()
    print("\nMaximum Sharpe Ratio Portfolio:")
    for asset, weight in zip(assets, max_sharpe_weights):
        print(f"  {asset}: {weight:.2%}")
    print(f"  Expected Return: {max_sharpe_ret:.4%}")
    print(f"  Volatility (Std): {max_sharpe_vol:.4%}")
    print(f"  Sharpe Ratio: {sharpe:.4f}")
    
    # Demonstrate portfolio std calculation
    equal_weights = np.array([0.25, 0.25, 0.25, 0.25])
    port_std = optimizer.portfolio_std(equal_weights)
    port_var = optimizer.portfolio_variance(equal_weights)
    print(f"\nEqual Weight Portfolio (25% each):")
    print(f"  Portfolio Variance: {port_var:.6f}")
    print(f"  Portfolio Std Dev: {port_std:.6f}")


def demo_risk_metrics():
    """Demonstrate risk metrics calculations."""
    print("\n" + "=" * 60)
    print("RISK METRICS CALCULATION")
    print("=" * 60)
    
    # Sample portfolio returns
    np.random.seed(123)
    portfolio_returns = np.random.normal(0.001, 0.015, 252)  # Daily returns
    
    print(f"\nSample Portfolio (252 trading days):")
    print(f"  Mean Daily Return: {np.mean(portfolio_returns):.4%}")
    print(f"  Daily Variance: {np.var(portfolio_returns):.6f}")
    print(f"  Daily Std Dev: {np.std(portfolio_returns):.4%}")
    print(f"  Annualized Mean: {np.mean(portfolio_returns) * 252:.2%}")
    print(f"  Annualized Std: {np.std(portfolio_returns) * np.sqrt(252):.2%}")
    
    # VaR calculation (Value at Risk)
    var_95 = np.percentile(portfolio_returns, 5)
    print(f"\nValue at Risk (95% confidence):")
    print(f"  Daily VaR: {var_95:.4%} (worst expected daily loss)")


if __name__ == "__main__":
    demo_basic_calculator()
    demo_portfolio_optimization()
    demo_risk_metrics()
    
    print("\n" + "=" * 60)
    print("All demonstrations completed successfully!")
    print("=" * 60)
