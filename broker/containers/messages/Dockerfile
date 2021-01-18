FROM python:3.7-slim

RUN mkdir -p /opt && mkdir -p /opt/src

WORKDIR /opt/src

RUN pip install amqp

COPY containers/messages/messages.txt /opt/src
COPY containers/messages/messages.py /opt/src

CMD python /opt/src/messages.py /opt/src/messages.txt