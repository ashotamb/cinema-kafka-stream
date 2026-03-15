import json
import random
from datetime import datetime

films = [
    "Dune 2",
    "Oppenheimer",
    "Interstellar",
    "Avatar 2",
    "The Batman"
]

halls = [1, 2, 3, 4]

def generate_message():

    hall = random.choice(halls)

    data = {
        "cinema_event": "ticket_sale",
        "film": random.choice(films),
        "hall": hall,
        "seat_row": random.randint(1, 10),
        "seat_number": random.randint(1, 20),
        "session_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "ticket_price": random.randint(300, 700),
        "timestamp": datetime.utcnow().isoformat()
    }

    return json.dumps(data)