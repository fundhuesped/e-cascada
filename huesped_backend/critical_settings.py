"""
Configuraciones criticas de publicar
"""
__author__ = 'Santi'
import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Path para los elementos estaticos
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# SECURITY WARNING: keep the secret key used in production secret!

SECRET_KEY = os.getenv('SECRET_KEY','SECRET_KEY_HARDCODED')

# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.sqlite3',
#        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#    }
#}
DB_NAME = os.getenv('DB_NAME','DB_NAME')
DB_USER = os.getenv('DB_USER','DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD','DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST','DB_HOST')
DB_PORT = os.getenv('DB_PORT','DB_PORT')


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': DB_NAME,
        'USER': DB_USER,
        'PASSWORD': DB_PASSWORD,
        'HOST': DB_HOST,
        'PORT': DB_PORT,
    }
}

#Configuracion CORS
CORS_ORIGIN_ALLOW_ALL = True

"""
#En produccion
    CORS_ORIGIN_WHITELIST = (
        'hostname.example.com',
    )
"""
