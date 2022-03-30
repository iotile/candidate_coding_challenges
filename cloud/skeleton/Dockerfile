FROM python:3.8-slim-buster

ENV PYTHONUNBUFFERED 1
WORKDIR /app

RUN apt-get update && \
    apt-get install -y netcat && \
    apt-get clean

COPY server/requirements.txt .

RUN pip install -U pip==22.0.4 && \
    pip install -r requirements.txt
