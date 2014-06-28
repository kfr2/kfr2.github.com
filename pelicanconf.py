#!/usr/bin/env python
# -*- coding: utf-8 -*- #

from __future__ import unicode_literals
from os import environ


SITENAME = u'Kevin Richardson'
AUTHOR = u'Kevin Richardson'
TAGLINE = u'explorer & tinkerer'
SITEURL = 'http://localhost:8000'
FEED_DOMAIN = SITEURL
FEED_RSS = 'feeds/all.rss'
TIMEZONE = 'America/New_York'
DEFAULT_LANG = u'en'
DATE_FORMATS = {
    'en': '%Y-%m-%d',
}
DEFAULT_PAGINATION = 1

THEME = 'themes/pelican-foundation'


# display items
MENUITEMS = (
    ('about me', '/pages/about.html', 'fa fa-user'),
    ('all articles', '/archives.html', 'fa fa-list'),
)
FOOTER_MESSAGE = u'This work is licensed under the <a href="http://creativecommons.org/licenses/by-sa/3.0/" rel="license">CC BY-SA</a>.'
TWITTER_USERNAME = u'kfredrichardson'


#STATIC_PATHS = ()
FILES_TO_COPY = (
    ('extra/README', 'README'),
    ('extra/LICENSE', 'LICENSE'),
    ('extra/CNAME', 'CNAME'),
    ('extra/humans.txt', 'humans.txt'),
    ('extra/favicon.ico', 'favicon.ico'),
    ('extra/404.html', '404.html'),
)

# Plugins and their settings.
PLUGIN_PATH = 'pelican-plugins'
PLUGINS = ['sitemap', 'gist']

GITHUB_USERNAME = 'kfr2'
GITHUB_AUTH_TOKEN = environ.get('GITHUB_AUTH_TOKEN')
if GITHUB_AUTH_TOKEN is None:
    raise NotImplementedError("You should define GITHUB_AUTH_TOKEN in your OS's environment.")

SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'weekly',
        'indexes': 'weekly',
        'pages': 'monthly'
    }
}

