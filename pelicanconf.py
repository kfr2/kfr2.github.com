#!/usr/bin/env python
# -*- coding: utf-8 -*- #

SITENAME = u'Kevin Richardson'
AUTHOR = u'Kevin Richardson'
TAGLINE = u'explorer & tinkerer'
SITEURL = 'http://localhost:8000'
FEED_DOMAIN = SITEURL
FEED_ATOM = 'feeds/all.atom.xml'
FEED_RSS = 'feeds/all.rss'
TIMEZONE = 'America/New_York'
DEFAULT_LANG = u'en'
DATE_FORMATS = {
    'en': '%Y-%m-%d',
}
DEFAULT_PAGINATION = 1

THEME = 'themes/pelican-svbtle'

HEADER_MESSAGE = u'Pax et Bonum'

# sidebar
LOGO_URL = 'http://www.gravatar.com/avatar/e6dddb3b7f19b71a97d604b9239dd86e.png'
MENUITEMS = (
    ('notes', 'http://dl.dropbox.com/u/7030113/notes/index.htm'),
    ('archives', '/archives.html'),
    ('feed', '/feeds/all.atom.xml'),
    ('github', 'https://github.com/kfr2/'),
)
DISPLAY_PAGES_ON_MENU = True
#LINKS = ()

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
PLUGINS = ['pelican.plugins.gravatar', 'pelican.plugins.sitemap']

SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'weekly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}
