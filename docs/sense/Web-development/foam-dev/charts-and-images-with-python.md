---
title: Charts and images with Python
type: note
tags: 
    - python
    - web-development
    - foam-dev
    - colophon
---

See also: [[foam-dev]], [[colophon]]

What are the possibilities and methods for plotting charts and generating images with Python that can subsequently be used in web pages (here on Memex and the blog)?

## Possibilities

See also [2022 post "What is the best interactive plotting library for Python"](https://sites.northwestern.edu/researchcomputing/2022/02/03/what-is-the-best-interactive-plotting-package-in-python/) which suggests a three-way tie between Bokeh, Plotly and Altair. However, [a later post](https://sites.northwestern.edu/researchcomputing/2023/04/12/experimenting-with-shiny-for-python/) from the same author recommends [Shiny for Python](https://shiny.posit.co/py/)]

- [Plotly](https://plotly.com/python/) - interactive charts
- [Matplotlib](https://matplotlib.org/) - static charts
- [Bokeh](https://bokeh.org) - interactive charts
- [Shiny](https://shiny.posit.co/py/) - [it appears](https://rstudio.github.io/cheatsheets/html/shiny-python.html) that Shiny requires a specific server to run.
- [Altair](https://altair-viz.github.io)

### Tradeoffs - saving

Appears likely that all approaches ability to display interactive charts depends on running in an appropriate environment. Shiny has a specific server. Altair has some runtime environments that work (e.g. Jupyter notebooks) and web pages with specific Javascript being loaded from CDNs. Most also provide the ability to export/save a static image.

Plotly provides the ability to be [used with Jinja templates](https://plotly.com/python/interactive-html-export/#inserting-plotly-output-into-html-using-a-jinja2-template) that may prove useful.


[//begin]: # "Autogenerated link references for markdown compatibility"
[foam-dev]: foam-dev "Explorations in Foam development"
[colophon]: ../../../colophon/colophon "About (Colophon)"
[//end]: # "Autogenerated link references"