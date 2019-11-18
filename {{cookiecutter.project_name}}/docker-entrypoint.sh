#!/usr/bin/env bash

echo "Waiting for Mongo..."

while ! nc -z mongo 27017; do
  sleep 0.1
done

echo "Mongo started. Preparing to start web application..."

pipenv run python manage.py runserver