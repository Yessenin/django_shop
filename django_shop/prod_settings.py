from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = '&m0_ygq0ciu!9bwwv2v!w3m@y2+a1=!pz4z12$m+y(z_tr8ap%'

DEBUG = False

ALLOWED_HOSTS = ['127.0.0.1', '']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'django_shop',
        'USER': 'dj_admin',
        'PASSWORD': 'qwerty123',
        'HOST': 'localhost',
        'PORT': '5432'
    }
}

STATIC_ROOT = BASE_DIR / 'static'

STATIC_URL = '/static/'
MEDIA_ROOT = BASE_DIR / 'media'
MEDIA_URL = '/media/'