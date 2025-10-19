import asyncio
import yfinance as yf
from indicators import calculate_rsi

async def fetch_data(ticker: str):
    print(f"Fetching data for {ticker}...")
    data = yf.download(ticker, period="7d", interval="1h")
    close_prices = data["Close"].squeeze().tolist()
    return close_prices

async def main():
    tickers = ["GC=F", "^GSPC", "SI=F"]

    for ticker in tickers:
        prices = await fetch_data(ticker)
        rsi_values = calculate_rsi(prices, period=14)
        last_rsi = rsi_values[-1] if rsi_values and rsi_values[-1] is not None else "n/a"
        print(f"{ticker} → RSI(14): {last_rsi}")

if __name__ == "__main__":
    asyncio.run(main())
