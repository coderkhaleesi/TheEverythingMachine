"""
WSGI config for config project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/
"""

import os
import sys

from django.core.wsgi import get_wsgi_application

# add the django project path into the sys.path
#sys.path.append('TheEverythingMachine/django')

# add the virtualenv site-packages path to the sys.path
#sys.path.append('<PATH_TO_VIRTUALENV>/Lib/site-packages')


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

application = get_wsgi_application()

