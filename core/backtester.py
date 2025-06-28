import pandas as pd

def run_backtest(prices, signals, initial_capital=10000):
    position = 0
    cash = initial_capital
    portfolio = []
    entry_price = 0

    for date, price in prices.items():
        signal = signals[date]
        if position == 0:
            if signal == 1:
                position = 1
                entry_price = price
            elif signal == -1:
                position = -1
                entry_price = price
        elif position == 1:
            if signal == -1:
                cash += (price - entry_price)
                position = 0
        elif position == -1:
            if signal == 1:
                cash += (entry_price - price)
                position = 0
        portfolio.append(cash)
    return pd.Series(portfolio, index=prices.index)
