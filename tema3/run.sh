#!/bin/bash

if [[ -z "${SPRC_DVP}" ]]; then
    echo "Please set the SPRC_DVP environment variable."
    exit 1
fi

echo "Importing Grafana config..."

GRAFANA_CONF_DIR="$SPRC_DVP/grafana"
if [ -d "$GRAFANA_CONF_DIR" ] ; then
    read -p "$GRAFANA_CONF_DIR already exists. Should I delete it? y/n: " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]] ; then
        rm $GRAFANA_CONF_DIR -r
        cp volumes/grafana $GRAFANA_CONF_DIR -r
    else
        echo "$GRAFANA_CONF_DIR is needed to run the Grafana service correctly. Please rename or move the existing folder and try again."
        exit 1
    fi
else
    cp volumes/grafana $GRAFANA_CONF_DIR -r
fi

echo "Creating adapter..."
IMAGE_NAME=adapter

docker service create --name registry --publish 5000:5000 registry:2

docker build -t $IMAGE_NAME ./$IMAGE_NAME
docker tag $IMAGE_NAME localhost:5000/$IMAGE_NAME
docker push localhost:5000/$IMAGE_NAME

docker service rm registry

echo "Done. Let's run this beauty!"
docker stack deploy sprc3 -c stack.yml
