FROM python:3.9

# Label
LABEL maintainer="Sal Anvarov <msalanvarov@gmail.com>"

# App directory
WORKDIR /app

# Environment setup
COPY .env.docker.example .env

# Copy source files
COPY . .

# Download dependencies
RUN python3 -m pip install -r requirements.txt

# Expose port
EXPOSE 5000
