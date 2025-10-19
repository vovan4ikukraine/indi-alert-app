from fastapi import APIRouter

router = APIRouter()

@router.get("/{ticker}")
def get_rsi(ticker: str):
    """
    Placeholder endpoint:
    Should later fetch the current RSI value for the given ticker
    (e.g. from yfinance or another data source).
    """
    return {"ticker": ticker, "rsi": None, "status": "not implemented"}
