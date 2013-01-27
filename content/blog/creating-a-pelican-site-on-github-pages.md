Title: Creating A Pelican Site on GitHub Pages  
Date: 2013-01-27 16:07  
Tags: meta,github,blogging  
Slug: 2013-01-27/creating-a-pelican-site-on-github-pages  
Author: Kevin Richardson  
Summary: This post outlines how one can use the Pelican blog generator to establish a website on GitHub Pages.  
Status: draft

### Prologue
As I stated in [my "Hello World" post](http://magically.us/2013-01-01/hello-world.html), magically.us is created with [Pelican](http://blog.getpelican.com/) -- a static website generator -- and hosted on [GitHub Pages](http://pages.github.com/).  Benefits of static websites are abundant.  This combination allows one to easily update the look and feel of a site as well as its content while maintaining a complete revision history through the [Git version control system](http://git-scm.com/).  Static websites are awesome because they allow one to maintain a copy of her content and not worry about the "walled garden" effects of sites like Facebook where content can be challenging to export to other platforms.  Because static websites are HTML, it is incredibly easy to move one's site to other webhosts as is necessary or desired.  GitHub Pages also provides the URI `http://username.github.com` and allows the user to use her own domain.  Static website generators (like Pelican) generally allow one to write content in lightweight markup languages (like [Markdown](https://en.wikipedia.org/wiki/Markdown)) that is translated to HTML as necessary.

This post introduces how I maintain this website and (hopefully) provides the reader a starting place for her own experimentations.


### Assumptions
1. You're using a Unix-like machine and are comfortable using a command-line terminal and shell.  If you're using Windows, you may want to examine my [python-web-dev-box](https://github.com/kfr2/python-web-dev-box), a [Vagrant](http://vagrantup.com) virtual machine.
2. You have Python, [virtualenv](http://www.virtualenv.org/en/latest/), [virtualenvwrapper](http://www.doughellmann.com/projects/virtualenvwrapper/), and [pip](http://pypi.python.org/pypi/pip).
3. You have installed Git and have created a [GitHub](http://github.com) account.  I furthermore assume you have working knowledge of Git.  [GitHub's help pages](https://help.github.com/) may prove useful for many questions.


### Setup
1. [Fork my kfr2.github.com repository](https://github.com/kfr2/kfr2.github.com/fork).
2. Underneath the repository's settings, rename the forked repository to `your_username.github.com`
3. Open a terminal.
4. Clone the repository to your machine with the command `git clone https://github.com/your_username/your_username.github.com`
5. Make a new virtualenv for the project by running `mkvirtualenv your_username.github.com`
6. Run `cd your_username.github.com`
7. Run `setvirtualenvproject` to established `your_username.github.com` as the virtualenv's default directory.
8. Run `git checkout source` to see the site's source files (rather than its "compiled" HTML files).
9. Install the project's requirements:  `pip install -r requirements.txt`


### Configuration
1. `mkdir themes`
2. Download a theme and place it within a subdirectory of `themes`.  For instance, you can download my site's theme via `git clone https://github.com/kfr2/pelican-svbtle.git your_username.github.com/themes/pelican-svbtle`
3. Update the settings within `pelicanconf.py` and `publishconf.py`.  You may find Pelican's [settings documentation](http://docs.getpelican.com/en/3.1.1/settings.html) helpful.
4. Update content within `content`'s subdirectories.  For instance, you will likely want to delete any entries underneath `content/blog` as well as modify `content/extra` and `content/pages` to your liking.
5. If you'd like to serve this site at something other than `your_username.github.com`, update `content/extra/CNAME` to include the desired domain.  See [Setting up a custom domain with Pages](https://help.github.com/articles/setting-up-a-custom-domain-with-pages) for further instructions.
6. You may examine your changes with the command `make devserver`.  The site should be accessible at [http://localhost:8000](http://localhost:8000)
7. When satisfied, commit your changes: `git commit -am "A description of your changes."`
8. Push your source file changes: `git push source master`
9. Run `make github` to push your compiled source files to GitHub.  You will likely receive an email notification regarding your page build status.


### General Workflow
1. Run `workon your_username.github.com`
2. Run `python new_post.py` to create a new post.
3. Edit the post in your favorite text editor.
4. Examine the post in context of your website with `make devserver`
5. When satisfied with the post, run `git commit -am "Message describing the post"`
6. Push the source changes with `git push source master`
7. Push compiled files to your website with `make github`


### Interesting Alternatives
My suggested workflow may not suit your needs or interests.  Indeed, throughout the course of writing this post I realized how tedious a website may be to setup using the methods outlined above -- especially if one is unfamiliar with Git, GitHub, *nix, or Python.  Thus, you may be interested in examining how the alternatives listed below fit your needs.

#### GitHub Pages Automatic Page Generator
GitHub allows one to [create pages with an automatic generator](https://help.github.com/articles/creating-pages-with-the-automatic-generator) for both her user (at `username.github.com`) and individual projects (at `username.github.com/project-name`).  This could be much less maintenance than a Pelican-based approach as GitHub hosts [Jekyll](https://github.com/mojombo/jekyll), the static website generator powering the automatic generator, and runs your site files through it when you push changes to the repository.  In this situation, one will not need to have Python and the various Pelican dependencies installed.  You may wish to view [an example of Automatic Page Generator](http://magically.us/apg-test/).

#### gist.io
[gist.io](http://gist.io) allows one to create posts via [Gists](https://gist.github.com/), a GitHub feature that allows one to store snippets of code or text.  Gist.io's homepage describes how one may use it:

	1. Create a public gist on Github with one or more Markdown-syntax files.
	2. Note the gist ID number. It’s usually a longish number like 29388372.
	3. View your writing presented nicely at gist.io/gist-id-here
	
For reference, see the [example I made for gist.io](http://gist.io/4651080).  This method of content creation is incredibly rapid.  However, it is designed for one-off posts as it does not provide a method for viewing multiple posts by the same author.  If you like this style of content creation and wish gist.io acted more like a regular blog engine, it may be worth forking [gist.io's source](https://github.com/idan/gistio) into something that links to your gists and hosting it on a service like [Heroku](http://heroku.com).


### Conclusion
Hopefully this article has enlightened you to how you may use a static website generator like Pelican to share your content with the world.
