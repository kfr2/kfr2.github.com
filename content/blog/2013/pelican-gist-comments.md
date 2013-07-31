Title: Pelican-Gist-Comments Plugin  
Date: 2013-07-31 9:05  
Tags: meta, github, writing, python  
Slug: 2013-07-31/pelican-gist-comments-plugin  
Author: Kevin Richardson  
Summary: An introduction to a Pelican plugin allowing the user to utilize Gists as a comment engine for blog posts.  

The other day I created [Pelican-Gist-Comments](https://github.com/kfr2/pelican-gist-comments), a plugin for [Pelican](http://getpelican.com) that allows a Pelican site owner to utilize Gists as a comment engine for his blog posts. Essentially, a Gist will be created for an article (based on its slug) whenever it is rendered into HTML by Pelican. The ID of the Gist will then be stored in `gist_comment_ids.json` and added to the article's metadata as 'gist_id'. Afterwards, the ID can be accessed in a template via `{{ article.gist_id }}`. For more information, see [this example template](https://github.com/kfr2/pelican-foundation/blob/master/templates/article.html#L19).

However, the notion behind this plugin is not without its faults. At this time, [Gists do not notify their owner](https://gist.github.com/maxogden/3422419) whenever a user posts a comment. However, it may be possible to circumvent this limitation by writing a small program that occasionally checks the comments on your Gists and alerts you when their numbers change. In addition, the user must have a GitHub account to post a comment (but I suppose this may help reduce spam).

I don't believe Pelican-Gist-Comments is a finished product by any means but it was a very fun plugin to hack together. Nonetheless, I hope you find it useful. If you have any thoughts or suggestions, please submit [an issue](https://github.com/kfr2/pelican-gist-comments/issues) or [pull request](https://github.com/kfr2/pelican-gist-comments/pulls).