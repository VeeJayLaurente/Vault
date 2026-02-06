"""
WSGI config for artiste project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'artiste.settings')

application = get_wsgi_application()

# Add this at the bottom:
from django.core.management import call_command
if os.environ.get('RUN_MIGRATIONS') == 'True':
    call_command('migrate', interactive=False)