#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

import os
import sys
sys.path.append(os.curdir)

from theme_specific_texts import *

PATH = 'content'
THEME = 'theme'

OUTPUT_PATH = '../razvan_site'
# THEME_STATIC_PATHS = []
THEME_STATIC_DIR = 'theme'

DELETE_OUTPUT_DIRECTORY = False

TIMEZONE = 'Asia/Jerusalem'

DEFAULT_LANG = 'he'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Pelican plugins
PLUGIN_PATHS = ['../plugins']
PLUGINS = ['i18n_subsites']

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
