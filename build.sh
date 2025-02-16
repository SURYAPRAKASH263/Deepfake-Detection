#!/bin/bash
set -o errexit
pip install -r requirements.txt
python manage.py migrate

if [ "$CREATE_SUPERUSER" = "true" ]; then
    python manage.py createsuperuser --noinput --email "$DJANGO_SUPERUSER_EMAIL"
fi
python manage.py runserver