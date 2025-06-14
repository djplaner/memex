﻿---
tags:
- colophon
- about
title: Publishing graph interface
type: note
---
Foam has a graph/map feature for notes from within VS-Code (see the figure below) but that doesn't help when publishing to the web. Following are my notes playing around with adding a graph interface to this site.

<figure markdown>
![](https://djon.es/assets/memex/colophon/images/foam-graph.png)
<figcaption>Sample graph/map of memex (within VSCode)</figcaption>
</figure>

## Planning

Current possible plan is

- Use Python to extract data about the Foam graph

  The method used to add backlinks is a large step toward this, but doesn't do graph analysis. May also be better methods **TODO**

- Generate a JSON file with the graph data

- Implement a front-end that uses that JSON file to generate the graph interface

  [force-graph](https://github.com/vasturiano/force-graph) seems a reasonable fit.

## Resources

### Foam

Graphing in Foam can use any HTML/Javascript.

- [Github issue](https://github.com/foambubble/foam/issues/58) discussing "graph in published workspace"
- [Call for visualisation](https://github.com/foambubble/call-for-visualization) - a broader call to the Foam community to enhance graph visualisation
- [Github issue](https://github.com/foambubble/foam/issues/654) asking to be able to publish graph as JSON or other format

    - GEXF or GraphML as file formats
    - [comment](https://github.com/foambubble/foam/issues/654#issuecomment-1255619795) outline process to save graph from Foam now, includes adding Javascript code

## Examples

### Foam-like graph interfaces

- [Juggl](https://github.com/HEmile/juggl) - extensible graph view for Obsidian. Uses Cytoscape.js - [live site](https://juggl.io) which demonstrates its use with published Obsidian notes - nice.

- [Graph view component from a Gatsby/Foam template](https://github.com/theowenyoung/gatsby-theme-primer-wiki/blob/main/theme/src/components/graph-view.js) - is a nice implementation which allows navigation, but I wonder how it scales to larger graphs. Associated [github repo](https://github.com/mathieudutour/gatsby-digital-garden/tree/master). Uses [d3.js](https://github.com/mathieudutour/gatsby-digital-garden/blob/master/packages/gatsby-theme-garden/src/components/graph-visualisation.js)

  Gatsby's based on React.

- [/home/huka](https://hukacode.github.io/graph/) - his [process](https://discord.com/channels/729975036148056075/735778843151040512/850931487187402793)

- [Another example - (about graphs)](https://graph.stereobooster.com) - with a [graph visualisation](https://graph.stereobooster.com/notes/Visualisation) collection of notes

- [Obsidian example](https://notes.nicolevanderhoeven.com/obsidian-playbook/Using+Obsidian/01+First+steps+with+Obsidian/Obsidian)

- [Excalibrain](https://github.com/zsviczian/excalibrain) an interactive, structured mind-map for Obsidian.

  Distinguishes between 5 types of relationships: 
  
  - children - a forward link.
  - parents  - a back link
  - friends - files mutually link to each other
  - other friends, 
  - siblings - children of parents

- Use the code from Foam
- Add in some external JS
- write a script to build the graph data

[Paul's digital garden](https://garden.paulderaaij.nl/) - a more spacious and responsive popup design for the graph

## Graph libraries and related code

- [List of Javascript graph visualisation libraries](https://elise-deux.medium.com/the-list-of-graph-visualization-libraries-7a7b89aab6a6)
- [List of graph file formats](https://graph.stereobooster.com/notes/File-formats)
- [sigma.js](https://www.sigmajs.org)

  Highly capable. Loads GEXF

### [Cosmograph](https://cosmograph.app/#library)

A web application for analysing large data sets that also provides a [Javascript/React library](https://cosmograph.app/docs/cosmograph/Cosmograph%20JavaScript/Get%20Started). There is also now [Python support](https://cosmograph.app/docs/cosmograph/Cosmograph%20Python/get-started-widget/). Python support limited to Jupyter notebooks.

### Python

- [NetworkX](https://networkx.org/documentation/stable/index.html) - for the creation, manipulation and study of the structure of complex networks. Will read/write GEXF files. Not what we're looking for.

### [Foam detail on graph visualisation](https://foambubble.github.io/foam/user/features/graph-visualization.html)

- Foam gatsby templates including graph visualisations
  - [foam-gatsby-template](https://github.com/mathieudutour/foam-gatsby-template)
  - [foam-gatsby-template-kb](https://github.com/hikerpig/foam-template-gatsby-kb) - quite nice. The [source code](https://github.com/hikerpig/gatsby-project-kb/tree/master) and [documentation](https://gatsby-project-kb.vercel.app)

       Uses the Foam documentation as an example. Nice and navigable graph visualisation. Graph visualisation includes a search that highlights nodes.

       Graph visualisation provided by [note-graph](https://github.com/hikerpig/note-graph), which in turn draws on D3.js. Notes data is provided as an array of dicts, can be loaded from a JSON file. But is essentially a glue layer. Specifically to [force-graph](https://github.com/vasturiano/force-graph) which seems a more updated project.

- [mkdocs-roamlinks-plugin](https://github.com/Jackiexiao/mkdocs-roamlinks-plugin) - could help with ideas

- [Python code](https://github.com/foambubble/foam/issues/1351#issuecomment-2206544442) that geneates are graphml file by reading all markdown files

    - This works and the file can be opened in Gephi. Need to choose some layouts to get reasonably visualisation.
    - Also doesn't read the front matter etc. Meaning less than stellar context. But workable.
