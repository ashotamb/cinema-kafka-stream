from kafka import KafkaProducer
from generator import generate_message
import time

producer = KafkaProducer(
    bootstrap_servers="localhost:9092"
)

topic = "cinema"

while True:

    message = generate_message()

    print("Produced:", message)

    producer.send(topic, message.encode("utf-8"))

    time.sleep(2)