import json

def validate(message):

    try:
        data = json.loads(message)

        required_fields = [
            "cinema_event",
            "film",
            "hall",
            "seat_row",
            "seat_number",
            "session_time",
            "ticket_price"
        ]

        for field in required_fields:
            if field not in data:
                return False

        if data["ticket_price"] <= 0:
            return False

        if data["seat_row"] <= 0 or data["seat_number"] <= 0:
            return False

        return True

    except:
        return False