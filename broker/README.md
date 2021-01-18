# Please do not publish a solution in either a fork or clone. Keep all of your work local!
#### If you do want to store your work, we ask that you keep it in a private repo (github lets everyone do this now).


## Introduction

This project is designed to get you familiar with one of the most basic functionalities of the ArchFX Broker. Our platform at its core is a message transformation platform. We receive (and request) some set of signals from the outside world and transform them into various standardized outputs that feed into other systems. From this simple behavior we have a lot of complexity to handle in reality -- where do you route messages, how to you ensure traceability, how is state and metadata mapping conducted, and other behaviors along those lines.

In this exercise, we are going to stick with implementing some simple message processing behavior without handling the complexities mentioned above (for now).

## Description of Provided Files & Prerequisites

To get started, we have provided a few files to make creating a solution here straightforward. The only requirement is that you have Docker installed on your machine.

- The `rabbitmq` folder contains a basic set of files that creates a rabbitMQ-backed message broker with a couple of plugins that we happen to use on our real solution. This is where messages will be sent from the test program as well as your implemented solution.
- The `messages` folder contains a Docker image set with an entry point of the test script. When you are ready to send data to the rabbitMQ server, you can invoke this container to run the Python script. If you have Python already installed on your system, this script can be run standalone; the docker file is provided for convenience across systems.

## Building the containers

To build the rabbitMQ container, we will use docker.

These commands are to be executed from the same level as this README (one level above `containers`).
```
docker build -t rabbitmq-singlenode -f containers/rabbitmq/Dockerfile .
docker run -d -p 15672:15672 -p 5672:5672 rabbitmq-singlenode
```

Port 15672 is used for the web admin interface. Port 5672 is for AMQP 0.9.1 traffic.
- The test script uses AMQP so that it can establish some useful resources.
- When writing your solution you will need to use an AMQP Python client. We use https://github.com/celery/py-amqp (`pip install amqp`) on the broker. It's not required for this exercise, but there were good reasons for us to choose this one over the alternatives like `pika`.

To build the `messages` container, you can also directly build it with docker. Invoking this container as a `run` will execute the test program and then exit.
```
docker build -t test-messages -f containers/messages/Dockerfile .
docker run -d test-messages
```

## Validating the setup & Preparing

To ensure that your containers are running appropriately, we recommend that you review this section.

#### RabbitMQ Running

Once you run the rabbitMQ docker image, you should be able to access the administrative interface in your localhost at http://localhost:15672. Log in to the admin interface with the credentials `iotile`/`iotile`. You should see the root admin page. Here, you can monitor incoming message rates, consumers, and other administrative rabbitMQ settings.

#### Test message running

If you run the test message script, and it doesn't report any errors, then it is probably running well. You can use the rabbitMQ admin interface to see how many messages it has received in recent times, to serve as a second validation.

## Demo Message Descriptions

The messages file will publish messages to rabbitMQ's `amq.topic` exchange on the routing key `raw.arch.{site}.{machine_id}.{signal_id}`. The wildcards stand for:
- `site` is a string with a value set to `ps--xxxx-xxxx`. The eight `x` items will be hex characters. An example might be `ps--0501-f5c2`.
- `machine_id` will be a string with a value set to `m--xxxx-xxxx` with the same characteristics as the site. An example of a machine ID would be `m--abcd-1234`.
- `signal_id` is a 4-digit hex string. An example of the signal ID would be `1028`.

Along with the message payload, each message has a header (in the `application_headers`) set with a timestamp in the field `timestam_in_ms`.

### Project goal

*Artifacts*
- You will need to have a third folder, `solution`. At a minimum, the `solution` folder needs to contain a `Dockerfile`, your Python solution script, and a `README.md` with your description of the solution.

Your goal is to write a Python script that can use AMQP to consume the messages. The script will then publish a transformed set of messages based on the inputs received. Your output routing key needs to be of the form `data.arch.{site}.{machine_id}.{output_signal_id}`. The site and machine ID need to match the incoming message, and the output signal ID and message payload will be computed according to the descriptions in the next section.

In bullet form, these are the three requirements:
1. Your program shall consume messages from a rabbitMQ server that arrive on `amq.topic` with the routing key `raw.arch.{site}.{machine_id}.{signal_id}`. (Hint: look up how to create a queue and bind it to the exchange using AMQP).
2. Your program shall transform the messages consumed according to the Incoming Message Signal ID Processing Rules in the next section.
3. Publish the transformed messages to `amq.topic` using the new routing key `data.arch.{site}.{machine_id}.{output_signal_id}`. The payload will conform to the processing rules (make sure to include the header timestamp in the outgoing message payload).

You will need to use the username/password combo `iotile`/`iotile` to connect to AMQP.

## Incoming Message Signal ID Processing Rules

The incoming data being provided comes from an SMT factory with a few different sites.
- `ps--0000-0001` has two machines that produce a signal ID of 1028.
- `ps--0000-0002` has two machines that produce a signal ID of 1055.

#### 1028 processing rules

A 1028 signal input will be an integer value that will grow incrementally over time. When you see a 1028 value for a machine, you must compute the delta from the previous highest value on that machine.

You also need to retrieve the field `timestamp_in_ms` from the message headers and put the value in the outgoing message payload.

Terminology: delta = Difference in current value from previous highest value seen since reset

- If no value has been observed for a machine (e.g. it's the first value), no output is produced.
- If the delta is 0 or negative, no output is produced.
- If the delta is positive, produce an output signal ID of 5051 with a value set to the delta computed.

As an example, if you receive these three messages as your first three messages for a machine:
```
raw/arch/ps--0000-0001/d--0000-0001/1028 {"value": 1} ; header timestamp_in_ms = 1
raw/arch/ps--0000-0001/d--0000-0001/1028 {"value": 2} ; header timestamp_in_ms = 2
raw/arch/ps--0000-0001/d--0000-0001/1028 {"value": 5} ; header timestamp_in_ms = 3
```
Your program would need to output
```
data/arch/ps--0000-0001/d--0000-0001/5051 {"delta": 1, "timestamp_in_ms": 2}
data/arch/ps--0000-0001/d--0000-0001/5051 {"delta": 3, "timestamp_in_ms": 3}
```
Under the hood, your consumer would have observed two deltas. The first signal has no preceding data point so it doesn't generate a delta. The timestamp in the outgoing message payload would match the timestamp on the most recent message used to compute the delta.


#### 1055 processing description

A 1055 signal input will be a floating point value that is to be directly output in the `value` of the message. The timestamp needs to be pulled from the header into the message payload as well.

If you saw the following incoming messages:
```
raw/arch/ps--0000-0002/d--0000-0002/1055 {"value": 70.425} ; header timestamp_in_ms = 1
raw/arch/ps--0000-0002/d--0000-0002/1055 {"value": 68.35} ; header timestamp_in_ms = 65
raw/arch/ps--0000-0002/d--0000-0002/1055 {"value": 67.98} ; header timestamp_in_ms = 128
```
Your program would need to output
```
data/arch/ps--0000-0002/d--0000-0002/1055 {"value": 70.425, "timestamp_in_ms": 1}
data/arch/ps--0000-0002/d--0000-0002/1055 {"value": 68.35, "timestamp_in_ms": 65}
data/arch/ps--0000-0002/d--0000-0002/1055 {"value": 67.98, "timestamp_in_ms": 128}
```

## Next Step : Design Review

After we evaluate your submission, the next step is generally a synchronous design review (via Breezy/Zoom/etc.) In this session, we will spend a bit of time going over your solution, and a larger amount of time exploring enhancements and extensions for handling more complicated cases. Here, we are looking to understand how you think about and design/architect the complicated platform. We will want to consider features that would be considered important for installation and maintenance at a customer site, as well as scalability and developer efficiency.

To give a sense of the style of question, here is the first two we will cover:

1. When processing 1028 signals, the processor we implemented would "lose" a data output if the processor fails in some way and reboots. To alleviate this, we could consider methods of caching the data. What approach would you propose we take to solve this?
2. When processing 1055 signals, we want to augment the output signal to have more metadata included in the outgoing message. This metadata currently exists in a different part of the Arch ecosystem and is accessible by an API call to the cloud (and we have a library to do this). This metadata is relatively static, but sometimes changes and needs to be refreshed (maybe every few days, not every few minutes). What type of system would you propose to obtain this metadata?





