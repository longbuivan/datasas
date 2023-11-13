from kafka import KafkaProducer
import json

# Define a Kafka producer
producer = KafkaProducer(bootstrap_servers='localhost:9092')

# Define the topic name
topic_name = 'test_topic'

# Define the mock data
mock_data = [{"id": 1, "name": "John Doe"}, {"id": 2, "name": "Jane Doe"}]

# Convert the mock data to JSON
data = json.dumps(mock_data)

# Produce the data to the Kafka topic
producer.send(topic_name, key=bytes('key', 'utf-8'), value=bytes(data, 'utf-8'))

# Flush the producer to ensure the data is sent to the broker
producer.flush()

# Close the producer
producer.close()
