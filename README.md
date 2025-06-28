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

Install requirements:

```bash
pip install -r requirements.txt
```

Run the main script:

```bash
python main.py
```

You will be prompted to enter:
- Stock ticker symbol (e.g., AAPL)
- Start date (YYYY-MM-DD)
- End date (YYYY-MM-DD)

The script will fetch data, estimate OU parameters, generate trading signals, backtest the strategy, and display performance analytics and plots.

## Example Output

```yaml
===== Mean Reversion Strategy Backtest Summary =====
Symbol: AAPL
Date Range: 2020-01-01 to 2023-01-01
Total Trading Days: 756
Initial Capital: 10000
Final Portfolio Value: 11230.45
Total Return: 12.30%

Estimated Parameters:
  mu: 150.10
  theta: 0.18
  sigma: 4.32
```

## Requirements

- Python 3.8+
- pandas
- numpy
- scipy
- matplotlib
- yfinance

All requirements are listed in `requirements.txt`.

## Notes

- This project is for educational and research purposes only.
- Use at your own risk. Past performance does not guarantee future results.

## License

MIT License
