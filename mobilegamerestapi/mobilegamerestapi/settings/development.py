"""
For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os
from .base import *

DEBUG = True

ALLOWED_HOSTS.append('localhost')
ALLOWED_HOSTS.append('127.0.0.1')
