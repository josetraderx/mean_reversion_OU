import numpy as np
import pandas as pd

def mean_reversion_signals(prices, mu, sigma, threshold=1):
    signals = pd.Series(index=prices.index, data=0)
    signals[prices < (mu - threshold * sigma)] = 1   # Buy
    signals[prices > (mu + threshold * sigma)] = -1  # Sell
    return signals
