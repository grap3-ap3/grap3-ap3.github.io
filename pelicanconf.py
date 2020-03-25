#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Phil Grimes'
SITENAME = u'Chaos Monkey'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/Chicago'

DEFAULT_LANG = u'en'

# Plugin directives
PLUGIN_PATHS = [r'E:\Dropbox\phillipGrimes\pelican\pelican-plugins']
PLUGINS = ['pelican-page-hierarchy']

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('RedLegg', 'https://redlegg.com'),)

# Social widget
SOCIAL = (('Twitter', 'https://twitter.com/grap3_ap3'),
          ('Instagram', 'https://www.instagram.com/phil_grimes/?hl=en'),
          ('LinkedIn', 'https://www.linkedin.com/in/phil-grimes-a4486615/'),
          ('GitHub', 'https://github.com/grap3-ap3'))

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
