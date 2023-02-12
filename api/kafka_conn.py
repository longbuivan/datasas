"""
TODO:
1. Retrieve the data from kafka topic
2. Register schema information
3. Parse the data from kafka topic
4. Convert the data into a dataframe
5. Save the datafrom to s3 with Vault credentials
6. Upload the data to s3
7. Add logging to the code
8. Add commands the code
"""

import boto3
import hvac
import pandas as pd
from confluent_kafka import Consumer, KafkaError

# Connect to Hashicorp Vault to retrieve the AWS credentials
client = hvac.Client(url="http://vault.example.com:8200")
client.auth_approle("my-approle-id", "my-secret-id")

secret = client.read("secret/aws")

# Connect to AWS S3
s3 = boto3.client("s3",
                  aws_access_key_id=secret["data"]["access_key"],
                  aws_secret_access_key=secret["data"]["secret_key"])

# Consumer configuration
conf = {
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'mygroup',
    'auto.offset.reset': 'earliest'
}

# Parse the data from kafka topic
consumer = Consumer(conf)

try:
    data = consumer.poll(timeout_ms=1000)
except KafkaError as e:
    print(e)


# Register schema information
schema = {
    "type": "record",
    "name": "mydata",
    "fields": [
        {
            "name": "id",
            "type": "string"
        },
        {
            "name": "name",
            "type": "string"
        },
        {
            "name": "age",
            "type": "int"
        }
    ]
}


# Parse the data from kafka topic
data = consumer.poll(timeout_ms=1000)

# Convert the data into a dataframe
df = pd.DataFrame(data)

# Get current timestamp
timestamp = pd.Timestamp.now().strftime("%Y-%m-%d_%H-%M-%S")

# Save the data to s3 with Vault credentials
s3.upload_file(f"{timestamp}/mydata.csv", "mybucket", df.to_csv(index=False))

# Add logging to the code

# Add commands the code
