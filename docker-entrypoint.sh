#!/bin/bash

python manage.py migrate

gunicorn logic_service.wsgi --config logic_service/gunicorn_conf.py
