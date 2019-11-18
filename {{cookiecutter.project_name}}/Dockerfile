FROM python:{{cookiecutter.python_version}}

# Label
LABEL maintainer="Sal Anvarov <msalanvarov@gmail.com>"

# Install netcat
RUN apt-get update \
    && apt-get -y install netcat \
    && apt-get clean

# App directory
WORKDIR /app

# Copy source files
COPY . .

# Download dependencies
RUN python3 -m pip install pipenv

# Setup pipenv
RUN pipenv install

# Expose port
EXPOSE 5000

# Starting web app
ENTRYPOINT ["sh", "/docker-entrypoint.sh"]
