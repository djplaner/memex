---
title: Open graph per page
type: note
tags:
    - colophon
    - open-graph
    - pkm
---

[[Open Graph]](https://ogp.me) is a protocol that enables any web page to become a rich object in a social graph. Implement method to create a 

- default open graph set up for the site
- allow page specific open graph metadata to be added


## Open Graph basics

Open graph tags are added to the `<head>` section of a webpage's HTML. 

Open graph tags

- `og:title` - object title.
- 'og:image' - image URL that represents the object.
- `og:description` - a brief description of the object.
- `og:url` - canonical URL of the object.

e.g. 

```html
<meta property="og:title" content="Example Title" />
<meta property="og:description" content="This is an example description." />
<meta property="og:image" content="https://example.com/image.jpg" />
<meta property="og:url" content="https://example.com/page.html" />
```

## Design

### Default configuration

- Define default site open graph metadata in the `mkdocs.yml` configuration file.
- Modify each template to use the default open graph metadata.

    - URL should be dynamically set to the current page URL.

### Page specific configuration

- Specify page specific open graph metadata in the page's front matter.

    - Figure out which metadata files to support

        - `og-title` from existing page title
        - `og-description` - new metadata field
        - `og-image` - new metadata field

- Modify the template to handle the page specific


## Implementation

### Images

[One recommendation](https://doinwp.com/og-image-size-and-requirements/) 

- provide both 1200x630 (rectangular) and 1200x1200 (square) images
- less than 300Kb
- use JPG or PNG format

Use `assets/memex-ficus-small.jpeg` as the default image.




