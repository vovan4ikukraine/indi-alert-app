# Scheduler & RSI Check Job

## Overview
The scheduler runs periodic background tasks to check RSI values for all tracked instruments and trigger alerts if RSI crosses user-defined thresholds.

---

## Job Frequency
- Environment variable: `SCHEDULE_INTERVAL_MINUTES`
- Default: `15` minutes
- Scheduler: [APScheduler](https://apscheduler.readthedocs.io/en/stable/)

---

## Job Logic (Pseudocode)

```python
def check_rsi_job():
    """
    1. Fetch all subscribed instruments from the database
    2. For each instrument:
        - Retrieve the latest OHLC data using fetch_ohlc()
        - Compute RSI using calculate_rsi()
    3. For each user subscription:
        - Compare current RSI vs threshold (above/below)
        - If condition met and not recently alerted:
            - Record an Alert in DB
            - Send push notification via FCM
    4. Debounce: prevent duplicate alerts for same instrument within X minutes
    """
```

---

| Module         | Responsibility                     |
| -------------- | ---------------------------------- |
| `data_fetcher` | Get OHLC data via yfinance         |
| `indicators`   | Calculate RSI                      |
| `db`           | Store subscriptions and alerts     |
| `notifier`     | Send push notifications            |
| `scheduler`    | Register and run jobs periodically |

## Future improvements

- Add retry logic for failed API calls
- Add logging for skipped or failed instruments
- Allow dynamic rescheduling without restart
- Store job results for monitoring

---