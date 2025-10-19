from fastapi import FastAPI
from backend.routes import rsi, subscriptions

app = FastAPI(
    title="RSI Alert API",
    version="0.1.0",
    description="Backend service for RSI-based alerts and notifications"
)

# Register routers
app.include_router(rsi.router, prefix="/rsi", tags=["RSI"])
app.include_router(subscriptions.router, prefix="/subscriptions", tags=["Subscriptions"])

@app.get("/health")
def health_check():
    """
    Simple health check endpoint to verify that the API is running.
    """
    return {"status": "ok", "message": "RSI Alert API is healthy 🚀"}
