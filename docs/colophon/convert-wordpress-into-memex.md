---
title: Convert Wordpress into Memex
type: note
tags: 
    - colophon
---

See also: [[colophon]], [[version-3-memex-design]]

## What?

Convert my [Wordpress](https://djon.es/blog) blog into collection of markdown files hosted within this site.

## Export wordpress to markdown

Use [Wordpress export to Markdown](https://github.com/lonekorean/wordpress-export-to-markdown)

### Resources

Resources considered include

- Wordpress export to Markdown (CLI tool)

    - [Blog post](https://codersblock.com/blog/announcing-wordpress-export-to-markdown-v3/) announcing version 3 - 2025
    - [Github repo](https://github.com/lonekorean/wordpress-export-to-markdown)

- Markdown exporter for wordpress (Wordpress plugin)

    - [Blog post announcing](https://robertdevore.com/introducing-markdown-exporter-for-wordpress/) first version in 2024

        - Includes YAML front matter
        - Uses parsedown
    - [Github repo](https://github.com/robertdevore/markdown-exporter-for-wordpress)

        - 1 closed issue revealing design bug, solved by a PR

- Other user experiences

    - [XML > PHP > Markdown > 11ty](https://randomcoding.com/blog/2023-06-12-wordpress-to-markdown-and-then-on-to-11ty/)

- [wppparser](https://github.com/marteinn/wpparser) Python module to parse Wordpress export xml

### Process

1. Use Wordpress' in-built export to download ~36Mb XML file.

    Current blog post URL `~/blog/YYYY/MM/DD/slug`

2. Install and run `wordpress-export-to-markdown`

    Options chosen

    - Yes - Each post has own folder
    - No - prepend date to 
    - Year and month - date folders for posts
    - All images - save images

3. Analyse outcomes

    - All working fairly straight forward during process
    - Early blog posts don't appear to be using the same naming scheme (slug)
    - Some (55) images failing to download 404 and 410 errors (not suprising)
    - Copying into MEmex and it basically works. Fairly good as well.
    - Stats
        1794 posts, 76 pages, 75 attached images, 1317 images scraped from post body content

4. Re-run script using additional switches (maybe)

    - `--frontmatter-fields=title,date,categories,tags,author,draft` 
    - `--timezone=Australia/Brisbane`
    - `--include-time=true`
    - `--date-format=YYYY-MM-DD HH:mm:ss`

```bash
    npx wordpress-export-to-markdown --frontmatter-fields=title,date,categories,tags,author,draft --timezone=Australia/Brisban --include-time=true --date-format="YYYY-MM-DD HH:mm:ss" --request-delay=1000
```

### What's missing in display

- Pages
    - Stored in month/year/folder format, need to recreate old structure?
- Navigation
    - nav to pages
    - Does not maintain links within pages to other pages - 3.0.0 had a bug, fixed in 3.0.1
    - Is it possible to have different navigation/different template for the blog section
    - Most recent posts block
    - Latest comments
    - Block with archives by month
    - Home page with latest blog posts
- Posts 
  - A way to comment on a post
  - Post pre-amble - author, date, categories
  - Cover images for posts, cover images are included in yaml
  - RSS feed
  - Some images missing - need to check and recover
- No category pages - _Possible generator_
- No comments on posts
    - Are they included in the XML?
    - Are they included in the conversion process?

## Post conversion - Work to do

- Search and replace for old blog links and update

    davidtjones.wordpress

- Place blog post folders into relevant date folders

    - 2015/10/university... needs to be 2015/10/01/university

- Convert djon.es/blog links in Markdown to matching memex links 

    https://djon.es/blog/2015/10/01/university-e-learning-removing-the-context-and-adding-the-sediment/

    ~/memex/blog/2015/10/university-e-learning-removing-the-context-and-adding-the-sediment

- Move pages from date structure to original structure

### How to do it

Use Python and `wpparse` to provide more detailed data from the XML file.

- For pages, the link provides the folder to move to
- Similar for posts

Can work through all the posts from the folder and use the title to extract from parsed data

Can also add comments

### Outstanding work

- [ ] Out of date content to remove (cleanUpContent) 
    - [ ] \[googlevideo=http://video.google.com/videoplay?docid=961814934919323661#3m30s\]
    - [ ] broken links that are gone
        - indicate that in someway?
    - [ ] Adding a disclaimer of sorts along the bottom of older pages - warning it's out of date etc.


- [ ] Cover images may not have been downloaded

    - Announcing Canvas collecitons post, cover image
    - Check to see if others are missing
- [ ] Posts
- [ ] Pages
    - [x] the "about" page is old, out of data content, **Maybe two posts with same name**
    - [x] Need to handle folder hierarchy

        Currently assumes a flat structure, But some of the pages are in folders.
    - [ ] add publication date information to all posts (perhaps author?)
        - also categories etc
    - [ ] Do any pages have comments?

        - Proper about page has comments
- [ ] Navigation
    - Links to other djon.es/blog pages are currently full http links, rather than relative. Requires complete re-creation of the blog to work.
        - [ ] Is there a way to automatically convert these to relative links? 
            May have to wait for pages to be created first
    - make categories and tags links to appropriate generators
- [ ] Misc
    - Misc. conversion issues
        Going from Wordpress to Markdown to HTML means formatting breaks 

        - [ ] Use of # in markdown files overwriting the YAML title for page title 
        - [ ] Use of "funny" characters in YAML title can cause issues, can be solved by surrounding with : and # (but may be parser specific)
            - colon, hyphen
            - _working for colon_ others??  ?
        - [ ] internal links (esp on headings) will get modified by mkdocs practice 
            - Look to remove internal links (the page nav provides links)
        - markdown tables need an empty line before they start to be displayed
            - solving some problems of university learning part II (example)
        - lots of images missing and slowing down serve
        - \[code lang=""\]...\[/code] blocks e.g. concrete-lounge-1 
        - Just ``` all by themselves???
    - Errors being reported by mkdocs on serve/build
    - Files stored by Wordpress need to be moved

## Blog interface design

### Resources

- [Material for Mkdocs blog templates](https://andre601.ch/blog/2025/02-10-integrate-gitea-forgejo-stats/) and [here in the repo](https://github.com/squidfunk/mkdocs-material/blob/master/material/templates/blog-post.html)


### Blog templates

mkdocs template for blog home and blog post.

- How then to dynamically retrieve blog post details and add them?
- How does material do this

macro/generator as an alternatively

- How for blog template to call the generator - which is typically in the markdown file

### Design requirements

- All outdated information have a warning about out of date content, broken links etc

    - Possible via the `hero` block re-defined in `blog-post.html` template
    - Likely using variable metadata to test if the date is older than 2025

- Display publish date and categories/tags for each post

    - Possible by overriding the `content.html` partial to add this data under the title

- blog post cover image

- Explore a template for blog posts that adds
  - a header for old posts
  - ?? comments ??



[//begin]: # "Autogenerated link references for markdown compatibility"
[colophon]: colophon "About (Colophon)"
[version-3-memex-design]: version-3-memex-design "Memex - Version 3"
[//end]: # "Autogenerated link references"