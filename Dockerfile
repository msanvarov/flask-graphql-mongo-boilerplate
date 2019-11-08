FROM python:3.8

# App directory
WORKDIR /app

# Environment setup
COPY .env.example .env

# Copy source files
COPY . .

# Download dependencies
RUN pip install -r requirements.txt

CMD python manage.py runserver