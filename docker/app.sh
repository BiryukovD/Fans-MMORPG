#!/bin/sh


echo Hello!!!!!!!
python3 manage.py collectstatic --noinput --clear
 
python3 manage.py makemigrations --noinput
python3 manage.py migrate --noinput

python3 manage.py loaddata db_dump.json

gunicorn -b '0.0.0.0:8000' Fans_MMORPG.wsgi:application


