# Data Fetcher Specification

## Overview
The data fetcher module will handle retrieving OHLC (Open, High, Low, Close) data for given tickers using the **yfinance** library.

## Function: `fetch_ohlc(ticker: str, interval: str, period: str) -> pandas.DataFrame`
- **ticker** — the symbol (e.g. `"GC=F"`, `"^GSPC"`, `"SI=F"`).
- **interval** — data interval (`"1m"`, `"5m"`, `"1h"`, `"1d"`).
- **period** — how much data to retrieve (`"1d"`, `"5d"`, `"1mo"`, `"3mo"`, etc.).

### Expected Output
A DataFrame with columns:

Datetime | Open | High | Low | Close | Volume


### Notes
- Use `yfinance.download()` to get the data.
- Return only the `"Close"` column (for RSI calculations).
- If data is unavailable, handle exceptions gracefully (return empty DataFrame or raise custom error).

### Supported Tickers
| Market | Symbol |
|---------|---------|
| Gold    | GC=F |
| Silver  | SI=F |
| S&P 500 | ^GSPC |

---
### Example Usage (planned)
```python
from backend.indicators import fetch_ohlc

df = fetch_ohlc("GC=F", "1h", "5d")
print(df.tail())
```

## Testing

Run the test script backend/scripts/test_fetch.py to ensure connectivity and data availability.