#!/usr/bin/env bash

source env/bin/activate
FLASK_APP=hello.py flask run --host=0.0.0.0 --port=24876

