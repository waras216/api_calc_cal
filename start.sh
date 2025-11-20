#!/bin/bash

source /opt/venv/bin/activate

python manage.py migrate
python manage.py collectstatic --noinput

gunicorn backend_calories_calc.wsgi:application --bind 0.0.0.0:$PORT
