"""
WSGI config for sms_jilin project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
#from dj_static import Cling

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sms_jilin.settings')

application = get_wsgi_application()
