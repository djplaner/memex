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
So [memex][1] is up and going. Time to start using it and as I go figuring out the workflow and toolchain to use.

Aims for this post included

1.  Writing this post in memex and syncing to my blog
2.  Adding some "zettels" to sense taken from [my wikity][2]

### What's there now

Based on [Jarche's Seek > Sense > Share framework][3] [the home page][1] points off to three main sections: 

1.  [seek][4] A work in progress. 
2.  [sense][5] Where you'll find clost to 100 notes imported from my old Wikity site. These are organised into categories, including a "loose" category.
3.  [share][6] Another work in progress, but does point to the original markdown file for this blog post.

## Reflections

Having more content here has really started to highlight the functionality of Foam and its potential benefits. The auto-complete on Wiki links is very usable and appears likely to help understanding. e.g. it's already encouraged me to spend more time on naming of notes which means spending more time on thinking about how all this fits together.

At the start, I hadn't fully grokked the importance of naming files. The wiki-links autocompletion feature means that the location in the file hierarchy isn't has important as the name.

It's also reinforced that the very act of using Foam is a form of sharing.

It's also reinforced the benefit of the "best-of-breed" ecosystem approach to the way Foam is constructed. Each of the VSCode extensions adding a necessary and useful functionality. There's also been some of the complications of getting disparate systems to talk together. e.g. the aborted first attempt to sync this post and Wordpress. 

Different bits of the ecosystem introducing unexpected side effects. e.g. if there's not a blank line before the auto-generated wiki links, it doesn't display on github.

### What's next?

There are a few limitations/changes to workflow that I haven't yet figured out/got to

*   Adapting the Foam/Wordpress sync script to maintaining blog pages
*   Explore options for making the interface more visually appealing and easier to navigate
*   Spend a bit more time on the [seek][4] process

And generally start embedding this into how I work.

## Writing blog posts in memex

One of the assumptions of Foam is that the authoing environment (VSCode/markdown) can be a positive writing experience. I'm not such a fan of markedown. Writing blog posts in Foam will help me explore/change that in addition to all the benefits of [POSSE][7] and Foam.

### Wordpress <--> GitHub sync (failure to launch)

The hope is that the [Wordpress <--> GitHub sync plugin][8] for Wordpress will help.

Installation seems to have worked, but I've decided not to import existing posts here. Start afresh.

Is it working? That is the question.

After a bit of fiddling it works. However, it is removing files that Foam uses. Mmmm, not good. It's not 100% clear to me how and when its removing and moving files in the repo. This is making me nervous.

It's also 3 years since the last update to the repo, which include a call for maintainers. Moving on.

### Python python-wordpress.xmlrpc

There is an [option with Python][9] but it's even longer since it was last updated. But it works. There's also a [Python markdown module] to convert markdown to HTML.

I'm currently in the process of adding a featured image for each post. Which I'll do manually to start the post. I need a script that's going to: read the markdown file, extract config about which post/page it's related to, and then update that page.

That's done. Sufficient for now, but a huge kludge. But that's nothing new to what I do.

Needs some tidying up, but that's tomorrow's (which never comes?) job.

## Zettels from wikity?

From previous experimentations I have a [Wikity install][10] that contains a collection (not very big) of candidate "zettels". The idea is that importing those into memex should provide a good collection of zettels to experiment with using Foam. Giving some insights into if and how Foam can work managing such a collection.

The plan here is:

1.  Check out the format of the Wikity entries.
2.  Develop method to programatically extract them from Wikity.
3.  Transform and insert them into memex

### Wikity entry format

[Wikity][11] (I believe) was based on the idea of Cards and [CardBoxes][12]. Cards are the equivalent of zettels (which is German for a small piece of paper) and CardBoxes are the equivalent of structure notes (memex's paths).

One of the problems I face is that I doubt I ever used Wikity all that well. And what is there seems to have broken links

[Card:Three types of decentralisation][13] as some wonky content but does include a "see" link that is meant to point to a Cardbox. The content is in markdown and the "see" link is a wiki link `[[BAD]]`

[Cardbox:Affordances][14] contains two cards. It shows that a CardBox is essentially only links to other cards. The content is shown in the left hand nav bar. The content of this Wordpress post is two wiki links to the cards e.g.

> `[[Why the web scales]]` `[[Blackboard tweaks]]`

It appears that the only sign that it's a CardBox is that inclusion of *CardBox::* in the title.

Suggesting it should just be a matter of extracting the content of each post and writing it to a proper place and all should be good?

### Extract content from Wikity

Wikity is a theme on top of Wordpress. Hence the python-wordpress.xmlrpc package used above should be able to grab the cards.

And it can. Quite easily. The question now is how to insert it into memex.

### Transform and insert into memex

Since Wikity uses markdown (as does Foam/memex) there is no immediate need to transform. The question will be if there are any specific additional transformations (e.g. links) that need to be made to make it all work in Foam.

Plan is to insert the wikity cards and card boxes into the Sense section of memex. At some level the cards have already been 'sensed', just not very well. The question in my mind is how to do this? What structure to use?

The Foam community to the rescue with [this example][15] found on Twitter. A concrete example to explore. The [concepts directory][16] is holding the equivalent of card boxes. Semi-equivalent to the sense directory in memex. Each "card box" then has its own ["index"][17] and directory for cards

Steps:

*   Get a list of Cards and CardBoxes in Wikity Done. Simple Python code.
*   Make directories in sense for each of the card boxes Done. More simple processes
*   Save card boxes to files in sense directory Now it gets harder. More detail below. But not using wiki links
*   Save each card ito the appropriate directory (card box or "loose") Another case of a bit of markdown linking, rather than wiki-links
*   Add a list of card boxes to sense/index.md Will do this one manually, with a bit of help
*   Add a list of "loose" cards to sense/index.md

#### Generating md files using Python

It's simple to write the files using Python. But doing so bypasses VS-Code so doesn't run [the plugin][18] that enable wiki links to work.

1.  Figure out how to call the plugin from Python (or other means)
2.  Write normal markdown links using Python

Problem 1 is a step too far for my knowledge and time at the moment. 

### Fixing misc problems

The wikity notes are imported, but github pages isn't building. Potentially because the wikity stuff was all over the place. Some HTML, some markdown. Trawling through those, fixing problems and re-allocating notes.

Also removing colons from filenames.

It does appear to be working

[Why the web scales]: ../../sense/Affordances/Why the web scales "Why the web scales"

 [1]: https://djplaner.github.io/memex/
 [2]: http://wikity.djon.es/
 [3]: http://jarche.com/2014/02/the-seek-sense-share-framework/
 [4]: https://djplaner.github.io/memex/seek/seek
 [5]: https://djplaner.github.io/memex/sense/sense
 [6]: https://djplaner.github.io/memex/share/share
 [7]: https://indieweb.org/POSSE
 [8]: https://github.com/mAAdhaTTah/wordpress-github-sync
 [9]: https://pypi.org/project/python-wordpress-xmlrpc/1.4/
 [10]: https://wikity.djon.es/
 [11]: https://github.com/michaelarthurcaulfield/wikity-zero
 [12]: https://hapgood.us/2016/09/20/wikity-updates-0-4/
 [13]: https://wikity.djon.es/three-types-of-decentralisation/
 [14]: http://wikity.djon.es/why-the-web-scales/?cardbox=Affordances
 [15]: https://tslim.github.io/concepts/
 [16]: https://github.com/tslim/concepts/tree/master/concepts
 [17]: https://github.com/tslim/concepts/blob/master/concepts/cloud-computing.md
 [18]: https://kortina.nyc/essays/suping-up-vs-code-as-a-markdown-notebook/