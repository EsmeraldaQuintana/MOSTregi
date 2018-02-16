#!/bin/zsh
echo "!!! makemigrations:" &&
python3 manage.py makemigrations &&
echo "!!! migrate:" &&
python3 manage.py migrate &&
echo "!!! test:" &&
python3 manage.py test &&
echo "!!! runserver:" &&
python3 manage.py runserver
