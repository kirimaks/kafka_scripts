from kafka import KafkaConsumer
from pprint import pprint


topic = "kirimaks"

consumer = KafkaConsumer(topic, bootstrap_servers=['localhost:9092'])

for msg in consumer:
    pprint(msg)
