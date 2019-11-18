#!/usr/bin/env bash

if [[ "{{cookiecutter.docker_development}}" = "yes" ]]
then
    docker-compose up -d

    echo
    echo "Docker has composed the application and is executing at http://localhost:5000."
else
    if [[ "{{cookiecutter.open_source_license}}" = "No License" ]]
    then
        rm LICENSE
    fi
    echo "Preparing web application..."
    python3 -m pip install pipenv

    echo "Fetching dependencies"
    pipenv install

    if [[ "{{cookiecutter.start_server_after_generating_template}}" = "yes" ]]
    then
        echo
        echo "Starting web application"
        pipenv run python manage.py runserver
    fi
fi






