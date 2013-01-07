from datetime import datetime
from uuid import uuid4

from pelicanconf import AUTHOR


post = {}
post['author'] = AUTHOR
post['title'] = raw_input('Title: ')
post['slug'] = raw_input('Slug: ')
post['summary'] = raw_input('Summary: ')
post['tags'] = raw_input('Tags: ')
post['date'] = datetime.now().strftime('%Y-%m-%d')
post['time'] = datetime.now().strftime('%H:%M')

header = """Title: %(title)s
Date: %(date)s %(time)s
Tags: %(tags)s
Slug: %(date)s/%(slug)s
Author: %(author)s
Summary: %(summary)s
""" % (post)

out_file = 'content/blog/%s/%s.md' % (datetime.now().strftime('%Y'), post['slug'])

try:
    with open(out_file) as f:
        out_file = 'content/blog/%s/%s.md' % (datetime.now().strftime('%Y'), uuid4())
        print('The specified output file exists.  Writing to %s' % out_file)
except:
    pass

with open(out_file, 'w') as f:
    f.write(header)
