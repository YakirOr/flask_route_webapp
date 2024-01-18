# Exercise
## The project:
This project aims to deploy a PostgreSQL server and Flask web app router based on a Docker environment. The Flask web app is designed to return information from the PostgreSQL server and container health status, depending on the request the web router will receive. For the /health request, it will check and return the status and the name of the container. For /number_of_tables, it will count and return the number of tables in the PostgreSQL database. The web app router will respond with a JSON structure.

## The workflow:
This workflow will build the web app router application and push it to Docker Hub. If you want to change the Docker repository, please set the Docker login credentials in the GitHub secret repository with the following names:
 ```sh
DOCKERHUB_USERNAME
DOCKERHUB_TOKEN
```
OR
You can use this repository: https://hub.docker.com/repositories/dockerprojectuser

# Prerequisites:
Make sure you have Docker and the Docker-compose plugin installed. After you clone, use the .env file to set all the necessary values.

# How to deploy:
Save the docker-compose and the .env files in the same folder and run the following command:
> sudo docker-compose up.

For running with more output information, run:
 ```sh
 sudo docker-compose up --build
```
To run the containers in the background, use:
 ```sh
 sudo docker-compose up -d
```



 









