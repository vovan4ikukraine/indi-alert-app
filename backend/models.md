# 📘 Data Models

## User
- **id**: int — unique user identifier  
- **name**: str — user name or alias  
- **fcm_token**: str — Firebase Cloud Messaging token for push notifications  
- **created_at**: datetime — account creation timestamp  

---

## Instrument
- **id**: int — unique instrument identifier
- **ticker**: str — instrument symbol (e.g., "AAPL", "BTCUSD", "SPX500")  
- **name**: str — full title of the instrument
- **category**: str — instrument type (e.g., "stock", "crypto", "index")

---

## 🔔 Subscription
- **id**: int  
- **user_id**: int — reference to the User 
- **instrument_id**: int — reference to the Instrument
- **rsi_level**: float — RSI threshold (e.g., 30 or 70) 
- **direction**: str — either "above" or "below" 
- **interval**: str — timeframe for RSI check (e.g., "1h", "1d")

---

## ⚠️ Alert
- **id**: int  
- **user_id**: int  
- **instrument_id**: int  
- **rsi_value**: float — actual RSI value when triggered 
- **triggered_at**: datetime — alert trigger timestamp
