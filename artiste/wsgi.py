"""
WSGI config for artiste project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os
from django.core.management import call_command
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'artiste.settings')

application = get_wsgi_application()

# Vercel needs this line to find your Django app
app = application

# This runs collectstatic in the Vercel cloud environment
# so WhiteNoise has files to serve.
if os.environ.get('VERCEL'):
    try:
        call_command('collectstatic', '--noinput', '--clear')
    except Exception as e:
        print(f"Error running collectstatic: {e}")