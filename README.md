# Dockerizing_Python_App
Dockerizing a simple python flask application 

## EXPLANATION OF DOCKER FILE

### `FROM python:alpine3.7`

The FROM command is used to state what OS you intend to use as the base image. In this line we are inheriting our image from alpine 3.7 python image, As we will deploy a python app, so we have used alpine python image.

### `MAINTAINER Syed Saad Ahmed, syedsaadahmed2094.sa@gmail.com`

The name or other info of the person who is the maintainer of particular docker file.

### `COPY . /app`

To copy files from your Docker host to a Docker image, you can use the COPY command. We are copying all the files from our directory to docker images at */app*

### `WORKDIR /app`

WORKDIR allows you change directory while Docker builds the image, and the new directory remains the current directory for the rest of the build instructions.

### `RUN pip install -r requirements.txt`

While building a Docker image, you may need to run commands for reasons such as installing applications and packages to be part of the image.

### `EXPOSE 5000`

You’ll use the EXPOSE command to choose what ports should be available to communicate with a container. When running Docker containers, you can pass in the -p argument known as publish, which is similar to the EXPOSE command.

### `CMD python ./run.py`

Docker can run only one CMD command. Therefore, if you insert two or more CMD instructions, Docker would only run the last one i.e. the most recent one.
ENTRYPOINT is similar to CMD, however, you can run commands while launching and it wouldn’t override the instructions you’ve defined at ENTRYPOINT.

## EXECUTING THE APPLICATION

### Building the docker image first

`docker build -t sample_image .`

Here, sample_image is the name of the Docker image. You can give it another name. The dot (.) at the end of the command indicates that the files you’re working with are in the current directory.

### Running the docker container

`docker run -itd --name python-app -p 5000:5000 sample_image`

Here, python-app is the name of your container that will be started, docker run has multiple flags like -i, -t, -d. you can explore them in docker official docs [here](https://docs.docker.com/engine/reference/commandline/run/), -p flag is used to publish/expose the port of container to the host.

### Here is the Output

`https://localhost:5000/`

### Checking the logs of your application

`docker logs <container_id>`
