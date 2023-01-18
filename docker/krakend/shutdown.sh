echo "Shut down KrakenD"
docker image rm -f k8s.krakend:0.0.1
docker container rm -f k8s.krakend:0.0.