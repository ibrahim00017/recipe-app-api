From python:3.7-alpine
MAINTAINER Ibrahim ABLADON 

ENV PYTHONUNBUFFERED 1
COPY ./requirements.text /requirements.text
RUN pip install -r /requirements.text

RUN mkdir /app
WORKDIR /app
COPY ./app /app

RUN adduser -D user
USER user