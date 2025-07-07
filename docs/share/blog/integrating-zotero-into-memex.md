---
title: Integrating Zotero into Foam
---
```toml
post_title='Integrating Zotero into Foam'
layout="post"
published=false
id=
link=""
category="memex"
```

The next stage in setting up (Memex)[https://djplaner.github.io/memex/] ([previous step](https://djon.es/blog/2020/07/07/getting-started-with-memex/)) is to figure out if and how I can integrate (Zotero)[https://www.zotero.org/]. Zotero is how I manage citations (mostly) to the academic literature. It's a bit part of how I seek information (browser plugin to save stuff I come across), make sense of it (highlights and notes), and share (managing references for publications). 

Integration with Memex is intended to 

1. Improve sense-making by transforming highlights and quick notes into more independent notes.
2. Improve the sharing of information by making more of this process transparent and public.

In terms of the second aim, I'm wondering if it's possible to integrate/replicate [my Zotero library](https://www.zotero.org/djplanner/library) into Memex. Perhaps with networked wiki-link style connections to the refined notes.

**_summary here_**

Next steps might include

1. Improving the look and feel of memex.
2. ??

## What needs to happen

Necessary steps to the stated goals seem to include:

- Tidying up my Zotero library (e.g. removing duplicates).
- Merging my two distinct libraries.
- If and how to extract categories from my Zotero library.
- If and how to extract existing notes 
- If and how to extract notes/highlights the PDFs within my Zotero library.
- Integrating all this into my PKM process.

## But first, build errors

There were times when github-pages was failing to build memex - ```Page build failed```. Something in the naming or content of the markdown files wasn't playing nice.  The issue is that github-pages doesn't provide any indication of where the problem is happening.

The solution is to [test the github pages locally with Jekylly](https://docs.github.com/en/github/working-with-github-pages/testing-your-github-pages-site-locally-with-jekyll). For some reason, this took me quite some time to set up. In the end, the process was

- [Install ruby and the github-pages gem](https://kbroman.org/simple_site/pages/local_test.html)
- [Install and configure the Jekyll Optional Front Matter gem](https://github.com/benbalter/jekyll-optional-front-matter#one-potential-gotcha)
- build memex locally using Jekyll

Together this quickly identified the two problems

1. A filename that included a colon.
2. A note that included some text using a Liquid syntax, left over from Wikity.

Problem fixed.

## Removing duplicates from my Zotero library

[Zotero has duplicate detection](https://www.zotero.org/support/duplicate_detection) which supports merging duplicates. It's a slow process. Largely done.

## Merging my two distinct libraries

Due to a work change, I'm commonly using two computers: Linux (personal) and Windows (work). I keep Zotero on both but I've been lazy. They are separate repositories. [Semi-sync'd by Zotero](https://www.zotero.org/support/sync) but I've exceeded the space limits (without paying) for files.

Time to see if there's an alternative.

WebDAV is known to work.   ut the [known WebDAV providers](https://www.zotero.org/support/kb/webdav_services) are a bit limited.

Another, more likely alternative, uses [linked files](https://www.zotero.org/support/attaching_files#stored_files_and_linked_files), the [ZotFile plugin](http://zotfile.com/), and some Cloud drive service (e.g. Google Drive).  

My free Google drive currently provides 15Gb of space. Currently Zotero is storing 3.7Gb of PDFs. 

ZotFile also provides the capability to extract highlights and annotations from PDFs into notes in Zotero. Potentially useful for later steps here.

Time to follow [this tutorial](https://www.researchgate.net/publication/325828616_Tutorial_The_Best_Reference_Manager_Setup_Zotero_ZotFile_Cloud_Storage) for setting up Zotero with cloud storage and ZotFile.

1. Select your cloud storage service and set up the sync
   Google drive it is and [this post](https://linoxide.com/tools/how-use-google-drive-ubuntu-linux/) outlines some options for sync'ing Google Drive with Linux (I'll also need to do this with Windows). The Gnome Online Account feature works nicely, but has a crap path to Google drive.  Try Ocamlfuse instead. 
2. Install ZotFile and let it do it's work...

**Configure on windows**

**COnfigure again on iPhone**

## Extracting data from Zotero

[Pyzotero](https://pypi.org/project/Pyzotero/) is an API client for [the Zotero API](https://www.zotero.org/support/dev/web_api/v3/start)

From [the basics](https://www.zotero.org/support/dev/web_api/v3/basics) I'll need a [API key](https://www.zotero.org/settings/keys/new) and [my userid](https://www.zotero.org/settings/keys). Save those to the ``memex.toml`` file.

The API uses "paths" to access data start with ``/users/<userId>`` and then add
  - ``~/collections``
  - ``~/collections/top``
  - ``~/collections/<collectionKey>``
  - ``~/collections/<collectionKey>/collections`` - sub collection list
  - ``~/collections/<collectionKey>/items`` - items in that sub collection
  - ``~/items`` - all items, excluding trashed
  - and PyZotero [offers a nice API](https://pyzotero.readthedocs.io/en/latest/#read-api-methods)

The simple PyZotero test works. So what from Zotero would be nice to have in Memex?

- A publications page under [share](https://djplaner.github.io/memex/share/share)
  Since Zotero stores type of publication the script can automatically calculate the number of publications etc. Would be nice to have this done "correctly" and automatically. In theory, this could also be the basis for updating the publications page on my blog.  But this would suggest updating the Zotero library to point to the versions of the publication on my blog. 
- A to read page under [seek](https://djplaner.github.io/memex/seek/seek)
  A bit of public shaming to encourage actual reading (or at least not putting stuff into this category in Zotero)
- An "Incoming Notes" page under [seek](https://djplaner.github.io/memex/seek/seek)
  i.e. notes that need to be "made sense"

The plan is that these are automatically updated via Python scripts that are run periodically.  I just keep using Zotero for various tasks and it get integrated into memex. 

### Publications page

The [publications page](https://djplaner.github.io/memex/share/My%20Publications) on memex is now being built using [a Python script](https://github.com/djplaner/memex/blob/master/util/zotero/publicationsPage.py) that 
- Get's a list  from publications
- Checks the date of updates
- If updates writes the whole thing again



### Extracting notes from Zotero

### Extracting highlights/notes from PDFs

### Integrating into my PKM process

e.g.

- Have a to read folder linked to "seek"
-