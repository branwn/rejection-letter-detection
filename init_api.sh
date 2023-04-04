#!/usr/bin/env bash

set -x
set -e

pip3 install -r requirements.txt
python3 -m flask run --host=0.0.0.0 --port=13000