FROM python:3.9
#FROM ubuntu:20.04
#RUN apt-get update && \
#    apt-get install -y software-properties-common && \
#    add-apt-repository -y ppa:deadsnakes/ppa && \
#    apt-get update && \
#    apt install -y python3.8
#RUN pypip install --upgrade pip
RUN apt-get update && apt install mariadb-client -y
WORKDIR /jobsite-server
COPY . .
RUN pip install -r requirements.txt
#RUN cd jobsite
RUN cd jobsite
#CMD cd jobsite && python manage.py runserver
EXPOSE 8000