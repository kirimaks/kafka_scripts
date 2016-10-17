from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers=['localhost:9092'])
topic = "kirimaks"

producer.send(topic, b'raw_data')
producer.flush()
