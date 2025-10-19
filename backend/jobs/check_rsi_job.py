"""
check_rsi_job.py
----------------
Pseudocode for the RSI checking job that runs periodically via APScheduler.
"""

def check_rsi_job():

    instruments = get_instruments_with_subscriptions()


    for instrument in instruments:
        df = fetch_ohlc(instrument.ticker, interval="1h", period="1d")
        current_rsi = calculate_rsi(df["Close"]).iloc[-1]


        subs = get_subscriptions_for_instrument(instrument.id)
        for sub in subs:
            if is_threshold_crossed(current_rsi, sub):
                if not is_recently_alerted(sub.user_id, instrument.id):
                    create_alert(sub.user_id, instrument.id, current_rsi)
                    send_notification(sub.user_id, instrument.ticker, current_rsi)

    print("✅ RSI check job completed.")