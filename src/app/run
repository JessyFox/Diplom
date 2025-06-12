#!/usr/bin/env bash

set -e

python3 -m flask db upgrade
python3 -m gunicorn -b 0.0.0.0:3000 -w 4 app:app