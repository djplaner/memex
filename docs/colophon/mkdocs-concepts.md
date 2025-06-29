---
backlinks:
- title: Support documentation
  url: /colophon/support-documentation.html
tags:
- colophon
title: mkdocs concepts
type: note
---
[mkdocs](https://www.mkdocs.org) is a Python-based static site generator designed for project documentation. Since version 2.0 Memex has been using mkdocs for the interface. In particular, it's been using the [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/) theme. 

!!! note "Using _mkdocs_ interchangeably with _mkdocs-material_"
    
    The following using _mkdocs_ to refer to the combination of mkdocs and mkdocs-material. 

## Navigation

mkdocs navigation includes

- [site global navigation](https://www.mkdocs.org/user-guide/configuration/#documentation-layout)

    Specified by the top level of the `nav` section of the `mkdocs.yml` file. 

- [navigation sub-sections](https://www.mkdocs.org/user-guide/writing-your-docs/#configure-pages-and-navigation)

    Also specified in the `nav` section, indented from the global navigation

## Page styling

### Templates

YAML frontmatter for a page can specify a template. If specified, this template is used to render the page, rather than the default `main.html`.

Templates are written using [jinja templates](https://jinja.palletsprojects.com/en/stable/) and the [template designer docs](https://jinja.palletsprojects.com/en/stable/templates/).

How it works

- A template defines numerous blocks which can be overridden by child templates.
- Child template is defined by the `extends` statement
- Templates are [passed variables](https://mkdocs.readthedocs.io/en/859/user-guide/custom-themes/#template-variables) in the context of the page being rendered - global or [page](https://mkdocs.readthedocs.io/en/859/user-guide/custom-themes/#template-variables).

`base.html` defines the page layout. `Material for mkdocs` defines the [default `base.html`](https://github.com/squidfunk/mkdocs-material/blob/master/material/templates/base.html)

- It defines the two sidebars and then the main content area for content.
- `block announce` could be used for the old stuff? 
- `block outdated`
- `block hero`