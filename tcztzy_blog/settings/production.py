# -*- coding: utf-8 -*-
"""Production Setting Module"""
from tcztzy_blog.settings.base import *  # noqa

DEBUG = False

ALLOWED_HOSTS.append('tcztzy.me')

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
