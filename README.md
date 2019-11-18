# Flask Boilerplate

<p align="center">
  <a href="https://palletsprojects.com/p/flask/" target="blank"><img src="https://cdn.hashnode.com/res/hashnode/image/upload/v1518503935975/S1_-_WePM.png" width="320" alt="Flask Logo" /></a>
</p>

<p align="center"><a href="https://palletsprojects.com/p/flask/">Flask</a> is a lightweight WSGI web application framework.</p>

[![Build Status](https://travis-ci.org/msanvarov/flask-graphql-mongo-boilerplate.svg?branch=master)](https://travis-ci.org/msanvarov/flask-graphql-mongo-boilerplate)
[![codebeat badge](https://codebeat.co/badges/f8a6a8af-4118-4bfb-b329-e76c1fe4a5a0)](https://codebeat.co/projects/github-com-msanvarov-flask-graphql-mongo-boilerplate-master)

### 📚 Description

This boilerplate leverages the Flask framework to quickly prototype backend applications. It comes with database, logging, security, and authentication features out of the box.

---

### 🛠️ Prerequisites

#### 💻 Non Docker

- Please make sure to have MongoDB locally, or utilize Mongo on the cloud by configuring a cluster in [atlas](https://www.mongodb.com/cloud/atlas). Then grab the connection string and modify the `mongo_url` when configuring the project.

#### 🐳 Docker

- Please make sure to have docker desktop setup on any preferred operating system to quickly compose the whole project. Then follow the docker procedure outlined below.

**Note: Despite the fact that Docker Desktop comes free for both Mac and Windows, it only supports the Pro edition of Windows 10. A common workaround is to get Docker Toolbox which will bypass the Windows 10 Pro restriction by executing Docker in a VM.**

---

### 🚀 Deployment

#### Manual Deployment without Docker

- Install cookiecutter universally to scaffold the project.

```bash
# download cookiecutter
$ python3 -m pip install cookiecutter

# scaffold app with cookiecutter
$ cookiecutter https://github.com/msanvarov/flask-graphql-mongo-boilerplate
```

#### 🐳 Deploying with Docker

- When scaffolding the application using `cookiecutter`, select the option for `docker_development`.

- Then the web application, and MongoDB will be available to [http://localhost:5000](http://localhost:5000/), [http://localhost:27017](http://localhost:27017/) respectively.

### 🔒 Environment Configuration

By default, the application comes with a configuration module that can read every environment variable from the `.env` file. The [constants.py file](https://github.com/msanvarov/flask-graphql-mongo-boilerplate/blob/cookiecutter/%7B%7Bcookiecutter.project_name%7D%7D/%7B%7Bcookiecutter.app_name%7D%7D/constants.py) is responsible for mapping the environment variables to a python dictionary that can be accessed anywhere in the application.

**APP_URL** - the base URL for the application. Made mainly for E2E testing.

**MONGO_URL** - the URL to the MongoDB collection

**MONGO_DB** - the database to store data to

**WEBTOKEN_SECRET_KEY** - the secret key to encrypt/decrypt web tokens with. Make sure to generate a random alphanumeric string for this. Not

**WEBTOKEN_EXPIRATION_TIME** - **the time in seconds** indicating when the web token will expire; by default, it's 2400 seconds which is 40 mins.

**SMTP** - the simple mail transfer protocol url.

**SMTP_PORT** - usually the default standard ports: 25, 587, 465.

**EMAIL_USERNAME** - either username or email to authenticate smtp with.

**EMAIL_PASSWORD** - password to authenticate smtp with.

---

### 🍬 Features

- Based on [Flask](https://github.com/pallets/flask).

- GraphQL Framework for Python, [Graphene](https://github.com/graphql-python/graphene). With GraphQL support for Flask in the form of [Flask-GraphQL](https://github.com/graphql-python/flask-graphql).

- [PyJWT](https://github.com/jpadilla/pyjwt) library that allows encoding and decoding JSON Web Tokens (JWT).

- [PyMongo](https://github.com/mongodb/mongo-python-driver), the official Python driver for MongoDB.

- [Sentry SDK](http://sentry.io/) for tracking errors externally.
 
- [Tox](https://tox.readthedocs.io/en/latest/) to standardize Python testing.
 
- [Faker](https://github.com/joke2k/faker) for generating fake data in migrations.

---

### 🌱 Project Structure

A quick synopsis of the folder structure.

```text
.
├── LICENSE
├── cookiecutter.json
├── hooks
│   ├── post_gen_project.sh
│   └── pre_gen_project.py
├── renovate.json
└── {{cookiecutter.project_name}}
    ├── CHANGELOG.md
    ├── Dockerfile
    ├── LICENSE
    ├── Makefile
    ├── Pipfile
    ├── Pipfile.lock
    ├── README.md
    ├── docker-compose.yml
    ├── docker-entrypoint.sh
    ├── docs
    │   ├── Makefile
    │   ├── conf.py
    │   ├── console_script_setup.rst
    │   ├── index.rst
    │   ├── prompts.rst
    │   ├── pypi_release_checklist.rst
    │   ├── readme.rst
    │   ├── travis_pypi_setup.rst
    │   ├── troubleshooting.rst
    │   └── tutorial.rst
    ├── manage.py               // flask scripts
    ├── requirements.txt
    ├── tests
    │   ├── __init__.py
    │   ├── conftest.py     // test configuration
    │   └── test_e2e.py     // e2e testing
    ├── tox.ini
    └── {{cookiecutter.app_name}}
        ├── __init__.py
        ├── config.py
        ├── constants.py        // environment variables from .env file
        ├── resolvers
        │   ├── __init__.py
        │   └── auth.py         // authentication resolver
        ├── schemas
        │   ├── __init__.py
        │   └── profile.py      // profile schema
        └── utils
            ├── __init__.py
            ├── database.py     // database utility functions
            ├── email.py        // email utility functions
            ├── passwords.py    // hashing passwords
            └── webtokens.py    // encrypting/decrypting web tokens
```

___

### ✅ Testing

#### 🐳 Docker

Tests can be performed inside the docker container that contains the web application.

```bash
# e2e tests
$ docker exec -it {{cookiecutter.app_name}} pipenv run pytest
```

#### Non-Docker

```bash
# e2e tests for different python versions without pipenv
$ tox 

# e2e tests for different python versions without pipenv
$ pipenv run tox

# e2e tests without pipenv
$ pytest

# e2e tests with pipenv
$ pipenv run pytest
```

---

## License

Flask is [MIT licensed](LICENSE).

[Author](https://msanvarov.github.io/personal-portfolio/)
