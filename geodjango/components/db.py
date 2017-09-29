# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases
import os

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': os.environ.get("DBNAME"),
        'USER': os.environ.get("DBUSER"),
        'HOST': os.environ.get("DBHOST"),
        'PASSWORD': os.environ.get("DBPASS")
    }
}

if 'TRAVIS' in os.environ:
    DATABASES = {
        'default': {
            'ENGINE': 'django.contrib.gis.db.backends.postgis',
            'NAME': 'travisci',
            'USER': 'postgres',
            'PASSWORD': '',
            'HOST': 'localhost',
            'PORT': '',
        }
    }
