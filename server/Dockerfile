# Set base image (host OS)
FROM python:3.7-alpine3.14

# Infer from the build arguments the port to expose on the host machine
# By default, expose port 5000
ARG PORT=5000
ENV PORT=$PORT

EXPOSE ${PORT}/tcp

# Set the working directory in the container
WORKDIR /usr/app/

# Copy the dependencies file to the working directory
COPY . /usr/app/

# Install the dependencies
RUN pip install -r ./requirements.txt
