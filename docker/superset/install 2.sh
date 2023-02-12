echo "Pulling Repo from GitHub"
git clone https://github.com/apache/superset.git
cd superset
echo "Pulling images from Docker Hub"
docker-compose -f docker-compose-non-dev.yml pull
echo "Starting Superset"
docker-compose -f docker-compose-non-dev.yml up