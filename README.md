# Mean Reversion Trading Strategy 📈
![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

A sophisticated implementation of a mean-reversion trading bot using real market data and the Ornstein-Uhlenbeck process for optimal entry/exit points.

## 🚀 Features

- **Advanced OU Parameter Estimation**
  - Maximum Likelihood estimation
  - Robust statistical analysis
  - Adaptive parameter updates

- **Smart Signal Generation**
  - Buy/Sell signals based on mean deviations
  - Statistical confidence thresholds
  - Dynamic position sizing

- **Comprehensive Backtesting**
  - Portfolio performance tracking
  - Risk metrics calculation
  - Transaction cost modeling

- **Rich Visualizations**
  - Price and signal plots
  - Performance analytics
  - Real-time monitoring

## 🏗️ Project Structure

```plaintext
mean_reversion/
├── core/
│   ├── estimator.py     # OU parameter estimation
│   ├── strategy.py      # Trading signal generation
│   ├── backtester.py    # Backtesting engine
│   └── visualizer.py    # Plotting and analytics
├── main.py              # Main execution script
├── requirements.txt     # Project dependencies
└── README.md           # Documentation
```

## 🔧 Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/mean_reversion.git
cd mean_reversion
```

2. Install requirements:
```bash
pip install -r requirements.txt
```

## 📊 Usage

Run the main script:
```bash
python main.py
```

The script will prompt you for:
- Stock ticker symbol (e.g., AAPL)
- Start date (YYYY-MM-DD)
- End date (YYYY-MM-DD)

## 📈 Example Output

```yaml
===== Mean Reversion Strategy Backtest Summary =====
Symbol: AAPL
Date Range: 2020-01-01 to 2023-01-01
Total Trading Days: 756
Initial Capital: 10000
Final Portfolio Value: 11230.45
Total Return: 12.30%

Estimated Parameters:
  mu: 150.10    # Mean level
  theta: 0.18   # Mean reversion speed
  sigma: 4.32   # Volatility
```

## 📋 Requirements

- **Python 3.8+**
- Core Libraries:
  - pandas
  - numpy
  - scipy
  - matplotlib
  - yfinance

All dependencies are listed in `requirements.txt`

## ⚠️ Disclaimer

- This project is for educational and research purposes only
- Past performance does not guarantee future results
- Trade at your own risk
- Always validate strategies with paper trading first

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📧 Contact

For questions and feedback, please open an issue or reach out through GitHub.
