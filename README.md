# cognixus_challenge
A basic todo list server.

## 1.1 Instruction for prework
### 1. Docker installation
https://docs.docker.com/engine/install/
### 2. Check whether the docker and docker-compose are installed
- command: docker --version
- command: docker-compose --version
### 3. Git clone this repo.
## 1.2 Instruction for building and running the app
### 1. Go to this repo directory and run server.
- command: docker-compose up -d --build
### 2. Accessing the web container.
- command: docker exec -it challenge-web-1 /bin/bash
### 3. Create a superuser for the server in the container.
- command: python3 manage.py createsuperuser
## 1.3 Instruction for testing the app
### Check the admin url
- link: http://localhost:8000/admin/
## 1.4 Interface documentation
### 1. Token Authentication
- Create a token for admin/user in the admin url under "AUTH TOKEN"
### 2. Login with Facebook account
- Insert your facebook key and secret at SOCIAL_AUTH_FACEBOOK_KEY & SOCIAL_AUTH_FACEBOOK_SECRET inside the settings.py before running the server.
- Click login with Facebook at link: http://localhost:8000/login/
- Use admin account to set the password of the facebook account in the admin url.
### 3. Check authentication token using command
- command: curl -d "username=<username>" -d "password=<password>" -X post http://localhost:8000/api-token-auth/
### 4. List all todo tasks
- command: curl http://localhost:8000/api/v1/List/ -H "Authorization: Token <token>" -H 'Accept: application/json; indent=4'
### 5. Add new todo task
- command: curl http://localhost:8000/api/v1/List/ -H "Authorization: Token <token>" -X POST -d title="<title>" -d description="<description>"
### 6. Delete a todo task 
- command: curl http://localhost:8000/api/v1/task id/ -H "Authorization: Token <token>" -X DELETE
### 7. Mark a todo task as completed
- command: curl http://localhost:8000/api/v1/task id/ -H "Authorization: Token <token>" -X PUT -d completion="<true/false>" -d title="<title>" -d description="<description>"
