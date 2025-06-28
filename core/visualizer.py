import matplotlib.pyplot as plt

def plot_signals(prices, signals, mu, sigma):
    plt.figure(figsize=(12, 6))
    plt.plot(prices, label='Price')
    plt.axhline(mu, color='k', linestyle='--', label='Mean')
    plt.axhline(mu + sigma, color='r', linestyle=':', label='+1 Sigma')
    plt.axhline(mu - sigma, color='g', linestyle=':', label='-1 Sigma')
    plt.scatter(prices[signals == 1].index, prices[signals == 1], marker='^', color='green', label='Buy', alpha=1)
    plt.scatter(prices[signals == -1].index, prices[signals == -1], marker='v', color='red', label='Sell', alpha=1)
    plt.legend()
    plt.title("Mean Reversion Signals")
    plt.show()

def plot_portfolio(portfolio):
    plt.figure(figsize=(12, 6))
    plt.plot(portfolio, label='Portfolio Value')
    plt.legend()
    plt.title("Backtest Portfolio Value")
    plt.show()
