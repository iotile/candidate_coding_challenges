FROM rabbitmq:3.7.17-management-alpine

ENV TIMESTAMP_PLUGIN_SHA256=fcc801755ad72eae8ad15bcd5271454f8ce70053a7b9133d011b24003c3cf849

# Install timestamp plugin (verifying SHA256 against golden version)

RUN set -eux; \
	apk add --no-cache --virtual .build-deps \
	wget \
	unzip; \
	wget --no-check-certificate --progress dot:giga https://dl.bintray.com/rabbitmq/community-plugins/3.7.x/rabbitmq_message_timestamp/rabbitmq_message_timestamp-20170830-3.7.x.zip; \
	sha256sum rabbitmq_message_timestamp-20170830-3.7.x.zip | grep -q "^$TIMESTAMP_PLUGIN_SHA256 "; \
	unzip rabbitmq_message_timestamp-20170830-3.7.x.zip; \
	rm -f rabbitmq_message_timestamp-20170830-3.7.x.zip; \
	mv rabbitmq_message_timestamp-20170830-3.7.x.ez /plugins/; \
	rabbitmq-plugins list | grep -q 'rabbitmq_message_timestamp'; \
	apk del .build-deps;

RUN rabbitmq-plugins enable rabbitmq_shovel rabbitmq_shovel_management rabbitmq_amqp1_0 rabbitmq_auth_backend_http rabbitmq_auth_backend_cache;\
	rabbitmq-plugins list --enabled | grep -q 'rabbitmq_shovel' &\
	rabbitmq-plugins list --enabled| grep -q 'rabbitmq_shovel_management' &\
	rabbitmq-plugins list --enabled| grep -q 'rabbitmq_auth_backend_http' &\
	rabbitmq-plugins list --enabled| grep -q 'rabbitmq_auth_backend_cache' &\
	rabbitmq-plugins list --enabled| grep -q 'rabbitmq_amqp1_0'

ENV BROKER_USER=iotile
ENV BROKER_PASS=iotile
ENV BROKER_RO_USER=iotile_ro
ENV BROKER_RO_PASS=iotile_ro
ENV BROKER_RW_USER=iotile_rw
ENV BROKER_RW_PASS=iotile_rw

# We need jq available to be able to override the rabbitmq default username and password
RUN apk add jq

RUN rabbitmq-plugins enable --offline rabbitmq_mqtt rabbitmq_consistent_hash_exchange rabbitmq_message_timestamp
ADD containers/rabbitmq/config/definitions.json /etc/rabbitmq/


# Add in the custom docker entrypoint
COPY containers/rabbitmq/config/docker-entrypoint.sh /usr/local/bin/
RUN chmod +x /usr/local/bin/docker-entrypoint.sh
COPY containers/rabbitmq/config/generate_password.py /usr/local/bin/
