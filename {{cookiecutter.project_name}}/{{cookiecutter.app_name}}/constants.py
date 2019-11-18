import os

from dotenv import load_dotenv
from {{cookiecutter.app_name}}.config import ConfigurationType

load_dotenv()

CONSTANTS = {
    "HTTP_STATUS": {
        "404_NOT_FOUND": 404,
        "500_INTERNAL_ERROR": 500
    },
    # log levels: https://docs.python.org/3/library/logging.html
    "LOG_LEVEL": 20,
    "APP_URL": os.getenv("APP_URL"),
    "APP_ENV": ConfigurationType.DEVELOPMENT if os.getenv("APP_ENV") else ConfigurationType.PRODUCTION,
    "MONGO_URL": os.environ.get("MONGO_URL"),
    "MONGO_DB": os.getenv("MONGO_DB", "mongodb://localhost:27017"),
    # make sure to change the web
    # token secret key from "secret" to something else
    "WEB_TOKEN_SECRET_KEY": os.getenv("WEB_TOKEN_SECRET_KEY", "default"),
    # WEB_TOKEN_ACCESS_TOKEN_EXPIRES is meant to be in seconds
    "WEB_TOKEN_ACCESS_TOKEN_EXPIRES": os.getenv(
        "WEB_TOKEN_ACCESS_TOKEN_EXPIRES", 2400),
    "SMTP": os.getenv("SMTP"),
    "SMTP_PORT": os.getenv("SMTP_PORT"),
    "EMAIL_ACCOUNT": os.getenv("EMAIL_ACCOUNT"),
    "EMAIL_PASSWORD": os.getenv("EMAIL_PASSWORD"),
    "LOG_FILE_PATH": os.getenv("LOG_FILE_PATH"),
    "LOG_MAX_BYTES": int(os.getenv("LOG_MAX_BYTES")),
    "BACKUP_COUNT": os.getenv("BACKUP_COUNT"),
    "SENTRY_DSN": os.getenv("SENTRY_DSN"),
}
