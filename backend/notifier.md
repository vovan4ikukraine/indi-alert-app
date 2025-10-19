# Firebase Cloud Messaging (FCM) Integration Guide

## Overview
The backend uses **Firebase Cloud Messaging (FCM)** to send push notifications to users when RSI alerts are triggered.

---

## Step 1 — Create Firebase Project
1. Go to [Firebase Console](https://console.firebase.google.com/)
2. Click **Add Project**
3. Name your project (e.g., `rsi-alert-app`)
4. Disable Google Analytics (optional)
5. Once created, open **Project Settings → Cloud Messaging**
6. Copy your **Server Key (Legacy key)** — this will be used as `FCM_SERVER_KEY`

---

## Step 2 — Update `.env` file

Add this line to your `.env` file (and `.env.example`):

```bash
DATABASE_URL=sqlite:///./rsi_alert.db
SCHEDULE_INTERVAL_MINUTES=15
FCM_SERVER_KEY=your_firebase_key_here
```

## Step 3 — Notification Function (Concept)

```python
    def send_push(fcm_token: str, title: str, body: str, data: dict = {}):
        """
        Sends a push notification via Firebase Cloud Messaging (FCM).
        Params:
            fcm_token (str): Device registration token
            title (str): Notification title
            body (str): Notification body
            data (dict): Optional extra payload
        Returns:
            response (dict): Firebase API response
        """
        # Pseudocode:
        # - Prepare JSON payload
        # - Send POST request to https://fcm.googleapis.com/fcm/send
        # - Include "Authorization: key=<FCM_SERVER_KEY>" header
        # - Retry on 5xx errors or timeouts (max 3 attempts)

        # Error Handling & Retry
        # Retry sending if HTTP status 500–599 (server-side failure)
        # Backoff: wait 1s, 2s, 4s before retry
        # Log failures for debugging
        # Skip invalid tokens (status invalid-registration)
```

##  Step 4 — Test Script

Create a test script at backend/scripts/test_push.py (pseudocode):

```python
    """
    test_push.py — test sending a demo push notification via FCM
    """

    from backend.notifier import send_push

    TEST_FCM_TOKEN = "your_test_fcm_token"

    if __name__ == "__main__":
        print("Sending test notification...")
        response = send_push(
            TEST_FCM_TOKEN,
            title="RSI Alert Demo",
            body="Test push from backend integration",
            data={"ticker": "BTCUSDT", "rsi": 75.2}
        )
        print(response)
```

## Verification

Run: python backend/scripts/test_push.py
Expected: Firebase returns a JSON with "success": 1
If "error": "InvalidRegistration", check your test token or FCM key

## Future Enhancements

- Add batch sending for multiple tokens
- Queue notifications (e.g., using Celery or RQ)
- Localize titles & messages by user language