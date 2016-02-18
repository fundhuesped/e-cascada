"""
Configuraciones criticas de publicar
"""
__author__ = 'Santi'
import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# SECURITY WARNING: keep the secret key used in production secret!
if os.environ['SECRET_KEY']:
	SECRET_KEY = os.environ['SECRET_KEY']

# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
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