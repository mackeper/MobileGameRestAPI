"""
Django settings for mobilegamerestapi project.

Generated by 'django-admin startproject' using Django 2.0.7.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os
from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'hab5^u!c91w@jm9z#fq#h0(4l^gbl3c_*2$^6&s$91w+s%$u)6'

DEBUG = False

ALLOWED_HOSTS.append('localhost')
ALLOWED_HOSTS.append('127.0.0.1')