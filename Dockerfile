FROM ubuntu:20.04

WORKDIR /home/django

RUN apt-get update
RUN apt-get install -y python3-pip
RUN apt-get install -y curl
RUN pip3 install django==3.2.10
RUN pip3 install django-rest-framework-social-oauth2
RUN pip3 install drf_social_oauth2
RUN pip3 install asgiref==3.5.0
RUN pip3 install sqlparse==0.4.2
RUN pip3 install psycopg2-binary==2.9.3

ADD . .

# EXPOSE 8000

# CMD ["python3", "manage.py" , "runserver", "0.0.0.0:8000"]
