from kafka import KafkaConsumer
from validator import validate

consumer = KafkaConsumer(
    "cinema",
    bootstrap_servers="localhost:9092",
    auto_offset_reset="earliest",
    group_id="cinema-group"
)

for msg in consumer:

    message = msg.value.decode("utf-8")

    if validate(message):
        print("VALID:", message)
    else:
        print("NOT VALID:", message)