#!/bin/bash

# Default to docker-compose unless an argument is provided
if [ "$1" == "podman" ]; then
    echo "Using podman-compose"
    COMPOSER="podman-compose"
else
    echo "Using docker-compose"
    COMPOSER="docker-compose"
fi

# Start the collector
$COMPOSER up -d
