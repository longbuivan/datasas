
from confluent_kafka import Consumer, KafkaError
import logging
# set up logging
logging.basicConfig(filename='app.log', level=logging.INFO,
                    format='%(asctime)s %(message)s')



def _get_kafka_consumer(consumer_conf, credentials, topic_name):
    # Set up the Kafka consumer configuration
    conf = {
        'bootstrap.servers': consumer_conf['bootstrap_servers'],
        'group.id': consumer_conf['group_id'],
        'auto.offset.reset': 'earliest'
    }
    
    # Create a Kafka Consumer instance
    consumer = Consumer(conf)
    
    # Subscribe to the desired topic
    consumer.subscribe([topic_name])
    
    try:
        while True:
            msg = consumer.poll(1.0)
            
            if msg is None:
                print("No message received yet...")
                continue
            if msg.error():
                if msg.error().code() == KafkaError._PARTITION_EOF:
                    print("Reached end of partition event for {}.".format(msg.topic()))
                else:
                    print("Error while polling for messages: {}".format(msg.error()))
            else:
                print("Received message: key={}, value={}".format(msg.key(), msg.value()))
    except KeyboardInterrupt:
        print("Exiting the Kafka Consumer loop.")
    finally:
        # Close the Kafka Consumer instance
        consumer.close()

