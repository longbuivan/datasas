echo "Pulling Repo from GitHub"
git clone https://github.com/airbytehq/airbyte.git
cd airbyte
echo "Pulling images from Docker Hub"
docker-compose pull
echo "Starting Airbyte"
docker-compose up
