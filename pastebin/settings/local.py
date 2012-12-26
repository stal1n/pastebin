"""
Example settings for local development

Use this file as a base for your local development settings and copy
it to pastebin/settings/local.py. It should not be checked into
your code repository.

"""
from pastebin.settings.base import *   # pylint: disable=W0614,W0401

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('snake', 'collard41@gmail.com'),
)
MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(VAR_ROOT, 'dev.db'),
    }
}

# ROOT_URLCONF = 'pastebin.urls.local'
# WSGI_APPLICATION = 'pastebin.wsgi.local.application'
