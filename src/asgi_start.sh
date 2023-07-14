#!/bin/bash

set -o errexit
set -o pipefail
set -o nounset

daphne core.asgi:application -b 0.0.0.0 -p 9900