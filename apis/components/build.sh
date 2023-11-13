docker build -t integration-api .

docker run -p 5000:5000 --name integration-api integration-api
