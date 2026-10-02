import random
import uuid
from datetime import date, timedelta


def build_booking():
    """Unique booking per call, so runs never collide on the shared public site."""
    checkin = date.today() + timedelta(days=random.randint(1, 30))
    checkout = checkin + timedelta(days=random.randint(1, 14))
    return {
        "firstname": f"Test{uuid.uuid4().hex[:8]}",
        "lastname": "Student",
        "totalprice": random.randint(50, 500),
        "depositpaid": random.choice([True, False]),
        "bookingdates": {
            "checkin": checkin.isoformat(),
            "checkout": checkout.isoformat(),
        },
        "additionalneeds": "Breakfast",
    }
