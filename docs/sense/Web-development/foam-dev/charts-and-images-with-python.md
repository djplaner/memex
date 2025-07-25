﻿---
tags:
- python
- web-development
- foam-dev
- colophon
title: Charts and images with Python
type: note
---
What are the possibilities and methods for plotting charts and generating images with Python that can subsequently be used in web pages (here on Memex and the blog)?

!!! info "Completed - version 1.0"

    Using PyGal to generate SVG charts for [[recent-changes]]



??? info "Unexplored MkDocs Plotly Plugin"

    Discovered the [MkDocs Plotly Plugin](https://haoda-li.github.io/mkdocs-plotly-plugin/)

## Possibilities

See also [2022 post "What is the best interactive plotting library for Python"](https://sites.northwestern.edu/researchcomputing/2022/02/03/what-is-the-best-interactive-plotting-package-in-python/) which suggests a three-way tie between Bokeh, Plotly and Altair. However, [a later post](https://sites.northwestern.edu/researchcomputing/2023/04/12/experimenting-with-shiny-for-python/) from the same author recommends [Shiny for Python](https://shiny.posit.co/py/)]

- [Plotly](https://plotly.com/python/) - interactive charts
- [Matplotlib](https://matplotlib.org/) - static charts
- [Bokeh](https://bokeh.org) - interactive charts
- [Shiny](https://shiny.posit.co/py/) - [it appears](https://rstudio.github.io/cheatsheets/html/shiny-python.html) that Shiny requires a specific server to run.
- [Altair](https://altair-viz.github.io)

### Tradeoffs - saving

Appears likely that all approaches ability to display interactive charts depends on running in an appropriate environment. Shiny has a specific server. Altair has some runtime environments that work (e.g. Jupyter notebooks) and web pages with specific Javascript being loaded from CDNs. Most also provide the ability to export/save a static image.

Plotly provides the ability to be [used with Jinja templates](https://plotly.com/python/interactive-html-export/#inserting-plotly-output-into-html-using-a-jinja2-template) that may prove useful. Of course, you have to get Plotly to work, which I couldn't on Mac OS X.

Vega-Altair can export to JSON which can be displayed by [vega-embed](https://github.com/vega/vega-embed). Import vega from a CDN. Or generate SVG.

## Experiments with Altair

Early experiments starting with the [getting started guide](https://altair-viz.github.io/getting_started/overview.html)

- Altair data comes in ["tidy" dataframes](https://altair-viz.github.io/getting_started/starting.html#the-data)
- [Publishing your visualisation](https://altair-viz.github.io/getting_started/starting.html#publishing-your-visualization)

Saving generates HTML file with

- CSS defines
- script includes via a cdn
- inline Javascript
- a div into which the chart is rendered

## [SVG.Charts](https://svgcharts.readthedocs.io/en/latest/svg.charts.html)

Python module for generating SVG charts. Tested and mkdocs will display inline SVG images. However, the extra styling introduced by svg.charts doesn't work real well.

Not great documentation...made it difficult to figure out.

## [PyGal](https://www.pygal.org)

Similar to svg.charts. Better documentation. More obviously saves to SVG file. And works with macros and MkDocs.