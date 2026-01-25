---
tags:
- colophon
- about
title: Publishing graph interface
type: note
---

Version 1 using [force-graph](https://github.com/vasturiano/force-graph) is working is visible on  [[graph]].

## Implementation

Implemented as part of `corpusActions.py`
## Motivation

Foam has a graph/map feature for notes from within VS-Code (see the figure below) but that doesn't help when publishing to the web. Following are my notes playing around with adding a graph interface to this site. This type of feature is present in most Memex-like tools.

<figure markdown>
![](https://djon.es/assets/memex/colophon/images/foam-graph.png)
<caption>Sample graph/map of memex (within VSCode)</caption>
</figure>

Other live web-based examples include

- [Foam template](https://foam-template-gatsby-kb-hikerpig.vercel.app) uses the Foam documentation as an example and adds a graph visualisation (via a modal). Has a reasonable visual design and enables navigation around the network.
- [Paul's digital garden](https://garden.paulderaaij.nl/) provides a basic network visualisation (via a modal). Does not offer any navigation.
- [Obsidian example](https://notes.nicolevanderhoeven.com/obsidian-playbook/Using+Obsidian/01+First+steps+with+Obsidian/Obsidian) - a small graph visualisation is visible on the page and reacts to navigation through the pages. Can be opened as a modal that can be used to navigate.
- [Quartz](https://quartz.jzhao.xyz) - (typescript) SSG that includes a graph visualisation similar to some of the above. Used on the [graph site](https://graph.stereobooster.com).
- [/home/huka](https://hukacode.github.io) - uses a larger full page graph that supports navigation.

## Planning

### Features

Display 

- [x] A navigable graph on a stand alone page
- [ ] ~~graph in a modal~~

    Decided an in-page approach worked better.

- [ ] ~~graph as a macro in the page~~

    Implemented using a mkdocs template.

Features

- [x] Display a graph of all bubbles
  - [ ] color of background and nodes/edges fit the dark theme
  - [ ] color of background and nodes/edges fit the selected theme
- [x] Support navigation to individual bubbles
- [ ] Change the graph layout depending on the current visible bubble

### Possible implementation platforms

Numerous Javascript libraries (see comparisons: [one](https://www.cylynx.io/blog/a-comparison-of-javascript-graph-network-visualisation-libraries/)) available which all broadly follow the same implementation pattern. However, crafting that pattern to provide the functionality I want took a fair bit more experimentation than expected.

1. [force-graph](https://vasturiano.github.io/force-graph/)
2. [Sigma.js](https://www.sigmajs.org/)
3. [Cytoscape.js](https://js.cytoscape.org/)
4. [G6](https://g6.antv.antgroup.com/en/manual/introduction)

Implementation pipeline

- [[computational-components]] generate a JSON file with the graph data (using format expected by JS library)
- mkdocs template includes the Javascript library, and graph generation Javascript
- Graph generation Javascript 
  - reads the JSON file 
  - creates and configures the graph

To do
 
- check corpusActions
  - Now using mkdocs files, but issues
    - bird pages (e.g. memex/sense/birdwatching/spottedDove.html) do not have backlinks
    - none of the generated pages are showing backlinks - static is
      - life list content has backlinks (hardcoded in generator) but not showing on published page
      - ditto life list gallery
      - ditto wood duck meadows gallery
    - files are being included in documentation_pages
    - Is there any difference between these and other pages?
    - Are they being updated for backlinks
      - save Bubbles is writing back to files, but generated pages don't have real files
        - But spottedDove doesn't include any backlinks
      - extractFileContents is getting backLinks, but is the format right /memex/sense/...
    - added to network json

  - graph is not expanding - showing all in one line

  - does it run after bird list
    - the life list generator only creates files "in mkdocs serve/build", not accessible to the other generators
  - opening/writing JSON using mkdocs
- colouring and theming
- 

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
[//begin]: # "Autogenerated link references for markdown compatibility"1[graph]: graph "Memex network graph"1[computational-components]: computational-components "Computational components"1[//end]: # "Autogenerated link references"s for markdown compatibility"
[graph]: graph "Memex network graph"
[computational-components]: computational-components "Computational components"
[//end]: # "Autogenerated link references"


[//begin]: # "Autogenerated link references for markdown compatibility"
[graph]: graph "Memex network graph"
[computational-components]: computational-components "Computational components"
[//end]: # "Autogenerated link references"