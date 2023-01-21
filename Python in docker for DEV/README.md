# Python in Docker container for development

## Part 1:
Demo a python app running a fast API server on local machine without Docker.

main.py : Contains 2 API endpoints (root, channel)
channel.py : JSON data for fast API server

### Instructions:
1. Clone and checkout this commit : git checkout 46cf8ad
2. Run : pip install fastapi
3. Run : pip install pip install "uvicorn[standard]"
4. Run uvicorn server:  uvicorn main:app --host 0.0.0.0 --port 8080 --reload
5. Open URL: http://0.0.0.0:8080/

## Part 2:
Now we have the code that runs on local. In this part we make it on on a docker container with no reload feature

Dockerfile : Code to build docker image
requirements.txt: for dependencies installation

### Instructions:
1. Clone and checkout this commit : git checkout 4da7df7
2. Build docker image by running :  docker build -t channel-api .
3. Run docker image on container : docker run -d -p 8080:80 channel-api
4. Open URL: http://0.0.0.0:8080/
5. Open URL: http://0.0.0.0:8080/channels/jackherrington
6. Open URL: http://0.0.0.0:8080/channels/someincorrectname

# Part 3:
We have code that runs on docker container locally without being live. In this part, we make add docker compose YAML file with reload command to rebuild the image if file is changed.

requirements.txt : added wacthflies
### Instructions:
1. Clone and checkout this commit : git checkout 2196ab4
2. Build image via docker compose: docker-compose up --build
3. Open URL: http://0.0.0.0:8080/
4. Open URL: http://0.0.0.0:8080/channels/jackherrington
5. Open URL: http://0.0.0.0:8080/channels/someincorrectname