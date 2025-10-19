"""
Configuration loader for environment variables.
Will later use python-dotenv or Pydantic BaseSettings.
"""

# Example of what will be read from .env later:
# FCM_SERVER_KEY=your_fcm_key_here
# DATABASE_URL=sqlite:///./rsi_alerts.db
# SCHEDULE_INTERVAL_MINUTES=5

# For now this is just a placeholder
def load_config():
    """
    Placeholder function — later it will load .env values.
    """
    return {
        "FCM_SERVER_KEY": None,
        "DATABASE_URL": None,
        "SCHEDULE_INTERVAL_MINUTES": 5
    }
