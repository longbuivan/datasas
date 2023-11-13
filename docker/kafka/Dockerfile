# Use an official Java runtime as the base image
FROM openjdk:8-jre-alpine

# Download and install Apache Kafka
ARG KAFKA_VERSION=2.6.0
ARG SCALA_VERSION=2.13
ARG KAFKA_BINARY=https://downloads.apache.org/kafka/${KAFKA_VERSION}/kafka_${SCALA_VERSION}-${KAFKA_VERSION}.tgz

RUN apk add --no-cache bash curl tar
RUN curl -SL "$KAFKA_BINARY" | tar xzf - -C /opt \
&& ln -s /opt/kafka_${SCALA_VERSION}-${KAFKA_VERSION} /opt/kafka

# Add a script to start the broker
COPY start-kafka-broker.sh /usr/bin/start-kafka-broker.sh
RUN chmod +x /usr/bin/start-kafka-broker.sh

# Expose port 9092 for the Kafka broker
EXPOSE 9092

# Start the broker
CMD ["start-kafka-broker.sh"]
