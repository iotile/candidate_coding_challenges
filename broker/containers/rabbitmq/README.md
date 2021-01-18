# Single Node RabbitMQ Deployment

This container sets up a single rabbitmq node with AMQP and MQTT support.  It
has a single default user `iotile/iotile` that is configured.  The user name
and password can be configured with environment variables.  This container is
most suitable for demos and internal development.

Build using:

```
docker build -t rabbitmq-singlenode containers/rabbitmq
```

Run using:

```
docker run -d -p 15672:15672 -p 1883:1883 rabbitmq-singlenode
```

This will start up the rabbitmq node and listen on port 15672 for http
management connections and 1883 for MQTT published messages.

This container does not support multiple organizations in a single
installation so machine messages should be published to:

```
raw/<site>/<vendor>/<model>/<machine id>
```

## Environment Variables

The only supported environment variables are:

- `BROKER_USER`: (default `iotile`) The username of a user with administrative
  access to the broker
- `BROKER_PASS`: (default `iotile`) The password of that user.

- `BROKER_RO_USER`: (default `iotile_ro`) The username of a user with readonly
  access to the broker
- `BROKER_RO_PASS`: (default `iotile_ro`) The password of that user.

- `BROKER_RW_USER`: (default `iotile_rw`) The username of a user with read write
  access to the broker
- `BROKER_RW_PASS`: (default `iotile_rw`) The password of that user.

The contents of the environment variables are hashed at container launch time
and merged with the settings in `definitions.json` to create the settings for
the rabbitmq node.
