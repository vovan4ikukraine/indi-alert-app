from fastapi import APIRouter

router = APIRouter()

@router.post("/")
def create_subscription():
    """
    Placeholder endpoint:
    Should later create a new subscription for a user, including:
    - user_id
    - instrument_id
    - RSI threshold
    - direction ('above' or 'below')
    - interval (e.g. '1h')
    """
    return {"status": "not implemented"}

@router.get("/{user_id}")
def list_subscriptions(user_id: int):
    """
    Placeholder endpoint:
    Should later return all RSI alert subscriptions for a specific user.
    """
    return {"user_id": user_id, "subscriptions": []}
