---
title: Refine the authoring process
type: note
tags:
    - colophon
    - authoring
--- 

A key part of a new blog is how to author posts. With the conversion the new blog's content is in markdown format. How to author this content?

## Why not a simple text editor?

### Automate blog functionality 

Editing markdown directly would require additional manual work to provide/maintain blog functionality. The main example being the links to next/previous posts.

### Automate connections with memex

I use this [memex site](https://djon.es/memex) to develop and refine ideas. When I write blog posts it should be easy to link to ideas in Memex. The authoring process for Memex includes a method for linking that makes this easy. Earlier I had [written a Python script](https://djon.es/blog/2020/07/07/getting-started-with-memex/#python-python-wordpress-xmlrpc) that allowed me to write blog posts in Memex and publish them to Wordpress (before the Wordpress XMLRPC functionality was removed).

The aim is to recreate that.

!!! note "Blog too big to be part of memex"

    Originally the idea was that the blog and memex would be in the one repository. However, the number of Markdown files in a combined repository meant that the linking process was too slow. Meaning the blog and memex are in separate repositories.

## Memex and Python

Plan is to write a `updatePost.py` script in the `util` folder of Memex that will:

- Read a markdown file provided as a command line argument
- Make a copy of the post in blog repository following the `yyyy/mm/dd/slug` folder format
- Update the copy to
    - add next/previous links in the front matter
    - convert memex links to full URLs

## Draft post content

```markdown
---
title: <blog post title>
type: blog-post
categories:
    - <category-1>
    - <category-2>
tags:
    - <tag-1>
    - <tag-2>
---

<blog post content>

```


