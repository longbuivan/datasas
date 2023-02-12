docker build -t kafka-broker .

docker run -p 9092:9092 --name kafka-broker kafka-broker
