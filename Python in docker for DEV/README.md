# Python in Docker container for development

## Part 1:
Demo a python app running a fast API server on local machine without Docker.

main.py : Contains 2 API endpoints (root, channel)
channel.py : JSON data for fast API server

### Instructions:
1. Clone this folder/repo
2. Run : pip install fastapi
3. Run : pip install pip install "uvicorn[standard]"
4. Run uvicorn server:  uvicorn main:app --host 0.0.0.0 --port 8080 --reload
5. Open URL: http://0.0.0.0:8080/