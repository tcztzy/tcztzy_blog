# -*- coding: utf-8 -*-
"""Development Setting Module"""
from tcztzy_blog.settings.common import *  # noqa

DEBUG = True

STATICFILES_DIRS = (str(PROJECT_PACKAGE.joinpath('static')),)
