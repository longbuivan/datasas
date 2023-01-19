ROOT_PATH=`pwd`

DOCKER_COMPOSE="${ROOT_PATH}/docker-compose.yml"

echo "Closing Application"
docker-compose -f ${DOCKER_COMPOSE} down