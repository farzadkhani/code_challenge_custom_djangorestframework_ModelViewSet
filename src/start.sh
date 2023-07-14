#!/bin/bash

set -o errexit
set -o pipefail
set -o nounset

python /app/manage.py migrate
python /app/manage.py collectstatic --no-input --clear --no-post-process
python /app/manage.py runserver 0.0.0.0:9000