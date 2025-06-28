import pandas as pd
import yfinance as yf
from core.estimator import estimate_ou_params
from core.strategy import mean_reversion_signals
from core.backtester import run_backtest
from core.visualizer import plot_signals, plot_portfolio

def get_data(symbol, start, end):
    """
    Fetch historical stock data from Yahoo Finance.
    :param symbol: Stock symbol
    :param start: Start date (YYYY-MM-DD)
    :param end: End date (YYYY-MM-DD)
    :return: Series of closing prices with clean datetime index
    """
    df = yf.download(symbol, start=start, end=end)
    
    # Imprimir información del DataFrame para debug
    print("\nColumnas disponibles:", df.columns.tolist())
    
    # Manejar MultiIndex en columnas
    if isinstance(df.columns, pd.MultiIndex):
        # Si tenemos un MultiIndex, tomamos la columna 'Close' del primer nivel
        if 'Close' in df.columns.get_level_values(0):
            df = df['Close']  # Esto selecciona la columna 'Close' para todos los tickers
        else:
            raise ValueError("No se encontró la columna 'Close' en los datos")
    else:
        # Si no es MultiIndex, intentamos acceder directamente
        if 'Close' in df.columns:
            df = df['Close']
        else:
            raise ValueError("No se encontró la columna 'Close' en los datos")
    
    # Si df es un DataFrame (múltiples tickers), tomamos solo la primera columna
    if isinstance(df, pd.DataFrame):
        close = df.iloc[:, 0]
    else:
        close = df
    
    close = close.dropna()
    close.index = pd.to_datetime(close.index)
    
    return close

if __name__ == "__main__":
    # Get data
    symbol = 'AAPL'
    prices = get_data(symbol, '2020-01-01', '2023-01-01')

    # Estimate OU parameters
    mu, theta, sigma = estimate_ou_params(prices)

    # Generate trading signals
    signals = mean_reversion_signals(prices, mu, sigma, threshold=1)

    # Run backtest
    portfolio = run_backtest(prices, signals)

    # Visualize results
    plot_signals(prices, signals, mu, sigma)
    plot_portfolio(portfolio)

    # Print summary
    print("\n===== Mean Reversion Strategy Backtest Summary =====")
    print(f"Symbol: {symbol}")
    print(f"Date Range: {prices.index.min().date()} to {prices.index.max().date()}")
    print(f"Total Trading Days: {len(prices)}")
    print(f"Initial Capital: 10000")
    print(f"Final Portfolio Value: {portfolio.iloc[-1]:.2f}")
    print(f"Total Return: {(portfolio.iloc[-1] - 10000) / 10000 * 100:.2f}%")
    print(f"\nEstimated Parameters:\n  mu: {mu:.2f}\n  theta: {theta:.2f}\n  sigma: {sigma:.2f}")
    print("\nData Summary:")
    print(prices.describe())
    print("\nSignals Summary:")
    print(signals.value_counts())
    print(signals.describe())
    print("\nPortfolio Summary:")
    print(portfolio.describe())
    print("===================================================\n")
