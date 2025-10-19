# RSI Indicator Specification

## Function
`calculate_rsi(series: pd.Series, length: int = 14) -> pd.Series`

### Description
Calculates the Relative Strength Index (RSI) for a given time series of closing prices.

### Parameters
- **series**: `pd.Series` — sequence of closing prices (e.g., from Yahoo Finance)
- **length**: `int` — RSI period (default = 14)

### Returns
- **rsi**: `pd.Series` — RSI values (0–100), same index as input

### Notes
- Uses standard Wilder’s smoothing method.
- Can be implemented manually or via `pandas_ta.rsi()`.
- Values >70 indicate overbought, <30 indicate oversold conditions.
