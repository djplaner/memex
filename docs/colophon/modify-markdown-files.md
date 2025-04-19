---
title: Modify Markdown files
type: note
tags: 
    - colophon
---

See also: [[convert-wordpress-into-memex]], [[colophon]]

Take the output of the [[export-wordpress-to-markdown]] process, modify the files, and place them into the memex structure.

Done using Python and [`wpparse`](https://github.com/marteinn/wpparser) to provide more detailed data from the XML file.

## To do

Immediate

- [ ] post details
  - [ ] test category being added to template
  - [ ] tags??
- [ ] Comments 
  - [ ] Add comments to metadata
  - [ ] update template to include comments with link ids
- [ ] Generate RSS
- [ ] Archives
    - [ ] Add to navigation column list of months/years
    - [ ] Generate content for each month/year
- [ ] Category
    Doc file 'blog/2012/03/30/bim2-status-check-and-whats-next/index.md' contains a link '../../../../category/bim/bim2.md',
           but the target 'blog/category/bim/bim2.md' is not found among documentation files.

### Pages working

Get basic Markdown files for pages

- [ ] Add comments to Markdown

    - Possibly adding them as frontmatter and then using a template to add them to the page. Reuse the template for pages.
    - Comments have internal anchors e.g. `#comment-6088` which appears linked to the comment ID

- [ ] Implement category generator

    - [ ] Add category details into the frontmatter of posts with categories - generator retrieves them

### Posts working

### Templates

- [ ] show publication date, categories, tags in template
- [ ] show comments
- [ ] cover images ?? other images ??


### Misc other

- [ ] Blog posts that have been saved in folders named after post id
    - 4668
- [ ] Handle category pages (blog.py)

    Category pages provide an index to all posts/pages in the category
    - initial dummys implemented, still to be completed

- [ ] Handle tag pages (blog.py)

- [ ] Handle archive pages (months, years) (blog.py)

### What's missing in display

- Pages
    - Stored in month/year/folder format, need to recreate old structure?
- Navigation
    - nav to pages
    - Does not maintain links within pages to other pages - 3.0.0 had a bug, fixed in 3.0.1
    - **Yes** Is it possible to have different navigation/different template for the blog section 
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

Fixing up old content

- [ ] Search and replace for old blog links and update

    davidtjones.wordpress

- [ ] Place blog post folders into relevant date folders

    - 2015/10/university... needs to be 2015/10/01/university

- [ ] Convert djon.es/blog links in Markdown to matching memex links 

    current-research-projects

    - [ ] links to posts
        - https://djon.es/blog/2015/10/01/university-e-learning-removing-the-context-and-adding-the-sediment/
        - ~/memex/blog/2015/10/university-e-learning-removing-the-context-and-adding-the-sediment
    - [ ] links to pages
        Will have to re-create the structure done elsewhere, but this is **not** possible. e.g. current-research-projects can be linked to by research/current-research-projects/, but URL is without research. Need to do it manually in blogTidyUp

        See `Current research projects` and early link to `Moodle open book project`. On the blog it's in the '/research/the-moodle-open-book..' Need to recreate

- [ ] Move pages from date structure to original structure

### Outstanding work

- [ ] Out of date content to remove (cleanUpContent) 
    - [x] \[googlevideo=http://video.google.com/videoplay?docid=961814934919323661#3m30s\]
    - [ ] slideshare similar to google video
    - \[code lang=""\]...\[/code] blocks e.g. concrete-lounge-1 

Errors reported by mkdocs

- [ ] broken links that are gone

Interface

- [x] Adding a disclaimer of sorts along the bottom of older pages - warning it's out of date etc.
- [ ] Cover images may not have been downloaded

    - Announcing Canvas collecitons post, cover image
    - Check to see if others are missing

- [ ] Wordpress functionality
    - [ ] Add existing comments to pages and posts
    - [ ] Method for people adding comments to pages
    - [ ] Category pages
    - [ ] tag pages
    - [ ] Posts pages (archives)
    - [x] add publication date information to all posts (perhaps author?)
        - also categories etc


- [ ] Posts
- [ ] Pages
    - [x] the "about" page is old, out of data content, **Maybe two posts with same name**
    - [x] Need to handle folder hierarchy

        Currently assumes a flat structure, But some of the pages are in folders.
    - Doc file 'blog/publications/index.md' contains an absolute link '/papers/3.pdf', it was left as is.
    -  Doc file 'blog/publications/online-courses-and-collaborative-learning-underlying-philosophies-and-practices/index.md' contains a link 'images/Image3.gif', but the target 'blog/publications/online-courses-and-collaborative-learning-underlying-philosophies-and-practices/images/Image3.gif' is not found among documentation files.
    -  Doc file 'blog/publications/solving-some-problems-of-university-education-a-case-study/index.md' contains a link 'sound01.au', but the target 'blog/publications/solving-some-problems-of-university-education-a-case-study/sound01.au' is not found among documentation files.
 


- [ ] Navigation
    - Links to other djon.es/blog pages are currently full http links, rather than relative. Requires complete re-creation of the blog to work.
        - [ ] Is there a way to automatically convert these to relative links? 
            May have to wait for pages to be created first
    - make categories and tags links to appropriate generators
- [ ] Misc
    - Misc. conversion issues
        Going from Wordpress to Markdown to HTML means formatting breaks 

        - [ ] Use of # in markdown files overwriting the YAML title for page title 
        - [x] Use of "funny" characters in YAML title can cause issues, can be solved by surrounding with : and # (but may be parser specific)
            - colon, hyphen
            - _working for colon_ others??  ?
        - [x] internal links (esp on headings) will get modified by mkdocs practice 
            - Look to remove internal links (the page nav provides links)
        - markdown tables need an empty line before they start to be displayed
            - solving some problems of university learning part II (example)
        - lots of images missing and slowing down serve
        - Just ``` all by themselves???
    - Errors being reported by mkdocs on serve/build
    - Files stored by Wordpress need to be moved

## Tmp working space

### Implementing relative links

- Don't add index.md to relative links if there's a # (internal anchor) in the link
    blog/about-2/index.md
- Don't add index.md if there's a ?, publications includes
    ?attachment_id=502 and ?page_id=503
- publications/index.md is breaking link to student-feedback-anonymity-observable-change-and-course-barometers/index.md



### Comments



### Attachements

### PDFs







[//begin]: # "Autogenerated link references for markdown compatibility"
[convert-wordpress-into-memex]: convert-wordpress-into-memex "Convert Wordpress into Memex"
[colophon]: colophon "About (Colophon)"
[export-wordpress-to-markdown]: export-wordpress-to-markdown "Export Wordpress to Markdown"
[//end]: # "Autogenerated link references"