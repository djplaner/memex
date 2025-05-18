---
title: A new day
type: blog-post
tags:
    - blog 
    - colophon
--- 

See also: [[colophon]], [[convert-wordpress-into-memex]]

A new day dawns. A [planned technology migration](https://djon.es/blog/2025/01/12/what-now/) of my blog is complete. 

Goodbye to "big tech" Wordpress and its (IMHO) horrid authoring environment and bloated performance. Hello to a markdown based static site generated through Python and numerous open source tools. The blog is reasonably functionally complete, but tinkering will continue. After all, enabling tinkering was a key motivation for the migration. 

This post celebrates that move and is intended to:

1. share how it was done;
3. help develop the authoring process;
4. reflect on the process; and,
5. document some initial ideas for next steps.

!!! note "Linking the stream and the garden"

    Many of the links below demonstrate a linkage between the ["garden and the stream"](https://hapgood.us/2015/10/17/the-garden-and-the-stream-a-technopastoral/). 
    
    This blog post is part of my stream. A serialisation of more complete ideas I'm sharing with others. 

    Many of the links below are to my [memex site](https://djon.es/memex). My garden of ideas. A space within which I iteratively develop, refine and share ideas in ways that are tentative and interconnected. A space where I document experiments and slowly grapple with ideas.
    
    Experiments like [[convert-wordpress-into-memex|converting my Wordpress blog to Markdown]]. 

## How it was was done

The task of [[convert-wordpress-into-memex|converting my Wordpress blog to markdown]] included the following steps:

1. [[export-wordpress-to-markdown|Export]] contents of the Wordpress blog to markdown.

    Use Wordpress' in-built export functionality to download an XML file with all of the blog's content. Then use [Wordpress export to Markdown](https://github.com/lonekorean/wordpress-export-to-markdown) to generate a structured collection of markdown files ready for the next step. 
2. [[modify-markdown-files|Modify the markdown]] to mirror the old blog structure, fix outdated content, and create blog functionality. 

    Tidy up and correct the markdown files due to outdated blog content (e.g. Slideshare links I now longer use) and other issues (e.g. various outdated links). Modify the structure of the markdown files from the previous step to re-create the existing blog structure so that long-term URLs for blog posts stay the same. Add explicit support for blog functionality (e.g. category pages, archives, RSS feeds, existing comments/pingbacks) to the [MkDocs static site generator (SSG)](https://www.mkdocs.org).
    
        All done using Python. Initially standard Python scripts. Then using the ability provided by MkDocs' plugins to embed custom Python scripts which I've been calling my [[computational-components]].
4. [[modify-interface|Tweak the SSG interface]] to better suit the design of my new blog.

    Mostly involving tweaking the static site generator's ([Material for MkDocs](https://squidfunk.github.io/mkdocs) HTML and CSS templates.
5. [[comparing-wordpress-to-memex|Compare and refine]] the new blog against the old and expectations.

    Speed, accessibility, and validation tests on the new blog to see if it was faster and better than the old. 
6. Replace Wordpress.

    Edit the web server configuration to move the Wordpress blog and replace it with the new blog.

## Authoring process

The original intent was to merge the authoring of blog posts with the memex authoring process (see the [Foam authoring process](https://foambubble.github.io/foam/#how-do-i-use-foam)). Thereby better integrating the stream with the garden. Sadly the number of markdown files in the blog meant that the VSCode autocompletion process for links was really slow (tens of seconds). Hence I made the decision to blog and memex into separate repositories. That's one need to be addressed.

The other the additional functionality required of a blog. For example, links to the next and previous posts. As I've implemented my blog the next/previous links are added into the YAML frontmatter of the markdown files which is used by the static site generator to create the interface. Initially, the generation of these next/previous links was done by the Python script that imported the markdown files. Something similar needed to be done by the authoring process.

```sh
python util/updatePost.py --post <markdown file>
```

## Reflections

### everything old is new again - static sites

Harking back to webfuse days

Svelte

### interoperability 

Shirky (2008) - "The web is a platform for interoperability". The blog is now a collection of markdown files that can be used in other contexts. For example, the blog posts are now available in my memex.

### Reusability paradox

Not something that anyone else could easily use. Assemblage to something that is specific to me. VS-Code, Foam, Python,

### House of cards

Technologies change. Perl > Python > Svelte > Python


## Next steps

- commenting feature

    - Tim's approach using mastodon etc.

- stats

- Reduce reliance on big tech (e.g. GitHub, VSCode)

- Improve the authoring process

    - Blog post links to Memex mirroring any changes in Memex

- More statistical [[computational-components]] similar to [this]((https://blog.jim-nielsen.com/archive/)

[//begin]: # "Autogenerated link references for markdown compatibility"
[colophon]: ../../../colophon/colophon "About (Colophon)"
[convert-wordpress-into-memex]: ../../../colophon/convert-wordpress-into-memex "Convert Wordpress into Memex"
[convert-wordpress-into-memex|converting my Wordpress blog to markdown]: ../../../colophon/convert-wordpress-into-memex "Convert Wordpress into Memex"
[export-wordpress-to-markdown|Export]: ../../../colophon/export-wordpress-to-markdown "Export Wordpress to Markdown"
[modify-markdown-files|Modify the markdown]: ../../../colophon/modify-markdown-files "Modify Markdown files"
[modify-interface|Tweak the SSG interface]: ../../../colophon/modify-interface "Modify blog interface"
[comparing-wordpress-to-memex|Compare and refine]: ../../../colophon/comparing-wordpress-to-memex "Comparing Wordpress to Memex"
[computational-components]: ../../../colophon/computational-components "Computational components"
[//end]: # "Autogenerated link references"