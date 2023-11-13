#!bash
echo "Delete Existing"
# docker rmi $(docker images -qa -f 'dangling=true')
docker image rm -f k8s.krakend:0.0.1 || (echo "Image $(DOCKER_IMAGE) didn't exist so not removed."; exit 0)
docker build . -t k8s.krakend:0.0.1 -f Dockerfile --no-cache
echo "Running to install KrakenD"
docker run -p 8080:8080 k8s.krakend:0.0.1 run -dc krakend.json
echo "Finished launch KrakenD"