# PKM, SecondBrain, Zettelkasten and other

Experiment in trying to use [Foam](https://foambubble.github.io/foam/recipes) as a medium for notetaking, sensemaking and generally engaging in [Personal Knowledge Management (PKM)](http://jarche.com/pkm/) etc.

Sparked by @downes sharing of [details about Foam](http://www.downes.ca/cgi-bin/page.cgi?post=71058)

And intended/hoped to solve the problem I've suffered from (and done nothing about) for a long time a lack of discipline to organise and utilise all the "thinking" I do. Yea, technology is going to help with discipline!!

## How to do it?

The technology seems to be working, but that won't be enough. What will be the process? Can the technology effectively support the process?

The problem is that I can already see some limits of Foam. For example, common advice appears to be to avoid hierarchical categories and move to non-hierarchical network of nodes using tags. But Foam relies on github, which in turn relies on hierarchical directory/file structures!

The advantage is that being based on github & VSCode enables Foam to better kludged into the whatever assemblage I think I need to help. For example, if I want to: 

- Publish notes from Foam (PKM's share stage) to my [blog](https://djon.es/blog) 
  This [might help to Sync github & wordpress](https://github.com/mAAdhaTTah/wordpress-github-sync). 
- Import notes from Zotero (PKM's Seek/Sense stage)
  There's a [Pyton Zotero api](https://pypi.org/project/Pyzotero/) which I could use to write some scripts to update content in this repository 
- Import bookmarks from Diigo (PKM's Seek/Sense stage)
  Another [Python module](https://pypi.org/project/pydiigo/)
- What about images? The GitHub community must have solved that by now.
- Is there an alternative for markdown 
  I can use it, but it has never felt right. Though VSCode is helping.

And I've not even touched on the VSCode ecosystem

Moving away from the technology, I need a process that I can stick to. I've used 

### PKM + SecondBrain 

Early ideas here to combine bits of [Seek > Sense > Share](http://jarche.com/2014/02/the-seek-sense-share-framework/) from Jarche's PKM with the PARA idea from [SecondBrain](https://www.keepproductive.com/blog/how-to-build-a-second-brain)

- Seek - curate a network of information flowing in
  Twitter, Diigo, Zotero, journals, websites, colleagues etc. These will need to be connected into this secondBrain.
- Sense - organise, reflect and make sense of all that's flowing in
  - PARA to structure information
    This is where SecondBrain's PARA system might help. Divide the flow into
    - Projects - a folder/area to hold deliverables
    - Areas - on-going interests
    - Resources - relevant information for all tasks/projects
    - Archives - older stuff that isn't require in the foreseeable future
  - How to write notes
    Experience with the Smallest Federated Wiki identified the need to give some thought to how information stored here is written. **TODO** Need to explore this more
- Share - do stuff with this information and share it with others
  My blog, twitter and other social media fit here. This is where the [POSSE](https://indieweb.org/POSSE) idea becomes a good idea. Also where this being based on github with a local clone makes implementing this potentially easier.
  But this repository itself will be public. First as a [github repository](https://github.com/djplaner/secondBrain) but also as [github pages](https://djplaner.github.io/secondBrain/)?

# TODO List

1. Come up with a better name than secondBrain
1. Organise the following into a PARA structure - read [more about it](https://fortelabs.co/blog/para/)
1. Read more about writing/connecting content stored here e.g. [this](https://medium.com/swlh/how-i-use-my-second-brain-b5300d68e83a) and revisit some of the SFW/Wikity work
1. Play with the [backlinking](https://foambubble.github.io/foam/backlinking) and [graph visualisation](https://foambubble.github.io/foam/graph-visualisation) 
1. Think about how to connect up the various seek tools into this repo
1. Give more thought to how to implement [POSSE](https://indieweb.org/POSSE)
1. Explore more about VSCode and the various recommended plugins added here

## Using Foam

We've created a few Bubbles (markdown documents) to get you started.

- [[inbox]] - a place to write down quick notes to be categorised later
- [[foam-tips]] - tips to get the most out of your Foam workspace
- [[todo]] - a place to keep track of things to do

## Note on `[[wiki-links]]`

⚠️ Until [foambubble/foam#16](https://github.com/foambubble/foam/issues/16) is resolved, `[[wiki-links]]` links (like the links above) won't work in the GitHub Markdown preview (i.e. this Readme on github.com). 

They should work as expected in VS Code, and in rendered GitHub Pages.

If GitHub preview (or general 100% support with all Markdown tools) is a requirement, for the time being you can use the standard `[description](page.md)` syntax.


[//begin]: # "Autogenerated link references for markdown compatibility"
[inbox]: inbox "Inbox"
[foam-tips]: foam-tips "Foam tips"
[todo]: todo "Todo"
[//end]: # "Autogenerated link references"
