#!/bin/bash

docker stack rm iot_platform
echo "waiting 30 seconds..."
sleep 30
docker image rm localhost:5000/adapter adapter
docker volume rm iot_platform_db_data
docker image rm localhost:5000/fake_sensors