#! /bin/bash

python3 -m venv env
source env/bin/activate
pip install -r req.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver