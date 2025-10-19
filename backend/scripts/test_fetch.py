"""
Test script for data fetcher specification.
Fetches last 100 candles for Gold (GC=F) using yfinance and prints result.
"""

import yfinance as yf

def test_fetch():
    ticker = "GC=F"
    df = yf.download(ticker, period="5d", interval="1h")
    print(f"Fetched {len(df)} rows for {ticker}")
    if not df.empty:
        print("Last close:", df["Close"].iloc[-1])
    else:
        print("No data fetched.")

if __name__ == "__main__":
    test_fetch()