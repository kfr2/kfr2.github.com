Title: Introducing cmsplugin-biography  
Date: 2013-05-28 21:44  
Tags: python, django, django cms  
Slug: 2013-05-28/introducing-cmsplugin-biography  
Author: Kevin Richardson  
Summary: cmsplugin-biography is a django CMS plugin for managing and displaying biographical information.  

Recently, I've been exploring [django CMS](https://www.django-cms.org/en/) to gain an understanding of how to use it to extend the fantastic [Django web framework](https://www.djangoproject.com/) into a content management system that can be easily used by content managers. Overall, I have been incredibly impressed with the CMS and look forward to using it more in the future. Because the CMS is an extension to Django and consequently offers all the benefits of the web framework, it is very easy to integrate various extensions. If a current [add-on](https://www.django-cms.org/en/add-ons/) does not meet a requirement, it is possible to implement [custom plugins](http://docs.django-cms.org/en/2.4.0/extending_cms/custom_plugins.html).

As my current project moves forward, I need to create various plugins for the CMS that allow content managers to refer to various kinds of dynamic, database-driven content. To that end, I've decided to start with an easy project: a plugin for the creation and display of biographies.

[cmsplugin-biography](https://github.com/kfr2/cmsplugin-biography) is a django CMS plugin that allows the user to create a biography of a person and refer to it within any number of pages. For example, a user may want to create biographies of his company's leadership team and refer to them across a variety of web pages. Instead of having to update a biography's text across multiple locations should something change, he will only need to update the biography once and the change will propagate across the pages on which the biography is located. Furthermore, each instance of the plugin allows the user to provide a "short description" that will override the global description attached to the selected biography. This is useful if, for instance, it is desirable to to provide a summary that links to another page containing the biography's full description.

Creating the plugin didn't take much time and I am relatively pleased with the results. As I begin integrating it into a CMS-powered site over the coming weeks, I'll hopefully determine what features it is missing. Eventually, I'll be comfortable enough with the plugin to release it on [PyPI](https://pypi.python.org/pypi). If you use the plugin and run into any issues or would like a feature added, please leave a comment on the plugin's [issues page](https://github.com/kfr2/cmsplugin-biography/issues).
