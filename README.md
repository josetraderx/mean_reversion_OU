# Mean Reversion Trading Strategy (Ornstein-Uhlenbeck Process)

A modular implementation of a mean-reversion trading bot using real market data and the Ornstein-Uhlenbeck process.

## Features
- OU parameter estimation (Maximum Likelihood)
- Buy/Sell signal generation based on deviations from the mean
- Backtesting with portfolio tracking
- Visualizations of signals and performance

## Structure
- `core/estimator.py`: Parameter estimation
- `core/strategy.py`: Signal generation
- `core/backtester.py`: Backtest engine
- `core/visualizer.py`: Plots and analytics
- `main.py`: Main script

## Usage

1. **Install requirements:**
   ```bash
   pip install -r requirements.txt
