---
title: Twitter Memex Wordpress
---
```toml
post_title='Integrating Twitter, Wordpress and Memex'
layout="post"
published=false
id=
link=""
category="memex"
```

Recently I experimented with using Twitter to engage in some public "annotation" of readings. Since Twitter is largely ephemeral any "knowledge" embedded within those experiments will soon be lost. Hence the following is an exploration of how I can store that information in [my memex](https://djon.es/blog/2020/07/07/getting-started-with-memex/) and perhaps leverage them for more considered writing on this blog and beyond.

The aims here are

- [ ] Retrieve the information from Twitter and add them to Memex
- [ ] Combine that information with other annotations from the PDF
- [ ] Re-purpose them for Wordpress

## Twitter to Memex

I'm using Python to take Memex markdown files and publish them to this blog. So the plan is to use Python to extract the tweets from Twitter.

For that I'll be using [tweepy](http://docs.tweepy.org/en/latest/getting_started.html)