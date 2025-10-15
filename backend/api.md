# API Endpoints

## GET /rsi/{ticker}
**Description:** Returns the current RSI value for a given instrument. 
**Parameters:**  
- `ticker`: instrument symbol (e.g., `AAPL`)  
**Response:**  
```json
{
  "ticker": "AAPL",
  "rsi": 68.2,
  "interval": "1h",
  "updated_at": "2025-10-11T18:30:00Z"
}
```

## POST /subscribe
**Description:** Creates a new RSI alert subscription for the user. 
**Request body:**  
```json
{
  "user_id": 1,
  "instrument_id": 42,
  "rsi_level": 30,
  "direction": "below",
  "interval": "1h"
}
```
**Response:** 
```json
{
  "id": 101,
  "message": "Subscription created successfully"
}
```

## GET /subscriptions/{user_id}
**Description:** Returns all active RSI subscriptions for a specific user. 
**Response:** 
```json
[
  {
    "subscription_id": 101,
    "instrument": "AAPL",
    "rsi_level": 30,
    "direction": "below",
    "interval": "1h"
  }
]
```

## POST /webhook/fcm-token
**Description:** Registers or updates a user’s FCM device token.
**Request body:**  
```json
{
  "user_id": 1,
  "fcm_token": "fcm_123456789"
}
```
**Response:** 
```json
{
  "message": "Token updated"
}
```