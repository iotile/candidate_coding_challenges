#!/bin/bash

set -o errexit
set -o pipefail
set -o nounset

while ! nc -zw1 "${POSTGRES_HOST}" "${POSTGRES_PORT}"; do
  echo "Waiting for database at ${POSTGRES_HOST}:${POSTGRES_PORT}..."
  sleep 1
done

python manage.py migrate
python manage.py runserver 0.0.0.0:8000
