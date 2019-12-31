#!/bin/bash

SECONDS=20
if [ $# -gt 0 ] ; then
    SECONDS=$1
fi

docker stack rm sprc3
echo "waiting "$SECONDS" seconds..."
sleep $SECONDS
docker image rm adapter localhost:5000/adapter
docker volume rm sprc3_db_data
