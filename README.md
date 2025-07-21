# Mean Reversion Trading Strategy 📈
![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/josetraderx/mean_reversion_OU/main)
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/josetraderx/mean_reversion_OU/blob/main/mean_reversion_demo.ipynb)

A sophisticated implementation of a mean-reversion trading bot using real market data and the Ornstein-Uhlenbeck process for optimal entry/exit points.

## 🌐 Try it Online
**No installation required!** You can run this project directly in your browser:

- **📊 Interactive Demo**: Click the Binder badge above to launch a full Python environment
- **🚀 Quick Start**: Use the Colab badge for a guided notebook experience
- **⚡ Live Demo**: [View sample results](https://josetraderx.github.io/mean_reversion_OU/) (GitHub Pages)

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
├── mean_reversion_demo.ipynb  # Interactive notebook
├── requirements.txt     # Project dependencies
├── runtime.txt          # Python version for Binder
└── README.md           # Documentation
```

## 🔧 Installation

### Option 1: Run Online (Recommended for quick testing)
1. Click the **Binder** badge above
2. Wait for the environment to load (~2-3 minutes)
3. Open `mean_reversion_demo.ipynb`
4. Run all cells!

### Option 2: Local Installation
1. Clone the repository:
```bash
git clone https://github.com/josetraderx/mean_reversion_OU.git
cd mean_reversion_OU
```
2. Install requirements:
```bash
pip install -r requirements.txt
```

## 📊 Usage

### Interactive Notebook (Online)
The `mean_reversion_demo.ipynb` provides a step-by-step walkthrough with:
- Real data fetching
- Parameter estimation visualization
- Live backtesting results
- Interactive plots

### Command Line (Local)
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
  - jupyter (for notebooks)

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
