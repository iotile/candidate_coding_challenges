import amqp
import json
import time


def publish_messages():
    with amqp.Connection('localhost', userid="iotile", password="iotile", confirm_publish=True) as c:

        ch = c.channel()

        with open("/opt/src/messages.txt", "r") as input_messages:
            line = input_messages.readline()

            while len(line) > 0:
                signal, site, machine, value = line.split(",")
                body = {"value": float(value)}
                jbody = json.dumps(body)

                message = amqp.Message(body=jbody, application_headers={"timestamp_in_ms": int(time.time()*1000)})
                ch.basic_publish(message, exchange="amq.topic", routing_key=f'raw.arch.{site}.{machine}.{signal}')
                time.sleep(0.1)
                line = input_messages.readline()


if __name__ == "__main__":
    publish_messages()
