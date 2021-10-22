# syntax=docker/dockerfile:1
FROM python:3.6-slim-buster
WORKDIR /test
COPY requirements.txt requirements.txt 
RUN pip install -r requirements.txt
COPY . /test
EXPOSE 5000
CMD [ "python","-m","flask","run","--host=0.0.0.0"]

