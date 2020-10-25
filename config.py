"""Flask configuration variables."""
from os import environ, path, getenv
from dotenv import load_dotenv

# Load environment variables from file .env, stored in this directory.
load_dotenv()


class Config:
    # Set Flask configuration from .env file. The file structure is identical to the COVID model.

    # Flask configuration
    FLASK_APP = environ.get('FLASK_APP')
    FLASK_ENV = environ.get('FLASK_ENV')

    # Authentication variables
    SECRET_KEY = environ.get('SECRET_KEY')