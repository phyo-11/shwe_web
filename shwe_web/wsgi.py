"""
WSGI config for shwe_web project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

# import os

# from django.core.wsgi import get_wsgi_application

# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "shwe_web.settings")

# application = get_wsgi_application()


import os
import sys

# Update the following line with the correct path to your Django project on PythonAnywhere
path = '/home/phyonaing23/shwe_web'

if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'shwe_web.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

