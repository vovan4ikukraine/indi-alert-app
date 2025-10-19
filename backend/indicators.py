import pandas as pd

def calculate_rsi(prices, period: int = 14):
    """
    Calculate RSI (Relative Strength Index).
    :param prices: close prices list (list[float])
    :param period: period RSI (default 14)
    :return: values list of RSI
    """
    if len(prices) < period + 1:
        return [None] * len(prices)

    df = pd.DataFrame(prices, columns=["close"])
    delta = df["close"].diff()

    gain = delta.clip(lower=0)
    loss = -delta.clip(upper=0)

    avg_gain = gain.rolling(window=period).mean()
    avg_loss = loss.rolling(window=period).mean()

    rs = avg_gain / avg_loss
    rsi = 100 - (100 / (1 + rs))

    return rsi.tolist()
