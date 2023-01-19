ROOT_PATH=`pwd`

DOCKER_COMPOSE="${ROOT_PATH}/docker-compose.yml"
# docker-compose -f ${DOCKER-COMPOSE} up
echo "$DOCKER_COMPOSE"
docker-compose -f ${DOCKER_COMPOSE} up