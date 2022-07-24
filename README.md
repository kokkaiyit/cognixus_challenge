# cognixus_challenge
A basic todo list server.

## Installation
### 1. Docker installation
https://docs.docker.com/engine/install/
### 2. Check whether the docker and docker-compose are installed
- command: docker --version
- command: docker-compose --version
### 3. Git clone this repo.
### 4. Go to this repo directory and run server.
- command: docker-compose up -d --build
### 5. Accessing the web container.
- command: docker exec -it challenge-web-1 /bin/bash
### 6. Create a superuser for the server in the container.
- command: python3 manage.py createsuperuser
## Server guide
### Admin url
- link: http://localhost:8000/admin/
### Token Authentication
- Create a token for admin/user in the admin url under "AUTH TOKEN"
### Login with Facebook account
- Insert your facebook key and secret at SOCIAL_AUTH_FACEBOOK_KEY & SOCIAL_AUTH_FACEBOOK_SECRET inside the settings.py before running the server.
- Click login with Facebook at link: http://localhost:8000/login/
- Use admin account to set the password of the facebook account in the admin url.
### Check authentication token using command
- command: curl -d "username=<username>" -d "password=<password>" -X post http://localhost:8000/api-token-auth/
### List all todo tasks
- command: curl http://localhost:8000/api/v1/List/ -H "Authorization: Token <token>" -H 'Accept: application/json; indent=4'
### Add new todo task
- command: curl http://localhost:8000/api/v1/List/ -H "Authorization: Token <token>" -X POST -d title="<title>" -d description="<description>"
### Delete a todo task 
- command: curl http://localhost:8000/api/v1/<id>/ -H "Authorization: Token <token>" -X DELETE
### Mark a todo task as completed
- command: curl http://localhost:8000/api/v1/<id>/ -H "Authorization: Token <token>" -X PUT -d completion="<true/false>" -d title="<title>" -d description="<description>"
