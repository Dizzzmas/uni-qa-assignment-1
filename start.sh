#!/bin/bash

# Build the docker images for server/client
docker-compose build

# Run the containers for server/client
docker-compose up -d
