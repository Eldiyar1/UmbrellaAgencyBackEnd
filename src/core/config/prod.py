from pathlib import Path

from .helpers.env_reader import env, csv

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = env('SECRET_KEY')

DEBUG = env('DEBUG', default=False, cast=bool)

ALLOWED_HOSTS = env('ALLOWED_HOSTS', cast=csv())

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}