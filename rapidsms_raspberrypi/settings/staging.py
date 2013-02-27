from rapidsms_raspberrypi.settings.base import *

DEBUG = False
TEMPLATE_DEBUG = DEBUG

DATABASES['default']['NAME'] = '/var/tmp/rapidsms_raspberrypi_staging'

INSTALLED_APPS += (
    'gunicorn',
)

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
    }
}

EMAIL_SUBJECT_PREFIX = '[Rapidsms_Raspberrypi Staging] '

COMPRESS_ENABLED = True
