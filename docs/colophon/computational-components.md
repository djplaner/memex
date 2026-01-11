---
tags:
- colophon
title: Computational components
type: note
description: Overview of what "computational components" are (in this context) and a list of current computational components used here.
---

Originally the idea of a [memex](https://en.wikipedia.org/wiki/Memex) was to provide a personal filing and retrieval system - a [personal knowledge base](https://en.wikipedia.org/wiki/Personal_knowledge_base). The utility of such a system is linked to how effectively the owner can [[gather-weave-augment|gather, weave, and augment]] information (amongst other things e.g. retrieve information). 

A lot of the "Second Brain" ideas focus on people manually gathering and weaving content. Related tools provide functionality to help this manual work. For example, [Foam's key features](https://foamnotes.com) such as wikilinks, templates, tags. Features which support the manual authoring process.  In addition, most software supporting this work provides also provide various computational means to automate aspects of [[pkm|personal knowledge management]]. For example, [Obsidian plugins](https://obsidian.md/plugins) or how [Josh Comeau uses MDX](https://www.joshwcomeau.com/blog/how-i-built-my-blog-v2/#content-management-2) to create interactive components by combining Markdown and JSX through use of MDX. 

!!! note "Computational components defined"

    Computational components are the automations I've developed to help [[gather-weave-augment]] the information on my Memex.



## Current computational components

The ecosystem I'm using to [[some-assemblage-required|assemble]] Memex means that these computational components are implemented using Python and using a couple of [MkDocs plugins](https://github.com/mkdocs/catalog?tab=readme-ov-file#----catalog----) 

- 🚧 [[wood-duck-observations]] 🚧 

    Similar to [[wood-duck-work-history]], but intended to gather observations of animals, birds, insects, etc made on [[wood-duck-meadows]].

- [[wood-duck-work-history]]

    Allows [[regeneration]] work performed on [[wood-duck-meadows]] to be recorded and then woven together with where the work was done.

- [wood-duck-gallery](../sense/landscape-garden/wood-duck-gallery.md)
 
    The ([[wood-duck-gallery-generator]]) gathers all the photos from the zone and plant pages for [[wood-duck-meadows]]. Implemented using `mkdoc-gen-files` to integrate a Python script into `mkdocs`

- [life-list-gallery](../sense/birdwatching/life-list-gallery.md)

    [[life-list-generator]] is a stand alone Python script (**TODO** integrate using `mkdocs-gen-files`) generates the life list gallery from a combination of eBird CSV file download and images saved locally.

- [[recent-changes]] 
    read git commit log to display recent website updates

    Python script to generate JSON and Javascript to generate HTML, or Python script to replace bound text in a markdown file.

- 🚧 [[plant-location-generator]] 🚧 

    Early experiment to extract plant location data from plant photos.

- Various different functions as part of the [[convert-wordpress-into-memex]] process

    Category and archive pages, RSS feeds, and blog statistics are being generated using Python scripts.

- [[blog-statistics]]

    Generate and display statistics about the content of the blog.

- Corpus Actions

    Early work on a component to perform actions on the entire corpus of bubbles. Initial work done implementing [[integrate-backlinks-automatically-onto-pages]]

- [[graph|Bubble network visualisation]]

    Generate a public website version of [Foam's graph feature](https://foambubble.github.io/foam/user/features/graph-visualization).

## Architecture

There are two types of computational component based on what they generate. The two options are:

1. Macros - implemented using [mkdocs-macros-plugin](https://mkdocs-macros-plugin.readthedocs.io/en/latest/) - to generate content to be included in Markdown files.
2. Entire markdown files - implemented using [mkdocs-gen-files](https://oprypin.github.io/mkdocs-gen-files/index.html) - generating entire markdown files which `mkdocs` will then process as part of the site build.

### Configuration

Macros are configured by code within `util/macros.py`, for example

```python
    @env.macro
    def recentChangesTimeline( numChanges : int = -1 ):
        """
        Generate a timeline of the last numChanges changes to the current git repo.
        By default, will show all changes.
        """
        return getRecentChangesTimeline( numChanges )
```

`mkdocs-gen-files` configured via `mkdocs.yml` e.g. the following which configures:

- `woodDuck.py` - [[wood-duck-gallery-generator]]
- `lifeList.py` - [[life-list-generator]]
- `corpusActions.py` - various global tasks e.g. generating back links

```yaml
plugins:
  - macros
    - gen-files:
      scripts:
        - util/generators/woodDuck.py 
        - util/generators/lifeList.py 
        - util/generators/corpusActions.py
```

### corpus.py

Provides a class to support [[corpus-manipulation]]. The ability to retrieve all or select part of the corpus of bubbles, increasingly based on the idea of [[bubbles-as-objects]].

```python

from corpus import corpus
bubbles = corpus()

#-- get a list of work-history bubbles
regionWorkHistory = bubbles.get_bubble_by_type("work-history")
```




[//begin]: # "Autogenerated link references for markdown compatibility"
[gather-weave-augment|gather, weave, and augment]: ../sense/CASA/gwa/gather-weave-augment "Gather, Weave, Augment"
[pkm|personal knowledge management]: ../pkm "Personal Knowledge Management"
[some-assemblage-required|assemble]: some-assemblage-required "Some Assemblage Required"
[wood-duck-observations]: wood-duck-observations "Wood Duck observations"
[wood-duck-work-history]: wood-duck-work-history "Wood duck work history"
[wood-duck-meadows]: ../sense/landscape-garden/wood-duck-meadows "Wood duck meadows"
[regeneration]: ../sense/landscape-garden/regeneration "Bush regeneration (Wood duck meadows)"
[wood-duck-gallery-generator]: wood-duck-gallery-generator "Wood duck meadows gallery generator"
[life-list-generator]: life-list-generator "Life list generator"
[recent-changes]: recent-changes "Recent changes"
[plant-location-generator]: plant-location-generator "Plant location generator"
[convert-wordpress-into-memex]: convert-wordpress-into-memex "Convert Wordpress into Memex"
[blog-statistics]: blog-statistics "Blog Statistics"
[integrate-backlinks-automatically-onto-pages]: integrate-backlinks-automatically-onto-pages "Integrate backlinks automatically onto pages"
[graph|Bubble network visualisation]: graph "Memex network graph"
[corpus-manipulation]: corpus-manipulation "Corpus manipulation"
[bubbles-as-objects]: bubbles-as-objects "Bubbles as objects"
[//end]: # "Autogenerated link references"