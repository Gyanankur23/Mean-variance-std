"""
Portfolio Optimization using Mean-Variance Analysis (Markowitz Model)
Industry application of mean-variance-std calculations in finance.
"""

import numpy as np
import pandas as pd
from typing import List, Tuple, Optional


class PortfolioOptimizer:
    """
    Implements Modern Portfolio Theory (MPT) for portfolio optimization.
    Uses mean-variance optimization to find efficient portfolios.
    """
    
    def __init__(self, returns: pd.DataFrame):
        """
        Initialize with historical returns data.
        
        Args:
            returns: DataFrame with historical returns (columns = assets, rows = periods)
        """
        self.returns = returns
        self.assets = returns.columns.tolist()
        self.n_assets = len(self.assets)
        
        # Calculate expected returns (mean) and covariance matrix
        self.expected_returns = returns.mean()
        self.cov_matrix = returns.cov()
        
    def portfolio_performance(self, weights: np.ndarray) -> Tuple[float, float]:
        """
        Calculate expected return and volatility of a portfolio.
        
        Args:
            weights: Portfolio weights array
            
        Returns:
            Tuple of (expected_return, volatility)
        """
        expected_return = np.sum(self.expected_returns * weights)
        volatility = np.sqrt(np.dot(weights.T, np.dot(self.cov_matrix, weights)))
        return expected_return, volatility
    
    def portfolio_std(self, weights: np.ndarray) -> float:
        """
        Calculate portfolio standard deviation (volatility/risk).
        
        Args:
            weights: Portfolio weights array
            
        Returns:
            Portfolio standard deviation
        """
        return np.sqrt(np.dot(weights.T, np.dot(self.cov_matrix, weights)))
    
    def portfolio_variance(self, weights: np.ndarray) -> float:
        """
        Calculate portfolio variance.
        
        Args:
            weights: Portfolio weights array
            
        Returns:
            Portfolio variance
        """
        return np.dot(weights.T, np.dot(self.cov_matrix, weights))
    
    def random_portfolios(self, n_portfolios: int = 10000, risk_free_rate: float = 0.02) -> Tuple[List, List, List]:
        """
        Generate random portfolios for efficient frontier visualization.
        
        Args:
            n_portfolios: Number of random portfolios to generate
            risk_free_rate: Risk-free rate for Sharpe ratio calculation
            
        Returns:
            Tuple of (returns, volatilities, sharpe_ratios)
        """
        port_returns = []
        port_volatilities = []
        sharpe_ratios = []
        
        np.random.seed(42)
        
        for _ in range(n_portfolios):
            # Generate random weights that sum to 1
            weights = np.random.random(self.n_assets)
            weights /= np.sum(weights)
            
            # Calculate portfolio metrics
            ret, vol = self.portfolio_performance(weights)
            sharpe = (ret - risk_free_rate) / vol
            
            port_returns.append(ret)
            port_volatilities.append(vol)
            sharpe_ratios.append(sharpe)
            
        return port_returns, port_volatilities, sharpe_ratios
    
    def min_variance_portfolio(self) -> Tuple[np.ndarray, float, float]:
        """
        Find the minimum variance portfolio.
        
        Returns:
            Tuple of (optimal_weights, expected_return, volatility)
        """
        from scipy.optimize import minimize
        
        # Constraints: weights sum to 1
        constraints = ({'type': 'eq', 'fun': lambda x: np.sum(x) - 1})
        
        # Bounds: weights between 0 and 1 (no short selling)
        bounds = tuple((0, 1) for _ in range(self.n_assets))
        
        # Initial guess: equal weights
        x0 = np.array([1 / self.n_assets] * self.n_assets)
        
        # Minimize portfolio variance
        result = minimize(
            fun=lambda x: self.portfolio_variance(x),
            x0=x0,
            method='SLSQP',
            bounds=bounds,
            constraints=constraints
        )
        
        optimal_weights = result.x
        ret, vol = self.portfolio_performance(optimal_weights)
        
        return optimal_weights, ret, vol
    
    def max_sharpe_portfolio(self, risk_free_rate: float = 0.02) -> Tuple[np.ndarray, float, float, float]:
        """
        Find the maximum Sharpe ratio portfolio (tangency portfolio).
        
        Args:
            risk_free_rate: Risk-free rate
            
        Returns:
            Tuple of (optimal_weights, expected_return, volatility, sharpe_ratio)
        """
        from scipy.optimize import minimize
        
        def neg_sharpe(weights):
            ret, vol = self.portfolio_performance(weights)
            return -(ret - risk_free_rate) / vol
        
        # Constraints: weights sum to 1
        constraints = ({'type': 'eq', 'fun': lambda x: np.sum(x) - 1})
        
        # Bounds: weights between 0 and 1 (no short selling)
        bounds = tuple((0, 1) for _ in range(self.n_assets))
        
        # Initial guess: equal weights
        x0 = np.array([1 / self.n_assets] * self.n_assets)
        
        # Maximize Sharpe ratio (minimize negative Sharpe)
        result = minimize(
            fun=neg_sharpe,
            x0=x0,
            method='SLSQP',
            bounds=bounds,
            constraints=constraints
        )
        
        optimal_weights = result.x
        ret, vol = self.portfolio_performance(optimal_weights)
        sharpe = (ret - risk_free_rate) / vol
        
        return optimal_weights, ret, vol, sharpe


def calculate_asset_statistics(prices: pd.DataFrame) -> pd.DataFrame:
    """
    Calculate comprehensive statistics for assets.
    
    Args:
        prices: DataFrame with price data
        
    Returns:
        DataFrame with mean, std, variance, and other statistics
    """
    # Calculate returns
    returns = prices.pct_change().dropna()
    
    stats = pd.DataFrame({
        'Mean_Return': returns.mean(),
        'Std_Dev': returns.std(),
        'Variance': returns.var(),
        'Annualized_Mean': returns.mean() * 252,
        'Annualized_Std': returns.std() * np.sqrt(252),
        'Sharpe_Ratio': returns.mean() / returns.std() * np.sqrt(252),
        'Skewness': returns.skew(),
        'Kurtosis': returns.kurtosis(),
        'Min': returns.min(),
        'Max': returns.max()
    })
    
    return stats
