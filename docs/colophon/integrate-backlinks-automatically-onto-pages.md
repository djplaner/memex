﻿---
tags:
- colophon
- about
title: Integrate backlinks automatically onto pages
type: note
---
For much of the life of this site, I've manually added ["backlinks"](https://en.wikipedia.org/wiki/Backlink) to pages in the form of "See also:". The intent being to help make these connections explicit and ease navigation. The automated inclusion of backlinks has long been a core feature of wikis and is [supported by Foam](https://foambubble.github.io/foam/user/features/backlinking) (the tool I use) in the authoring process. But Foam is agnostic about publishing and my method did not support backlinks.

Until June 2025. Automatic creation and visualisation of backlinks is now integrated into this site through a [[computational-components|computational component]]. A bit of Python that generates backlinks for each page and adds them to the frontmatter of the page. The backlinks are then rendered in the page template. See above.

## Impact

Apart from removing the need for manual "see also" work, this should also remove the "pollution" of those "see also" links from the site's network graph. The following two figures offer a comparison. While (IMHO) recognisably the same graph, the second graph is cleaner. With numerous network structures formed by the "see also" links no longer visible.

Would be good to do some actual graph analysis to explore the difference further.

<figure markdown>
![](https://djon.es/assets/memex/colophon/./images/beforeBackLinks.png)
<caption>Memex network graph before backlinks implemented</caption>
</figure>

<figure markdown>
![](https://djon.es/assets/memex/colophon/./images/afterBackLinks.png)
<caption>Memex network graph after backlinks implemented</caption>
</figure>

## Sources of inspiration

See [lzrd.dev](https://lzrd.dev/memex/athena). Authored with Foam, [publishsed using 11ty](https://gitlab.com/lzrddev/athena) which adds backlinks.

Obsidian (somewhat equivalent to Foam) [supports backlinks](https://www.notion.com/help/create-links-and-backlinks). Also shows Obsidian's nice interface for backlinks. A crafted bullet list/almost drop down menu of backlinks.

## Design and implementation

Use some form of [[computational-components|computational component]] to generate backlinks for each page, implemented as part of [`corpusActions.py`](https://github.com/djplaner/memex/blob/master/util/generators/corpusActions.py) using the following method. 

1. `corpusActions.py` (implemented using the `mkdocs-gen-files` plugin) 

  Analysis content of all pages looking for links (2 different ways), generating a dictionary recording all backlinks, and using that to update the frontmatter of each page to include details about the backlinks. 
    ```python
    bubbles = retrieveMemexBubbles()
    backLinks = generateBackLinks(bubbles)
    updateFrontMatterBackLinks(bubbles, backLinks)
    ```

2. site content (Jinja) template checks for backlinks in the frontmatter and adds the necessary visual element.

??? note "Adding [[publishing-graph-interface]]

  The same basic approach and the backlink data also works for generating network visualisations of the site. See [[publishing-graph-interface]] for details.

**To do**:

- Handle relative memex markdown liks (e.g. pages generated by [[computational-components]]).

  e.g. some of the ficucs plant pages to australasianfigbird

### How to `retrieveMemexBubbles`

Originally, this was done by traversing the file system. But that's already been done by `mkdocs`, hence current version uses the `mkdocs` API instead.

### Handling pages generated by [[computational-components]]

A problem to face is how to get pages generated by [[computational-components|computational components]] to have backlinks that appear in both backlinks and network visualisation.  The proposed solution is

1. Generators will add appropriate "linkDefs" at the bottom of generated pages.

  Emulating what is used in an authored page.

2. `corpusActions.py` "reads" the generated page via `mkDocs` API

  - Based on output of `retrieveMemexBubbles life list generator seems to be working on this
  - Bubbles have `linkDefs` dictionary keyed on the path names to markdown files that link back to the current bubble.

3. `corpusActions.py` adds the backlinks to frontmatter via `mkdocs-gen-files` open function.


spottedDove has links to life-list and birding
life-list is the only one that points to spottedDove


[//begin]: # "Autogenerated link references for markdown compatibility"
[computational-components|computational component]: computational-components "Computational components"
[publishing-graph-interface]: publishing-graph-interface "Publishing graph interface"
[computational-components]: computational-components "Computational components"
[computational-components|computational components]: computational-components "Computational components"
[//end]: # "Autogenerated link references"