# QA Assignment 1. Docker

https://docs.google.com/document/d/1laT1QVVWXNbZZrSk_cuPFMxUZtbNLkGZyBwVX7j8HPI

Quick note: this solution uses `docker-compose` instead of running the usual `docker` commands.

## Pre-requisites

You should have docker installed: https://docs.docker.com/get-docker/

## Quickstart

Run `sh ./start.sh` for quickstart.

This command will:

- Build docker images for client/server
- Create a user-defined network named `qa_assignment_1`
- Create docker volumes `servervol` and `clientvol`
- Run the server container with the Flask app
- Run the client container which will immediately request a file from the server, write it to `clientdata` and compare checksums.

## Checking that things work

- Run `docker exec -it client /bin/sh` to enter the client container. Run `cd ./client/clientdata` & `cat file.txt` to see the contents that were written to the file.
- Checking the network: `docker inspect qa_assignment_1_cs_network`
- Checking the volumes: `docker inspect qa_assignment_1_servervol` & `docker inspect qa_assignment_1_clientvol`

Docker containers configuration could be found in `docker-compose.yml`.

## Server API

The server is a Flask app featuring these endpoints:

- `GET /` - returns the contents of the file `serverdata/blah.txt`
- `GET /checksum` - returns the checksum of the file `serverdata/blah.txt`

## Misc

- If you ever need to directly access the data of your docker volumes on a Mac, this could be useful: https://gist.github.com/BretFisher/5e1a0c7bcca4c735e716abf62afad389
