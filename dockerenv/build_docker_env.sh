#!/bin/bash

docker_image_name="currency_reporter:0.1"
docker_container_name="currency_reporter"

# Set up directories
working_dir=$(cd $(dirname $0); pwd)
cd $working_dir
script_dir=`realpath ../scripts`

docker build -t $docker_image_name .
docker run -d --rm \
    -v /var/run/docker.sock:/var/run/docker.sock \
    -v $script_dir:/root/scripts \
    --network host \
    -h $docker_container_name \
    --name $docker_container_name \
    $docker_image_name /root/scripts/report_deamon.py
