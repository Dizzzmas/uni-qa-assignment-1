# Set base image (host OS)
FROM python:3.7-alpine3.14

ARG SERVER_PORT=5000
ARG SERVER_HOST=http://server
ENV SERVER_PORT=$SERVER_PORT
ENV SERVER_HOST=$SERVER_HOST

# Set the working directory in the container
WORKDIR /usr/app

# Copy the dependencies file to the working directory
COPY . /usr/app/

# Install the dependencies
RUN pip install -r ./requirements.txt
