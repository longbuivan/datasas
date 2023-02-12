"""
# TODO:
1. Create a function to retrieve data from message_queue
2. Parse the message to tuple of data
3. Send data to s3 bucket

"""

import json
import logging
import os
import time
import uuid

import boto3
from botocore.exceptions import ClientError

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def lambda_handler(event, context):
    logger.info("Received event: " + json.dumps(event, indent=2))

    message_queue = event["Records"][0]["Sns"]["Message"]
    logger.info("Received message: " + message_queue)

    message = json.loads(message_queue)
    logger.info("Parsed message: " + json.dumps(message, indent=2))

    bucket_name = os.environ["BUCKET_NAME"]
    s3_client = boto3.client("s3")
    s3_resource = boto3.resource("s3")
    s3_resource.Bucket(bucket_name).put_object(
        Body=json.dumps(message),
        Key=str(uuid.uuid4()) + ".json",
    )

    logger.info("Successfully sent message to S3")

    return {
        "statusCode": 200,
        "body": json.dumps(message),
        "headers": {
            "Content-Type": "application/json",
        },
    }


if __name__ == "__main__":
    lambda_handler({}, {})
    time.sleep(10)

