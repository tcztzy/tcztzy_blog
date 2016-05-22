# -*- coding: utf-8 -*-
"""Development Setting Module"""
from tcztzy_blog.settings.base import *  # noqa

DEBUG = True

ALLOWED_HOSTS.append('localhost')

STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)
