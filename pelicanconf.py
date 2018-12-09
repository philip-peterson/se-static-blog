#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

import os

AUTHOR = u'The Starry Expanse Team'
SITENAME = u'The Starry Expanse Project'
SITEURL = 'file://' + os.path.join(os.path.dirname(os.path.abspath(__file__)), 'output')

TIMEZONE = 'America/New_York'

PLUGIN_PATH = '../pelican-plugins/'
PLUGINS = (
	'html_rst_directive',
)

DIRECT_TEMPLATES = (
	#'myhello',
)

THEME = "themes/sedark"

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS =  (('Pelican', 'http://getpelican.com/'),
          ('Python.org', 'http://python.org/'),
          ('Jinja2', 'http://jinja.pocoo.org/'),
          ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
