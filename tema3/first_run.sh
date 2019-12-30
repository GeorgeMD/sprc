#!/bin/bash

IMAGE_NAME=adapter
FAKE_SENSORS=fake_sensors

if [[ $# -eq 1 ]] ; then
    echo "Creating registry..."
    docker service create --name registry --publish 5000:5000 registry:2
fi

docker build -t $IMAGE_NAME ./$IMAGE_NAME
docker tag $IMAGE_NAME localhost:5000/$IMAGE_NAME
docker push localhost:5000/$IMAGE_NAME

docker build -t $FAKE_SENSORS ./$FAKE_SENSORS
docker tag $FAKE_SENSORS localhost:5000/$FAKE_SENSORS
docker push localhost:5000/$FAKE_SENSORS