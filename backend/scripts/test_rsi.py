import pandas as pd
import yfinance as yf
import pandas_ta as ta

def calculate_rsi(series: pd.Series, length: int = 14):
    """Calculate RSI using pandas_ta (for testing purpose)."""
    return ta.rsi(series, length=length)

if __name__ == "__main__":
    ticker = "GC=F"
    print(f"Fetching data for {ticker}...")
    df = yf.download(ticker, period="5d", interval="1h")

    if isinstance(df.columns, pd.MultiIndex):
        df.columns = df.columns.get_level_values(0)

    if "Close" not in df.columns:
        raise ValueError("No 'Close' column found in data.")

    df["RSI"] = calculate_rsi(df["Close"])
    print(df.tail()[["Close", "RSI"]])
