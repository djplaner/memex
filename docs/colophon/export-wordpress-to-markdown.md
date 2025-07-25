﻿---
tags:
- colophon
title: Export Wordpress to Markdown
type: note
---
Used [Wordpress export to Markdown](https://github.com/lonekorean/wordpress-export-to-markdown) to generate a collection of markdown files that are then further copied/manipulated into Memex through the [[modify-markdown-files]] process.

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
npx wordpress-export-to-markdown --frontmatter-fields=title,date,categories,tags,author,draft --timezone=Australia/Brisbane --include-time=true --date-format="YYYY-MM-DD HH:mm:ss" --request-delay=1000
```


[//begin]: # "Autogenerated link references for markdown compatibility"
[modify-markdown-files]: modify-markdown-files "Modify Markdown files"
[//end]: # "Autogenerated link references"