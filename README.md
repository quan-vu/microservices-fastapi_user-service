# Microservices with FastAPI - User Service

## Build Service as Docker Image

```
$ docker build -t image_microsercies-fastapi_user-service .
```

Run a container based on your image:

```
docker run -d --name container_microsercies-fastapi_user-service -p 8001:80 image_microsercies-fastapi_user-service
```

## Check it

Open your browser at: http://127.0.0.1:8001/items/5?q=somequery (using your Docker host). 

You will see something like:

```json
{"item_id": 5, "q": "somequery"}
```

Interactive API docs

Now you can go to http://192.168.99.100/docs or http://127.0.0.1:8001/docs (or equivalent, using your Docker host).

You will see the automatic interactive API documentation (provided by Swagger UI)