---
ID: 17864
post_title: Getting started with memex
author: admin
post_excerpt: ""
layout: post
permalink: >
  https://djon.es/blog/2020/07/07/getting-started-with-memex/
published: true
post_date: 2020-07-07 11:20:22
---
So \[memex\](https://djplaner.github.io/memex/) is up and going. Time to start using it and as I go figuring out the workflow and toolchain to use. Aims for this post include 1. Writing this post in memex and syncing to my blog 2. Adding some "zettels" to sense taken from \[my wikity\](http://wikity.djon.es/) ## Writing blog posts in memex One of the assumptions of Foam is that the authoing environment (VSCode/markdown) can be a positive writing experience. I'm not such a fan of markedown. Writing blog posts in Foam will help me explore/change that in addition to all the benefits of \[POSSE\](https://indieweb.org/POSSE) and Foam. ### Wordpress GitHub sync (failure to launch) The hope is that the \[Wordpress GitHub sync plugin\](https://github.com/mAAdhaTTah/wordpress-github-sync) for Wordpress will help. Installation seems to have worked, but I've decided not to import existing posts here. Start afresh. Is it working? That is the question. After a bit of fiddling it works. However, it is removing files that Foam uses. Mmmm, not good. It's not 100% clear to me how and when its removing and moving files in the repo. This is making me nervous. It's also 3 years since the last update to the repo, which include a call for maintainers. Moving on. ### Python python-wordpress.xmlrpc There is an \[option with Python\](https://pypi.org/project/python-wordpress-xmlrpc/1.4/) but it's even longer since it was last updated. But it works. There's also a [Python markdown module] to convert markdown to HTML. I'm currently in the process of adding a featured image for each post. Which I'll do manually to start the post. I need a script that's going to: read the markdown file, extract config about which post/page it's related to, and then update that page. (Kludgy)