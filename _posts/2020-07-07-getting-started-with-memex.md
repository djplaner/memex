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

Aims for this post include

1.  Writing this post in memex and syncing to my blog
2.  Adding some "zettels" to sense taken from [my wikity][2]

## Writing blog posts in memex

One of the assumptions of Foam is that the authoing environment (VSCode/markdown) can be a positive writing experience. I'm not such a fan of markedown. Writing blog posts in Foam will help me explore/change that in addition to all the benefits of [POSSE][3] and Foam.

### Wordpress <--> GitHub sync (failure to launch)

The hope is that the [Wordpress <--> GitHub sync plugin][4] for Wordpress will help.

Installation seems to have worked, but I've decided not to import existing posts here. Start afresh. 

Is it working? That is the question.

After a bit of fiddling it works. However, it is removing files that Foam uses. Mmmm, not good. It's not 100% clear to me how and when its removing and moving files in the repo. This is making me nervous.

It's also 3 years since the last update to the repo, which include a call for maintainers. Moving on.

### Python python-wordpress.xmlrpc

There is an [option with Python][5] but it's even longer since it was last updated. But it works. There's also a [Python markdown module] to convert markdown to HTML.

I'm currently in the process of adding a featured image for each post. Which I'll do manually to start the post. I need a script that's going to: read the markdown file, extract config about which post/page it's related to, and then update that page.

That's done. Sufficient for now, but a huge kludge. But that's nothing new to what I do.

Needs some tidying up, but that's tomorrow's (which never comes?) job.

## Zettels from wikity?

From previous experimentations I have a [Wikity install][6] that contains a collection (not very big) of candidate "zettels". The idea is that importing those into memex should provide a good collection of zettels to experiment with using Foam. Giving some insights into if and how Foam can work managing such a collection.

The plan here is:

1.  Check out the format of the Wikity entries.
2.  Develop method to programatically extract them from Wikity. 
3.  Transform and insert them into memex

### Wikity entry format

[Wikity][7] (I believe) was based on the idea of Cards and [CardBoxes][8]. Cards are the equivalent of zettels (which is German for a small piece of paper) and CardBoxes are the equivalent of structure notes (memex's paths). 

One of the problems I face is that I doubt I ever used Wikity all that well. And what is there seems to have broken links

[Card:Three types of decentralisation][9] as some wonky content but does include a "see" link that is meant to point to a Cardbox. The content is in markdown and the "see" link is a wiki link `[[BAD]]`

[Cardbox:Affordances][10] contains two cards. It shows that a CardBox is essentially only links to other cards. The content is shown in the left hand nav bar. The content of this Wordpress post is two wiki links to the cards e.g.

> `[[Why the web scales]]` `[[Blackboard tweaks]]`

It appears that the only sign that it's a CardBox is that inclusion of *CardBox::* in the title.

Suggesting it should just be a matter of extracting the content of each post and writing it to a proper place and all should be good?

### Extract content from Wikity

Wikity is a theme on top of Wordpress. Hence the python-wordpress.xmlrpc package used above should be able to grab the cards.

And it can. Quite easily. The question now is how to insert it into memex.

### Transform and insert into memex

Since Wikity uses markdown (as does Foam/memex) there is no immediate need to transform. The question will be if there are any specific additional transformations (e.g. links) that need to be made to make it all work in Foam.

Plan is to insert the wikity cards and card boxes into the Sense section of memex. At some level the cards have already been 'sensed', just not very well. The question in my mind is how to do this? What structure to use?

The Foam community to the rescue with [this example][11] found on Twitter. A concrete example to explore. The [concepts directory][12] is holding the equivalent of card boxes. Semi-equivalent to the sense directory in memex. Each "card box" then has its own ["index"][13] and directory for cards

Steps: 

*   [X] Get a list of Cards and CardBoxes in Wikity
*   [ ] Make directories in sense for each of the card boxes
*   [ ] Save card boxes to files in sense directory
*   [ ] Save each card ito the appropriate directory (card box or "loose")
*   [ ] Add a list of card boxes to sense/index.md
*   [ ] Add a list of "loose" cards to sense/index.md

*

 [1]: https://djplaner.github.io/memex/
 [2]: http://wikity.djon.es/
 [3]: https://indieweb.org/POSSE
 [4]: https://github.com/mAAdhaTTah/wordpress-github-sync
 [5]: https://pypi.org/project/python-wordpress-xmlrpc/1.4/
 [6]: https://wikity.djon.es/
 [7]: https://github.com/michaelarthurcaulfield/wikity-zero
 [8]: https://hapgood.us/2016/09/20/wikity-updates-0-4/
 [9]: https://wikity.djon.es/three-types-of-decentralisation/
 [10]: http://wikity.djon.es/why-the-web-scales/?cardbox=Affordances
 [11]: https://tslim.github.io/concepts/
 [12]: https://github.com/tslim/concepts/tree/master/concepts
 [13]: https://github.com/tslim/concepts/blob/master/concepts/cloud-computing.md