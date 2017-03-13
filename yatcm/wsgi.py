"""
WSGI config for yatcm project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""

import os
import sys

from django.core.wsgi import get_wsgi_application
root_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
sys.path.insert(0, os.path.abspath(os.path.join(root_path, '/home/jiohua/virtualenvs/yatcm/lib/python2.7/site-packages/')))
sys.path.insert(0, os.path.abspath(os.path.join(root_path, '/home/jiohua/programs/rdkit-Release_2015_03_1')))


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "yatcm.settings")

application = get_wsgi_application()
