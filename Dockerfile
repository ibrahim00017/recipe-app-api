From python:3.7-alpine
MAINTAINER Ibrahim ABLADON 

ENV PYTHONUNBUFFERED 1
COPY ./requirements.text /requirements.text
RUN apk add --update --no-cache postgresql-client
RUN apk add --update --no-cache --virtual .tmp-build-deps \
    gcc libc-dev linux-headers postgresql-dev

RUN pip install -r /requirements.text
RUN apk del .tmp-build-deps

RUN mkdir /app
WORKDIR /app
COPY ./app /app

RUN adduser -D user
USER user